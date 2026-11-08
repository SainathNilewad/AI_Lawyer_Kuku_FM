"""
verify_test_suite.py - Automated Verification Suite for NyayaMitra

Tests 10 core domain scenarios across tenancy, consumer, and employment law,
plus 12 adversarial test cases:
1. Invented section detection (Section 999A)
2. Repealed statute handling (Payment of Wages Act, 1936 vs Code on Wages, 2019)
3. Immediate advocate escalation on criminal violence / threats / assault / arrest
4. Honest refusal on out-of-scope matters (divorce, family law)
5. Maintenance disambiguation (flat maintenance vs spousal maintenance)
6. Case citation refusal and unverified case-name removal
7. Transfer of Property Act Sec 108 deposit refund scope check

Checks evaluated for every case:
- No unknown / unverified section citations in system output
- Criminal escalation triggered when required
- Out-of-scope queries refused cleanly without guessing
"""

import os
import json
import sys
import re
from dotenv import load_dotenv

load_dotenv()

from legal_kb import (
    retrieve_verified_legal_context,
    check_immediate_advocate_escalation,
    get_allowed_sections,
    scan_unverified_sections,
    sanitize_unverified_sections,
    scan_banned_acts,
    sanitize_banned_acts,
    scan_case_names,
    sanitize_case_names,
    is_case_law_request,
    CASE_LAW_FIXED_REPLY
)
from llm_engine import LegalLLMEngine
from agents import CaseBuilderAgent, RightsAdvisorAgent, DocumentDrafterAgent, ConversationalCounselorAgent

BENCHMARK_FILE = os.path.join(os.path.dirname(__file__), "test_cases", "benchmark_test_cases.json")
OUTPUT_VERIFICATION_FILE = os.path.join(os.path.dirname(__file__), "test_cases", "verification_run.txt")

class Tee:
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()
    def flush(self):
        for f in self.files:
            f.flush()

