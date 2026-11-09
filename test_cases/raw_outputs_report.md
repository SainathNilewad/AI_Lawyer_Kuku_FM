# NyayaMitra - Official Unedited Raw Outputs for Test Cases

> **Execution Metadata:** Generated on `2026-11-09T00:07:30.137324+00:00` using Provider: `Gemini`, Model: `gemini-3.5-flash-lite`.
> **Strict Ground Rule:** Real agent calls only. No post-editing, no mock datasets.

## TC-01: Bengaluru Tenant Security Deposit Withholding

- **Timestamp:** `2026-11-09T00:06:26.569224+00:00`
- **Provider / Model:** `Gemini` / `gemini-3.5-flash-lite`
- **Category:** `Tenancy & Rental`

### 1. Raw User Input
```text
I was renting a 2BHK flat in HSR Layout, Bengaluru for 2 years at Rs 28,000/month. I gave 1 lakh rupees as security deposit. I gave proper 1-month notice on 1st October and vacated the flat on 31st October 2024. I cleared all electricity and water bills and handed over keys. Landlord Mr. Ramesh promised to refund the deposit via UPI in 3 days. Now it has been 25 days, he stopped picking my calls, and yesterday he messaged saying he is deducting Rs 45,000 for 'complete house repainting, marble polishing, and deep cleaning'. There was no damage, just normal nail holes for photo frames and standard wear and tear. I have move-in photos, move-out handover video, all rent payment bank statements, and WhatsApp chat where he acknowledged receiving the flat in good condition. How can I get my Rs 45,000 back?
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Arbitrary Security Deposit Deduction by Landlord in HSR Layout",
  "category": "Tenancy & Rental",
  "summary": "Tenant vacated a 2BHK flat in Bengaluru after providing proper notice and clearing all utility bills, but the landlord is wrongfully withholding Rs 45,000 from the Rs 1,00,000 security deposit under the guise of repainting, polishing, and cleaning despite normal wear and tear.",
  "complainant": "Tenant",
  "opposite_party": "Landlord Mr. Ramesh",
  "disputed_amount": "Rs 45,000",
  "timeline": [
    {
      "date_or_period": "1st October 2024",
      "event": "Tenant provided proper 1-month notice to vacate the flat."
    },
    {
      "date_or_period": "31st October 2024",
      "event": "Tenant vacated the flat, cleared all electricity and water bills, and handed over the keys."
    },
    {
      "date_or_period": "Early November 2024 (3 days post-vacation)",
      "event": "Landlord Mr. Ramesh promised to refund the deposit via UPI within 3 days but failed to do so."
    },
    {
      "date_or_period": "25 days post-vacation",
      "event": "Landlord stopped picking up calls and sent a message claiming a deduction of Rs 45,000 for house repainting, marble polishing, and deep cleaning."
    }
  ],
  "evidence_held": [
    "Move-in photos",
    "Move-out handover video",
    "All rent payment bank statements",
    "WhatsApp chat where the landlord acknowledged receiving the flat in good condition"
  ],
  "evidence_needed": [
    "Copy of the written Rental Agreement (if any) containing clauses regarding maintenance and security deposit deductions",
    "Written record or receipts of cleared electricity and water bills"
  ],
  "evidence_strength_score": 8,
  "evidence_strength_explanation": "Strong documentary and visual proof including handover video and WhatsApp acknowledgment supporting the tenant's claim against arbitrary deductions.",
  "escalation_check": {
    "requires_real_lawyer": false,
    "is_physical_danger": false,
    "reasons": [],
    "reason": "",
    "legal_aid_contact": "District Legal Services Authority (DLSA) / NALSA Toll-Free Helpline: 15100"
  }
}
```

