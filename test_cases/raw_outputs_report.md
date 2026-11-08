# NyayaMitra - Official Unedited Raw Outputs for Test Cases

> **Execution Metadata:** Generated on `2026-11-08T20:12:15.744108+00:00` using Provider: `Gemini`, Model: `gemini-3.5-flash-lite`.
> **Strict Ground Rule:** Real agent calls only. No post-editing, no mock datasets.

## TC-01: Bengaluru Tenant Security Deposit Withholding

- **Timestamp:** `2026-11-08T20:11:19.082413+00:00`
- **Provider / Model:** `Gemini` / `gemini-3.5-flash-lite`
- **Category:** `Tenancy & Rental`

### 1. Raw User Input
```text
I was renting a 2BHK flat in HSR Layout, Bengaluru for 2 years at Rs 28,000/month. I gave 1 lakh rupees as security deposit. I gave proper 1-month notice on 1st October and vacated the flat on 31st October 2024. I cleared all electricity and water bills and handed over keys. Landlord Mr. Ramesh promised to refund the deposit via UPI in 3 days. Now it has been 25 days, he stopped picking my calls, and yesterday he messaged saying he is deducting Rs 45,000 for 'complete house repainting, marble polishing, and deep cleaning'. There was no damage, just normal nail holes for photo frames and standard wear and tear. I have move-in photos, move-out handover video, all rent payment bank statements, and WhatsApp chat where he acknowledged receiving the flat in good condition. How can I get my Rs 45,000 back?
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Arbitrary Security Deposit Deduction by Landlord in Bengaluru",
  "category": "Tenancy & Rental",
  "summary": "Tenant vacated a 2BHK flat in Bengaluru after providing proper notice and clearing all utility bills. Landlord has withheld Rs 45,000 from the Rs 1,00,000 security deposit under the guise of repainting and cleaning, despite prior acknowledgment that the flat was handed over in good condition.",
  "complainant": "Tenant",
  "opposite_party": "Landlord Mr. Ramesh",
  "disputed_amount": "Rs. 45,000",
  "timeline": [
    {
      "date_or_period": "2 years",
      "event": "Tenancy period for 2BHK flat in HSR Layout, Bengaluru at Rs 28,000/month with Rs 1,00,000 security deposit."
    },
    {
      "date_or_period": "1st October 2024",
      "event": "Tenant gave proper 1-month notice to vacate the flat."
    },
    {
      "date_or_period": "31st October 2024",
      "event": "Tenant vacated the flat, cleared all electricity and water bills, and handed over keys."
    },
    {
      "date_or_period": "3 days post-vacation",
      "event": "Landlord Mr. Ramesh promised to refund the deposit via UPI, but failed to do so."
    },
    {
      "date_or_period": "25 days post-vacation",
      "event": "Landlord stopped picking calls and messaged a deduction of Rs 45,000 for repainting, marble polishing, and deep cleaning."
    }
  ],
  "evidence_held": [
    "Move-in photos",
    "Move-out handover video",
    "All rent payment bank statements",
    "WhatsApp chat acknowledging flat was received in good condition"
  ],
  "evidence_needed": [
    "Written Rent Agreement specifying security deposit refund terms and wear-and-tear clauses",
    "Formal written demand or legal notice regarding the full deposit refund"
  ],
  "evidence_strength_score": 8,
  "evidence_strength_explanation": "Strong documentary and visual proof including handover video, bank statements, and WhatsApp acknowledgment of good condition.",
  "escalation_check": {
    "requires_real_lawyer": false,
    "reasons": [],
    "legal_aid_contact": "District Legal Services Authority (DLSA) / NALSA Toll-Free Helpline: 15100"
  }
}
```

