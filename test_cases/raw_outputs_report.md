# NyayaMitra - Official Unedited Raw Outputs for Test Cases

> **Execution Metadata:** Generated on `2026-11-09T00:46:49.946138+00:00` using Provider: `Gemini`, Model: `gemini-3.5-flash-lite`.
> **Strict Ground Rule:** Real agent calls only. No post-editing, no mock datasets.

## TC-01: Bengaluru Tenant Security Deposit Withholding

- **Timestamp:** `2026-11-09T00:45:52.160765+00:00`
- **Provider / Model:** `Gemini` / `gemini-3.5-flash-lite`
- **Category:** `Tenancy & Rental`

### 1. Raw User Input
```text
I was renting a 2BHK flat in HSR Layout, Bengaluru for 2 years at Rs 28,000/month. I gave 1 lakh rupees as security deposit. I gave proper 1-month notice on 1st October and vacated the flat on 31st October 2024. I cleared all electricity and water bills and handed over keys. Landlord Mr. Ramesh promised to refund the deposit via UPI in 3 days. Now it has been 25 days, he stopped picking my calls, and yesterday he messaged saying he is deducting Rs 45,000 for 'complete house repainting, marble polishing, and deep cleaning'. There was no damage, just normal nail holes for photo frames and standard wear and tear. I have move-in photos, move-out handover video, all rent payment bank statements, and WhatsApp chat where he acknowledged receiving the flat in good condition. How can I get my Rs 45,000 back?
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Security Deposit Withholding Dispute with Landlord in Bengaluru",
  "category": "Tenancy & Rental",
  "summary": "The tenant vacated the 2BHK flat in Bengaluru after providing proper notice and clearing all utility bills, but the landlord has wrongfully withheld Rs 45,000 from the security deposit under the pretext of repainting and deep cleaning for normal wear and tear.",
  "complainant": "Tenant",
  "opposite_party": "Landlord Mr. Ramesh",
  "disputed_amount": "Rs 45,000",
  "timeline": [
    {
      "date_or_period": "2 years prior",
      "event": "Rented 2BHK flat in HSR Layout, Bengaluru at Rs 28,000/month and paid Rs 1,00,000 as security deposit."
    },
    {
      "date_or_period": "1st October",
      "event": "Gave proper 1-month notice to vacate."
    },
    {
      "date_or_period": "31st October 2024",
      "event": "Vacated the flat, cleared all electricity and water bills, and handed over keys."
    },
    {
      "date_or_period": "3 days post-vacation",
      "event": "Landlord Mr. Ramesh promised to refund the deposit via UPI."
    },
    {
      "date_or_period": "25 days later (Yesterday)",
      "event": "Landlord stopped picking up calls and sent a message deducting Rs 45,000 for house repainting, marble polishing, and deep cleaning."
    }
  ],
  "evidence_mentioned": [
    "Move-in photos",
    "Move-out handover video",
    "All rent payment bank statements",
    "WhatsApp chat where landlord acknowledged receiving the flat in good condition"
  ],
  "evidence_needed": [
    "Original lease/rental agreement",
    "Receipt of security deposit payment",
    "Formal written demand notice sent to the landlord"
  ],
  "evidence_held": [
    "Move-in photos",
    "Move-out handover video",
    "All rent payment bank statements",
    "WhatsApp chat where landlord acknowledged receiving the flat in good condition"
  ],
  "escalation_check": {
    "requires_real_lawyer": false,
    "is_physical_danger": false,
    "is_past_incident": false,
    "clarification_question": "",
    "reasons": [],
    "reason": "",
    "legal_aid_contact": "District Legal Services Authority (DLSA) / NALSA Toll-Free Helpline: 15100"
  }
}
```