### 3. Plain-Language Rights & Statutory Standing (Direct Model Output)
```json
{
  "plain_language_standing": "You are well-protected under Indian law regarding your security deposit, as routine wear and tear cannot be charged to you. Under the Transfer of Property Act, 1882, normal aging like minor paint wear is considered standard, and you are not liable to pay for full repainting or deep cleaning. Because this is a monetary dispute, it is a civil matter and not a criminal offense unless fraud was present from the beginning.\n\nKey Statutory Rule: Section 108(B)(m) of the Transfer of Property Act protects tenants from being penalized for normal wear and tear when handing back possession.\n\nImmediate Takeaway: Gather your move-in and move-out photos, handover videos, and chat history, and prepare a formal legal demand notice to request your full deposit back.",
  "governing_laws": [
    {
      "act_name": "Transfer of Property Act, 1882",
      "section": "Section 108(B)(m)",
      "relevance": "Protects you from bearing costs for changes caused by reasonable wear and tear upon returning possession of the property."
    },
    {
      "act_name": "Transfer of Property Act, 1882",
      "section": "Section 108(B)(q)",
      "relevance": "Outlines your duty as a lessee to put the lessor back into possession upon lease termination."
    },
    {
      "act_name": "General Legal Principle",
      "section": "Civil vs. Criminal Boundary",
      "relevance": "Clarifies that withholding a deposit is a civil breach of contract rather than criminal cheating, meaning you should pursue civil remedies rather than police complaints."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Immediate Pre-Litigation Action (Formal Legal Notice)",
      "timeline": "Suggested 15 days (customary pre-litigation practice)",
      "details": "Send a formal written legal notice demanding the full refund of your security deposit. Explicitly cite Section 108(B)(m) to dispute the unauthorized wear-and-tear deductions using your move-out video and WhatsApp evidence."
    },
    {
      "step_number": 2,
      "title": "Statutory Authority / Grievance Portal Filing",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "Since tenancy rules depend on state legislation, ask your state's specific rent authority guidelines. Note: DLSA helpline (15100) provides free legal aid and guidance only; it is never a forum for hearings or proceedings against a landlord."
    },
    {
      "step_number": 3,
      "title": "Statutory Forum / Civil Court Petition",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "If the landlord fails to respond to your legal notice or refund the money, file a recovery suit or application before the local civil court / Small Causes Court or appropriate Rent Authority depending on your state."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "You can draft and send a legal demand notice and file initial applications on your own using your strong documentary evidence. However, if the landlord contests the case aggressively in a civil court, you may consult a licensed advocate to represent you.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
### LEGAL NOTICE DRAFT – REVIEW BEFORE SENDING DRAFT – REVIEW BEFORE SENDING

**FROM:** 
[Your Name] 
[Your Address] 
Phone: [Your Phone Number] 
Email: [Your Email Address] 

**DATE:** 09/11/2026 

**MODE OF DISPATCH:** Speed Post with Acknowledgement Due (AD) / Registered Email 

**TO:** 
Mr. Ramesh 
[Landlord's Address / HSR Layout, Bengaluru, Karnataka] 

---

**SUBJECT: LEGAL DEMAND NOTICE FOR THE REFUND OF ILLEGALLY WITHHELD SECURITY DEPOSIT OF RS. 45,000/- RELATING TO TENANCY OF 2BHK FLAT IN HSR LAYOUT, BENGALURU**

Sir, 

I, am a resident of [Your Current Address], and am acting in person on my own behalf. I hereby serve you with this formal legal demand notice under Indian law, setting forth the facts and my demands as under:

1. That I was a lawful tenant under your ownership in respect of the 2BHK residential flat situated at HSR Layout, Bengaluru, pursuant to our tenancy understanding, during which I deposited a sum of Rs. 1,00,000/- (Rupees One Lakh Only) as a security deposit with you. 

2. That on 1st October 2024, in accordance with the terms governing our tenancy, I provided proper 1-month notice to you expressing my intention to vacate the said flat. 

3. That on 31st October 2024, I successfully vacated the flat, cleared all electricity and water bills up to the last date of my occupation, and formally handed over the physical keys of the property back to you. 

4. That in Early November 2024 (3 days post-vacation), you inspected the premises, acknowledged that the flat was received in good condition, and explicitly promised to refund my security deposit of Rs. 1,00,000/- via UPI within 3 days. However, you failed to honor this commitment and did not transfer the funds. 

5. That approximately 25 days post-vacation, after completely ignoring my follow-ups and stopping to pick up my phone calls, you sent a message arbitrarily claiming a wrongful deduction of Rs. 45,000/- from my security deposit under the pretext of house repainting, marble polishing, and deep cleaning. 

6. That I state and submit that your sudden and arbitrary deduction of Rs. 45,000/- is completely unjustified, unlawful, and contrary to the settled principles of Indian tenancy law. Under Section 108(B)(m) of the Transfer of Property Act, 1882, a tenant is explicitly protected from bearing costs or liabilities for changes, deterioration, or wear and tear caused by reasonable and normal aging of the property upon returning possession. The conditions cited by you—namely normal paint wear, minor cleaning, and routine upkeep—fall entirely within the scope of normal wear and tear during a residential tenancy and cannot be legally deducted from my security deposit. 

7. That I am holding robust evidence supporting my claim, including move-in photos, a comprehensive move-out handover video, all rent payment bank statements, and WhatsApp chat records wherein you expressly acknowledged receiving the flat in good condition. 

8. That your unjustified withholding of my hard-earned money amounting to Rs. 45,000/- constitutes a civil breach of our tenancy obligations and causes severe financial loss and mental harassment to me. 

**DEMAND FOR RECTIFICATION:** 

Therefore, through this notice, I hereby call upon you to refund the illegally withheld security deposit amount of **Rs. 45,000/-** to me within a suggested **15-day period (customary pre-litigation practice)** from the date of receipt of this notice, via online bank transfer / UPI to my registered account details. 

Please take note that if you fail to remit the aforementioned sum of Rs. 45,000/- within the stipulated period, I shall be constrained to initiate appropriate legal proceedings before the competent civil court / Small Causes Court or appropriate Rent Authority to recover the said amount, along with associated costs and legal expenses. For free legal aid and guidance regarding this matter, I may also approach the District Legal Services Authority (DLSA Helpline: 15100). 

This notice is issued without prejudice to my rights, remedies, and contentions available under law. 

---

**ANNEXURE INVENTORY:** 
1. Copy of Move-in photos and Move-out handover video footage reference. 
2. Copies of rent payment bank statements. 
3. Transcripts / screenshots of WhatsApp chats acknowledging the good condition of the flat upon handover. 
4. Copies of cleared electricity and water bills. 

---

Sincerely / Yours faithfully, 

*(Signature)* 
[Your Name]

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Mr. Ramesh, as per Section 108 of the Transfer of Property Act and the Model Tenancy framework, ordinary wear and tear like wall paint aging cannot be deducted from my deposit. I have the handover video and our chat proof. Please refund my balance 45,000 within 7 days."*
- **Opponent Reaction:** Arre, Section 108 aur kya-kya bol rahe ho! Dekho ji, agreement padho, usme clearly likha hai flat ko 'as-is, where-is' condition me wapas dena padta hai. Painting toh rules me hai, aur cleaning ka kharcha toh aana hi hai. Thoda negotiate kar sakte hain, 45,000 pura nahi toh chaliye 35,000 final settle kar lete hain, zyada behas mat karo.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You effectively cited Transfer of Property Act Section 108 regarding normal wear and tear, and backed it up with concrete evidence (handover video and chat proofs) and a clear deadline.",
  "what_to_improve": "The landlord is trying to settle for a partial amount. Stay firm on your stance that normal wear and tear cannot be charged at all, and do not compromise on your hard-earned money.",
  "suggested_next_counter": "Mr. Ramesh, normal wear and tear is legally exempt, and my handover video proves the property was returned in good condition. I expect the full Rs 45,000 refund, or I will be forced to escalate this formally."
}
```

