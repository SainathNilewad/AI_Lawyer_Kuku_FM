# NyayaMitra - Official Unedited Raw Outputs for Test Cases

> **Execution Metadata:** Generated on `2026-11-08T13:32:11.499904+00:00` using Provider: `Gemini`, Model: `gemini-3.5-flash-lite`.
> **Strict Ground Rule:** Real agent calls only. No post-editing, no mock datasets.

## TC-01: Bengaluru Tenant Security Deposit Withholding

- **Timestamp:** `2026-11-08T13:29:13.820925+00:00`
- **Provider / Model:** `Gemini` / `gemini-3.5-flash-lite`
- **Category:** `Tenancy & Rental`

### 1. Raw User Input
```text
I was renting a 2BHK flat in HSR Layout, Bengaluru for 2 years at Rs 28,000/month. I gave 1 lakh rupees as security deposit. I gave proper 1-month notice on 1st October and vacated the flat on 31st October 2024. I cleared all electricity and water bills and handed over keys. Landlord Mr. Ramesh promised to refund the deposit via UPI in 3 days. Now it has been 25 days, he stopped picking my calls, and yesterday he messaged saying he is deducting Rs 45,000 for 'complete house repainting, marble polishing, and deep cleaning'. There was no damage, just normal nail holes for photo frames and standard wear and tear. I have move-in photos, move-out handover video, all rent payment bank statements, and WhatsApp chat where he acknowledged receiving the flat in good condition. How can I get my Rs 45,000 back?
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Arbitrary Security Deposit Deduction for Normal Wear and Tear",
  "category": "Tenancy & Rental",
  "summary": "The landlord, Mr. Ramesh, is arbitrarily withholding Rs. 45,000 from the user's Rs. 1,00,000 security deposit for repainting, marble polishing, and deep cleaning after the flat was vacated in good condition following proper notice.",
  "complainant": "Tenant",
  "opposite_party": "Landlord Mr. Ramesh",
  "disputed_amount": "Rs. 45,000",
  "timeline": [
    {
      "date_or_period": "1st October 2024",
      "event": "User provided proper 1-month notice to vacate the 2BHK flat."
    },
    {
      "date_or_period": "31st October 2024",
      "event": "User vacated the flat, cleared all utility bills, and handed over the keys."
    },
    {
      "date_or_period": "Early November 2024 (Within 3 days of vacation)",
      "event": "Landlord Mr. Ramesh promised to refund the deposit via UPI in 3 days but failed to do so and stopped picking calls."
    },
    {
      "date_or_period": "25 days post-vacation (Yesterday)",
      "event": "Landlord sent a message claiming a deduction of Rs. 45,000 for house repainting, marble polishing, and deep cleaning."
    }
  ],
  "evidence_held": [
    "Move-in photos",
    "Move-out handover video",
    "All rent payment bank statements",
    "WhatsApp chat acknowledging receipt of the flat in good condition",
    "Proof of cleared electricity and water bills"
  ],
  "evidence_needed": [
    "Copy of the signed Rent Agreement (to verify clauses regarding painting and security deposit deductions)",
    "Written formal demand/legal notice sent to the landlord (if any)"
  ],
  "evidence_strength_score": 9,
  "evidence_strength_explanation": "The user possesses strong visual and documentary proof including move-in/out media, payment statements, and WhatsApp acknowledgments from the landlord.",
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
  "plain_language_standing": "You have a strong legal standing to recover your unlawfully deducted security deposit under Indian tenancy principles. Routine wear and tear like normal paint aging or cleaning is legally excluded from tenant liability, and your video and photographic evidence heavily support your claim. This is a civil dispute and a breach of contract rather than a criminal offense.\n\nUnder the Transfer of Property Act, 1882, a tenant is only required to return the property subject to reasonable wear and tear. Your comprehensive evidence, including move-in/out media and bank statements, places you in a secure position to demand your full refund.\n\nYour immediate takeaway is to formally document your demand for the remaining security deposit using your collected proof before pursuing civil resolution.",
  "governing_laws": [
    {
      "act_name": "Transfer of Property Act, 1882",
      "section": "Section 108(B)(m)",
      "relevance": "Protects you from liability for changes caused by reasonable wear and tear when returning property possession."
    },
    {
      "act_name": "General Legal Principle (Civil vs. Criminal Boundary)",
      "section": "General Guidance",
      "relevance": "Establishes that deposit withholding is a civil matter of contract breach, meaning criminal police complaints are not appropriate."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Immediate Pre-Litigation Action (Formal Legal Notice)",
      "timeline": "Suggested 15 days (customary pre-litigation practice)",
      "details": "Serve a formal written legal notice citing Section 108(B)(m) to demand the full refund of your unlawfully deducted deposit amount, attaching copies of your move-out video, WhatsApp chats, and bank statements."
    },
    {
      "step_number": 2,
      "title": "Statutory Authority / Grievance Guidance",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "If the landlord fails to respond, seek free legal aid and guidance from the District Legal Services Authority (DLSA) via Helpline 15100. Note: DLSA provides free legal aid and guidance only; it is never a forum for hearings or proceedings against a landlord."
    },
    {
      "step_number": 3,
      "title": "Statutory Forum / Civil Suit Filing",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "If informal notices and DLSA guidance do not resolve the issue, file a recovery suit for the remaining security deposit before the local civil court or Small Causes Court."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "You can represent yourself in many lower civil forums and consumer courts without an advocate, but consulting a licensed advocate or utilizing DLSA free legal aid is recommended for drafting formal legal notices and navigating civil court procedures.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
**BY SPEED POST / REGISTERED EMAIL**

**LEGAL DEMAND NOTICE**

**Date:** 08/11/2026

**To,** 
Mr. Ramesh 
[Landlord Address / Contact Details as known] 

**From,** 
[Tenant Name / Complainant] 
[Tenant Address] 
[Tenant Contact Number / Email Address] 

---

**SUBJECT: LEGAL DEMAND NOTICE FOR UNLAWFUL WITHHOLDING AND ARBITRARY DEDUCTION OF SECURITY DEPOSIT AMOUNTING TO RS. 45,000/- IN RESPECT OF THE VACATED 2BHK FLAT.**

Sir,

Under instructions from and on behalf of my client, the Tenant, I do hereby serve upon you this formal Legal Demand Notice under the applicable provisions of Indian law, and submit as under:

1. That my client was a lawful tenant residing in your 2BHK flat pursuant to the terms of tenancy between you and my client. 
2. That on **1st October 2024**, my client provided proper 1-month notice to vacate the said 2BHK flat.
3. That on **31st October 2024**, my client successfully vacated the flat, cleared all utility bills (including electricity and water bills), and formally handed over the keys to you.
4. That **Early November 2024 (Within 3 days of vacation)**, you explicitly promised to refund the full security deposit of Rs. 1,00,000/- via UPI within 3 days, but failed to do so and subsequently stopped picking up phone calls from my client.
5. That **25 days post-vacation (Yesterday)**, after maintaining silence and avoiding communication for weeks, you sent a message claiming an arbitrary and unlawful deduction of Rs. 45,000/- from the total security deposit towards house repainting, marble polishing, and deep cleaning.
6. That my client is holding comprehensive evidence substantiating the good condition in which the flat was returned, including move-in photos, a move-out handover video, all rent payment bank statements, WhatsApp chats acknowledging receipt of the flat in good condition, and proof of cleared utility bills.

**VIOLATION OF STATUTORY PROVISIONS:**
* Your arbitrary deduction of Rs. 45,000/- for routine house repainting, marble polishing, and deep cleaning is completely illegal, unjustified, and contrary to established legal principles governing tenancies in India.
* Under **Section 108(B)(m) of the Transfer of Property Act, 1882**, a tenant is only required to return the property subject to reasonable wear and tear. Normal paint aging and routine cleaning constitute standard wear and tear and cannot be legally charged to a departing tenant.
* Withholding my client’s security deposit without lawful justification constitutes a civil wrong and a breach of the tenancy arrangement.

**CALL TO ACTION AND 15-DAY RECTIFICATION DEMAND:**

I, therefore, through this Notice, call upon you to remit the full unlawfully deducted amount of **Rs. 45,000/-** to my client via proper banking channels within **15 (fifteen) days** from the receipt of this Notice, failing which my client shall be constrained to initiate appropriate legal proceedings.

**WARNING OF FURTHER LEGAL ACTION:**

Please take notice that if you fail to comply with the demand within the stipulated 15-day period, my client reserves the right to:
1. Approach the District Legal Services Authority (DLSA) for free legal aid and guidance (Helpline: 15100). *Note: DLSA provides free legal aid and guidance only and is not a forum for proceedings against a landlord.*
2. File a formal civil suit for recovery of the withheld security deposit along with applicable costs and interest before the appropriate civil court or Small Causes Court.

This Notice is issued without prejudice to my client's rights and remedies available under law.

Sincerely,

*(Signature)* 
**[Tenant Name / Complainant]** 

---

### **ANNEXURE INVENTORY (Evidence Attached):**
1. Copy of move-in photos.
2. Copy of move-out handover video.
3. Copies of all rent payment bank statements.
4. Copies of WhatsApp chats acknowledging receipt of the flat in good condition.
5. Proof of cleared electricity and water bills.

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Mr. Ramesh, as per Section 108 of the Transfer of Property Act and the Model Tenancy framework, ordinary wear and tear like wall paint aging cannot be deducted from my deposit. I have the handover video and our chat proof. Please refund my balance 45,000 within 7 days."*
- **Opponent Reaction:** Arre yaar, law and section mat batao mujhe! Yeh sab kitabein baatein hain. Video-vidio kya dikha rahe ho, flat ka halat dekha hai kya? Marble pe scratches hain, deep cleaning ka kharcha toh lagega na! Chalo theek hai, zyada mat bolo, 45,000 nahi... ek kaam karo, 25,000 kaat ke baaki le lo. Final offer hai mera, court-kachhari mat karo.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You firmly cited the relevant legal principles (Transfer of Property Act/Model Tenancy framework), distinguished wear and tear, and provided evidence (handover video and chats) with a clear deadline.",
  "what_to_improve": "Do not accept his partial offer of settlement immediately. Reiterate that structural or cleaning costs for normal usage are the landlord's responsibility and demand the full amount.",
  "suggested_next_counter": "Mr. Ramesh, normal wear and tear is legally non-deductible; please release the full Rs. 45,000 or I will escalate this to the DLSA or local authorities."
}
```

