"""
agents.py - Specialized Multi-Agent Legal Workflow for NyayaMitra
Implements the 4 core capabilities for Problem 2 (AI Lawyer):
1. CaseBuilderAgent: Messy story -> Facts, Timeline, Evidence Checklist
2. RightsAdvisorAgent: Plain-language legal standing, grounded in verified Indian statutes
3. DocumentDrafterAgent: Formal ready-to-send Legal Demand Notices & Complaints
4. RoleplayOpponentAgent: Dispute simulator allowing user to practice counter-arguments
"""

from typing import Dict, Any, List
import json
from legal_kb import retrieve_verified_legal_context, check_immediate_advocate_escalation
from llm_engine import LegalLLMEngine

class CaseBuilderAgent:
    """Turn a messy story into what happened, when, and what proof they have."""
    def __init__(self, engine: LegalLLMEngine):
        self.engine = engine

    def run(self, raw_story: str, language: str = "English") -> Dict[str, Any]:
        # Step 1: Pre-flight advocate escalation safety check
        escalation_check = check_immediate_advocate_escalation(raw_story)

        system_prompt = f"""
You are the Senior Intake Legal Assistant at NyayaMitra India.
Your job is to listen to an everyday Indian person's messy story (which may be in English, Hindi, or Hinglish) 
and organize it into a crystal-clear factual dossier.

CRITICAL INSTRUCTIONS:
1. Extract the facts objectively without assuming unstated information.
2. Build a Chronological Timeline (what happened first, next, and most recently).
3. Audit the Evidence: List what proof the user currently mentions, and what critical missing evidence they should collect.
4. Rate the Evidence Strength on a scale of 1 to 10.
5. Determine the dispute category: 'Tenancy & Rental', 'Consumer & E-Commerce', 'Employment & Salary', or 'General Civil'.

Output MUST be a valid JSON object with EXACTLY this structure:
{{
  "case_title": "Short title describing the dispute",
  "category": "Tenancy & Rental / Consumer & E-Commerce / Employment & Salary / Other",
  "summary": "2-3 sentence plain language summary of the core dispute",
  "complainant": "Name or designation of aggrieved person (e.g. Tenant, Consumer, Ex-Employee)",
  "opposite_party": "Name or entity being complained against (e.g. Landlord Mr. Sharma, E-Commerce Seller)",
  "disputed_amount": "Amount in INR if applicable (e.g. Rs. 45,000) or 'Not Specified'",
  "timeline": [
    {{"date_or_period": "Date or relative time", "event": "Specific factual occurrence"}}
  ],
  "evidence_held": [
    "List of proof user already has (e.g. UPI transfer receipts, WhatsApp chat screenshots, Rent Agreement)"
  ],
  "evidence_needed": [
    "List of crucial missing documents user should gather before taking action"
  ],
  "evidence_strength_score": 7,
  "evidence_strength_explanation": "Brief 1-sentence rationale for the score"
}}
"""
        user_prompt = f"User's Messy Story:\n\"\"\"{raw_story}\"\"\"\n\nPreferred Language: {language}"
        result = self.engine.generate_json(system_prompt, user_prompt)
        
        if not isinstance(result, dict) or "case_title" not in result:
            raw_txt = result.get("raw_text", str(result)) if isinstance(result, dict) else str(result)
            result = {
                "case_title": "Everyday Legal Dispute",
                "category": "Civil Dispute",
                "summary": raw_story[:280],
                "complainant": "Aggrieved Citizen",
                "opposite_party": "Opposing Party",
                "disputed_amount": "To be determined",
                "timeline": [{"date_or_period": "Initial Occurrence", "event": raw_story[:120]}],
                "evidence_held": ["User oral/written statement"],
                "evidence_needed": ["Bank receipts", "Chat history", "Invoices / Agreement"],
                "evidence_strength_score": 7,
                "evidence_strength_explanation": "Preliminary statement recorded; formal documentation pending.",
                "raw_text": raw_txt
            }

        # Attach the escalation status
        result["escalation_check"] = escalation_check
        return result


