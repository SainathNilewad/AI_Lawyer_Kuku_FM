"""
agents.py - Specialized Multi-Agent Legal Workflow for NyayaMitra
Implements the 4 core capabilities for Problem 2 (AI Lawyer):
1. CaseBuilderAgent: Messy story -> Facts, Timeline, Evidence Checklist
2. RightsAdvisorAgent: Plain-language legal standing, grounded in verified Indian statutes
3. DocumentDrafterAgent: Formal ready-to-send Legal Demand Notices & Complaints
4. RoleplayOpponentAgent: Dispute simulator allowing user to practice counter-arguments
"""

from typing import Dict, Any, List, Optional
import json
import datetime
import re
import sys
import os
from pathlib import Path

# Explicitly ensure repo root is in sys.path on Streamlit Cloud / Linux
_REPO_ROOT = str(Path(__file__).resolve().parent)
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

try:
    from legal_kb import (
        retrieve_verified_legal_context,
        check_immediate_advocate_escalation,
        sanitize_unverified_sections,
        scan_unverified_sections,
        scan_banned_acts
    )
except ImportError:
    from .legal_kb import (
        retrieve_verified_legal_context,
        check_immediate_advocate_escalation,
        sanitize_unverified_sections,
        scan_unverified_sections,
        scan_banned_acts
    )

try:
    from llm_engine import LegalLLMEngine
except ImportError:
    from .llm_engine import LegalLLMEngine

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
6. Do not state court fees, interest rates, processing times, penalties or portal names unless they appear in the provided knowledge base or in the user's message. If needed, say 'confirm this locally or with a lawyer / DLSA 15100.'

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
        if isinstance(result, dict) and ("error" in result or result.get("status") == "error"):
            return result
        
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
        
        # FIX 5: Honest out-of-scope fallback (no guessing or inventing law)
        if kb_result.get("out_of_scope"):
            return {
                "plain_language_standing": (
                    "This legal matter falls outside the verified everyday domains currently covered by NyayaMitra "
                    "(Tenancy & Rental, Consumer Protection, and Code on Wages Employment). "
                    "NyayaMitra strictly avoids guessing or inventing law for uncovered domains. "
                    "Please consult a practicing advocate or contact the free District Legal Services Authority (DLSA) / NALSA Helpline at 15100."
                ),
                "governing_laws": [],
                "action_options": [
                    {
                        "step_number": 1,
                        "title": "Consult a Licensed Advocate or DLSA",
                        "timeline": "Immediate",
                        "cost_estimate": "Free legal aid via DLSA",
                        "details": "Contact your local District Legal Services Authority or call toll-free 15100 for official legal assistance."
                    }
                ],
                "real_lawyer_needed": True,
                "real_lawyer_guidance": "Matters outside NyayaMitra's verified domains require representation by a licensed advocate.",
                "disclaimer": "⚠️ NyayaMitra provides self-advocacy information for verified civil domains only."
            }

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
5. Answer length & structure: Lead with a concise 3-line summary (core legal standing, key statutory rule, immediate takeaway), followed by clear details.
6. Do not state court fees, interest rates, processing times, penalties or portal names unless they appear in the provided knowledge base or in the user's message. If needed, say 'confirm this locally or with a lawyer / DLSA 15100.' (Note: e-Daakhil applies strictly to consumer disputes, NEVER to employment or salary matters).
7. PROVISION RELEVANCE: Only cite provisions that appear in the VERIFIED STATUTORY GROUNDING. If Section 18 is not in the grounding, do NOT cite Section 18 or deduction rules. Never describe Section 18(3) as preventing an employer from withholding wages; it only caps deductions.
8. DLSA & FORUM RULES: Describe DLSA strictly as free legal aid and guidance (Helpline 15100). NEVER describe DLSA as a forum for hearings or proceedings against an employer. For wage claims, direct the user to 'the competent labour authority (confirm locally)'.
9. COSTS & TIMELINES RULE: Do NOT include any fee, court fee, or cost estimates (do NOT state 'Cost: Nominal / Free', 'Cost: Free / Speed Post', or specific rupee amounts for filing). Any deadline or timeline must be explicitly labelled 'Suggested' (e.g. 'Suggested 15 days (customary pre-litigation notice period)').

VERIFIED STATUTORY GROUNDING:
{grounding_text}