### 3. Plain-Language Rights & Statutory Standing (Direct Model Output)
```json
{
  "plain_language_standing": "You have a strong civil claim to recover the unlawfully deducted security deposit from your landlord under Indian rental and property principles. Under the law, routine aging and normal use of a property are considered reasonable wear and tear, and a landlord cannot make arbitrary deductions for standard repainting or cleaning if the property was handed over in good condition. Since your dispute involves a financial disagreement and breach of rental understandings, it is strictly a civil matter rather than a criminal offense.\n\nYour core legal standing is firmly supported by your visual evidence, bank statements, and WhatsApp chat acknowledgments from the landlord. Your immediate takeaway is to formally demand the full refund of your security deposit using your documented proof before pursuing formal civil remedies.",
  "governing_laws": [
    {
      "act_name": "Transfer of Property Act, 1882",
      "section": "Section 108(B)(m)",
      "relevance": "Protects tenants from bearing the cost of changes caused by reasonable wear and tear or routine property aging when handing over possession."
    },
    {
      "act_name": "General Legal Principle (Civil vs. Criminal Boundary)",
      "section": "General Guidance",
      "relevance": "Clarifies that withholding a deposit or breaching a contract is a civil dispute, meaning criminal police complaints are not appropriate unless fraud existed from inception."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Immediate Pre-Litigation Action (Formal Legal Notice)",
      "timeline": "Suggested 15 days (customary pre-litigation practice)",
      "details": "Serve a formal written legal notice to the landlord citing Section 108(B)(m) of the Transfer of Property Act, attaching your move-out handover video, bank statements, and WhatsApp chats to demand the full refund of the unlawfully deducted security deposit."
    },
    {
      "step_number": 2,
      "title": "Statutory Authority / Grievance Portal Filing",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "Approach the local Rent Authority or civil forum (confirm locally). Note: DLSA provides free legal aid and guidance only (Helpline 15100); it is never a forum for hearings or proceedings against a landlord."
    },
    {
      "step_number": 3,
      "title": "Statutory Forum / Civil Court Petition",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "If the landlord fails to respond or refund the amount after the legal notice period, file a recovery suit or summary suit for money recovery before the local civil court or Small Causes Court."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "You can initiate pre-litigation notices and represent yourself or seek free guidance from the District Legal Services Authority (DLSA Helpline 15100). However, engaging a physical advocate is recommended if you decide to file a formal civil recovery suit in court for better procedural handling.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
**LEGAL DEMAND NOTICE**

**BY SPEED POST WITH ACKNOWLEDGEMENT DUE (AD) / REGISTERED EMAIL**

**Date:** 09/11/2026

**To:** 
Mr. Ramesh 
[Landlord Address / Contact Details as known] 

**From (Complainant / Tenant):** 
[Tenant Name] 
[Tenant Address / Contact Details] 

---

**SUBJECT: LEGAL DEMAND FOR IMMEDIATE REFUND OF UNLAWFULLY DEDUCTED SECURITY DEPOSIT OF RS. 45,000/- REGARDING THE TENANCY OF PREMISES LOCATED IN HSR LAYOUT, BENGALURU.**

Sir,

Under instructions from my client, [Tenant Name], I/the undersigned do hereby serve upon you this formal Legal Demand Notice calling upon you to refund the unlawfully deducted security deposit amount of **Rs. 45,000/-** (Rupees Forty-Five Thousand Only) within **15 days** from the receipt of this notice, failing which my client shall be constrained to initiate appropriate legal proceedings before the competent civil forum. 

The facts and circumstances giving rise to this notice are detailed as under:

### 1. FACTUAL SEQUENCE & TIMELINE
1. **Tenancy Period:** That my client resided as a lawful tenant in your 2BHK residential flat situated in HSR Layout, Bengaluru, for a duration of **2 years**, paying a monthly rent of Rs. 28,000/- and having deposited a total sum of **Rs. 1,00,000/-** as an interest-free security deposit at the commencement of the tenancy.
2. **Notice to Vacate:** That on **1st October 2024**, in full compliance with the rental understanding, my client duly served a proper 1-month notice expressing the intention to vacate the said flat.
3. **Vacating and Handover:** That on **31st October 2024**, my client completely vacated the flat, cleared all outstanding electricity and water utility bills in full, and formally handed over the physical keys of the premises to you. 
4. **Initial Promise:** That **3 days post-vacation**, you explicitly promised to refund the full security deposit via UPI transfer, but failed to honor your commitment.
5. **Arbitrary Deduction:** That **25 days post-vacation**, after suddenly stopping answering my client's phone calls, you sent a text message arbitrarily deducting **Rs. 45,000/-** from the security deposit under the pretext of repainting, marble polishing, and deep cleaning.

### 2. AVAILABILITY OF EVIDENCE
My client's position is backed by irrefutable documentary and visual evidence, including:
* Move-in photographs and the move-out handover video establishing the good condition of the flat upon exit.
* All monthly rent payment bank statements.
* WhatsApp chat logs and acknowledgments explicitly confirming that the flat was handed over to you in good condition.

### 3. VIOLATION OF STATUTORY PROVISIONS & LEGAL STANDING
1. Under **Section 108(B)(m) of the Transfer of Property Act, 1882**, a tenant is bound to restore the property in as good a condition as it was in at the time he was put in possession, subject only to reasonable wear and tear and damage caused by irresistible force. Routine aging, standard property wear and tear, and normal usage cannot be made a financial liability of the tenant.
2. Your arbitrary deduction of Rs. 45,000/- for repainting and deep cleaning despite prior acknowledgment that the flat was received in good condition constitutes an unlawful withholding of my client's hard-earned money and a breach of trust.
3. Please note that this is strictly a civil dispute concerning financial recovery and breach of rental understanding. 

---

### DEMAND FOR RECTIFICATION

You are hereby called upon to refund the unlawfully withheld balance security deposit amount of **Rs. 45,000/-** to my client via proper banking channels within **15 days** from the receipt of this notice.

If you fail to clear the said dues within the stipulated 15-day rectification window, my client reserves the right to initiate formal civil recovery proceedings before the appropriate civil court / Small Causes Court to recover the principal amount along with applicable costs and legal expenses. 

*Note: For free legal guidance regarding your rights or options, you may contact the District Legal Services Authority (DLSA) / NALSA Toll-Free Helpline at 15100.*

A copy of this notice is retained in my office records for future reference and necessary action.

Yours faithfully,

*(Signature)* 
**[Tenant Name / Counsel for Tenant]** 
[Contact Number] 
[Email Address] 

---

### ANNEXURE INVENTORY
1. Copy of Move-in Photos and Move-out Handover Video (Digital/Print Reference)
2. Copies of Rent Payment Bank Statements
3. Transcripts / Screenshots of WhatsApp Chats acknowledging flat was received in good condition

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Mr. Ramesh, as per Section 108 of the Transfer of Property Act and the Model Tenancy framework, ordinary wear and tear like wall paint aging cannot be deducted from my deposit. I have the handover video and our chat proof. Please refund my balance 45,000 within 7 days."*
- **Opponent Reaction:** Arre sahib, don't teach me Section-Vection! Agreement mein clearly likha hai flat must be returned in pristine, freshly painted condition. Video-vudio se kya hota hai, wear and tear toh hota hi hai na! Chalo, 45 thousand toh impossible hai, 15 thousand kaat ke baki le lo final settlement.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You effectively cited the Transfer of Property Act and Model Tenancy Act, while referencing concrete proof (handover video and chat logs) and setting a firm timeline.",
  "what_to_improve": "Reiterate that withholding a deposit without itemized bills or actual receipts is legally untenable. Stand firm on the 7-day deadline without compromising.",
  "suggested_next_counter": "Mr. Ramesh, verbal agreements or arbitrary deductions override neither the Transfer of Property Act nor our written WhatsApp acknowledgment. Provide official GST repair bills for the exact amount, or refund the full Rs. 45,000 by our deadline."
}
```

