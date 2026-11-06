"""
generate_test_outputs.py - Generates the official unedited raw test case outputs for NyayaMitra
Saves:
- test_cases/test_case_1_landlord_deposit.json
- test_cases/test_case_2_ecommerce_refund.json
- test_cases/test_case_3_unpaid_salary.json
- test_cases/raw_outputs_report.md
"""

import os
import json
from legal_kb import retrieve_verified_legal_context
from agents import CaseBuilderAgent, RightsAdvisorAgent, DocumentDrafterAgent, RoleplayOpponentAgent
from llm_engine import LegalLLMEngine

TEST_SCENARIOS = [
    {
        "id": "TC-01",
        "name": "Bengaluru Tenant Security Deposit Withholding",
        "category": "Tenancy & Rental",
        "raw_story": (
            "I was renting a 2BHK flat in HSR Layout, Bengaluru for 2 years at Rs 28,000/month. "
            "I gave 1 lakh rupees as security deposit. I gave proper 1-month notice on 1st October and vacated the flat on 31st October 2024. "
            "I cleared all electricity and water bills and handed over keys. Landlord Mr. Ramesh promised to refund the deposit via UPI in 3 days. "
            "Now it has been 25 days, he stopped picking my calls, and yesterday he messaged saying he is deducting Rs 45,000 for 'complete house repainting, "
            "marble polishing, and deep cleaning'. There was no damage, just normal nail holes for photo frames and standard wear and tear. "
            "I have move-in photos, move-out handover video, all rent payment bank statements, and WhatsApp chat where he acknowledged receiving the flat in good condition. "
            "How can I get my Rs 45,000 back?"
        ),
        "sample_roleplay_user_turn": "Mr. Ramesh, as per Section 108 of the Transfer of Property Act and the Model Tenancy framework, ordinary wear and tear like wall paint aging cannot be deducted from my deposit. I have the handover video and our chat proof. Please refund my balance 45,000 within 7 days."
    },
    {
        "id": "TC-02",
        "name": "E-Commerce Defective Smartphone Refund Denial",
        "category": "Consumer & E-Commerce",
        "raw_story": (
            "I ordered a Samsung Galaxy smartphone worth Rs 26,999 on an e-commerce app on 10th November 2024. "
            "It was delivered on 14th November. Within 24 hours of opening the box, the screen started flickering with green lines and touch stopped working. "
            "I raised a replacement request on 15th November. The app sent a technician for inspection on 21st November. The technician confirmed it is a manufacturing hardware defect "
            "and took sign on his job sheet. But on 23rd November, customer support cancelled my return request stating 'The 7-day return window expired on 21st November'. "
            "They are telling me to go to an authorized brand service center 40 km away. I paid for a brand new working phone, not a defective phone repaired on day one. "
            "I have the invoice, delivery receipt, technician inspection job sheet copy, and chat screenshots."
        ),
        "sample_roleplay_user_turn": "Under Section 2(11) and Section 84 of the Consumer Protection Act 2019, delivering a defective phone and delaying inspection past your return window is a clear deficiency in service and unfair trade practice. I have the technician report confirming hardware fault. I demand an immediate refund or I will escalate to the National Consumer Helpline and e-Daakhil."
    },
    {
        "id": "TC-03",
        "name": "Gurugram Tech Employee Unpaid Salary & Relieving Letter Withheld",
        "category": "Employment & Salary",
        "raw_story": (
            "I worked as a frontend developer at an IT consultancy firm in Cyber City, Gurugram for 18 months at Rs 70,000/month. "
            "I submitted my resignation on 1st August 2024 and completed my full 60-day notice period till 30th September 2024. "
            "All project handovers and company assets (MacBook, ID card) were handed over and I received an asset clearance certificate from IT. "
            "My August salary was delayed, and my September salary plus 15 days encashable leave (total Rs 1,65,000) has not been paid. "
            "It has been 50 days since my last working day. Whenever I email HR, they say 'finance team is facing client payment delays'. "
            "More importantly, they are withholding my Relieving Letter and Experience Certificate. My new employer is threatening to cancel my job offer if I don't submit my relieving letter by end of this week. "
            "I have my appointment letter, resignation acceptance email, and signed clearance form."
        ),
        "sample_roleplay_user_turn": "Under the Payment of Wages Act and Delhi/Haryana Shops and Commercial Establishments rules, full and final dues must be cleared within 30 days of exit, and withholding my relieving letter violates my right to livelihood under Article 21. If my Rs 1,65,000 and relieving letter are not issued within 3 days, I will file a formal complaint with the District Labor Commissioner."
    }
]