---

## TC-02: E-Commerce Defective Smartphone Refund Denial

- **Timestamp:** `2026-11-09T00:06:45.888923+00:00`
- **Provider / Model:** `Gemini` / `gemini-3.5-flash-lite`
- **Category:** `Consumer & E-Commerce`

### 1. Raw User Input
```text
I ordered a Samsung Galaxy smartphone worth Rs 26,999 on an e-commerce app on 10th November 2024. It was delivered on 14th November. Within 24 hours of opening the box, the screen started flickering with green lines and touch stopped working. I raised a replacement request on 15th November. The app sent a technician for inspection on 21st November. The technician confirmed it is a manufacturing hardware defect and took sign on his job sheet. But on 23rd November, customer support cancelled my return request stating 'The 7-day return window expired on 21st November'. They are telling me to go to an authorized brand service center 40 km away. I paid for a brand new working phone, not a defective phone repaired on day one. I have the invoice, delivery receipt, technician inspection job sheet copy, and chat screenshots.
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Defective Smartphone Delivery & Arbitrary Rejection of Replacement by E-Commerce App",
  "category": "Consumer & E-Commerce",
  "summary": "The user purchased a Samsung Galaxy smartphone for Rs 26,999, which arrived with a manufacturing defect. Although a technician verified the defect within the return window, customer support cancelled the replacement request based on an arbitrary expiry date and refused a refund.",
  "complainant": "Consumer",
  "opposite_party": "E-Commerce App / Seller",
  "disputed_amount": "Rs 26,999",
  "timeline": [
    {
      "date_or_period": "10th November 2024",
      "event": "User ordered a Samsung Galaxy smartphone worth Rs 26,999 on the e-commerce app."
    },
    {
      "date_or_period": "14th November 2024",
      "event": "Phone was delivered to the user."
    },
    {
      "date_or_period": "15th November 2024",
      "event": "Within 24 hours of opening the box, screen started flickering and touch stopped working; user raised a replacement request."
    },
    {
      "date_or_period": "21st November 2024",
      "event": "E-commerce app technician inspected the phone, confirmed the manufacturing hardware defect, and took a signature on his job sheet."
    },
    {
      "date_or_period": "23rd November 2024",
      "event": "Customer support cancelled the return request stating the 7-day return window expired on 21st November and directed the user to an authorized service center."
    }
  ],
  "evidence_held": [
    "Invoice",
    "Delivery receipt",
    "Technician inspection job sheet copy",
    "Chat screenshots with customer support"
  ],
  "evidence_needed": [
    "Unboxing video (if available)",
    "Written service center report or job card if visited",
    "Email trail or communication logs with the seller"
  ],
  "evidence_strength_score": 8,
  "evidence_strength_explanation": "Strong documentary proof exists, including an official technician job sheet confirming the manufacturing hardware defect within the timeline.",
  "escalation_check": {
    "requires_real_lawyer": false,
    "is_physical_danger": false,
    "reasons": [],
    "reason": "",
    "legal_aid_contact": "District Legal Services Authority (DLSA) / NALSA Toll-Free Helpline: 15100"
  }
}
```