---

## TC-02: E-Commerce Defective Smartphone Refund Denial

- **Timestamp:** `2026-11-08T20:11:35.752550+00:00`
- **Provider / Model:** `Gemini` / `gemini-3.5-flash-lite`
- **Category:** `Consumer & E-Commerce`

### 1. Raw User Input
```text
I ordered a Samsung Galaxy smartphone worth Rs 26,999 on an e-commerce app on 10th November 2024. It was delivered on 14th November. Within 24 hours of opening the box, the screen started flickering with green lines and touch stopped working. I raised a replacement request on 15th November. The app sent a technician for inspection on 21st November. The technician confirmed it is a manufacturing hardware defect and took sign on his job sheet. But on 23rd November, customer support cancelled my return request stating 'The 7-day return window expired on 21st November'. They are telling me to go to an authorized brand service center 40 km away. I paid for a brand new working phone, not a defective phone repaired on day one. I have the invoice, delivery receipt, technician inspection job sheet copy, and chat screenshots.
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Defective Smartphone Delivery & Arbitrary Return Cancellation",
  "category": "Consumer & E-Commerce",
  "summary": "The user purchased a Samsung Galaxy smartphone for Rs 26,999, which arrived with a manufacturing defect. Although a replacement request was raised within 24 hours of delivery and a technician verified the hardware defect within the 7-day window, customer support arbitrarily cancelled the return citing expiration of the window.",
  "complainant": "Consumer",
  "opposite_party": "E-Commerce Platform / Seller",
  "disputed_amount": "Rs. 26,999",
  "timeline": [
    {
      "date_or_period": "10th November 2024",
      "event": "Ordered Samsung Galaxy smartphone worth Rs 26,999 on the e-commerce app."
    },
    {
      "date_or_period": "14th November 2024",
      "event": "Smartphone was delivered to the user."
    },
    {
      "date_or_period": "Within 24 hours of delivery",
      "event": "Screen started flickering with green lines and touch stopped working; user noticed the defect."
    },
    {
      "date_or_period": "15th November 2024",
      "event": "Raised a replacement request on the e-commerce app."
    },
    {
      "date_or_period": "21st November 2024",
      "event": "Technician sent by the app inspected the phone, confirmed the manufacturing hardware defect, and took a signature on the job sheet."
    },
    {
      "date_or_period": "23rd November 2024",
      "event": "Customer support cancelled the return request claiming the 7-day return window expired on 21st November and directed the user to a brand service center."
    }
  ],
  "evidence_held": [
    "Tax invoice",
    "Delivery receipt",
    "Technician inspection job sheet copy",
    "Customer support chat screenshots"
  ],
  "evidence_needed": [
    "Unboxing video or photos showing the defect immediately upon delivery (if available)",
    "Written refusal email or chat log from customer support showing the cancellation reason"
  ],
  "evidence_strength_score": 8,
  "evidence_strength_explanation": "Strong documentary evidence including tax invoice, delivery receipt, and an official technician job sheet confirming the manufacturing defect.",
  "escalation_check": {
    "requires_real_lawyer": false,
    "reasons": [],
    "legal_aid_contact": "District Legal Services Authority (DLSA) / NALSA Toll-Free Helpline: 15100"
  }
}
```