class RightsAdvisorAgent:
    """Explains where the user stands and what their options are, grounded in real Indian law."""
    def __init__(self, engine: LegalLLMEngine):
        self.engine = engine

    def run(self, case_dossier: Dict[str, Any], language: str = "English") -> Dict[str, Any]:
        category = case_dossier.get("category", "")
        summary = case_dossier.get("summary", "")
        
        # Grounding: Retrieve real Indian statutory context
        kb_result = retrieve_verified_legal_context(f"{category} {summary}")
        grounding_text = kb_result["grounding_text"]

        system_prompt = f"""
You are the Chief Legal Standing Advisor at NyayaMitra India.
Your mission is to explain an everyday citizen's legal standing in SIMPLE, PLAIN, REASSURING language.
Do NOT use intimidating courtroom Latin jargon. Emphasize their rights and practical remedy pathways.

LANGUAGE INSTRUCTION:
The user selected language: {language}.
Formulate your 'plain_language_standing' and 'action_options' in {language}.
- If Hindi: Write in authentic, clear Hindi (हिन्दी) or Devanagari script.
- If Hinglish: Write in conversational Roman Hindi/English mix.
- If Regional (Tamil, Telugu, Kannada, Bengali, Marathi, Gujarati, Malayalam, Punjabi): Write in that language's script, while keeping legal statute names identifiable.
- If English: Write in plain, accessible English.

STRICT HALLUCINATION PREVENTION RULES:
1. You may ONLY cite Acts, Sections, and Precedents provided in the VERIFIED STATUTORY GROUNDING below.
2. NEVER invent fake section numbers, punishments, or past judgments.
3. If a section is not in the grounding text, explain the general legal principle without manufacturing a citation.
4. Clearly state whether the issue is Civil or Criminal. (Remind users that monetary/contract disputes are NOT criminal cheating).

VERIFIED STATUTORY GROUNDING:
{grounding_text}

Output format MUST be valid JSON with this structure:
{{
  "plain_language_standing": "A clear, reassuring 2-3 paragraph explanation of where the person stands under Indian law and why they have a strong/valid claim.",
  "governing_laws": [
    {{"act_name": "Name of Statute", "section": "Specific Section", "relevance": "Why it protects the user"}}
  ],
  "action_options": [
    {{
      "step_number": 1,
      "title": "Immediate Pre-Litigation Action (e.g. Formal Legal Notice)",
      "timeline": "e.g. 15 Days",
      "cost_estimate": "Free to minimal (Speed Post / Email)",
      "details": "Concrete instructions on what to do"
    }},
    {{
      "step_number": 2,
      "title": "Government Grievance Portal Filing (e.g. e-Daakhil / NCH / Rent Authority)",
      "timeline": "e.g. 30-45 Days",
      "cost_estimate": "Zero court fees up to Rs. 5 Lakhs",
      "details": "Concrete instructions on portal registration"
    }},
    {{
      "step_number": 3,
      "title": "Statutory Forum / Consumer Commission Petition",
      "timeline": "e.g. 60-90 Days",
      "cost_estimate": "Nominal",
      "details": "How to proceed if earlier steps fail"
    }}
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "Clear explanation of when a physical advocate is required vs when the user can represent themselves (e.g. Consumer Forum allows self-representation).",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}}
"""
        user_prompt = f"Case Dossier:\n{json.dumps(case_dossier, indent=2)}\n\nLanguage: {language}"
        result = self.engine.generate_json(system_prompt, user_prompt)
        if not isinstance(result, dict) or "plain_language_standing" not in result:
            raw_txt = result.get("raw_text", str(result)) if isinstance(result, dict) else str(result)
            result = {
                "plain_language_standing": raw_txt if raw_txt else "Under Indian Law, you have a strong statutory claim to seek full recovery or refund, as arbitrary withholding or deficient services are unlawful.",
                "governing_laws": [
                    {"act_name": "Indian Statutory Law", "section": "Governing Provisions", "relevance": "Protects against unfair deduction and deficiency in service"}
                ],
                "action_options": [
                    {"step_number": 1, "title": "Serve Formal 15-Day Legal Demand Notice", "timeline": "15 Days", "cost_estimate": "Free / Speed Post", "details": "Issue notice via Speed Post and Email."},
                    {"step_number": 2, "title": "File on Government Grievance Portal", "timeline": "30-45 Days", "cost_estimate": "Zero to nominal", "details": "Register on e-Daakhil / NCH / Rent Authority."}
                ],
                "real_lawyer_needed": False,
                "real_lawyer_guidance": "You can pursue pre-litigation notice and statutory portals yourself without an advocate.",
                "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws."
            }
        return result