def run_all_test_cases():
    # Use Gemini or offline engine
    engine = LegalLLMEngine()
    case_builder = CaseBuilderAgent(engine)
    rights_advisor = RightsAdvisorAgent(engine)
    doc_drafter = DocumentDrafterAgent(engine)
    opponent_roleplay = RoleplayOpponentAgent(engine)

    outputs = []
    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_cases_dir = os.path.join(base_dir, "test_cases")
    os.makedirs(test_cases_dir, exist_ok=True)

    for scenario in TEST_SCENARIOS:
        print(f"Running {scenario['id']}: {scenario['name']}...")
        
        # 1. Build Case
        dossier = case_builder.run(scenario["raw_story"])
        
        # 2. Rights Advice
        rights = rights_advisor.run(dossier)
        
        # 3. Document Draft
        notice_draft = doc_drafter.run(dossier, rights, doc_type="Legal Demand Notice")
        
        # 4. Roleplay Turn
        roleplay_res = opponent_roleplay.run(
            dossier, 
            [{"role": "assistant", "content": "Look, as per company policy / house rules, deductions are final."}],
            scenario["sample_roleplay_user_turn"]
        )

        full_output = {
            "test_case_id": scenario["id"],
            "name": scenario["name"],
            "raw_input": scenario["raw_story"],
            "case_dossier": dossier,
            "rights_advice": rights,
            "legal_notice_draft": notice_draft,
            "sample_roleplay_turn": {
                "user_argument": scenario["sample_roleplay_user_turn"],
                "opponent_response": roleplay_res
            }
        }

        # Save individual JSON
        filename = f"{scenario['id'].lower().replace('-', '_')}_{scenario['category'].lower().split()[0]}.json"
        filepath = os.path.join(test_cases_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(full_output, f, indent=2)

        outputs.append(full_output)

    # Write Markdown Report
    report_path = os.path.join(test_cases_dir, "raw_outputs_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# NyayaMitra - Unedited Raw Outputs for Problem 2 Test Cases\n\n")
        f.write("> **Evaluation Deliverable:** Official raw test case execution logs showing Case Intake, Legal Standing, Document Draft, and Roleplay Arena.\n\n")
        
        for out in outputs:
            f.write(f"## {out['test_case_id']}: {out['name']}\n\n")
            f.write("### 1. Raw User Input\n")
            f.write(f"```text\n{out['raw_input']}\n```\n\n")
            
            f.write("### 2. Extracted Case Dossier (Facts, Timeline & Evidence Checklist)\n")
            f.write(f"```json\n{json.dumps(out['case_dossier'], indent=2)}\n```\n\n")
            
            f.write("### 3. Plain-Language Rights & Grounded Statutory Analysis\n")
            f.write(f"```json\n{json.dumps(out['rights_advice'], indent=2)}\n```\n\n")
            
            f.write("### 4. Generated Legal Demand Notice\n")
            f.write(f"{out['legal_notice_draft']}\n\n")
            
            f.write("### 5. Roleplay Negotiation Arena\n")
            f.write(f"- **User Argument:** *\"{out['sample_roleplay_turn']['user_argument']}\"*\n")
            f.write(f"- **Opponent Reaction:** {out['sample_roleplay_turn']['opponent_response'].get('opponent_reply', '')}\n")
            f.write(f"- **Coach Feedback:** {json.dumps(out['sample_roleplay_turn']['opponent_response'].get('coach_evaluation', {}), indent=2)}\n\n")
            f.write("---\n\n")

    print(f"✅ Generated all test outputs and markdown report at {report_path}")

if __name__ == "__main__":
    run_all_test_cases()