### 3. Plain-Language Rights & Statutory Standing (Direct Model Output)
```json
{
  "plain_language_standing": "You have a strong consumer protection claim because your smartphone arrived with a verified manufacturing defect and your return request was initiated on time. Under Indian consumer law, selling defective goods and arbitrarily cancelling a valid return amounts to unfair trade practices and deficiency in service. You can successfully seek a full refund or replacement, along with compensation, through consumer dispute forums without needing a lawyer.",
  "governing_laws": [
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(7)",
      "relevance": "Defines you as a consumer since you purchased goods for consideration."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(10)",
      "relevance": "Covers manufacturing defects and shortcomings in product quality."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(11)",
      "relevance": "Defines deficiency in service for arbitrary cancellation of return and poor customer support."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(47)",
      "relevance": "Classifies deceptive practices and refusal to refund/replace within stipulated timelines as an unfair trade practice."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 84",
      "relevance": "Establishes product manufacturer liability for manufacturing defects regardless of negligence."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 35",
      "relevance": "Provides the statutory right and electronic filing mechanism for a consumer complaint before the District Commission."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Immediate Pre-Litigation Action",
      "timeline": "Suggested 15 days (customary pre-litigation practice)",
      "details": "Serve a formal Legal Demand Notice to the e-commerce platform and seller enclosing your tax invoice, delivery receipt, and the technician inspection job sheet."
    },
    {
      "step_number": 2,
      "title": "Statutory Authority / Grievance Portal Filing",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "Lodge a formal complaint on the National Consumer Helpline (NCH) toll-free number 1915 or via consumerhelpline.gov.in. Note: DLSA helpline 15100 provides free legal aid and guidance only; it is never a forum for hearings or proceedings."
    },
    {
      "step_number": 3,
      "title": "Statutory Forum / Consumer Commission Petition",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "File an electronic consumer complaint online on e-Daakhil (edaakhil.nic.in) attaching your order invoice, defect photos, technician job sheet, and customer support chat logs."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "Consumer Commissions are designed for self-representation, allowing you to argue your case and present evidence personally without hiring a licensed advocate.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
**LEGAL DEMAND NOTICE**

**MODE OF DISPATCH:** Speed Post with Acknowledgement Due (AD) / Registered Email 
**DATE:** 09/11/2026 

**FROM:** 
[Complainant / Consumer Name] 
[Complainant Address Line 1] 
[Complainant Address Line 2] 
Phone: [Complainant Phone Number] 
Email: [Complainant Email Address] 

**TO:** 
1. **The Grievance Officer / Managing Director** 
 [E-Commerce Platform Name / Seller Name] 
 [Company Address Line 1] 
 [Company Address Line 2] 

---

**SUBJECT: LEGAL DEMAND NOTICE FOR DEFECTIVE PRODUCT DELIVERY, ARBITRARY CANCELLATION OF RETURN REQUEST, DEFICIENCY IN SERVICE, AND UNFAIR TRADE PRACTICES UNDER THE CONSUMER PROTECTION ACT, 2019.**

---

Under instructions from my client, the undersigned submits as under:

1. That my client is a consumer as defined under Section 2(7) of the Consumer Protection Act, 2019, having purchased goods for consideration through your e-commerce platform.

2. **RECITALS OF FACTS AND TIMELINE:**
 - **10th November 2024:** My client placed an online order on your e-commerce platform for a Samsung Galaxy smartphone worth **Rs. 26,999/-** (Rupees Twenty-Six Thousand Nine Hundred and Ninety-Nine Only) against Tax Invoice No. [Invoice Number].
 - **14th November 2024:** The said smartphone was delivered to my client.
 - **Within 24 hours of delivery:** Upon unboxing and setting up the device, my client noticed a severe manufacturing hardware defect, wherein the screen started flickering with green lines and the touch screen stopped working entirely.
 - **15th November 2024:** Immediately, well within any applicable return and replacement windows, my client raised a formal replacement request on your e-commerce application.
 - **21st November 2024:** An authorized technician sent by your platform physically inspected the smartphone at my client's premises, independently verified and confirmed the manufacturing hardware defect, and collected my client's signature on the official technician inspection job sheet.
 - **23rd November 2024:** Despite the technician's verification, your customer support arbitrarily and wrongfully cancelled my client's return request, falsely claiming that the 7-day return window had expired on 21st November 2024, and improperly directed my client to approach a brand service center instead of honoring your platform's return/replacement policy.

3. **VIOLATION OF STATUTORY PROVISIONS:**
 - The delivery of a defective smartphone constitutes a direct violation of product quality standards under Section 2(10) of the Consumer Protection Act, 2019.
 - The arbitrary cancellation of a validly raised return request and failure to provide proper after-sales redressal constitutes a gross "deficiency in service" under Section 2(11) of the Consumer Protection Act, 2019.
 - Refusing to honor a valid replacement/refund for a defective product verified by your own technician amounts to an "unfair trade practice" under Section 2(47) of the Consumer Protection Act, 2019.
 - Under Section 84 of the Consumer Protection Act, 2019, the product manufacturer and platform are liable for manufacturing defects.

4. **EVIDENCE HELD BY CLIENT:**
 - Tax invoice
 - Delivery receipt
 - Technician inspection job sheet copy confirming the manufacturing defect
 - Customer support chat screenshots

---

### **DEMAND FOR RECTIFICATION**

Through this notice, my client hereby calls upon you to fulfill the following demands within **15 days** from the receipt of this notice:

1. Arrange for an immediate pickup and process a **full refund of Rs. 26,999/-** (or a brand-new replacement unit as originally requested) for the defective Samsung Galaxy smartphone.
2. Cease and desist from engaging in arbitrary cancellations of verified return requests and unfair trade practices.

---

**WARNING OF LEGAL ACTION:**

PLEASE TAKE NOTICE THAT if you fail to comply with the above demands within the stipulated **15-day** rectification window, my client shall be constrained to initiate appropriate legal proceedings. This shall include filing a formal consumer complaint before the appropriate statutory **District Consumer Disputes Redressal Commission** via the e-Daakhil portal (edaakhil.nic.in), as well as lodging a grievance on the National Consumer Helpline (NCH) platform, seeking a full refund, statutory compensation for mental agony and harassment, and litigation costs, entirely at your sole risk, cost, and peril.

*(Note: For free legal guidance and information regarding your consumer rights, you may contact the District Legal Services Authority (DLSA) / NALSA Toll-Free Helpline at **15100**).*

---

Sincerely,

*(Signature)* 
**[Complainant / Consumer Name]** 
(Acting on behalf of self) 

---

### **ANNEXURE INVENTORY:**
1. Copy of Tax Invoice
2. Copy of Delivery Receipt
3. Copy of Technician Inspection Job Sheet
4. Screenshots of Customer Support Chats

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under Section 2(11) and Section 84 of the Consumer Protection Act 2019, delivering a defective phone and delaying inspection past your return window is a clear deficiency in service and unfair trade practice. I have the technician report confirming hardware fault. I demand an immediate refund or I will escalate to the National Consumer Helpline and e-Daakhil."*
- **Opponent Reaction:** Arre sir/madam, why are you threatening with consumer helpline and all that big-big legal English? See, our system automatically cancelled the return because the automated barcode scan updated after 7 days. Technician report is fine, but company internal policy is final, na? Okay, okay, don't shout—let me check with my senior manager if we can give you a store voucher instead of cash refund.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You brilliantly cited specific sections of the Consumer Protection Act 2019 (Section 2(11) for deficiency in service and Section 84) along with concrete proof like the technician report.",
  "what_to_improve": "Do not accept a store voucher if you want a full cash refund. Hold your ground on the monetary refund to your original payment method.",
  "suggested_next_counter": "I reject the store voucher; as per RBI guidelines and Consumer Protection Act, I demand an immediate full refund to my original payment source, or I proceed with my formal complaint."
}
```