class DocumentDrafterAgent:
    """Prepares ready-to-serve formal Legal Demand Notices and Complaints."""
    def __init__(self, engine: LegalLLMEngine):
        self.engine = engine

    def run(self, case_dossier: Dict[str, Any], rights_advice: Dict[str, Any], doc_type: str = "Legal Demand Notice") -> str:
        system_prompt = """
You are the Expert Legal Drafter at NyayaMitra India.
Your job is to draft a rigorous, professionally formatted Indian Legal Document that an ordinary citizen 
can immediately print, sign, and serve via Speed Post with Acknowledgement Due (AD) or registered email.

DOCUMENT STANDARDS:
1. Professional Indian Legal Notice / Grievance format.
2. Include: Header, Date, Mode of Dispatch (Speed Post / Email), Details of Sender and Recipient.
3. Structured Factual Sequence: 'Under instructions from my client / The undersigned submits as under...'
4. Clear recital of facts, timeline, amounts, and violation of statutory provisions.
5. Strict 15-Day Rectification Demand Window.
6. Explicit warning of further legal action (Consumer Commission / Rent Authority / Labor Court) with 12% statutory interest and litigation damages if not settled.
7. Space for signatures and annexure inventory.
8. Output formatted in clean Markdown.
"""
        user_prompt = f"""
Draft Document Type: {doc_type}

Case Facts Dossier:
{json.dumps(case_dossier, indent=2)}

Legal Standing & Grounded Laws:
{json.dumps(rights_advice, indent=2)}

Please write the complete, unedited, ready-to-send document.
"""
        return self.engine.generate(system_prompt, user_prompt, temperature=0.2)


class RoleplayOpponentAgent:
    """Dispute Simulator: plays the opposing party so the user can practice their arguments."""
    def __init__(self, engine: LegalLLMEngine):
        self.engine = engine

    def run(self, case_dossier: Dict[str, Any], conversation_history: List[Dict[str, str]], user_argument: str, language: str = "Auto-Detect") -> Dict[str, Any]:
        opposite_party = case_dossier.get("opposite_party", "Opposing Party")
        category = case_dossier.get("category", "")
        
        system_prompt = f"""
You are simulating the OPPOSING PARTY in an everyday Indian dispute.
You are playing the role of: {opposite_party} ({category}).
Language Style: Match the user's language ({language}). If Hindi/Hinglish, speak like a typical stubborn Indian landlord/manager. If Tamil/Telugu/Kannada/Bengali/Marathi/Gujarati/Malayalam/Punjabi, respond in that language or bilingual tone.
Your character traits:
- You are defensive, dismissive, make typical Indian landlord/corporate excuses (e.g. 'Read the agreement', 'Painting costs money', 'Company policy', 'Return window expired').
- You try to intimidate the user with jargon or delays.
- HOWEVER, if the user firmly cites exact facts, dates, receipts, or statutory consumer/tenancy laws, you begin to soften and negotiate!

You must also act as a 'Coach' to evaluate the user's argument.

Output format MUST be valid JSON with this structure:
{{
  "opponent_reply": "What the opposing party says back to the user in direct dialogue (in the conversational language/tone)",
  "coach_evaluation": {{
    "strength_rating": "Strong / Moderate / Weak",
    "what_went_well": "Specific compliment on user's argument",
    "what_to_improve": "Specific advice on what facts or laws the user forgot to mention",
    "suggested_next_counter": "A powerful 1-line retort the user can use next"
  }}
}}
"""
        user_prompt = f"""
Case Background:
Title: {case_dossier.get('case_title')}
Summary: {case_dossier.get('summary')}
Disputed Amount: {case_dossier.get('disputed_amount')}

Conversation So Far:
{json.dumps(conversation_history, indent=2)}

User's Latest Statement/Argument:
\"{user_argument}\"
"""
        res = self.engine.generate_json(system_prompt, user_prompt)
        if not isinstance(res, dict) or "opponent_reply" not in res or not res.get("opponent_reply"):
            raw_txt = res.get("raw_text", "") if isinstance(res, dict) else ""
            res = {
                "opponent_reply": raw_txt if raw_txt else "Look, I have already explained our stance. We operate strictly by our terms and policies, so I cannot agree to this right now.",
                "coach_evaluation": {
                    "strength_rating": "Moderate",
                    "what_went_well": "You maintained a clear and determined position.",
                    "what_to_improve": "Quote the exact 15-day timeline and statutory liability under Indian law.",
                    "suggested_next_counter": "Remind them that persistent refusal attracts 12% statutory interest in formal court proceedings."
                }
            }
        return res