### 3. Plain-Language Rights & Statutory Standing (Direct Model Output)
```json
{
  "plain_language_standing": "Your dispute with your landlord over the withholding of your security deposit is a civil matter governed by your rental agreement and state rent laws. Under Indian law, routine wear and tear of a property cannot be used as a valid excuse by a landlord to make deductions from your security deposit. You hold strong evidence, including move-in and move-out media and WhatsApp acknowledgments, to support your claim for a full refund.\n\nKey Legal Standing: The Transfer of Property Act protects you from unjustified charges for normal wear and tear when returning possession of a property. Mere failure to refund a deposit is a civil dispute and not a criminal offense.\n\nImmediate Takeaway: Gather your lease agreement, bank statements, and chat records, and serve a formal written demand notice to your landlord to initiate the recovery process.",
  "governing_laws": [
    {
      "act_name": "Transfer of Property Act, 1882",
      "section": "Section 108(B)(m)",
      "relevance": "Protects you by establishing that a tenant is only required to return the property subject to changes caused by reasonable wear and tear, shielding you from unjustified repainting and cleaning deductions."
    },
    {
      "act_name": "Transfer of Property Act, 1882",
      "section": "Section 108(B)(q)",
      "relevance": "Affirms your duty to hand over possession, which you successfully fulfilled by returning the keys and clearing utility dues."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Serve Formal Legal Notice",
      "timeline": "Suggested 15 days (customary pre-litigation practice)",
      "details": "Send a formal written legal notice to your landlord demanding the full refund of the withheld Rs 45,000 security deposit. Clearly cite Section 108(B)(m) to dispute unauthorized wear-and-tear deductions, attaching your move-in/move-out evidence and WhatsApp chat acknowledgments."
    },
    {
      "step_number": 2,
      "title": "Seek Free Legal Guidance via DLSA",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "Contact the District Legal Services Authority (DLSA) via Helpline 15100 for free legal guidance and support. Note: DLSA provides free legal aid and guidance only; it is never a forum for hearings or proceedings against a landlord."
    },
    {
      "step_number": 3,
      "title": "File a Civil Recovery Suit",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "If the landlord fails to respond or refund the amount after the notice period, file a recovery suit or application before the local civil court / Small Causes Court in Bengaluru based on your rental agreement and state rent regulations."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "For filing a civil recovery suit in a local civil court or Small Causes Court, consulting or engaging a licensed advocate is recommended to properly draft pleadings and represent your case.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
### LEGAL NOTICE DRAFT – REVIEW BEFORE SENDING

**FROM:** 
[Your Name] 
[Your Address] 
Phone: [Your Phone Number] 
Email: [Your Email Address] 

**DATE:** 09/11/2026

**MODE OF DISPATCH:** Speed Post with Acknowledgement Due (AD) / Registered Email 

**TO:** 
Mr. Ramesh 
[Landlord's Address in Bengaluru] 
Phone: [Landlord's Phone Number, if known] 
Email: [Landlord's Email Address, if known] 

---

**SUBJECT: LEGAL DEMAND NOTICE FOR WRONGFUL WITHHOLDING OF SECURITY DEPOSIT AMOUNTING TO RS 45,000 IN RESPECT OF PREMISES LOCATED AT HSR LAYOUT, BENGALURU.**

Sir,

I, am a resident of Bengaluru and was a tenant occupying your 2BHK flat located in HSR Layout, Bengaluru (hereinafter referred to as the "Scheduled Premises"). I hereby issue this legal demand notice to you, Mr. Ramesh, calling upon you to refund the wrongfully withheld security deposit of Rs 45,000, as per the facts and legal standing detailed below:

### FACTUAL SEQUENCE OF EVENTS

1. That 2 years prior, I entered into a tenancy arrangement with you for the Scheduled Premises at a monthly rent of Rs 28,000, and paid a security deposit of Rs 1,00,000 at the commencement of the tenancy.
2. That on 1st October, I duly served a proper 1-month notice to vacate the Scheduled Premises, in accordance with our rental terms.
3. That on 31st October 2024, I successfully vacated the Scheduled Premises, cleared all pending electricity and water utility bills, and formally handed over the keys to you.
4. That 3 days post-vacation, you inspected the premises and promised to refund my security deposit via UPI.
5. That 25 days later (Yesterday), you abruptly stopped picking up my phone calls and sent a text message stating that you were deducting Rs 45,000 from my security deposit for house repainting, marble polishing, and deep cleaning.

### VIOLATION OF STATUTORY PROVISIONS AND TERMS

1. I state and submit that your deduction of Rs 45,000 under the pretext of repainting and deep cleaning is completely unjustified and arbitrary. Under Section 108(B)(m) of the Transfer of Property Act, 1882, a tenant is only required to return the property subject to changes caused by reasonable wear and tear, and cannot be held liable to bear the costs of routine wear and tear or general maintenance like repainting and polishing upon vacating.
2. I have duly fulfilled my obligation under Section 108(B)(q) of the Transfer of Property Act, 1882, by peacefully returning possession of the property after clearing all utility dues.
3. Furthermore, I hold contemporaneous evidence, including move-in photos, a move-out handover video, all rent payment bank statements, and WhatsApp chat records where you explicitly acknowledged receiving the flat in good condition.

### DEMAND FOR RECTIFICATION

Therefore, through this notice, I hereby call upon you to refund the wrongfully withheld security deposit amount of **Rs 45,000** to my bank account within a suggested 15-day period (customary pre-litigation practice) from the date of receipt of this notice. 

The bank account details for the transfer are as follows: 
- **Account Holder Name:** [Your Name] 
- **Bank Name:** [Your Bank Name] 
- **Account Number:** [Your Account Number] 
- **IFSC Code:** [Your IFSC Code] 

### WARNING OF FURTHER LEGAL ACTION

Please take notice that if you fail to refund the aforementioned sum of Rs 45,000 within the suggested 15-day period, I shall be constrained to initiate appropriate legal proceedings. This will include filing a civil recovery suit or application before the local civil court / Small Causes Court in Bengaluru to recover the principal amount along with costs, and seeking guidance from the District Legal Services Authority (DLSA Helpline: 15100) for free legal support, entirely at your risk, cost, and consequences.

A copy of this notice is retained in my records for further necessary action.

Sincerely / Yours faithfully,

*(Signature)* 
[Your Name] 

---

### ANNEXURE INVENTORY
1. Copy of the Original Lease / Rental Agreement
2. Receipt of Security Deposit Payment
3. Move-in Photographs
4. Move-out Handover Video
5. All Rent Payment Bank Statements
6. Screenshots of WhatsApp Chat Acknowledging Property Condition

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Mr. Ramesh, as per Section 108 of the Transfer of Property Act and the Model Tenancy framework, ordinary wear and tear like wall paint aging cannot be deducted from my deposit. I have the handover video and our chat proof. Please refund my balance 45,000 within 7 days."*
- **Opponent Reaction:** Arre, Section-wection kya bol rahe ho ji! Agreement padha hai kya tune? Clause 14 mein clearly likha hai flat pristine condition mein hand over karna padega. Deep cleaning aur painting ka kharcha toh tenant ko hi dena padta hai. Video dikhane se kuch nahi hota, market mein painting ka rate pata hai kya tumhe?
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You successfully cited Section 108 of the Transfer of Property Act and the Model Tenancy framework, along with concrete evidence like the handover video and chat proofs.",
  "what_to_improve": "Maintain your ground on the exact deadline. While you mentioned 7 days, firmly reiterate that withholding deposit for normal wear and tear without itemized damage proof is legally untenable.",
  "suggested_next_counter": "Mr. Ramesh, the handover video clearly proves there is only normal wear and tear, which is legally excluded from deductions, so please transfer the Rs 45,000 immediately."
}
```