---

## TC-03: Gurugram Tech Employee Unpaid Salary & Relieving Letter Withheld

- **Timestamp:** `2026-11-08T20:11:56.000202+00:00`
- **Provider / Model:** `Gemini` / `gemini-3.5-flash-lite`
- **Category:** `Employment & Salary`

### 1. Raw User Input
```text
I worked as a frontend developer at an IT consultancy firm in Cyber City, Gurugram for 18 months at Rs 70,000/month. I submitted my resignation on 1st August 2024 and completed my full 60-day notice period till 30th September 2024. All project handovers and company assets (MacBook, ID card) were handed over and I received an asset clearance certificate from IT. My August salary was delayed, and my September salary plus 15 days encashable leave (total Rs 1,65,000) has not been paid. It has been 50 days since my last working day. Whenever I email HR, they say 'finance team is facing client payment delays'. More importantly, they are withholding my Relieving Letter and Experience Certificate. My new employer is threatening to cancel my job offer if I don't submit my relieving letter by end of this week. I have my appointment letter, resignation acceptance email, and signed clearance form.
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Withholding of Final Settlement & Relieving Letter by IT Firm",
  "category": "Employment & Salary",
  "summary": "The complainant completed an 18-month tenure and a 60-day notice period at an IT consultancy in Gurugram, successfully clearing all asset handovers. The employer has withheld the final salary and leave encashment totaling Rs. 1,65,000 for 50 days, along with the essential Relieving Letter and Experience Certificate, threatening the complainant's new job offer.",
  "complainant": "Frontend Developer (Ex-Employee)",
  "opposite_party": "IT Consultancy Firm, Cyber City, Gurugram (Management / HR)",
  "disputed_amount": "Rs. 1,65,000",
  "timeline": [
    {
      "date_or_period": "18 months prior to August 2024",
      "event": "Complainant worked as a frontend developer at Rs 70,000/month."
    },
    {
      "date_or_period": "1st August 2024",
      "event": "Complainant submitted resignation."
    },
    {
      "date_or_period": "30th September 2024",
      "event": "Completed 60-day notice period, handed over assets, and received asset clearance certificate."
    },
    {
      "date_or_period": "Past 50 days (Post-30th September 2024)",
      "event": "Salary for August and September plus leave encashment unpaid; HR cites client payment delays; Relieving letter withheld."
    }
  ],
  "evidence_held": [
    "Appointment letter",
    "Resignation acceptance email",
    "Signed asset clearance form / certificate from IT"
  ],
  "evidence_needed": [
    "Bank statements showing salary credits for previous months to establish salary baseline",
    "Written correspondence / email threads with HR regarding the payment delay",
    "Employment contract / offer letter outlining notice period and leave encashment terms",
    "Written communication from the new employer regarding the threat of offer cancellation"
  ],
  "evidence_strength_score": 7,
  "evidence_strength_explanation": "Strong documentary proof of employment, resignation acceptance, and formal clearance exists, though written follow-ups regarding the unpaid dues should be formally consolidated.",
  "escalation_check": {
    "requires_real_lawyer": true,
    "reasons": [
      "High-severity issue (threat)"
    ],
    "legal_aid_contact": "District Legal Services Authority (DLSA) / NALSA Toll-Free Helpline: 15100"
  }
}
```