### 3. Plain-Language Rights & Statutory Standing (Direct Model Output)
```json
{
  "plain_language_standing": "You are well-protected under Indian consumer protection laws as a rightful buyer who received a defective product. Under the Consumer Protection Act, 2019, refusing to refund or replace defective goods within a reasonable period is considered an unfair trade practice. Your immediate takeaway is that you hold strong documentary proof, including a technician's job sheet, and can successfully seek redressal through consumer dispute forums without needing a lawyer initially.\n\nAs a consumer who bought a smartphone for personal use, you have full legal standing to seek a complete refund or replacement. The e-commerce platform and seller cannot arbitrarily hide behind internal return window policies when their own authorized technician officially verified the manufacturing defect.",
  "governing_laws": [
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(7)",
      "relevance": "Protects you as a consumer who bought goods for consideration."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(10)",
      "relevance": "Defines a 'defect' in goods, covering the hardware and screen issues you experienced."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(47)",
      "relevance": "Classifies refusing to refund or replace defective goods as an unfair trade practice."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 35",
      "relevance": "Provides the legal basis for filing your consumer complaint electronically."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Immediate Pre-Litigation Action (Formal Legal Notice & Helpline)",
      "timeline": "Suggested 15 days (customary pre-litigation practice)",
      "details": "Lodge an initial grievance on the National Consumer Helpline (NCH) via toll-free 1915 or consumerhelpline.gov.in. Simultaneously, serve a formal legal demand notice to the seller and e-commerce platform attaching your invoice and the technician's job sheet."
    },
    {
      "step_number": 2,
      "title": "Statutory Authority / Grievance Portal Filing",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "File an electronic consumer complaint online on e-Jagriti with your order invoice, defect photos, technician job sheet, and chat history. Note: DLSA provides free legal aid and guidance only (Helpline 15100); it is never a forum for hearings or proceedings."
    },
    {
      "step_number": 3,
      "title": "Statutory Forum / Consumer Commission Petition",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "If the platform fails to respond or resolve the issue following your notice and e-Jagriti filing, formally approach the District Consumer Disputes Redressal Commission with your complete evidence dossier."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "You can represent yourself comfortably in the Consumer Commission without hiring a physical advocate, as consumer forums are specifically designed for citizen self-representation. A lawyer is optional unless you prefer professional assistance for drafting documents.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
### LEGAL NOTICE DRAFT – REVIEW BEFORE SENDING DRAFT – REVIEW BEFORE SENDING

**FROM:** 
[Your Name] 
[Your Address] 
Phone: [Your Phone Number] 
Email: [Your Email Address] 

**DATE:** 09/11/2026 

**MODE OF DISPATCH:** Speed Post with Acknowledgement Due (AD) / Registered Email 

**TO:** 
1. The Customer Support / Grievance Officer 
 [Name of E-Commerce App / Platform] 
 [Company Address / Registered Office Address] 

2. The Seller 
 [Name of Seller, if available on invoice] 
 [Seller Address] 

---

**SUBJECT: LEGAL DEMAND NOTICE FOR REFUND OF RS 26,999/- ALONG WITH COMPENSATION FOR SUPPLY OF DEFECTIVE SAMSUNG GALAXY SMARTPHONE AND UNFAIR TRADE PRACTICES UNDER THE CONSUMER PROTECTION ACT, 2019.**

Dear Sir/Madam,

I, am serving this legal demand notice upon you in my individual capacity as a consumer, to demand the immediate rectification of the grievance detailed herein.

### I hereby state and submit as under:

1. That on 10th November 2024, I ordered a Samsung Galaxy smartphone worth Rs 26,999 on your e-commerce platform under Order ID #[Insert Order ID].
2. That the said smartphone was delivered to my address on 14th November 2024.
3. That within 24 hours of opening the box, on 15th November 2024, the phone exhibited major functional defects as the screen started flickering and touch stopped working entirely. Consequently, I raised a replacement request on your application on the same day.
4. That on 21st November 2024, your e-commerce app technician visited my location, inspected the phone, officially confirmed the manufacturing hardware defect, and took my signature on his job sheet.
5. That despite your own authorized technician verifying the defect, your customer support arbitrarily cancelled my return request on 23rd November 2024, falsely stating that the 7-day return window had expired on 21st November 2024, and directed me to an authorized service center instead.
6. That supplying a defective product and subsequently refusing a replacement or refund despite internal verification constitutes a clear deficiency in service and an unfair trade practice under Section 2(10) and Section 2(47) of the Consumer Protection Act, 2019.

### DEMAND FOR RECTIFICATION

In light of the above facts and statutory provisions under the Consumer Protection Act, 2019, I hereby call upon you to:

1. Refund the full purchase amount of **Rs 26,999/-** immediately; OR
2. Provide a brand-new, defect-free replacement of the Samsung Galaxy smartphone as originally ordered, without imposing arbitrary conditions.

I suggest that you comply with the above demands within a **suggested 15-day period (customary pre-litigation practice)** from the date of receipt of this notice. 

*(Note: Under Section 84 of the Consumer Protection Act, 2019, liability applies strictly to the product manufacturer. E-commerce platforms and sellers remain liable for unfair trade practices and deficiencies in service as outlined above.)*

### WARNING

If you fail to comply with this notice within the suggested timeframe, I shall be constrained to initiate formal legal proceedings against you by filing an electronic consumer complaint on the e-Jagriti portal and subsequently before the competent District Consumer Disputes Redressal Commission, seeking a full refund, compensation for mental agony, and legal costs, at your sole risk, cost, and consequences.

---

### ANNEXURE INVENTORY:
1. Copy of Order Invoice
2. Delivery Receipt
3. Technician Inspection Job Sheet Copy
4. Screenshots of Chat with Customer Support

Sincerely / Yours faithfully,

*(Signature)* 
[Your Name]

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under Section 2(11) and Section 84 of the Consumer Protection Act 2019, delivering a defective phone and delaying inspection past your return window is a clear deficiency in service and unfair trade practice. I have the technician report confirming hardware fault. I demand an immediate refund or I will escalate to the National Consumer Helpline and e-Jagriti."*
- **Opponent Reaction:** Arre sir, why are you threatening with all these sections and Acts? Dekhiye, policy is policy. Technician report may be there, but our system says replacement window is strictly 7 days from delivery date, and it expired. We cannot bypass automated system rules for anyone. Maximum we can do is direct you to the authorized brand service center for repair. Refund is not possible at all.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You effectively cited the Consumer Protection Act, 2019 (Sections 2(11) and 84) and presented the technician report as concrete proof.",
  "what_to_improve": "Reiterate the exact dates of delivery, technician visit, and cancellation to trap them in their own timeline contradiction.",
  "suggested_next_counter": "Your technician verified the hardware defect within the active window; refusing a replacement or refund for a defective product amounts to an unfair trade practice under the Consumer Protection Act, 2019, and service center repair cannot replace my right to a defect-free product at delivery."
}
```