---

## TC-02: E-Commerce Defective Smartphone Refund Denial

- **Timestamp:** `2026-11-09T00:46:09.767824+00:00`
- **Provider / Model:** `Gemini` / `gemini-3.5-flash-lite`
- **Category:** `Consumer & E-Commerce`

### 1. Raw User Input
```text
I ordered a Samsung Galaxy smartphone worth Rs 26,999 on an e-commerce app on 10th November 2024. It was delivered on 14th November. Within 24 hours of opening the box, the screen started flickering with green lines and touch stopped working. I raised a replacement request on 15th November. The app sent a technician for inspection on 21st November. The technician confirmed it is a manufacturing hardware defect and took sign on his job sheet. But on 23rd November, customer support cancelled my return request stating 'The 7-day return window expired on 21st November'. They are telling me to go to an authorized brand service center 40 km away. I paid for a brand new working phone, not a defective phone repaired on day one. I have the invoice, delivery receipt, technician inspection job sheet copy, and chat screenshots.
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Defective Smartphone Delivery and Wrongful Replacement Denial",
  "category": "Consumer & E-Commerce",
  "summary": "The complainant ordered a Samsung Galaxy smartphone worth Rs 26,999 which arrived with a manufacturing defect. Although a technician inspected and confirmed the defect within the return period, customer support cancelled the replacement request citing the expiry of the 7-day return window and asked the user to visit a distant service center.",
  "complainant": "Consumer",
  "opposite_party": "E-commerce App / Seller",
  "disputed_amount": "Rs 26,999",
  "timeline": [
    {
      "date_or_period": "10th November 2024",
      "event": "Ordered a Samsung Galaxy smartphone on the e-commerce app."
    },
    {
      "date_or_period": "14th November 2024",
      "event": "Smartphone was delivered to the complainant."
    },
    {
      "date_or_period": "Within 24 hours of delivery",
      "event": "Screen started flickering with green lines and touch stopped working."
    },
    {
      "date_or_period": "15th November 2024",
      "event": "Raised a replacement request on the e-commerce app."
    },
    {
      "date_or_period": "21st November 2024",
      "event": "Technician inspected the device, confirmed manufacturing hardware defect, and took signature on job sheet."
    },
    {
      "date_or_period": "23rd November 2024",
      "event": "Customer support cancelled the return request stating the 7-day return window expired on 21st November."
    }
  ],
  "evidence_mentioned": [
    "Mentions invoice",
    "Mentions delivery receipt",
    "Mentions technician inspection job sheet copy",
    "Mentions chat screenshots"
  ],
  "evidence_needed": [
    "Original payment receipt / bank statement showing the transaction",
    "Written emails or logs of customer support communication",
    "Manufacturer warranty card or terms of sale"
  ],
  "evidence_held": [
    "Mentions invoice",
    "Mentions delivery receipt",
    "Mentions technician inspection job sheet copy",
    "Mentions chat screenshots"
  ],
  "escalation_check": {
    "requires_real_lawyer": false,
    "is_physical_danger": false,
    "is_past_incident": false,
    "clarification_question": "",
    "reasons": [],
    "reason": "",
    "legal_aid_contact": "District Legal Services Authority (DLSA) / NALSA Toll-Free Helpline: 15100"
  }
}
```