### 3. Plain-Language Rights & Statutory Standing (Direct Model Output)
```json
{
  "plain_language_standing": "Your dispute regarding unpaid wages and final documents is strictly civil in nature, meaning criminal police complaints are not appropriate here. Under Indian law, your wages must be paid promptly following your departure. You hold strong documentation such as an asset clearance certificate and resignation acceptance to support your claim.",
  "governing_laws": [
    {
      "act_name": "Code on Wages, 2019",
      "section": "Section 17(2)",
      "relevance": "Mandates that wages of an employee who is removed, dismissed, retrenched, or resigns must be paid within two working days of that event."
    },
    {
      "act_name": "General Legal Principle (Civil vs. Criminal Boundary)",
      "section": "General Guidance",
      "relevance": "Establishes that withholding wages or breach of employment terms is a civil matter and not a criminal offense, requiring civil/statutory forum resolution instead of police complaints."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Immediate Pre-Litigation Action",
      "timeline": "Suggested 15 days (customary pre-litigation practice)",
      "details": "Send a formal written demand email to your former employer citing Section 17(2) of the Code on Wages, 2019, requesting the immediate release of your unpaid wages and relieving documents within two working days."
    },
    {
      "step_number": 2,
      "title": "Statutory Authority / Grievance Portal Filing",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "Approach the competent labour authority (confirm locally) for formal proceedings and recovery of your unpaid wages. Note: The District Legal Services Authority (DLSA) / NALSA Helpline 15100 provides free legal aid and guidance only; it is never a forum for hearings or proceedings against an employer."
    },
    {
      "step_number": 3,
      "title": "Statutory Forum / Conciliation Petition",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "If the employer fails to comply with your written demand, file a formal dispute petition before the labour authority for conciliation and recovery of dues."
    }
  ],
  "real_lawyer_needed": true,
  "real_lawyer_guidance": "Given the complexity involving your new job offer and withholding of relieving documents, consulting a licensed advocate or contacting the District Legal Services Authority (DLSA) via helpline 15100 for free legal aid and guidance is recommended.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
**BY SPEED POST WITH ACKNOWLEDGEMENT DUE (AD) / REGISTERED EMAIL**

**To,** 
Management / HR Department 
IT Consultancy Firm 
Cyber City, Gurugram, Haryana 

**From:** 
Frontend Developer (Ex-Employee) 
[Complainant Address / Contact Details] 

**Date:** 09/11/2026 

---

### **SUBJECT: LEGAL DEMAND NOTICE FOR WITHHOLDING OF FINAL SETTLEMENT (RS. 1,65,000), LEAVE ENCASHMENT, AND ESSENTIAL RELIEVING DOCUMENTS**

Sir/Madam,

Under instructions from my client, the undersigned submits as under:

1. That my client was employed with your IT consultancy firm situated at Cyber City, Gurugram, as a Frontend Developer for an[unverified reference removed]-month tenure prior to August 2024, drawing a monthly salary of Rs. 70,000/-.
2. That on 1st August 2024, my client formally submitted their resignation from the said position.
3. That my client successfully completed their 60-day notice period ending on 30th September 2024, during which all company assets were duly handed over, and my client received the official signed asset clearance form/certificate from the IT department.
4. That despite the successful completion of the notice period and asset handover, your office has withheld my client's final salary for August and September alongside leave encashment, totaling Rs. 1,65,000/-, for the past 50 days (post-30th September 2024), citing internal client payment delays as an arbitrary excuse.
5. That your office has further withheld my client’s essential Relieving Letter and Experience Certificate, which has severely jeopardized my client's new employment offer and career prospects.

#### **VIOLATION OF STATUTORY PROVISIONS:**
* **Section 17(2) of the Code on Wages, 2019:** Mandates that wages of an employee who resigns must be paid within two working days of their departure. Your failure to clear my client's dues for over 50 days is a blatant violation of statutory wage mandates.
* **General Legal Principle:** Withholding lawful earnings and mandatory exit documents constitutes a civil breach of employment terms. *(Note: For free legal aid and guidance regarding this matter, citizens may reach out to the District Legal Services Authority (DLSA) / NALSA Toll-Free Helpline: 15100).*

---

#### **DEMAND FOR RECTIFICATION:**

You are hereby called upon to clear and disburse the total withheld amount of **Rs. 1,65,000/-** (representing unpaid salary and leave encashment) and issue the mandatory **Relieving Letter and Experience Certificate** to my client within a strict **15-day window** from the receipt of this notice.

Failure to comply within the stipulated 15-day rectification window will compel my client to initiate formal legal proceedings by filing a dispute petition and seeking recovery before **the competent labour authority (confirm locally)**, alongside pursuing all available remedies under civil law for damages and mental harassment, entirely at your risk as to costs and consequences.

---

**Signature:**

________________________________________ 
**Frontend Developer (Ex-Employee)** 
[Date: 09/11/2026] 

---

#### **ANNEXURE INVENTORY (Documents Held by Complainant):**
1. Appointment letter
2. Resignation acceptance email
3. Signed asset clearance form / certificate from IT

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under employment laws, full and final dues must be cleared timely and withholding my relieving letter violates my right to livelihood. If my Rs 1,65,000 and relieving letter are not issued within 3 days, I will file a formal complaint with the District Labor Commissioner."*
- **Opponent Reaction:** Arre yaar, yeh sab District Labor Commissioner aur right to livelihood ki dhamkiyan humein mat do! Company policy saaf kehti hai ki exit formalities aur internal audit clear hone ke baad hi FNF process hota hai. Thoda patience rakho, HR team review kar rahi hai. Aise 3 din ki deadline dene se kaam thodi fast ho jayega, agreement padho apna!
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You firmly invoked statutory rights, exact dues (Rs. 1,65,000), a strict timeline, and threatened a specific legal authority (District Labor Commissioner).",
  "what_to_improve": "You didn't mention specific sections of the Industrial Disputes Act, Shops & Establishment Act, or the exact date your notice period ended and asset clearance was acknowledged via email.",
  "suggested_next_counter": "Cite our email confirmation dated [Date] where asset handover was accepted, and remind them that withholding FNF beyond standard statutory timelines attracts legal escalation under the relevant Shops and Establishment Act."
}
```

---