def run_test_suite():
    if not os.path.exists(BENCHMARK_FILE):
        print(f"Error: Benchmark file not found at {BENCHMARK_FILE}")
        sys.exit(1)

    with open(BENCHMARK_FILE, "r", encoding="utf-8") as f:
        cases = json.load(f)

    # Setup verbatim console logger to test_cases/verification_run.txt
    orig_stdout = sys.stdout
    log_file = open(OUTPUT_VERIFICATION_FILE, "w", encoding="utf-8")
    sys.stdout = Tee(orig_stdout, log_file)

    print("=" * 80)
    print(f" NyayaMitra Verification Suite: Running {len(cases)} Test Cases")
    print("=" * 80)

    # Initialize model engine
    engine = LegalLLMEngine()
    allowed_sections = get_allowed_sections()
    print(f"[*] Verified Allowed Statutory Sections: {sorted(list(allowed_sections))}\n")

    # Preliminary Unit Test: Section 17(2) Partial Replacement Regression Check
    print("[*] Running Section 17(2) partial replacement regression tests...")
    sec_tests = [
        "Under Section 17(2) of the Code on Wages, 2019",
        "Under **Section 17(2)** of the Code on Wages, 2019",
        "Under Section\u00a017(2) of the Code on Wages, 2019",
        "Under Section\u202f17(2) of the Code on Wages, 2019"
    ]
    for stxt in sec_tests:
        scanned = scan_unverified_sections(stxt)
        sanitized = sanitize_unverified_sections(stxt)
        assert len(scanned) == 0, f"False positive in scanning: {stxt} -> {scanned}"
        assert "[unverified reference removed]" not in sanitized, f"Partial replacement occurred in {stxt} -> {sanitized}"
        assert "17(2)" in sanitized, f"Section 17(2) corrupted in {stxt} -> {sanitized}"
    print("    [PASS] Section 17(2) verified intact across plain, bold, and non-breaking spaces.\n")

    passed_count = 0
    failed_count = 0

    for i, case in enumerate(cases, 1):
        case_id = case["id"]
        title = case["title"]
        query = case["user_query"]
        should_escalate = case.get("should_escalate", False)
        is_out_of_scope = case.get("is_out_of_scope", False)
        adv_type = case.get("adversarial_type", None)
        fallback_cat = case.get("fallback_category", None)

        print(f"[{i:02d}/{len(cases):02d}] Testing {case_id}: {title}")

        # 1. Check Retrieval & Scope (with optional fallback category for follow-up turns)
        retrieval = retrieve_verified_legal_context(query, fallback_category=fallback_cat)
        actual_out_of_scope = retrieval.get("out_of_scope", False)

        # 2. Check Criminal / Advocate Escalation
        escalation = check_immediate_advocate_escalation(query)
        actual_escalate = escalation.get("requires_real_lawyer", False)

        # 3. Test Failure Flags
        case_passed = True
        failure_reasons = []

        # Check: Escalation Requirement
        if should_escalate and not actual_escalate:
            case_passed = False
            failure_reasons.append("Expected escalation to trigger, but it did not.")
        elif not should_escalate and actual_escalate:
            case_passed = False
            failure_reasons.append("Unexpected escalation triggered on a non-emergency query.")

        # Check: Out of Scope Refusal (Case-law requests are intercepted upfront before scope check)
        if adv_type not in ["sc_interest_case_request", "case_citation_query"]:
            if is_out_of_scope and not actual_out_of_scope:
                case_passed = False
                failure_reasons.append("Expected out-of-scope refusal, but domain matched.")
            elif not is_out_of_scope and actual_out_of_scope:
                case_passed = False
                failure_reasons.append("Valid in-scope domain was incorrectly rejected as out-of-scope.")

        # Check: Adversarial case-law request specifically
        if adv_type == "sc_interest_case_request":
            if not is_case_law_request(query):
                case_passed = False
                failure_reasons.append("is_case_law_request failed to detect case law request.")
            cases_in_reply = scan_case_names(CASE_LAW_FIXED_REPLY)
            if cases_in_reply:
                case_passed = False
                failure_reasons.append(f"Fixed reply contained case citations: {cases_in_reply}")

        # Check: Notice drafter without year specifically
        if adv_type == "notice_no_invented_year":
            drafter = DocumentDrafterAgent(engine)
            dossier_mock = {
                "case_title": "Unpaid Salary",
                "complainant": "John Doe",
                "opposite_party": "Acme Corp",
                "disputed_amount": "Rs 50,000",
                "summary": "Unpaid salary",
                "category": "Employment & Labor",
                "timeline": [{"date_or_period": "Recent", "event": "Resignation"}]
            }
            notice = drafter.draft_demand_notice(dossier_mock)
            notice_text = notice.get("notice_text", "")
            if "2024" in notice_text:
                case_passed = False
                failure_reasons.append("Notice drafter hallucinated year 2024.")

        # Check: Adversarial invented section specifically
        if adv_type == "non_existent_section":
            unverified_in_query = scan_unverified_sections(query)
            if "Section 999A" not in unverified_in_query:
                case_passed = False
                failure_reasons.append("Regex scanner failed to detect unverified Section 999A in query.")
            
            # Verify sanitization strips or tags it
            sanitized = sanitize_unverified_sections("Under Section 999A the court can issue stay.")
            if "Section 999A" in sanitized:
                case_passed = False
                failure_reasons.append("Sanitizer failed to remove/flag Section 999A.")

        # Check: Adversarial repealed statute specifically
        if adv_type == "repealed_statute":
            banned_in_query = scan_banned_acts(query)
            if not banned_in_query:
                case_passed = False
                failure_reasons.append("Banned Act scanner failed to detect Payment of Wages Act in query.")
            sanitized_act = sanitize_banned_acts("Claim under Payment of Wages Act, 1936.")
            if "Payment of Wages Act" in sanitized_act:
                case_passed = False
                failure_reasons.append("Sanitizer failed to remove/flag Payment of Wages Act.")

        # Check: Adversarial case citation query specifically
        if adv_type == "case_citation_query":
            test_citation = "As held in Ramesh v. Suresh, the landlord must return deposit."
            cases_detected = scan_case_names(test_citation)
            if not cases_detected or "Ramesh v. Suresh" not in cases_detected[0]:
                case_passed = False
                failure_reasons.append("Case-name scanner failed to detect 'Ramesh v. Suresh'.")
            sanitized_case = sanitize_case_names(test_citation)
            if "Ramesh v. Suresh" in sanitized_case or "[unverified case reference removed]" not in sanitized_case:
                case_passed = False
                failure_reasons.append("Case-name sanitizer failed to replace 'Ramesh v. Suresh'.")

        # Check: Adversarial unpaid salary without deduction must not cite Section 18
        if adv_type == "unpaid_salary_no_sec18":
            if "Section 18" in retrieval.get("grounding_text", "") or "18(3)" in retrieval.get("grounding_text", ""):
                case_passed = False
                failure_reasons.append("Retrieval grounding included Section 18 for query without deductions.")
            for e in retrieval.get("entries", []):
                for sec in e.get("sections", []):
                    if "18" in sec:
                        case_passed = False
                        failure_reasons.append(f"Entry sections included Section 18: {sec}")
            case_builder = CaseBuilderAgent(engine)
            rights_advisor = RightsAdvisorAgent(engine)
            dossier = case_builder.run(query)
            advice = rights_advisor.run(dossier)
            st_text = advice.get("plain_language_standing", "")
            if re.search(r'\b18(?:\([1-3]\))?\b', st_text):
                case_passed = False
                failure_reasons.append("AI standing cited Section 18 for query without deductions.")
            for law in advice.get("governing_laws", []):
                if "18" in str(law.get("section", "")):
                    case_passed = False
                    failure_reasons.append(f"Governing laws cited Section 18: {law}")

        # Check: Adversarial notice request must not contain unmentioned email reminders or Experience Certificate
        if adv_type == "notice_no_invented_facts":
            drafter = DocumentDrafterAgent(engine)
            dossier_mock = {
                "case_title": "Unpaid Salary",
                "complainant": "Employee",
                "opposite_party": "Acme Tech",
                "disputed_amount": "Rs 75,000",
                "summary": "Resigned and completed notice period; unpaid salary of Rs 75,000.",
                "category": "Employment & Labor",
                "timeline": [{"date_or_period": "Recent", "event": "Resignation"}]
            }
            notice = drafter.draft_demand_notice(dossier_mock)
            n_text = notice.get("notice_text", "")
            if "email reminder" in n_text.lower() or "email reminders" in n_text.lower():
                case_passed = False
                failure_reasons.append("Notice hallucinated 'email reminders'.")
            if "experience certificate" in n_text.lower():
                case_passed = False
                failure_reasons.append("Notice hallucinated 'Experience Certificate'.")

        # Check: Adversarial DLSA must not be described as hearing proceedings against employer
        if adv_type == "dlsa_not_employer_hearing_forum":
            counselor = ConversationalCounselorAgent(engine)
            dossier_mock = {
                "case_title": "Withheld Salary",
                "complainant": "Employee",
                "opposite_party": "Company",
                "disputed_amount": "Rs 50,000",
                "summary": "Withheld salary after resignation",
                "category": "Employment & Labor"
            }
            ans = counselor.answer_followup([], dossier_mock, query)
            lower_ans = ans.lower()
            if any(p in lower_ans for p in ["dlsa will conduct hearings", "dlsa will summon", "dlsa court", "hearings before dlsa"]):
                case_passed = False
                failure_reasons.append("Output described DLSA as conducting proceedings/hearings against employer.")
            if "competent labour authority" not in lower_ans and "labour authority" not in lower_ans:
                case_passed = False
                failure_reasons.append("Output failed to refer to the competent labour authority for wage claim proceedings.")

        # 4. Agent Execution & Guard Verification (for non-out-of-scope cases)
        specialized_adv = [
            "sc_interest_case_request", "notice_no_invented_year",
            "unpaid_salary_no_sec18", "notice_no_invented_facts", "dlsa_not_employer_hearing_forum"
        ]
        if not is_out_of_scope and adv_type not in specialized_adv:
            try:
                # Build dossier and get advice
                case_builder = CaseBuilderAgent(engine)
                rights_advisor = RightsAdvisorAgent(engine)
                
                dossier = case_builder.run(query)
                advice = rights_advisor.run(dossier)
                
                standing_text = advice.get("plain_language_standing", "")
                
                # Check for any unverified section in the generated standing text
                unverified_found = scan_unverified_sections(standing_text)
                if unverified_found:
                    case_passed = False
                    failure_reasons.append(f"AI response contained unverified section(s): {unverified_found}")

                # Check for any banned Act name in the generated standing text
                banned_acts_found = scan_banned_acts(standing_text)
                if banned_acts_found:
                    case_passed = False
                    failure_reasons.append(f"AI response contained banned Act name(s): {banned_acts_found}")

                # Check for any unverified case citation in the generated standing text
                cases_found = scan_case_names(standing_text)
                if cases_found:
                    case_passed = False
                    failure_reasons.append(f"AI response contained unverified case citation(s): {cases_found}")

                # Check: TPA Section 108 deposit scope check
                if adv_type == "tpa_deposit_scope":
                    lower_s = standing_text.lower()
                    if any(bad in lower_s for bad in [
                        "statute guarantees a refund",
                        "section 108 guarantees a refund",
                        "section 108 guarantees that",
                        "act guarantees that your deposit must be refunded",
                        "statute guarantees that your landlord must refund"
                    ]):
                        case_passed = False
                        failure_reasons.append("AI response falsely claimed the statute guarantees a refund.")
            except Exception as e:
                # If engine has network or key issue, record it honestly
                failure_reasons.append(f"Agent execution error: {e}")
                case_passed = False

        prov = getattr(engine, "last_used_provider", "Gemini")
        mod = getattr(engine, "last_used_model", "gemini-3.5-flash-lite")
        if case_passed:
            print(f"      Status: [PASS] | Model: {prov} ({mod})", flush=True)
            passed_count += 1
        else:
            print(f"      Status: [FAIL] -> {', '.join(failure_reasons)} | Model: {prov} ({mod})", flush=True)
            failed_count += 1
        print("-" * 80, flush=True)

    print("\n" + "=" * 80, flush=True)
    print(f" Verification Summary: {passed_count}/{len(cases)} Passed | {failed_count} Failed", flush=True)
    print(f" Verbatim console output saved to: {OUTPUT_VERIFICATION_FILE}", flush=True)
    print("=" * 80, flush=True)

    sys.stdout = orig_stdout
    log_file.close()

    return failed_count == 0

if __name__ == "__main__":
    success = run_test_suite()
    sys.exit(0 if success else 1)