### 3. Plain-Language Rights & Statutory Standing (Direct Model Output)
```json
{
  "plain_language_side": null,
  "plain_language_standing": "Your complaint regarding a defective smartphone and the seller's unfair denial of replacement is fully protected under consumer law.\nUnder the Consumer Protection Act, 2019, delivering faulty goods and refusing to refund or replace them constitutes a statutory deficiency in service and unfair trade practice.\nYou have the right to seek a complete replacement or refund along with compensation for the trouble caused, and you can represent yourself without needing a lawyer in the Consumer Commission.",
  "governing_laws": [
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(7)",
      "relevance": "Protects you as a consumer who bought goods for a consideration."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(10)",
      "relevance": "Defines a defect in goods covering faults or imperfections in quality and standards."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(11)",
      "relevance": "Defines deficiency in service covering negligence or omission in fulfilling a contract."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(47)",
      "relevance": "Qualifies refusing to refund or replace defective goods within stipulated terms as an unfair trade practice."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 35",
      "relevance": "Provides the procedure for filing a consumer complaint electronically or physically."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Lodge Preliminary Grievance and Serve Notice",
      "timeline": "Suggested 15 days (customary pre-litigation practice)",
      "details": "Lodge a formal grievance on the National Consumer Helpline (NCH) via toll-free number 1915 or consumerhelpline.gov.in. Simultaneously, serve a formal 15-day legal demand notice to the seller and e-commerce platform attaching your invoice and technician job sheet."
    },
    {
      "step_number": 2,
      "title": "File Electronic Complaint on e-Jagriti Portal",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "File an electronic consumer complaint online on e-Jagriti (launched 1 Jan 2025, replacing e-Daakhil). Upload your order invoice, delivery receipt, technician inspection job sheet copy, and chat screenshots. Note: DLSA provides free legal aid and guidance (Helpline 15100) only; it is never a forum for hearings or proceedings."
    },
    {
      "step_number": 3,
      "title": "Proceed with District Consumer Commission Petition",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "If the seller fails to resolve the issue after the notice and online grievance, pursue your formal petition before the District Consumer Disputes Redressal Commission for product replacement, refund, and compensation."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "You can represent yourself entirely on your own before the Consumer Commission without hiring a physical advocate, as the Consumer Protection Act allows consumers to argue their own cases.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
### LEGAL NOTICE DRAFT – REVIEW BEFORE SENDING

**FROM:** 
[Your Name] 
[Your Address] 
Phone: [Your Phone Number] 
Email: [Your Email Address] 

**DATE:** 09/11/2026 

**MODE OF DISPATCH:** Speed Post (Acknowledgment Due) / Registered Email 

**TO:** 
The E-commerce Platform / Seller Management 
[Recipient Company Name / Seller Name] 
[Recipient Address] 
[Recipient Email Address] 

---

**SUBJECT: LEGAL DEMAND NOTICE FOR REPLACEMENT/REFUND OF DEFECTIVE SMARTPHONE AND UNFAIR TRADE PRACTICE UNDER THE CONSUMER PROTECTION ACT, 2019.**

Dear Sir/Madam,

I, am serving this legal demand notice upon you in my individual capacity as a consumer, setting forth my grievance regarding the delivery of a defective smartphone and the subsequent arbitrary cancellation of my replacement request.

I hereby state and submit as under:

1. That on 10th November 2024, I ordered a Samsung Galaxy smartphone worth Rs 26,999 on your e-commerce app, bearing Order ID [Insert Order ID / Details]. I paid the full consideration amount of Rs 26,999 for the purchase, confirming my status as a consumer under Section 2(7) of the Consumer Protection Act, 2019.

2. That the said smartphone was delivered to me on 14th November 2024 along with the invoice and delivery receipt. 

3. That within 24 hours of delivery, serious hardware defects manifested in the device: the screen started flickering with green lines and the touch functionality stopped working entirely.

4. That immediately upon noticing the defect, on 15th November 2024, I raised a formal replacement request on your e-commerce app within the stipulated return window.

5. That on 21st November 2024, an authorized technician visited to inspect the device, confirmed the manufacturing hardware defect, and took my signature on the job sheet. 

6. That despite the technician's confirmation well within time, on 23rd November 2024, your customer support arbitrarily cancelled my return request, stating that the 7-day return window expired on 21st November 2024, and advised me to visit a distant service center. This cancellation disregards the fact that my replacement request and inspection were initiated and processed within the applicable timelines.

7. That delivering a defective product and subsequently refusing to provide a replacement or refund—despite timely reporting and technician verification—constitutes a clear "defect" in goods under Section 2(10), "deficiency in service" under Section 2(11), and an "unfair trade practice" under Section 2(47) of the Consumer Protection Act, 2019.

8. That I am holding the following evidentiary documents in support of my claim:
 - Invoice
 - Delivery receipt
 - Technician inspection job sheet copy
 - Chat screenshots

**DEMAND FOR RECTIFICATION:**

In light of the above facts and statutory provisions, I hereby call upon you to rectify this grievance within a suggested 15-day period (customary pre-litigation practice) from the receipt of this notice, by taking the following actions:

1. Arrange for an immediate pickup and complete replacement of the defective Samsung Galaxy smartphone with a brand-new, unblemished unit, OR alternatively, process a full refund of Rs 26,999 to my original payment source.
2. Pay reasonable compensation for the mental agony, physical inconvenience, and deficiency in service caused by your arbitrary refusal.

**WARNING:**

Please take notice that if you fail to comply with the demands made above within the suggested 15-day period, I shall be constrained to initiate formal legal proceedings against you by filing a consumer complaint electronically on the e-Jagriti Portal or before the competent District Consumer Disputes Redressal Commission under Section 35 of the Consumer Protection Act, 2019, seeking product replacement, full refund, costs, and compensation, at your sole risk, cost, and consequences.

For guidance or free legal aid inquiries prior to filing, the District Legal Services Authority (DLSA) / NALSA Toll-Free Helpline is available at 15100.

Sincerely / Yours faithfully,

*(Signature)* 
[Your Name] 

---

**ANNEXURE INVENTORY:**
1. Copy of Order Invoice
2. Copy of Delivery Receipt
3. Copy of Technician Inspection Job Sheet
4. Copies of Chat Screenshots with Customer Support

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under Section 2(11) and Section 84 of the Consumer Protection Act 2019, delivering a defective phone and delaying inspection past your return window is a clear deficiency in service and unfair trade practice. I have the technician report confirming hardware fault. I demand an immediate refund or I will escalate to the National Consumer Helpline and e-Jagriti."*
- **Opponent Reaction:** Arre sir, why are you shouting Consumer Protection Act and all? Look, system is system! Return window is 7 days only, policy is policy. Technician report is fine, but company approval needs time. If you want, go to service center and get it repaired. Refund is not possible now.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You clearly cited specific sections of the Consumer Protection Act, 2019 (Section 2(11) for deficiency in service and Section 84 for product liability/unfair trade practices) along with concrete proof (the technician report).",
  "what_to_improve": "Keep holding your ground on the exact date the technician inspected the phone within the 7-day window. Emphasize that their internal system delay cannot override statutory rights.",
  "suggested_next_counter": "Your internal return window cannot override statutory rights under the Consumer Protection Act when the defect and technician verification happened well within the 7 days."
}
```

