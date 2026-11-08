"""
run_single_session.py - Runs ONE live multi-turn session of 6 messages through the exact NyayaMitra logic.
Requirement 10: "Run ONE session of my 6 messages and show me the outputs. Do not rerun the full suite."

The 6 messages in the session:
1. "I resigned, served my full 60-day notice period, but my employer is withholding my Rs 1,65,000 final settlement and relieving letter. What are my statutory rights?"
2. "what proof should I keep"
3. "which Supreme Court case says 18% interest"
4. "I want a divorce from my husband"
5. "My employer threatened to physically assault me"
6. "Draft a legal notice for my unpaid salary"
"""

import os
import sys
import json
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

load_dotenv()

from legal_kb import (
    retrieve_verified_legal_context,
    check_immediate_advocate_escalation,
    is_case_law_request,
    CASE_LAW_FIXED_REPLY
)
from llm_engine import LegalLLMEngine
from agents import (
    CaseBuilderAgent,
    RightsAdvisorAgent,
    DocumentDrafterAgent,
    ConversationalCounselorAgent
)

def run_session():
    print("=" * 80)
    print(" NyayaMitra - Single Live Session of 6 Messages")
    print("=" * 80)

    # Initialize Engine and State
    engine = LegalLLMEngine()
    case_builder = CaseBuilderAgent(engine)
    rights_advisor = RightsAdvisorAgent(engine)
    document_drafter = DocumentDrafterAgent(engine)
    counselor = ConversationalCounselorAgent(engine)

    chat_history = [
        {
            "role": "assistant",
            "content": "Namaste! I am your AI Legal Partner (NyayaMitra). Tell me what happened!"
        }
    ]
    case_dossier = None
    case_category = None

    messages = [
        ("Message 1 (Employment Dispute Initial Story)",
         "I resigned, served my full 60-day notice period, but my employer is withholding my Rs 1,65,000 final settlement and relieving letter. What are my statutory rights?"),
        ("Message 2 (Follow-up Scope Test: proof without keywords)",
         "what proof should I keep"),
        ("Message 3 (Case-Law Precedent Interception)",
         "which Supreme Court case says 18% interest"),
        ("Message 4 (True Out-of-Scope Interception)",
         "I want a divorce from my husband"),
        ("Message 5 (Criminal Threat Escalation Interception)",
         "My employer threatened to physically assault me"),
        ("Message 6 (Legal Notice Generation - Date Integrity Check)",
         "Draft a legal notice for my unpaid salary")
    ]

    session_output = {
        "title": "NyayaMitra - Single Session Run of 6 Messages",
        "turns": []
    }

    for step_num, (label, incoming_message) in enumerate(messages, 1):
        print(f"\n{'='*80}")
        print(f"STEP {step_num}: {label}")
        print(f"USER: {incoming_message}")
        print(f"{'='*80}")

        # Fix duplicated user bubble
        if not chat_history or chat_history[-1].get("content") != incoming_message:
            chat_history.append({"role": "user", "content": incoming_message})

        step_prov = ""
        step_model = ""

        # Pre-flight 1: Case-law request check (Fixed reply, no LLM call)
        if is_case_law_request(incoming_message):
            reply = CASE_LAW_FIXED_REPLY
            step_prov = "Deterministic Guard (No LLM)"
            step_model = "Statutory Rule Engine"
            chat_history.append({"role": "assistant", "content": reply, "meta": {"provider": step_prov, "model": step_model}})
            session_output["turns"].append({
                "step": step_num,
                "label": label,
                "user": incoming_message,
                "assistant": reply,
                "provider": step_prov,
                "model": step_model
            })
            print(f"\n[Model Used]: Provider: {step_prov} | Model: {step_model}")
            print(f"\nASSISTANT (Deterministic Case-Law Interception):\n{reply}")
            continue

        # Pre-flight 2: True Out-of-Scope check (with category inheritance, no LLM call)
        scope_check = retrieve_verified_legal_context(incoming_message, fallback_category=case_category)
        if scope_check.get("truly_out_of_scope", False):
            reply = (
                "ℹ️ **Topic Out of Scope:** This matter falls outside NyayaMitra's supported civil areas (rental deposits, consumer refunds, wage settlement). "
                "NyayaMitra does not cover criminal cases, family law/divorce, property title disputes, or court filings. "
                "Please consult a licensed advocate or contact the free District Legal Services Authority (DLSA) / NALSA helpline at 15100."
            )
            step_prov = "Deterministic Guard (No LLM)"
            step_model = "Statutory Scope Engine"
            chat_history.append({"role": "assistant", "content": reply, "meta": {"provider": step_prov, "model": step_model}})
            session_output["turns"].append({
                "step": step_num,
                "label": label,
                "user": incoming_message,
                "assistant": reply,
                "provider": step_prov,
                "model": step_model
            })
            print(f"\n[Model Used]: Provider: {step_prov} | Model: {step_model}")
            print(f"\nASSISTANT (Deterministic Scope Interception):\n{reply}")
            continue

        # Pre-flight 3: Immediate Escalation check (Short fixed advice, no LLM call)
        esc_check = check_immediate_advocate_escalation(incoming_message)
        if esc_check.get("requires_real_lawyer", False):
            reason = esc_check.get("reason", "High-risk matter")
            reply = (
                f"🚨 **Please speak to a lawyer immediately:** This situation involves serious legal or criminal risk.\n"
                f"Escalation trigger: *{reason}*.\n"
                f"Please consult a practicing advocate immediately or call the free District Legal Services Authority (DLSA) / NALSA helpline at **15100**.\n\n"
                f"**Immediate safety steps:**\n"
                f"- **Keep written records:** Preserve all messages, notices, emails, and call logs.\n"
                f"- **Do not sign anything:** Do not sign any settlement, resignation, or admission under threat or pressure.\n"
                f"- **Speak to a lawyer or DLSA 15100:** NyayaMitra cannot predict what police or courts will do. Please contact your local District Legal Services Authority or call 15100 for official legal protection."
            )
            step_prov = "Deterministic Guard (No LLM)"
            step_model = "Safety Escalation Rule"
            chat_history.append({"role": "assistant", "content": reply, "meta": {"provider": step_prov, "model": step_model}})
            session_output["turns"].append({
                "step": step_num,
                "label": label,
                "user": incoming_message,
                "assistant": reply,
                "provider": step_prov,
                "model": step_model
            })
            print(f"\n[Model Used]: Provider: {step_prov} | Model: {step_model}")
            print(f"\nASSISTANT (Deterministic Emergency Escalation):\n{reply}")
            continue

        # Notice Generation trigger
        if "draft" in incoming_message.lower() and "notice" in incoming_message.lower() and case_dossier:
            notice_res = document_drafter.draft_demand_notice(case_dossier)
            reply = notice_res.get("notice_text", "")
            step_prov = getattr(engine, "last_used_provider", "Gemini")
            step_model = getattr(engine, "last_used_model", "gemini-3.5-flash-lite")
            chat_history.append({"role": "assistant", "content": reply, "meta": {"provider": step_prov, "model": step_model}})
            session_output["turns"].append({
                "step": step_num,
                "label": label,
                "user": incoming_message,
                "assistant": reply,
                "provider": step_prov,
                "model": step_model
            })
            print(f"\n[Model Used]: Provider: {step_prov} | Model: {step_model}")
            print(f"\nASSISTANT (Generated Pre-Litigation Legal Notice):\n{reply}")
            continue

        # Turn 1: Build Dossier & Rights Advice
        if case_dossier is None:
            dossier = case_builder.run(incoming_message)
            case_dossier = dossier
            case_category = dossier.get("category", "")

            rights = rights_advisor.run(case_dossier)
            standing_text = rights.get("plain_language_standing", "")
            options = rights.get("action_options", [])

            reply = f"{standing_text}\n\n"
            if options:
                reply += "### 🎯 Your Immediate Action Steps:\n"
                for opt in options[:2]:
                    tl = opt.get('suggested_timeline') or opt.get('timeline')
                    if tl:
                        if "suggest" not in tl.lower():
                            tl = f"Suggested: {tl}"
                        reply += f"- **{opt.get('title')}:** {opt.get('details')} *({tl})*\n"
                    else:
                        reply += f"- **{opt.get('title')}:** {opt.get('details')}\n"

            reply += "\n👉 **Take a look at the Case Intelligence panel on the right:** I've organized your case timeline and evidence checklist. You can ask follow-up questions, or click **Draft Legal Notice** anytime!"

            step_prov = getattr(engine, "last_used_provider", "Gemini")
            step_model = getattr(engine, "last_used_model", "gemini-3.5-flash-lite")
            chat_history.append({"role": "assistant", "content": reply, "meta": {"provider": step_prov, "model": step_model}})
            session_output["turns"].append({
                "step": step_num,
                "label": label,
                "user": incoming_message,
                "assistant": reply,
                "provider": step_prov,
                "model": step_model
            })
            print(f"\n[Model Used]: Provider: {step_prov} | Model: {step_model}")
            print(f"\nASSISTANT (Turn 1 Intake & Advice - Category Inherited: '{case_category}'):\n{reply}")

        # Subsequent Turns: Multi-Turn Dialogue
        else:
            answer = counselor.answer_followup(chat_history, case_dossier, incoming_message)
            step_prov = getattr(engine, "last_used_provider", "Gemini")
            step_model = getattr(engine, "last_used_model", "gemini-3.5-flash-lite")
            chat_history.append({"role": "assistant", "content": answer, "meta": {"provider": step_prov, "model": step_model}})
            session_output["turns"].append({
                "step": step_num,
                "label": label,
                "user": incoming_message,
                "assistant": answer,
                "provider": step_prov,
                "model": step_model
            })
            print(f"\n[Model Used]: Provider: {step_prov} | Model: {step_model}")
            print(f"\nASSISTANT (Follow-up Turn):\n{answer}")

    out_json_path = os.path.join(os.path.dirname(__file__), "single_session_output.json")
    with open(out_json_path, "w", encoding="utf-8") as f:
        json.dump(session_output, f, indent=2, ensure_ascii=False)
    print(f"\n[Saved Session Provenance and Outputs to {out_json_path}]")

    print("\n" + "=" * 80)
    print(" Session Completed Successfully!")
    print("=" * 80)

if __name__ == "__main__":
    run_session()