class ConversationalCounselorAgent:
    """Handles multi-turn conversational follow-up questions with full context memory."""
    def __init__(self, engine: LegalLLMEngine):
        self.engine = engine

    def answer_followup(self, chat_history: List[Dict[str, str]], case_dossier: Dict[str, Any], user_message: str, language: str = "Auto-Detect") -> str:
        category = case_dossier.get("category", "") if case_dossier else ""
        summary = case_dossier.get("summary", "") if case_dossier else ""
        
        kb_result = retrieve_verified_legal_context(f"{category} {summary} {user_message}")
        grounding_text = kb_result["grounding_text"]

        system_prompt = f"""
You are NyayaMitra, a compassionate, highly competent AI Legal Counselor for everyday Indian citizens.
You are having an ongoing, multi-turn conversational consultation with a user about their legal problem.

LANGUAGE SPECIFICATION:
Target Language: {language}
- If 'Auto-Detect': Detect the language the user is speaking or typing in (e.g., Hindi, Tamil, Telugu, Kannada, Bengali, Marathi, Gujarati, Malayalam, Punjabi, Hinglish, or English) and reply in that EXACT SAME language with natural fluency.
- If a specific language is chosen (e.g. Hindi, Tamil, Telugu), answer primarily in that language while keeping legal terminology clear.

ESTABLISHED CASE CONTEXT:
- Case Title: {case_dossier.get('case_title', 'Legal Dispute') if case_dossier else 'N/A'}
- Parties: {case_dossier.get('complainant', 'Citizen')} vs {case_dossier.get('opposite_party', 'Opposing Party') if case_dossier else 'N/A'}
- Category: {category}
- Disputed Amount: {case_dossier.get('disputed_amount', 'N/A') if case_dossier else 'N/A'}
- Factual Summary: {summary}

VERIFIED STATUTORY GROUNDING (NO HALLUCINATIONS):
{grounding_text}

INSTRUCTIONS FOR MULTI-TURN CHAT:
1. Answer the user's follow-up question DIRECTLY, warmly, and practically.
2. If the user asks 'what if...', 'can I...', 'how do I...', or about proofs/threats/police/courts, give them clear, step-by-step practical guidance under Indian law.
3. If the user shares new facts or evidence, acknowledge them and incorporate them into your advice.
4. Keep the language natural, reassuring, and conversational.
5. Never invent fake section numbers or fake case laws.
6. If a physical courtroom appearance or high-risk criminal step is needed, tell them clearly to consult an advocate.
"""
        # Format recent conversation history (last 8 turns for context)
        recent_history = chat_history[-8:] if len(chat_history) > 8 else chat_history
        formatted_history = "\n".join([f"{m['role'].upper()}: {m['content']}" for m in recent_history if m.get('content')])

        user_prompt = f"""
CONVERSATION TRANSCRIPT SO FAR:
{formatted_history}

USER'S LATEST FOLLOW-UP MESSAGE:
"{user_message}"

Please respond naturally to the user's question with practical Indian legal counsel.
"""
        ans = self.engine.generate(system_prompt, user_prompt, temperature=0.3)
        if not ans or not ans.strip():
            ans = "I understand your point. Based on the facts established in your case and relevant Indian statutes, you are legally entitled to press for your rightful refund or dues. Would you like me to generate your ready-to-send Legal Demand Notice now?"
        return ans