---

## TC-03: Gurugram Tech Employee Unpaid Salary & Relieving Letter Withheld

- **Timestamp:** `2026-11-09T00:46:29.571828+00:00`
- **Provider / Model:** `Gemini` / `gemini-3.5-flash-lite`
- **Category:** `Employment & Salary`

### 1. Raw User Input
```text
I worked as a frontend developer at an IT consultancy firm in Cyber City, Gurugram for 18 months at Rs 70,000/month. I submitted my resignation on 1 June 2026 and completed my full 60-day notice period till my last working day on 31 July 2026. All project handovers and company assets (MacBook, ID card) were handed over and I received an asset clearance certificate from IT. My June salary was delayed, and my July salary plus 15 days encashable leave (total Rs 1,65,000) has not been paid. It has been 50 days since my last working day. Whenever I email HR, they say 'finance team is facing client payment delays'. More importantly, they are withholding my Relieving Letter and Experience Certificate. My new employer is threatening to cancel my job offer if I don't submit my relieving letter by end of this week. I have my appointment letter, resignation acceptance email, and signed clearance form.
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Non-payment of Final Salary, Leave Encashment, and Withholding of Relieving Documents",
  "category": "Employment & Salary",
  "summary": "The complainant worked as a frontend developer for 18 months and completed a 60-day notice period ending on 31 July 2026 after submitting their resignation on 1 June 2026. The employer has failed to pay the June salary, July salary, and 15 days of encashable leave totaling Rs 1,65,000, and is withholding the relieving letter and experience certificate despite the completion of asset handover and clearance.",
  "complainant": "Frontend Developer (Ex-Employee)",
  "opposite_party": "IT Consultancy Firm, Cyber City, Gurugram",
  "disputed_amount": "Rs. 1,65,000",
  "timeline": [
    {
      "date_or_period": "18 months prior to July 2026",
      "event": "Complainant worked as a frontend developer at the IT consultancy firm."
    },
    {
      "date_or_period": "1 June 2026",
      "event": "Complainant submitted their resignation and initiated the 60-day notice period."
    },
    {
      "date_or_period": "31 July 2026",
      "event": "Complainant's last working day after completing the notice period; completed asset handover and received asset clearance certificate from IT."
    },
    {
      "date_or_period": "50 days post-last working day (around late September 2026)",
      "event": "Pending dues remain unpaid and HR cites client payment delays while withholding relieving and experience certificates."
    }
  ],
  "evidence_mentioned": [
    "Mentions appointment letter",
    "Mentions resignation acceptance email",
    "Mentions signed clearance form",
    "Mentions asset clearance certificate from IT",
    "Mentions email communications with HR regarding salary delays"
  ],
  "evidence_needed": [
    "Bank statements reflecting salary credits or non-receipt of June and July salary",
    "Written employment agreement or company policy document outlining leave encashment and notice period terms",
    "Formal emails or written proof of demand for dues and relieving letters sent to HR/management"
  ],
  "evidence_held": [
    "Mentions appointment letter",
    "Mentions resignation acceptance email",
    "Mentions signed clearance form",
    "Mentions asset clearance certificate from IT",
    "Mentions email communications with HR regarding salary delays"
  ],
  "escalation_check": {
    "requires_real_lawyer": true,
    "is_physical_danger": false,
    "is_past_incident": false,
    "clarification_question": "",
    "reasons": [
      "High-severity issue (threat)"
    ],
    "reason": "High-severity issue (threat)",
    "legal_aid_contact": "District Legal Services Authority (DLSA) / NALSA Toll-Free Helpline: 15100"
  }
}
```