---

## TC-02: E-Commerce Defective Smartphone Refund Denial

- **Timestamp:** `2026-11-08T13:30:50.703975+00:00`
- **Provider / Model:** `Gemini` / `gemini-3.5-flash-lite`
- **Category:** `Consumer & E-Commerce`

### 1. Raw User Input
```text
I ordered a Samsung Galaxy smartphone worth Rs 26,999 on an e-commerce app on 10th November 2024. It was delivered on 14th November. Within 24 hours of opening the box, the screen started flickering with green lines and touch stopped working. I raised a replacement request on 15th November. The app sent a technician for inspection on 21st November. The technician confirmed it is a manufacturing hardware defect and took sign on his job sheet. But on 23rd November, customer support cancelled my return request stating 'The 7-day return window expired on 21st November'. They are telling me to go to an authorized brand service center 40 km away. I paid for a brand new working phone, not a defective phone repaired on day one. I have the invoice, delivery receipt, technician inspection job sheet copy, and chat screenshots.
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Defective Smartphone Delivery and Refused Replacement",
  "category": "Consumer & E-Commerce",
  "summary": "The complainant purchased a Samsung Galaxy smartphone for Rs 26,999, which arrived with a manufacturing defect. Although a technician verified the defect within the return window, customer support later cancelled the replacement request claiming the return window expired.",
  "complainant": "Consumer",
  "opposite_party": "E-Commerce App / Seller",
  "disputed_amount": "Rs. 26,999",
  "timeline": [
    {
      "date_or_period": "10th November 2024",
      "event": "Ordered Samsung Galaxy smartphone on the e-commerce app."
    },
    {
      "date_or_period": "14th November 2024",
      "event": "Smartphone was delivered."
    },
    {
      "date_or_period": "Within 24 hours of delivery",
      "event": "Screen started flickering with green lines and touch stopped working."
    },
    {
      "date_or_period": "15th November 2024",
      "event": "Raised a replacement request on the app."
    },
    {
      "date_or_period": "21st November 2024",
      "event": "Technician inspected the device, confirmed the manufacturing hardware defect, and took a signature on the job sheet."
    },
    {
      "date_or_period": "23rd November 2024",
      "event": "Customer support cancelled the return request stating the 7-day return window expired on 21st November."
    }
  ],
  "evidence_held": [
    "Invoice",
    "Delivery receipt",
    "Technician inspection job sheet copy",
    "Chat screenshots with customer support"
  ],
  "evidence_needed": [
    "Unboxing video (if any exists)",
    "Payment transaction receipt/bank statement",
    "Written emails sent to customer support"
  ],
  "evidence_strength_score": 8,
  "evidence_strength_explanation": "Strong documentary proof including invoice, delivery receipt, and an official technician job sheet confirming the manufacturing defect.",
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
  "plain_language_selling": null,
  "plain_language_standing": "Your consumer rights are fully protected under Indian law, as you reported a manufacturing defect within the permitted timeframe and possess an official technician's verification. Under the Consumer Protection Act, supplying a defective product and refusing to refund or replace it constitutes both a 'defect in goods' and an 'unfair trade practice'. Your immediate takeaway is that you have strong documentary evidence (invoice, job sheet, chats) to challenge the e-commerce platform's unfair refusal of your replacement.",
  "governing_laws": [
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(7)",
      "relevance": "Protects you as a consumer who bought goods for consideration through an online e-commerce transaction."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(10)",
      "relevance": "Defines a 'defect' as any fault, imperfection, or shortcoming in the quality, quantity, or standard required under a contract."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(47)",
      "relevance": "Classifies refusing to refund or replace defective goods within the stipulated or reasonable period as an 'unfair trade practice'."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 84",
      "relevance": "Establishes product manufacturer and seller liability for manufacturing and design defects."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Immediate Pre-Litigation Action (Formal Legal Notice / Helpline)",
      "timeline": "Suggested 15 days (customary pre-litigation practice)",
      "details": "Lodge a formal grievance on the National Consumer Helpline (NCH) toll-free at 1915 or via consumerhelpline.gov.in. Additionally, serve a formal Legal Demand Notice to the seller and e-commerce platform highlighting the technician's job sheet and your timely reporting."
    },
    {
      "step_number": 2,
      "title": "Statutory Authority / Grievance Portal Filing",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "File an electronic consumer complaint online on e-Daakhil (edaakhil.nic.in) attaching your order invoice, defect photos, technician job sheet, and communication history. Note: DLSA Helpline 15100 provides free legal aid and guidance only; it is never a forum for hearings or proceedings."
    },
    {
      "step_number": 3,
      "title": "Statutory Forum / Consumer Commission Petition",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "If the pre-litigation notice and NCH escalation do not yield a replacement or refund, pursue a formal consumer complaint before the District Consumer Disputes Redressal Commission."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "You do not need a physical advocate to file a consumer complaint. Consumer Commissions in India are designed for self-representation, allowing citizens to file and argue their cases personally without mandatory legal representation.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
**LEGAL DEMAND NOTICE**

**BY SPEED POST WITH ACKNOWLEDGEMENT DUE / REGISTERED EMAIL**

**Date:** 08/11/2026

**To,** 
The Grievance Officer / Authorized Representative, 
[E-Commerce Platform / Seller Name], 
[Company Address Line 1], 
[Company Address Line 2], 
City - [Pincode]. 

---

**SUBJECT: LEGAL DEMAND NOTICE FOR SUPPLYING DEFECTIVE GOODS, UNFAIR TRADE PRACTICES, AND WRONGFUL REFUSAL OF REPLACEMENT REGARDING ORDER OF SAMSUNG GALAXY SMARTPHONE (AMOUNT: RS. 26,999).**

---

Sir / Madam,

Under instructions from and on behalf of my client, **[Complainant's Name]**, residing at [Complainant's Address] (hereinafter referred to as the **"Client"**), I do hereby serve upon you this formal Legal Demand Notice under the relevant provisions of the Consumer Protection Act, 2019, on account of supplying a defective product and subsequently engaging in unfair trade practices by refusing a valid replacement, and state as under:

### **1. RECITALS & FACTUAL SEQUENCE**

1.1. That on **10th November 2024**, the Client placed an online order for a Samsung Galaxy smartphone through your e-commerce platform/application, paying a valuable consideration of **Rs. 26,999** [Payment transaction details / Receipt Reference if applicable]. 
1.2. That the said smartphone was delivered to the Client on **14th November 2024**. 
1.3. That **within 24 hours of delivery**, the smartphone exhibited severe hardware defects—specifically, the screen started flickering with green lines and touch functionality completely stopped working. 
1.4. That acting promptly and within the permissible return/replacement window, the Client raised a formal replacement request on your application on **15th November 2024**. 
1.5. That on **21st November 2024**, an authorized technician visited the Client, thoroughly inspected the device, physically verified and confirmed the manufacturing hardware defect, and obtained the Client's signature on the official inspection job sheet. 
1.6. That despite the official verification by your authorized technician, your customer support arbitrarily and wrongfully cancelled the return request on **23rd November 2024**, falsely alleging that the 7-day return window had supposedly expired on 21st November 2024, completely ignoring the fact that the request was raised well within time on 15th November 2024.

---

### **2. VIOLATION OF STATUTORY PROVISIONS**

Your aforesaid acts of delivering a defective product and subsequently refusing a legitimate replacement by raising arbitrary procedural technicalities constitute direct violations of the consumer rights protected under the **Consumer Protection Act, 2019**:

* **Section 2(7) of the Consumer Protection Act, 2019:** Protects the Client as a consumer who bought goods for consideration through an online e-commerce transaction.
* **Section 2(10) of the Consumer Protection Act, 2019:** Defines a "defect" as any fault, imperfection, or shortcoming in the quality, quantity, or standard required under a contract. The delivered Samsung Galaxy smartphone suffered from a direct manufacturing hardware defect.
* **Section 2(47) of the Consumer Protection Act, 2019:** Classifies refusing to refund or replace defective goods within the stipulated or reasonable period as an "unfair trade practice."
* **Section 84 of the Consumer Protection Act, 2019:** Establishes product manufacturer and seller liability for manufacturing and design defects.

---

### **3. DEMAND FOR RECTIFICATION**

In light of the above facts and statutory provisions, you are hereby called upon to:

1. **Process and deliver a brand-new, defect-free replacement** of the Samsung Galaxy smartphone, OR in the alternative, **issue a complete refund of Rs. 26,999** directly to the Client's original payment source; and
2. Confirm compliance with this demand within a strict **15-day rectification demand window** from the date of receipt of this notice.

---

### **4. WARNING OF FURTHER LEGAL ACTION**

Please take notice that if you fail to comply with the demands outlined above within the stipulated **15-day period**, my client shall be constrained to initiate appropriate legal proceedings against your entity without any further reference. 

These proceedings will include filing a formal consumer complaint before the appropriate **District Consumer Disputes Redressal Commission**, seeking a full refund/replacement, compensation for mental agony, and litigation costs. Additionally, the matter shall be escalated to the National Consumer Helpline (NCH) via 1915 / consumerhelpline.gov.in. 

*(Note: For free legal guidance and information regarding consumer rights, citizens may contact the District Legal Services Authority (DLSA) / NALSA Toll-Free Helpline at **15100**. DLSA provides free legal aid and guidance only and is not a forum for proceedings against employers or commercial entities).*

Please treat this notice with the urgency it deserves.

Yours faithfully,

*(Signed)* 
**[Complainant's Name / Authorized Representative]** 
[Contact Number] 
[Email Address] 

---

### **ANNEXURE INVENTORY (ENCLOSED DOCUMENTS):**
1. Copy of Order Invoice (Rs. 26,999)
2. Delivery receipt dated 14th November 2024
3. Technician inspection job sheet copy dated 21st November 2024
4. Chat screenshots with customer support showing cancellation on 23rd November 2024

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under Section 2(11) and Section 84 of the Consumer Protection Act 2019, delivering a defective phone and delaying inspection past your return window is a clear deficiency in service and unfair trade practice. I have the technician report confirming hardware fault. I demand an immediate refund or I will escalate to the National Consumer Helpline and e-Daakhil."*
- **Opponent Reaction:** Arre sir/madam, why are you threatening with consumer court and all? Look, our system automatically locks the replacement option after 7 days, no matter what. The technician report is fine, but backend team says policy is policy. Still... since you have the report and you are creating a big issue, let me check with my senior manager... okay, we can offer you a repair or store credit, but full cash refund of Rs. 26,999 is not possible directly. Take the repair na?
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You precisely cited Section 2(11) for deficiency in service and Section 84 for product liability under the Consumer Protection Act 2019, while mentioning concrete proof (technician report) and escalation channels.",
  "what_to_improve": "Do not accept store credit or forced repairs for a DOA (Dead on Arrival) or manufacturing defect received out-of-the-box. Insist on a complete refund to the original payment source.",
  "suggested_next_counter": "Under Section 14 of the Consumer Protection Act, supplying a defective product mandates a full refund of Rs. 26,999 along with compensation; I reject store credit and demand a full cash refund immediately."
}
```