---

## TC-03: Gurugram Tech Employee Unpaid Salary & Relieving Letter Withheld

- **Timestamp:** `2026-11-09T00:07:10.152434+00:00`
- **Provider / Model:** `Gemini` / `gemini-3.5-flash-lite`
- **Category:** `Employment & Salary`

### 1. Raw User Input
```text
I worked as a frontend developer at an IT consultancy firm in Cyber City, Gurugram for 18 months at Rs 70,000/month. I submitted my resignation on 1st August 2024 and completed my full 60-day notice period till 30th September 2024. All project handovers and company assets (MacBook, ID card) were handed over and I received an asset clearance certificate from IT. My August salary was delayed, and my September salary plus 15 days encashable leave (total Rs 1,65,000) has not been paid. It has been 50 days since my last working day. Whenever I email HR, they say 'finance team is facing client payment delays'. More importantly, they are withholding my Relieving Letter and Experience Certificate. My new employer is threatening to cancel my job offer if I don't submit my relieving letter by end of this week. I have my appointment letter, resignation acceptance email, and signed clearance form.
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Withheld Salary and Service Certificates Dispute",
  "category": "Employment & Salary",
  "summary": "An ex-frontend developer completed a 60-day notice period at an IT firm in Gurugram on 30th September 2024 after 18 months of service. The employer has withheld the August and September salary along with 15 days encashable leave totaling Rs 1,65,000, as well as the Relieving Letter and Experience Certificate, endangering a new job offer.",
  "complainant": "Frontend Developer (Ex-Employee)",
  "opposite_party": "IT Consultancy Firm, Cyber City, Gurugram",
  "disputed_amount": "Rs. 1,65,000",
  "timeline": [
    {
      "date_or_period": "1st August 2024",
      "event": "Submitted resignation to the IT consultancy firm."
    },
    {
      "date_or_period": "30th September 2024",
      "event": "Completed full 60-day notice period, handed over project assets and ID card, and received asset clearance certificate from IT."
    },
    {
      "date_or_period": "Past 50 days",
      "event": "Repeated follow-ups via email regarding unpaid August salary, September salary, and encashable leave, to which HR replied citing client payment delays."
    }
  ],
  "evidence_held": [
    "Appointment letter",
    "Resignation acceptance email",
    "Signed asset clearance form",
    "Emails with HR regarding payment delays"
  ],
  "evidence_needed": [
    "Bank statements showing past salary credits",
    "Employment contract detailing notice period and leave encashment terms",
    "Written communication from the new employer regarding the threat to cancel the job offer"
  ],
  "evidence_strength_score": 7,
  "evidence_strength_explanation": "Strong documentary proof of employment, resignation acceptance, and formal clearance exists, though final pay slips and bank statements should be compiled.",
  "escalation_check": {
    "requires_real_lawyer": true,
    "is_physical_danger": false,
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
  "plain_language_standing": "You are well within your legal rights to demand your full and final settlement from your former employer after completing your notice period. Under Indian labor law, unpaid wages upon resignation must be settled promptly, and withholding earned compensation is a civil matter rather than a criminal one. Your strong documentary evidence, including your resignation acceptance and clearance form, puts you in a solid position to seek your dues.\n\nThe Code on Wages, 2019 protects your right to receive your final wages within the legally mandated timeframe following your separation from the company. By following the proper pre-litigation and administrative channels, you can systematically pursue your unpaid salary and leave encashment without needing to resort to inappropriate police complaints.\n\nTake immediate action by issuing a formal written demand to your former employer citing the relevant wage code, and prepare to approach the competent labor authority if they fail to comply within a reasonable period.",
  "governing_laws": [
    {
      "act_name": "Code on Wages, 2019",
      "section": "Section 17(2)",
      "relevance": "States that the wages of an employee who resigns must be paid within two working days of that event."
    },
    {
      "act_name": "General Legal Principle (Civil vs. Criminal Boundary)",
      "section": "General Guidance",
      "relevance": "Establishes that failure to pay wages is a civil dispute or breach of contract rather than criminal cheating, meaning you should pursue labor authorities rather than police complaints."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Immediate Pre-Litigation Action (Formal Legal Notice / Email)",
      "timeline": "Suggested 15 days (customary pre-litigation practice)",
      "details": "Send a formal written demand email to your former employer citing Section 17(2) of the Code on Wages, 2019, requesting immediate release of your unpaid wages within two working days. For your relieving or experience letters, note that no fixed legal deadline is stated in the statute; check your contract and company policy, or consult a lawyer. Do not file criminal police complaints as this is a civil monetary dispute."
    },
    {
      "step_number": 2,
      "title": "Statutory Authority / Grievance Portal Filing",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "For formal proceedings or recovery of unpaid wages, approach the competent labour authority (confirm locally). Remember that the District Legal Services Authority (DLSA) / NALSA Helpline 15100 provides free legal aid and guidance only, and is never a forum for hearings or proceedings against an employer."
    },
    {
      "step_number": 3,
      "title": "Statutory Forum / Labor Petition",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "If the employer fails to respond to your written demands or the labor authority conciliation does not resolve the issue, consult with the competent labor authority or a legal professional to file a formal claim for your remaining dues."
    }
  ],
  "real_lawyer_needed": true,
  "real_lawyer_guidance": "Since this dispute involves potential threats to a new job offer and a significant withheld amount, consulting a licensed advocate or utilizing free guidance from the District Legal Services Authority (DLSA Helpline 15100) is strongly advised to draft a formal legal notice and navigate the labor authority proceedings effectively.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
### LEGAL NOTICE DRAFT – REVIEW BEFORE SENDING DRAFT – REVIEW BEFORE SENDING

**FROM:**
[Your Name] 
[Your Address] 
Phone: [Your Phone Number] 
Email: [Your Email Address] 

**DATE:** 09/11/2026

**MODE OF DISPATCH:** Speed Post with Acknowledgement Due (AD) & Registered Email

**TO:**
IT Consultancy Firm, 
Cyber City, 
Gurugram, 
Haryana 

---

**SUBJECT: LEGAL NOTICE FOR WITHHOLDING DUES, UNPAID SALARY, LEAVE ENCASHMENT, AND SERVICE CERTIFICATES**

Dear Sir/Madam,

I, [Your Name], residing at [Your Address], do hereby issue this formal legal demand notice to you, the management of the IT Consultancy Firm located at Cyber City, Gurugram, calling upon you to clear my outstanding dues and release my professional service documents immediately, as detailed hereunder:

### I hereby state and submit as under:

1. That I was employed with your firm as a Frontend Developer and faithfully completed 18 months of service, discharging my professional responsibilities to the satisfaction of the management.
2. That on 1st August 2024, I formally submitted my resignation to the IT consultancy firm, providing the full contractual notice period.
3. That on 30th September 2024, I completed my full 60-day notice period, successfully handed over all project assets and my ID card, and obtained a signed asset clearance certificate from the IT department.
4. That despite the successful and clean separation, you have wrongfully withheld my salary for the month of August 2024, my salary for the month of September 2024, and 15 days of encashable leave, totaling an amount of Rs. 1,65,000 (Rupees One Lakh Sixty-Five Thousand Only).
5. That in addition to withholding my earned wages, you have also withheld my Relieving Letter and Experience Certificate, despite repeated follow-ups over the past 50 days where your HR department merely cited client payment delays as an excuse for non-payment.
6. That the withholding of my statutory dues and essential service certificates is causing severe financial distress and is endangering my new job offer, which constitutes an untenable withholding of earned compensation.
7. That under Section 17(2) of the Code on Wages, 2019, the wages of an employee who resigns must be paid within the statutory timeline. Furthermore, withholding earned remuneration upon lawful separation constitutes a civil dispute regarding breach of contract and unpaid dues.

### DEMAND FOR RECTIFICATION

Therefore, through this notice, I call upon you to settle my full and final dues amounting to **Rs. 1,65,000** along with my **Relieving Letter and Experience Certificate** within a suggested 15-day period (customary pre-litigation practice) from the receipt of this notice.

Please note that if you fail to disburse the said amount and release my service certificates within the stipulated timeframe, I shall be constrained to initiate formal legal proceedings by approaching the competent labour authority (confirm locally) and taking further legal action under the applicable laws, holding your establishment liable for all attendant costs and consequences. 

*(Note: For free legal guidance or aid regarding this matter, the District Legal Services Authority / NALSA Helpline is 15100).*

Sincerely / Yours faithfully,

*(Signature)* 
[Your Name] 

---

### ANNEXURE INVENTORY
1. Copy of Appointment Letter
2. Copy of Resignation Acceptance Email
3. Copy of Signed Asset Clearance Form
4. Copies of correspondence / emails with HR regarding payment delays

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under employment laws, full and final dues must be cleared timely and withholding my relieving letter violates my right to livelihood. If my Rs 1,65,000 and relieving letter are not issued within 3 days, I will file a formal complaint with the District Labor Commissioner."*
- **Opponent Reaction:** Arre bhai, don't throw empty threats at us with District Labor Commissioner and all! Read your employment agreement properly—Clause 14 clearly says clearance depends on project handover and management discretion. Company policy is final, and our HR head is on leave till next week anyway. Don't disturb us unnecessarily.
- **Coach Feedback:**
```json
{
  "strength_rating": "Moderate",
  "what_went_well": "You firmly demanded your pending dues and relieving letter, and set a clear 3-day deadline while highlighting the threat to your livelihood.",
  "what_to_improve": "You mentioned vague 'employment laws' without citing any specific provisions from the Code on Wages, 2019 regarding timely payment of wages, or the Consumer Protection Act, 2019 for deficient service.",
  "suggested_next_counter": "Under the Code on Wages, 2019, earned wages must be paid promptly, and withholding them along with my relieving letter is legally untenable."
}
```

---