### 3. Plain-Language Rights & Statutory Standing (Direct Model Output)
```json
{
  "plain_language_standing": "Core Legal Standing: You have a valid civil employment claim for your unpaid wages and dues, governed by the Code on Wages, 2019.\nKey Statutory Rule: Under Section 17(2), wages of an employee who resigns must be paid within two working days of their last working day.\nImmediate Takeaway: Send a formal written demand email to your employer citing Section 17(2) and approach the competent labour authority for recovery if they fail to pay.\n\nAs an ex-employee who successfully completed your resignation and notice period ending on 31 July 2026, you possess a clear right under the Code on Wages, 2019 to receive your final wages within two working days of your departure. Because your last working day was 31 July 2026 (which is after the 21 November 2025 commencement date of the Code on Wages, 2019), Section 17(2) fully applies to your wage dues. \n\nPlease note that non-payment of salary is strictly a civil employment dispute, not a criminal matter, so filing a criminal police complaint or FIR for a salary delay is legally improper. Regarding your relieving letter and experience certificate, please remember that no fixed legal deadline is stated in the law for these documents; you should check your employment contract and company policy, or consult a lawyer. For your wage claims, the District LegalServices Authority (DLSA) / NALSA Helpline 15100 is available to provide free legal aid and guidance only, and is not an adjudicating forum for proceedings against your employer.",
  "governing_laws": [
    {
      "act_name": "Code on Wages, 2019",
      "section": "Section 17(2)",
      "relevance": "Mandates that the wages of an employee who resigns must be paid within two working days of their resignation or last working day."
    },
    {
      "act_name": "General Legal Principle (Civil vs. Criminal Boundary)",
      "section": "General Guidance",
      "relevance": "Clarifies that unpaid wages and employment disputes are purely civil matters and do not constitute criminal cheating."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Immediate Pre-Litigation Action (Formal Legal Notice)",
      "timeline": "Suggested 15 days (customary pre-litigation practice)",
      "details": "Send a formal written demand email and notice to your employer citing Section 17(2) of the Code on Wages, 2019, requesting the immediate release of your unpaid wages within two working days. For your relieving or experience letters, note that no fixed legal deadline is stated in the law; check your contract and company policy, or ask a lawyer."
    },
    {
      "step_number": 2,
      "title": "Statutory Authority / Grievance Portal Filing",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "For formal proceedings and recovery of your unpaid wages, approach the competent labour authority (confirm locally). Remember that the District Legal Services Authority (DLSA) / NALSA Helpline 15100 provides free legal aid and guidance only, and is never a forum for hearings or proceedings against an employer."
    },
    {
      "step_number": 3,
      "title": "Statutory Forum / Labour Dispute Petition",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "If the employer fails to comply with your formal demand or conciliation efforts through the competent labour authority, proceed with formal labor claims or legal proceedings with the assistance of a licensed advocate or DLSA guidance."
    }
  ],
  "real_lawyer_needed": true,
  "real_lawyer_guidance": "Since this involves formal employment claims, recovery of withheld dues, and potential complications regarding relieving letters, consulting a licensed advocate or seeking guidance from the District Legal Services Authority (DLSA Helpline 15100) is strongly recommended.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
### LEGAL NOTICE DRAFT – REVIEW BEFORE SENDING

**FROM:** 
[Your Name] 
[Your Address] 
Phone: [Your Phone Number] 
Email: [Your Email Address] 

**DATE:** 09/11/2026

**MODE OF DISPATCH:** Speed Post with Acknowledgement Due (AD) / Registered Email

**TO:** 
The Management / Human Resources Department 
IT Consultancy Firm 
Cyber City, Gurugram 

---

**SUBJECT: LEGAL DEMAND NOTICE FOR NON-PAYMENT OF FINAL SALARY, LEAVE ENCASHMENT, AND WITHHOLDING OF RELIEVING DOCUMENTS**

Dear Sir/Madam,

I, **[Your Name]**, residing at **[Your Address]**, do hereby serve you with this formal legal demand notice on my own behalf, stating and submitting as under:

1. That I was employed with your IT consultancy firm as a frontend developer, having rendered dedicated services for a period of 18 months prior to July 2026 under the terms of my appointment letter.

2. That on 1 June 2026, I formally submitted my resignation, duly initiating and serving my 60-day notice period as per company policy.

3. That my last working day successfully concluded on 31 July 2026, upon the completion of my notice period. On the said date, I completed the complete asset handover and received the official asset clearance certificate from the IT department, alongside a signed clearance form.

4. That despite my full and final discharge of duties, asset handover, and clearance, you have unlawfully withheld my legitimate statutory and contractual dues amounting to **Rs. 1,65,000**, which specifically includes my unpaid salary for the month of June 2026, unpaid salary for the month of July 2026, and 15 days of encashable leave.

5. That even by 50 days post-last working day (around late September 2026), my pending dues remain completely unpaid, and HR has unjustifiably cited internal client payment delays while simultaneously withholding my essential relieving letter and experience certificate.

6. That my rightful claim is governed by the **Code on Wages, 2019**. Specifically, under **Section 17(2)** of the said Code, the wages of an employee who resigns must be paid within two working days of their last working day. As my last working day was 31 July 2026 (which is subsequent to the commencement date of the Code on Wages, 2019), Section 17(2) fully applies to my wage dues, and your failure to clear these payments within the statutory window constitutes a clear violation of law.

7. That while I note no fixed legal deadline is stated in the law for the issuance of relieving letters and experience certificates (the terms for which should be checked against employment contracts and company policies), withholding these documents indefinitely after complete clearance and asset handover causes severe prejudice to my career and professional standing.

8. That I have maintained email communications with HR regarding these salary delays, but no constructive resolution has been provided to date.

---

### **DEMAND FOR RECTIFICATION**

I hereby call upon you to clear my total outstanding dues amounting to **Rs. 1,65,000** and issue my formal relieving letter and experience certificate within a suggested **15-day period** (customary pre-litigation practice) from the date of receipt of this notice. 

Please remit the aforementioned amount directly to my bank account on record, details of which are available with your finance department, and confirm the same in writing.

### **WARNING**

In the event of your failure to settle my dues and release my relieving documents within the suggested 15-day rectification window, I shall be constrained to initiate formal legal proceedings by approaching the competent labour authority (confirm locally) for the recovery of my wages, along with seeking further appropriate legal remedies available to me under law, entirely at your risk as to costs and consequences.

For guidance and free legal aid regarding my rights, I may also reach out to the District Legal Services Authority (DLSA) / NALSA Toll-Free Helpline: **15100**.

---

Sincerely / Yours faithfully,

*(Signature)* 
[Your Name] 

---

**ANNEXURE INVENTORY (Copies Enclosed/Referenced):**
1. Appointment Letter
2. Resignation Acceptance Email
3. Signed Clearance Form
4. Asset Clearance Certificate from IT Department
5. Email Communications with HR Regarding Salary Delays

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under employment laws, full and final dues must be cleared timely and withholding my relieving letter violates my right to livelihood. If my Rs 1,65,000 and relieving letter are not issued within 3 days, I will file a formal complaint with the District Labor Commissioner."*
- **Opponent Reaction:** Arre, District Labor Commissioner ko kyun beech mein la rahe ho? Company policy clear hai—pehle internal clearance aur client feedback review hoga, uske baad hi full and final settlement process hota hai. Agreement padha tha na joining ke waqt? 90 days ka buffer period hota hai accounting verification ke liye. Aur waise bhi, tumhara notice period aur asset handover ka kuch discrepancy hai accounts team ke paas. Thoda wait karo, khud call aa jayega HR se!
- **Coach Feedback:**
```json
{
  "strength_rating": "Moderate",
  "what_went_well": "You firmly demanded your pending dues and relieving letter while setting a clear 3-day deadline, and highlighted how withholding documents impacts your livelihood.",
  "what_to_improve": "Avoid citing outside labor acts not in our database. Instead, focus strictly on the Code on Wages, 2019 provisions regarding timely wage payment upon termination or resignation.",
  "suggested_next_counter": "Under the Code on Wages, 2019, my earned wages for June and July along with leave encashment must be paid immediately upon exit, and holding my relieving documents is illegal."
}
```

---