---

## TC-03: Gurugram Tech Employee Unpaid Salary & Relieving Letter Withheld

- **Timestamp:** `2026-11-08T13:31:41.714208+00:00`
- **Provider / Model:** `Gemini` / `gemini-3.5-flash-lite`
- **Category:** `Employment & Salary`

### 1. Raw User Input
```text
I worked as a frontend developer at an IT consultancy firm in Cyber City, Gurugram for 18 months at Rs 70,000/month. I submitted my resignation on 1st August 2024 and completed my full 60-day notice period till 30th September 2024. All project handovers and company assets (MacBook, ID card) were handed over and I received an asset clearance certificate from IT. My August salary was delayed, and my September salary plus 15 days encashable leave (total Rs 1,65,000) has not been paid. It has been 50 days since my last working day. Whenever I email HR, they say 'finance team is facing client payment delays'. More importantly, they are withholding my Relieving Letter and Experience Certificate. My new employer is threatening to cancel my job offer if I don't submit my relieving letter by end of this week. I have my appointment letter, resignation acceptance email, and signed clearance form.
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Withholding of Final Salary, Leave Encashment, and Relieving Documents by IT Employer",
  "category": "Employment & Salary",
  "summary": "The complainant worked as a frontend developer for 18 months and completed a 60-day notice period ending September 30, 2024. The employer has withheld the August salary, September salary, and 15 days of leave encashment totaling Rs 1,65,000, along with the relieving letter and experience certificate, threatening a new job offer.",
  "complainant": "Frontend Developer (Ex-Employee)",
  "opposite_party": "IT Consultancy Firm, Cyber City, Gurugram",
  "disputed_amount": "Rs. 1,65,000",
  "timeline": [
    {
      "date_or_period": "18 months prior to August 2024",
      "event": "Complainant worked as a frontend developer at an IT consultancy firm in Gurugram at Rs 70,000/month."
    },
    {
      "date_or_period": "1st August 2024",
      "event": "Complainant submitted resignation."
    },
    {
      "date_or_period": "30th September 2024",
      "event": "Completed 60-day notice period, handed over all project assets, and received an asset clearance certificate from IT."
    },
    {
      "date_or_period": "Past 50 days",
      "event": "Repeated follow-ups with HR regarding pending dues and relieving letters, with HR citing client payment delays."
    }
  ],
  "evidence_held": [
    "Appointment letter",
    "Resignation acceptance email",
    "Signed clearance form / asset clearance certificate from IT",
    "Emails with HR regarding payment delays"
  ],
  "evidence_needed": [
    "Bank statements showing salary credit history for the last 18 months",
    "Written formal demand/legal notice sent to company leadership",
    "Written communication from the new employer regarding the deadline for the relieving letter"
  ],
  "evidence_strength_score": 8,
  "evidence_strength_explanation": "The claim is well-supported by an appointment letter, resignation acceptance, and a formal signed asset clearance certificate, though bank records and a formal demand notice would further solidify the case.",
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
  "plain_language_standing": "Your unpaid wage and document withholding issue is fundamentally a civil employment dispute, not a criminal matter, and the law protects your right to timely payment. Under Section 17(2) of the Code on Wages, 2019, an employee's wages upon resignation must be paid within two working days. Your immediate takeaway is that you should formally demand your unpaid dues and relieving documents in writing while preparing to approach the competent labour authority if the employer fails to comply.",
  "governing_laws": [
    {
      "act_name": "Code on Wages, 2019",
      "section": "Section 17(2)",
      "relevance": "Mandates that the wages of an employee who resigns must be paid within two working days of their resignation or separation date."
    },
    {
      "act_name": "General Legal Principle (Civil vs. Criminal Boundary)",
      "section": "General Guidance",
      "relevance": "Clarifies that withholding salary or breaching an employment contract is a civil dispute, meaning criminal police complaints or FIRs are legally improper."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Immediate Pre-Litigation Action",
      "timeline": "Suggested 15 days (customary pre-litigation practice)",
      "details": "Send a formal written demand email or notice to your employer citing Section 17(2) of the Code on Wages, 2019, requesting the immediate release of your unpaid wages and relieving documents within two working days."
    },
    {
      "step_number": 2,
      "title": "Statutory Authority / Grievance Portal Filing",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "For formal proceedings or recovery of unpaid wages, approach the competent labour authority (confirm locally). Note: The District Legal Services Authority (DLSA) / NALSA Helpline 15100 provides free legal aid and guidance only, and is never a forum for hearings or proceedings against an employer."
    },
    {
      "step_number": 3,
      "title": "Statutory Forum / Labour Dispute Resolution",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "If the employer fails to respond to your formal demand, file a formal wage claim petition before the competent labour authority (confirm locally) for conciliation and recovery."
    }
  ],
  "real_lawyer_needed": true,
  "real_lawyer_guidance": "Given the complexities of negotiating with corporate HR, withheld relieving documents affecting a new job offer, and employer resistance, consulting a licensed advocate or utilizing free legal aid via the District Legal Services Authority (DLSA) Helpline 15100 is advised.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
**MODE OF DISPATCH: SPEED POST WITH ACKNOWLEDGEMENT DUE (AD) / REGISTERED EMAIL**

**LEGAL DEMAND NOTICE**

**Date:** 08/11/2026

**FROM:** 
[Your Name / Ex-Employee] 
Frontend Developer 
[Your Residential Address] 
Contact Number: [Your Phone Number] 
Email: [Your Email Address] 

**TO:** 
The Management / Human Resources Department 
IT Consultancy Firm 
Cyber City, Gurugram 
[Company Pin Code] 

---

**SUBJECT: LEGAL DEMAND NOTICE FOR WITHHOLDING OF FINAL SALARY, LEAVE ENCASHMENT, RELIEVING LETTER, AND EXPERIENCE CERTIFICATE TOTALING RS. 1,65,000/-**

**Under instructions from my client, the undersigned submits as under:**

1. That my client was employed with your IT consultancy firm at Cyber City, Gurugram, as a Frontend Developer, at a monthly salary of Rs. 70,000/-, for a period of[unverified reference removed] months prior to August 2024.
2. That on 1st August 2024, my client formally submitted their resignation from the said position.
3. That my client diligently served and completed the mandatory 60-day notice period, which culminated on 30th September 2024. Upon completion, my client successfully handed over all project assets and obtained a signed clearance form / asset clearance certificate from the IT department of your firm.
4. That despite the successful separation and handover, your establishment has wrongfully withheld my client’s salary for the month of August 2024, salary for the month of September 2024, and 15 days of leave encashment, aggregating to a total undisputed sum of Rs. 1,65,000/-.
5. That in addition to withholding the statutory dues of Rs. 1,65,000/-, your firm has also wrongfully withheld my client's relieving letter and experience certificate, thereby creating severe impediments and threats to my client's new job offer.
6. That over the past 50 days, my client has made repeated follow-ups with the Human Resources department regarding the clearance of pending dues and the issuance of relieving documents. However, your representatives have cited arbitrary reasons such as client payment delays, which hold no legal bearing on my client’s statutory right to receive earned wages upon separation.
7. That your aforesaid acts are in direct violation of statutory provisions, specifically **Section 17(2) of the Code on Wages, 2019**, which mandates that the wages of an employee who resigns or whose employment is terminated must be paid within two working days of their separation date.
8. That withholding earned wages and mandatory employment documents constitutes a civil employment breach and causes severe mental agony and professional injury to my client. For legal guidance and support regarding this dispute, my client has been advised of available resources, including the District Legal Services Authority (DLSA) / NALSA Toll-Free Helpline: 15100.

---

**DEMAND FOR RECTIFICATION**

Through this notice, my client hereby calls upon you to clear and disburse the total withheld amount of **Rs. 1,65,000/-** (Rupees One Lakh Sixty-Five Thousand Only) towards the August 2024 salary, September 2024 salary, and leave encashment, along with the immediate issuance of the relieving letter and experience certificate, **within a strict 15-day window** from the receipt of this notice.

**WARNING OF FURTHER LEGAL ACTION**

Take notice that if you fail to comply with the demands detailed above within the stipulated 15-day rectification window, my client shall be constrained to initiate appropriate formal legal proceedings without any further reference. This shall include filing a formal wage claim petition and instituting legal action before **the competent labour authority (confirm locally)** for the recovery of dues, interest, and compensation, holding your establishment fully liable for all associated costs and consequences.

Kindly treat this matter as urgent and time-sensitive.

---

**SINCERELY AND UNDER INSTRUCTIONS,**

*(Signature)* 
**[Your Name]** 
Frontend Developer (Ex-Employee)

---

**ANNEXURE INVENTORY (ENCLOSED COPIES):**
1. Copy of Appointment Letter
2. Copy of Resignation Acceptance Email
3. Copy of Signed Clearance Form / Asset Clearance Certificate from IT
4. Copy of Emails with HR regarding payment delays

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under employment laws, full and final dues must be cleared timely and withholding my relieving letter violates my right to livelihood. If my Rs 1,65,000 and relieving letter are not issued within 3 days, I will file a formal complaint with the District Labor Commissioner."*
- **Opponent Reaction:** Arre, why are you threatening like this? District Labor Commissioner and all? See, read your appointment letter clause 14.2 properly. Full and final settlement has a standard processing time of 90 working days, and internal audit clearances are still pending from your project manager. Regarding documents, until the exit formalities and knowledge transfer sign-off are complete, HR cannot issue the relieving letter. Don't unnecessarily create tension over email, okay?
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You firmly stated the total amount (Rs 1,65,000), specific timeline, and threatened a direct legal escalation (District Labor Commissioner) while highlighting the violation of your right to livelihood.",
  "what_to_improve": "You didn't mention specific dates or provide proof of your handover completion. Mentioning exact dates of your notice period completion (September 30, 2024) and citing that withholding wages beyond standard statutory timelines attracts strict liability would break their standard 'internal audit' excuse.",
  "suggested_next_counter": "My notice period ended on September 30, 2024, and internal delays cannot override statutory wage timelines; release my dues and documents immediately or face the labor court."
}
```

---