Output format MUST be valid JSON with this structure:
{{
  "plain_language_standing": "A clear, reassuring explanation of where the person stands under Indian law. MUST start with a 3-line summary of their standing, followed by details.",
  "governing_laws": [
    {{"act_name": "Name of Statute", "section": "Specific Section", "relevance": "Why it protects the user"}}
  ],
  "action_options": [
    {{
      "step_number": 1,
      "title": "Immediate Pre-Litigation Action (e.g. Formal Legal Notice)",
      "timeline": "Suggested 15 days (customary pre-litigation practice)",
      "details": "Concrete instructions on what to do"
    }},
    {{
      "step_number": 2,
      "title": "Statutory Authority / Grievance Portal Filing",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "Instructions on proper forum: e-Daakhil for consumer, Rent Authority for tenancy, the competent labour authority (confirm locally) for wage claims. Note: DLSA provides free legal aid and guidance only; it is never a forum for hearings or proceedings against an employer."
    }},
    {{
      "step_number": 3,
      "title": "Statutory Forum / Consumer Commission Petition",
      "timeline": "Timeline varies by state (confirm locally)",
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
        if isinstance(result, dict) and ("error" in result or result.get("status") == "error"):
            return result
        if not isinstance(result, dict) or "plain_language_standing" not in result:
            raw_txt = result.get("raw_text", str(result)) if isinstance(result, dict) else str(result)
            is_emp = "employ" in str(case_dossier.get("category", "")).lower() or "wage" in str(case_dossier.get("category", "")).lower()
            step_2_title = "Approach the Competent Labour Authority (Confirm Locally)" if is_emp else "File on Government Grievance Portal"
            step_2_details = "Register claim before the competent labour authority (confirm locally), or seek free legal aid and guidance via DLSA Helpline 15100." if is_emp else "Register on statutory portal (e.g. e-Daakhil for consumer disputes, Rent Authority for tenancy)."

            result = {
                "plain_language_standing": raw_txt if raw_txt else "Under Indian Law, you have a strong statutory claim to seek full recovery or refund, as arbitrary withholding or deficient services are unlawful.",
                "governing_laws": [
                    {"act_name": "Indian Statutory Law", "section": "Governing Provisions", "relevance": "Protects against arbitrary withholding and deficient services"}
                ],
                "action_options": [
                    {"step_number": 1, "title": "Serve Formal 15-Day Legal Demand Notice", "timeline": "Suggested 15 days (customary pre-litigation practice)", "details": "Issue notice via Speed Post and Email."},
                    {"step_number": 2, "title": step_2_title, "timeline": "Timeline varies by state (confirm locally)", "details": step_2_details}
                ],
                "real_lawyer_needed": False,
                "real_lawyer_guidance": "You can pursue pre-litigation notice and statutory portals yourself without an advocate.",
                "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws."
            }

        context_text = f"{case_dossier.get('category', '')} {case_dossier.get('summary', '')}"
        is_emp_case = "employ" in str(case_dossier.get("category", "")).lower() or "wage" in str(case_dossier.get("category", "")).lower()
        has_deduction = any(t in context_text.lower() for t in ["deduct", "deduction", "fine", "advance", "cut from salary", "deductions", "deducted", "fines", "advances", "salary cut"])

        # Code-level guard: Sanitize plain language standing for unverified section references & banned Acts
        if isinstance(result, dict) and "plain_language_standing" in result:
            result["plain_language_standing"] = sanitize_unverified_sections(result["plain_language_standing"], context_text=context_text)

        # Code-level guard: Check governing laws list against allowed statutory sections & banned Acts
        if isinstance(result, dict) and "governing_laws" in result and isinstance(result["governing_laws"], list):
            filtered_laws = []
            for item in result["governing_laws"]:
                if isinstance(item, dict):
                    act_name = str(item.get("act_name", ""))
                    banned_a = scan_banned_acts(act_name)
                    if banned_a:
                        item["status"] = "unverified reference removed"
                        item["act_name"] = "[unverified reference removed]"
                    sec = str(item.get("section", ""))
                    unv = scan_unverified_sections(sec)
                    if unv:
                        item["status"] = "unverified reference removed"
                        item["section"] = "[unverified reference removed]"
                    # If employment dispute with NO deduction mentioned, do NOT cite Section 18
                    if is_emp_case and not has_deduction and re.search(r'\b18\b', sec):
                        continue
                    filtered_laws.append(item)
            result["governing_laws"] = filtered_laws

        # Code-level guard: Sanitize action options and remove unsourced cost estimates
        if isinstance(result, dict) and "action_options" in result and isinstance(result["action_options"], list):
            for opt in result["action_options"]:
                if isinstance(opt, dict):
                    if "cost_estimate" in opt:
                        del opt["cost_estimate"]
                    if "details" in opt and isinstance(opt["details"], str):
                        opt["details"] = sanitize_unverified_sections(opt["details"], context_text=context_text)
                    if "title" in opt and isinstance(opt["title"], str):
                        opt["title"] = sanitize_unverified_sections(opt["title"], context_text=context_text)

        return result


class DocumentDrafterAgent:
    """Prepares ready-to-serve formal Legal Demand Notices and Complaints."""
    def __init__(self, engine: LegalLLMEngine):
        self.engine = engine

    def draft_demand_notice(self, case_dossier: Dict[str, Any], rights_advice: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Convenience method returning structured dict containing the notice text."""
        text = self.run(case_dossier, rights_advice or {})
        return {"notice_text": text}

    def run(self, case_dossier: Dict[str, Any], rights_advice: Dict[str, Any], doc_type: str = "Legal Demand Notice") -> str:
        today_str = datetime.date.today().strftime("%d/%m/%Y")
        timeline_dates = [t.get("date_or_period", "") for t in case_dossier.get("timeline", []) if t.get("date_or_period")]
        category = case_dossier.get("category", "")
        is_emp = "employ" in str(category).lower() or "wage" in str(category).lower()

        system_prompt = f"""
You are the Expert Legal Drafter at NyayaMitra India.
Your job is to draft a rigorous, professionally formatted Indian Legal Document that an ordinary citizen 
can immediately print, sign, and serve via Speed Post with Acknowledgement Due (AD) or registered email.

DOCUMENT STANDARDS:
1. Professional Indian Legal Notice / Grievance format.
2. Include: Header, Date, Mode of Dispatch (Speed Post / Email), Details of Sender and Recipient.
3. Structured Factual Sequence: 'Under instructions from my client / The undersigned submits as under...'
4. Clear recital of facts, timeline, amounts, and violation of statutory provisions.
5. Strict 15-Day Rectification Demand Window (suggested customary pre-litigation practice).
6. Warning of further legal action before the appropriate statutory forum: for wage claims, before the competent labour authority (confirm locally).
7. DATE RULES: Today's date is {today_str}. Never invent a year or date. Use only the specific dates provided in the case timeline ({', '.join(timeline_dates) if timeline_dates else 'none provided'}) or the user's story; if a date is unknown, use the placeholder '[DD/MM/YYYY]'. Do NOT assume the year is 2024 or any other year unless explicitly stated in the case facts.
8. FACT INTEGRITY (STRICT): Use ONLY facts explicitly stated by the user or present in the case dossier. NEVER invent or assume facts. Specifically:
   - Do NOT invent a job title / designation (e.g. Software Engineer, Marketing Associate) unless the user stated it; use '[Job Title / Designation]' or leave it out.
   - Do NOT invent emails sent or reminder dates (e.g. do NOT write 'despite multiple emails sent on...', 'as per my email dated...', 'email reminders') unless the user explicitly provided dates/copies of emails sent.
   - Do NOT invent demands for unmentioned documents like 'Experience Certificate' unless explicitly requested by the user.
   Anything not explicitly stated by the user must be a [bracketed placeholder] or left out.
9. DLSA & FORUM RULES: DLSA provides free legal aid and guidance only (Helpline: 15100). NEVER describe DLSA as a forum for proceedings against an employer. For wage claims, state that proceedings will be filed before 'the competent labour authority (confirm locally)'.
10. UNVERIFIED SPECIFICS: Do not state court fees, interest rates, processing times, penalties or portal names unless they appear in the provided knowledge base or in the user's message. If needed, say 'confirm this locally or with a lawyer / DLSA 15100.' {'(Note: For employment disputes, do NOT mention e-Daakhil; e-Daakhil is strictly for consumer cases).' if is_emp else ''}
11. Space for signatures and annexure inventory.
12. Output formatted in clean Markdown.
"""
        user_prompt = f"""
Draft Document Type: {doc_type}

Case Facts Dossier:
{json.dumps(case_dossier, indent=2)}

Legal Standing & Grounded Laws:
{json.dumps(rights_advice, indent=2)}

Today's Date: {today_str}
Dossier Timeline Dates: {', '.join(timeline_dates) if timeline_dates else 'Use [DD/MM/YYYY]'}

Please write the complete, unedited, ready-to-send document.
"""
        raw_draft = self.engine.generate(system_prompt, user_prompt, temperature=0.2)
        
        # Post-processing fact integrity check: Remove hallucinated email reminders or experience certificate if user did not provide them
        dossier_text = json.dumps(case_dossier).lower()
        if "experience certificate" not in dossier_text:
            raw_draft = re.sub(r'(?i)(?:and\s+)?experience\s+certificate', '', raw_draft)
            raw_draft = re.sub(r'(?i)experience\s+and\s+relieving\s+certificate', 'relieving letter', raw_draft)
        if "email reminder" not in dossier_text and "email reminders" not in dossier_text and "reminder email" not in dossier_text:
            raw_draft = re.sub(r'(?i)email\s+reminders?', '[reminders, if any]', raw_draft)
        raw_draft = re.sub(r'  +', ' ', raw_draft)

        return sanitize_unverified_sections(raw_draft, context_text=dossier_text)


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
- Do not state court fees, interest rates, processing times, penalties or portal names unless they appear in the provided knowledge base or in the user's message. If needed, say 'confirm this locally or with a lawyer / DLSA 15100.'

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

        # Code-level guard: Sanitize opponent reply and coach feedback
        if isinstance(res, dict):
            if "opponent_reply" in res and isinstance(res["opponent_reply"], str):
                res["opponent_reply"] = sanitize_unverified_sections(res["opponent_reply"])
            if "coach_evaluation" in res and isinstance(res["coach_evaluation"], dict):
                for k, v in res["coach_evaluation"].items():
                    if isinstance(v, str):
                        res["coach_evaluation"][k] = sanitize_unverified_sections(v)

        return res


class ConversationalCounselorAgent:
    """Handles multi-turn conversational follow-up questions with full context memory."""
    def __init__(self, engine: LegalLLMEngine):
        self.engine = engine

    def answer_followup(self, chat_history: List[Dict[str, str]], case_dossier: Dict[str, Any], user_message: str, language: str = "Auto-Detect") -> str:
        category = case_dossier.get("category", "") if case_dossier else ""
        summary = case_dossier.get("summary", "") if case_dossier else ""
        today_str = datetime.date.today().strftime("%d/%m/%Y")
        is_emp = "employ" in str(category).lower() or "wage" in str(category).lower()
        
        # Pass fallback_category so follow-up queries inherit active case domain
        kb_result = retrieve_verified_legal_context(f"{category} {summary} {user_message}", fallback_category=category)
        if kb_result.get("out_of_scope"):
            return (
                "This topic falls outside the verified everyday legal domains covered by NyayaMitra "
                "(Tenancy & Rental, Consumer Protection, and Code on Wages Employment). "
                "To ensure you receive accurate guidance, NyayaMitra does not answer queries outside verified domains. "
                "Please consult a practicing advocate or call the free District Legal Services Authority (DLSA) / NALSA Helpline at 15100."
            )

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
2. ANSWER STRUCTURE: Lead with a clear 3-line summary of your direct advice, followed by concise bulleted details and practical steps.
3. If the user asks 'what if...', 'can I...', 'how do I...', or about proofs/threats/police/courts, give them clear, step-by-step practical guidance under Indian law.
4. DATE & TIME RULES: Today's date is {today_str}. Never invent years or dates. Use only dates provided in the case facts or [DD/MM/YYYY]. Do not assume 2024 or any year unless stated in the case facts.
5. UNVERIFIED SPECIFICS: Do not state court fees, interest rates, processing times, penalties or portal names unless they appear in the provided knowledge base or in the user's message. If needed, say 'confirm this locally or with a lawyer / DLSA 15100.' {'(Note: For employment disputes, do NOT mention e-Daakhil; e-Daakhil is strictly for consumer cases).' if is_emp else ''}
6. FACT INTEGRITY (STRICT): Use ONLY facts the user stated or the dossier contains. NEVER invent job titles, dates of reminders, emails sent, or unmentioned documents like 'Experience Certificate' unless the user stated them. Use bracketed placeholders like '[Job Title]' or leave them out.
7. DLSA & FORUM RULES: Describe DLSA strictly as free legal aid and guidance (Helpline 15100). NEVER describe DLSA as a forum for hearings or proceedings against an employer. For wage claims, refer to 'the competent labour authority (confirm locally)'.
8. PROVISION RELEVANCE: Never cite Section 18 unless deduction/fine/advance triggers were mentioned. Never describe Section 18(3) as preventing an employer from withholding wages; it only caps deductions.
9. If the user shares new facts or evidence, acknowledge them and incorporate them into your advice.
10. Keep the language natural, reassuring, and conversational.
11. Never invent fake section numbers or fake case laws.
12. If a physical courtroom appearance or high-risk criminal step is needed, tell them clearly to consult an advocate.
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
        # Code-level guard: Sanitize conversational follow-up response
        return sanitize_unverified_sections(ans, context_text=f"{category} {summary} {user_message}")

