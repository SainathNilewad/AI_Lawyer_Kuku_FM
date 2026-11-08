# NyayaMitra - Official Unedited Raw Outputs for Test Cases

> **Execution Metadata:** Generated on `2026-11-08T20:55:11.091011+00:00` using Provider: `Gemini`, Model: `gemini-3.5-flash-lite`.
> **Strict Ground Rule:** Real agent calls only. No post-editing, no mock datasets.

## TC-01: Bengaluru Tenant Security Deposit Withholding

- **Timestamp:** `2026-11-08T20:54:00.177020+00:00`
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
  "summary": "The landlord, Mr. Ramesh, withheld Rs. 45,000 from the tenant's security deposit of Rs. 1,00,000 for house repainting, marble polishing, and deep cleaning after the tenant vacated the premises in good condition. The tenant has cleared all utility bills, given proper notice, and possesses comprehensive proof including move-in/move-out records and WhatsApp acknowledgments.",
  "complainant": "Tenant",
  "opposite_party": "Landlord Mr. Ramesh",
  "disputed_amount": "Rs. 45,000",
  "timeline": [
    {
      "date_or_period": "1st October 2024",
      "event": "Tenant gave proper 1-month notice to vacate the 2BHK flat."
    },
    {
      "date_or_period": "31st October 2024",
      "event": "Tenant vacated the flat, cleared all electricity and water bills, and handed over keys."
    },
    {
      "date_or_period": "Within 3 days of 31st October 2024",
      "event": "Landlord Mr. Ramesh promised to refund the security deposit via UPI."
    },
    {
      "date_or_period": "25 days post-vacation / Yesterday",
      "event": "Landlord stopped picking calls and sent a message deducting Rs. 45,000 for repainting, polishing, and deep cleaning."
    }
  ],
  "evidence_held": [
    "Move-in photos",
    "Move-out handover video",
    "All rent payment bank statements",
    "WhatsApp chat where the landlord acknowledged receiving the flat in good condition"
  ],
  "evidence_needed": [
    "Copy of the signed Rent Agreement (to verify clauses regarding painting, cleaning, and security deposit refund timelines)",
    "Written formal demand/legal notice or final written response sent to the landlord"
  ],
  "evidence_strength_score": 9,
  "evidence_strength_explanation": "The evidence strength is high due to comprehensive documentation including handover videos, move-in/move-out records, and direct WhatsApp acknowledgments from the landlord.",
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
  "plain_language_standing": "You are well-protected under Indian tenancy law regarding the return of your security deposit, as routine wear and tear cannot be charged to you. Under the Transfer of Property Act, 1882, tenants are only responsible for returning the property in its original condition subject to normal wear and tear. Your comprehensive evidence, including WhatsApp chats and handover videos, places you in a very strong legal position to recover your withheld funds.\n\nKey Legal Rule: Normal aging, minor scuffs, and routine wear and tear are legally the landlord's responsibility, and unauthorized deductions from your security deposit constitute a civil breach of contract.\n\nImmediate Takeaway: Do not file a criminal complaint, as this is purely a civil dispute; instead, gather your written agreement and serve a formal demand notice for your full refund.",
  "governing_laws": [
    {
      "act_name": "Transfer of Property Act, 1882",
      "section": "Section 108(B)(m)",
      "relevance": "Protects you from being penalized for reasonable wear and tear, ensuring you are not liable for routine repainting or natural property aging."
    },
    {
      "act_name": "[unverified reference removed]",
      "section": "General Guidance",
      "relevance": "Clarifies that withholding a deposit is a civil dispute and breach of contract, preventing improper criminal police complaints.",
      "status": "unverified reference removed"
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Serve a Formal Legal Demand Notice",
      "timeline": "Suggested 15 days (customary pre-litigation practice)",
      "details": "Draft and send a formal written legal notice to the landlord citing Section 108(B)(m) of the Transfer of Property Act, demanding the immediate return of the unlawfully deducted deposit amount using your move-out photos and WhatsApp acknowledgments as proof."
    },
    {
      "step_number": 2,
      "title": "Utilize Free Legal Guidance and Support",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "If the landlord fails to respond, contact the District Legal Services Authority (DLSA) via helpline 15100 for free legal aid and guidance. Note: DLSA provides free legal aid and guidance only; it is never a forum for hearings or proceedings against a landlord."
    },
    {
      "step_number": 3,
      "title": "File a Recovery Suit before the Civil Court",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "If the pre-litigation notice and DLSA guidance do not resolve the matter, file a recovery suit for the withheld amount before the local civil court or Small Causes Court using your rent agreement, bank statements, and handover videos."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "You can initiate a pre-litigation legal notice and approach DLSA for free guidance on your own. However, if you choose to file a formal civil recovery suit in court, consulting a licensed advocate will help ensure your documentation and pleadings are properly structured.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
**FROM:**
[Your Name] 
[Your Address] 
Phone: [Your Phone Number] 
Email: [Your Email Address] 

**DATE:** 09/11/2026

**MODE OF DISPATCH:** Speed Post (AD) / Registered Email

**TO:** 
Mr. Ramesh 
[Landlord's Address] 

---

### **SUBJECT: LEGAL DEMAND NOTICE FOR THE UNLAWFUL WITHHOLDING AND ARBITRARY DEDUCTION OF SECURITY DEPOSIT**

Sir,

I, am a tenant and former occupant of the residential premises situated at [Property Address]. I hereby serve upon you this formal legal demand notice regarding the arbitrary and unlawful deduction of Rs. 45,000 from my security deposit of Rs. 1,00,000, and I hereby state and submit as under:

1. That on 1st October 2024, I provided you with a proper 1-month notice to vacate the 2BHK flat that I had rented from you.
2. That on 31st October 2024, I completely vacated the flat, cleared all outstanding electricity and water utility bills, and formally handed over the keys back to you.
3. That within 3 days of 31st October 2024, you acknowledged the handover of the premises and explicitly promised to refund my security deposit of Rs. 1,00,000 via UPI.
4. That despite my peaceful surrender of the premises in good condition—which is fully supported by my move-in photos, move-out handover video, all rent payment bank statements, and WhatsApp chats where you acknowledged receiving the flat in good condition—you failed to refund the full security deposit.
5. That 25 days post-vacation / yesterday, after you suddenly stopped picking up my phone calls, you sent me a message arbitrarily deducting Rs. 45,000 from my security deposit under the pretexts of house repainting, marble polishing, and deep cleaning.
6. That under Section 108(B)(m) of the Transfer of Property Act, 1882, a tenant is only required to restore the property in as good a condition as it was in at the time he was put in possession, subject to changes caused by reasonable wear and tear and irresistible force. Normal aging, minor scuffs, and routine property maintenance such as repainting and deep cleaning after a tenancy are legally the landlord's responsibility and cannot be arbitrarily charged or deducted from my security deposit.
7. That your sudden deduction of Rs. 45,000 constitutes an unauthorized withholding of my funds and a civil breach of our tenancy terms, especially in light of your explicit WhatsApp acknowledgments confirming that the flat was returned in good condition.

### **DEMAND**

I, therefore, call upon you through this notice to pay/refund the unlawfully withheld amount of **Rs. 45,000** to my bank account [or via UPI] within **15 days** from the date of receipt of this notice. 

Please note that if you fail to comply with this demand within the stipulated 15-day rectification window, I shall be constrained to initiate appropriate legal proceedings against you before the appropriate civil forum for the recovery of the said amount, along with associated costs. You may also seek free legal guidance from the District Legal Services Authority (DLSA) via helpline 15100 if required.

Copies of this notice and all supporting evidence are being retained for future legal action.

Sincerely / Yours faithfully,

*(Signature)* 
[Your Name]

---

### **ANNEXURE INVENTORY**
1. Move-in photos
2. Move-out handover video
3. All rent payment bank statements
4. WhatsApp chat screenshots showing landlord's acknowledgment of the flat in good condition
5. Copy of the signed Rent Agreement [if applicable]

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Mr. Ramesh, as per Section 108 of the Transfer of Property Act and the Model Tenancy framework, ordinary wear and tear like wall paint aging cannot be deducted from my deposit. I have the handover video and our chat proof. Please refund my balance 45,000 within 7 days."*
- **Opponent Reaction:** Arre sahab, sections mat sunao mujhe! Agreement clause 14 padha hai kya? Har tenant ko flat waise hi dena padta hai jaise mila tha. Cleaning aur painting ka kharcha toh aana hi hai, sab log yahi karte hain. Chalo theek hai, zyada jhanjhat mat karo, main 20,000 kaat kar baaki bhej deta hoon, final settlement maan lo.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You firmly cited the Transfer of Property Act and Model Tenancy principles regarding normal wear and tear, and backed it up with concrete evidence like handover videos and WhatsApp chats.",
  "what_to_improve": "Do not accept his partial offer of 20,000. Reiterate that no deductions are permissible for normal wear and tear under law, and demand the full Rs. 45,000.",
  "suggested_next_counter": "Mr. Ramesh, normal wear and tear is legally excluded from deductions, and my video proof shows the property was returned in good condition; I expect the full Rs. 45,000 without any arbitrary cuts."
}
```

---

## TC-02: E-Commerce Defective Smartphone Refund Denial

- **Timestamp:** `2026-11-08T20:54:28.350150+00:00`
- **Provider / Model:** `Gemini` / `gemini-3.5-flash-lite`
- **Category:** `Consumer & E-Commerce`

### 1. Raw User Input
```text
I ordered a Samsung Galaxy smartphone worth Rs 26,999 on an e-commerce app on 10th November 2024. It was delivered on 14th November. Within 24 hours of opening the box, the screen started flickering with green lines and touch stopped working. I raised a replacement request on 15th November. The app sent a technician for inspection on 21st November. The technician confirmed it is a manufacturing hardware defect and took sign on his job sheet. But on 23rd November, customer support cancelled my return request stating 'The 7-day return window expired on 21st November'. They are telling me to go to an authorized brand service center 40 km away. I paid for a brand new working phone, not a defective phone repaired on day one. I have the invoice, delivery receipt, technician inspection job sheet copy, and chat screenshots.
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Defective Smartphone Delivery and Denied Replacement by E-Commerce Platform",
  "category": "Consumer & E-Commerce",
  "summary": "The user purchased a smartphone worth Rs. 26,999 which arrived with a manufacturing defect. Despite raising a return request within the window and having a technician verify the defect, the e-commerce platform cancelled the return citing the expiry of the return window and directed the user to a service center.",
  "complainant": "Consumer",
  "opposite_party": "E-Commerce Platform / Seller",
  "disputed_amount": "Rs. 26,999",
  "timeline": [
    {
      "date_or_period": "10th November 2024",
      "event": "User ordered a Samsung Galaxy smartphone on the e-commerce app for Rs. 26,999."
    },
    {
      "date_or_period": "14th November 2024",
      "event": "The smartphone was delivered to the user."
    },
    {
      "date_or_period": "Within 24 hours of delivery (approx. 15th November 2024)",
      "event": "Screen started flickering with green lines and touch stopped working; user raised a replacement request."
    },
    {
      "date_or_period": "21st November 2024",
      "event": "Technician inspected the phone, confirmed the manufacturing hardware defect, and had the user sign the job sheet."
    },
    {
      "date_or_period": "23rd November 2024",
      "event": "Customer support cancelled the return request stating the 7-day return window expired on 21st November."
    }
  ],
  "evidence_held": [
    "Purchase invoice",
    "Delivery receipt",
    "Technician inspection job sheet copy",
    "Chat screenshots with customer support"
  ],
  "evidence_needed": [
    "Unboxing video (if any)",
    "Written communication or emails with the platform detailing the cancellation reason"
  ],
  "evidence_strength_score": 8,
  "evidence_strength_explanation": "Strong documentary and technical proof including an official technician job sheet confirming the manufacturing defect and timely initial complaint.",
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
  "plain_language_selling": "",
  "plain_language_standing": "You are well within your legal rights as a consumer because you reported the defect promptly and obtained an official technician verification. Under Indian law, supplying a defective product and refusing a timely replacement or refund amounts to a deficiency in service and an unfair trade practice. Your immediate takeaway is that you have strong documentary evidence—including the invoice and the technician's job sheet—to demand a full replacement or refund through consumer forums.",
  "governing_laws": [
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(7)",
      "relevance": "Protects you as a consumer who bought goods for consideration."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(10) & 2(11)",
      "relevance": "Defines product defects and deficiencies in service, holding the seller accountable for faulty goods."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(47)",
      "relevance": "Classifies unjustified refusal to refund or replace defective goods as an unfair trade practice."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Lodge Grievance on NCH & Send Formal Legal Notice",
      "timeline": "Suggested 15 days (customary pre-litigation practice)",
      "details": "Lodge a formal complaint on the National Consumer Helpline (NCH) via toll-free number 1915 or consumerhelpline.gov.in. Simultaneously, serve a formal 15-day Legal Demand Notice to the seller and e-commerce platform detailing your technician's job sheet and purchase invoice."
    },
    {
      "step_number": 2,
      "title": "File Electronic Complaint on e-Daakhil",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "If the platform fails to respond or redress your grievance after the notice period, file an electronic consumer complaint online on e-Daakhil (edaakhil.nic.in). Attach your purchase invoice, delivery receipt, technician inspection job sheet copy, and chat screenshots. (Note: For free legal guidance and aid, you may contact the District Legal Services Authority via Helpline 15100)."
    },
    {
      "step_number": 3,
      "title": "District Consumer Disputes Redressal Commission Proceedings",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "Pursue your petition before the District Consumer Commission for formal adjudication, seeking a refund of Rs. 26,999, compensation for mental agony, and litigation costs."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "You can comfortably represent yourself in the Consumer Commission without hiring a physical advocate, as the Consumer Protection Act is designed for self-representation. However, you may consult a lawyer or contact DLSA (Helpline 15100) if you need assistance drafting your formal notice or complaint petition.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
**FROM:** 
[Your Name] 
[Your Address] 
Phone: [Your Phone Number] 
Email: [Your Email Address] 

**DATE:** 09/11/2026 

**MODE OF DISPATCH:** Speed Post with Acknowledgement Due (AD) / Registered Email 

**TO:** 
[Name of E-Commerce Platform / Seller] 
[Registered Office / Business Address of E-Commerce Platform / Seller] 
[City, State, Pincode] 

---

### **SUBJECT: LEGAL DEMAND NOTICE FOR SUPPLYING DEFECTIVE PRODUCT, UNJUSTIFIED CANCELLATION OF RETURN REQUEST, DEFICIENCY IN SERVICE, AND UNFAIR TRADE PRACTICE UNDER THE CONSUMER PROTECTION ACT, 2019**

---

Dear Sir/Madam,

I, am a consumer residing at the address mentioned above in the sender block. I am serving this legal demand notice upon you directly, in my personal capacity, to demand the immediate replacement of the defective product supplied to me or, alternatively, a full refund of the amount paid, along with compensation for the deficiency in service and unfair trade practices committed by your platform and seller.

I hereby state and submit as under:

1. **Purchase and Delivery of the Product:** 
 On 10th November 2024, I placed an online order for a Samsung Galaxy smartphone on your e-commerce platform for a total consideration of Rs. 26,999. The said product was successfully delivered to my address on 14th November 2024.

2. **Immediate Reporting of Defect:** 
 Within 24 hours of delivery (approx. on 15th November 2024), I discovered that the smartphone suffered from a severe manufacturing defect—specifically, the screen started flickering with green lines and the touch functionality completely stopped working. Promptly upon discovering the defect, I raised a replacement request on your platform within the permitted return window.

3. **Technician Verification and Job Sheet:** 
 On 21st November 2024, an authorized technician inspected the smartphone at my location, confirmed the manufacturing hardware defect, and had me sign the official technician inspection job sheet copy. 

4. **Unjustified Cancellation of Return:** 
 Despite the technician's clear verification and my timely initial complaint, your customer support arbitrarily cancelled my return request on 23rd November 2024, stating that the 7-day return window had allegedly expired on 21st November 2024, and improperly directed me to approach a service center.

5. **Statutory Violations & Deficiencies:** 
 Your refusal to process my replacement or refund despite a confirmed manufacturing defect constitutes a direct deficiency in service and an unfair trade practice under Section 2(10), Section 2(11), and Section 2(47) of the Consumer Protection Act, 2019. As a consumer who purchased goods for valid consideration under Section 2(7) of the said Act, I am fully entitled to receive goods of merchantable and defect-free quality.

---

### **DEMAND FOR RECTIFICATION**

Therefore, through this notice, I call upon you to fulfill the following within **15 days** from the receipt of this notice:

1. Arrange for the immediate pickup of the defective smartphone and deliver a brand-new replacement of the same model in working condition; **OR**, in the alternative, issue a full refund of **Rs. 26,999** to my original payment source.
2. Cease and desist from engaging in unfair trade practices of rejecting valid return requests backed by your authorized technician's job sheet.

If you fail to comply with the aforesaid demands within the stipulated 15-day period, I shall be constrained to initiate formal legal proceedings against you before the District Consumer Disputes Redressal Commission via e-Daakhil (`edaakhil.nic.in`), and seek appropriate relief including a full refund, compensation for mental agony, and litigation costs, without any further reference to you. 

*(For free legal guidance and assistance regarding consumer rights, I may also consult the District Legal Services Authority / NALSA Toll-Free Helpline: 15100).*

Please treat this matter with the urgency it deserves.

---

Sincerely / Yours faithfully,

*(Signature)* 
[Your Name] 

---

**ANNEXURE INVENTORY (Documents Enclosed):**
1. Copy of Purchase Invoice (Rs. 26,999)
2. Copy of Delivery Receipt
3. Copy of Technician Inspection Job Sheet signed on 21st November 2024
4. Screenshots of customer support chat logs and return cancellation notification

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under Section 2(11) and Section 84 of the Consumer Protection Act 2019, delivering a defective phone and delaying inspection past your return window is a clear deficiency in service and unfair trade practice. I have the technician report confirming hardware fault. I demand an immediate refund or I will escalate to the National Consumer Helpline and e-Daakhil."*
- **Opponent Reaction:** Arre sir, why are you threatening with all these big legal terms? Look, our system shows the return window is strictly 7 days and it expired. Technician report or whatever, company policy is policy! You go to the service center and get it repaired under warranty. We cannot process a direct refund sitting here.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You effectively cited specific sections of the Consumer Protection Act, 2019 (Section 2(11) for deficiency in service and Section 84 for product liability), and referenced the technician report.",
  "what_to_improve": "Keep up the pressure on the fact that your return request was raised *within* the valid window before they delayed it. Remind them that forcing a brand-new defective product to a service center instead of replacing it is also an unfair trade practice.",
  "suggested_next_counter": "My return request was logged well within the permitted window; running out the clock with your internal delays does not absolve your liability under Section 84 of the Consumer Protection Act, 2019."
}
```

---

## TC-03: Gurugram Tech Employee Unpaid Salary & Relieving Letter Withheld

- **Timestamp:** `2026-11-08T20:54:52.898344+00:00`
- **Provider / Model:** `Gemini` / `gemini-3.5-flash-lite`
- **Category:** `Employment & Salary`

### 1. Raw User Input
```text
I worked as a frontend developer at an IT consultancy firm in Cyber City, Gurugram for 18 months at Rs 70,000/month. I submitted my resignation on 1st August 2024 and completed my full 60-day notice period till 30th September 2024. All project handovers and company assets (MacBook, ID card) were handed over and I received an asset clearance certificate from IT. My August salary was delayed, and my September salary plus 15 days encashable leave (total Rs 1,65,000) has not been paid. It has been 50 days since my last working day. Whenever I email HR, they say 'finance team is facing client payment delays'. More importantly, they are withholding my Relieving Letter and Experience Certificate. My new employer is threatening to cancel my job offer if I don't submit my relieving letter by end of this week. I have my appointment letter, resignation acceptance email, and signed clearance form.
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Withholding of Final Settlement and Relieving Letter by IT Consultancy Firm",
  "category": "Employment & Salary",
  "summary": "The complainant worked as a frontend developer for 18 months, completed a 60-day notice period ending September 30, 2024, and cleared all company assets. The employer has failed to pay the August salary, September salary, and 15 days of encashable leave totaling Rs. 1,65,000, and is additionally withholding the relieving letter and experience certificate, jeopardizing the complainant's new job offer.",
  "complainant": "Frontend Developer (Ex-Employee)",
  "opposite_party": "IT Consultancy Firm, Cyber City, Gurugram",
  "disputed_amount": "Rs. 1,65,000",
  "timeline": [
    {
      "date_or_period": "18 months prior to August 2024",
      "event": "Complainant worked as a frontend developer at the IT consultancy firm in Gurugram at Rs. 70,000/month."
    },
    {
      "date_or_period": "1st August 2024",
      "event": "Complainant submitted resignation and served the 60-day notice period."
    },
    {
      "date_or_period": "30th September 2024",
      "event": "Last working day; complainant completed project handovers, returned company assets, and received an asset clearance certificate."
    },
    {
      "date_or_period": "Post 30th September 2024 (past 50 days)",
      "event": "Salary for August, September, and 15 days encashable leave (total Rs. 1,65,000) remained unpaid, and HR delayed responding with excuses of client payment delays while withholding the Relieving Letter and Experience Certificate."
    }
  ],
  "evidence_held": [
    "Appointment letter",
    "Resignation acceptance email",
    "Signed asset clearance form",
    "Emails with HR regarding payment delays"
  ],
  "evidence_needed": [
    "Bank statements reflecting salary credits for previous months",
    "Written communication or emails demanding full and final (F&F) settlement",
    "Offer letter from the new employer showing deadline for relieving letter submission"
  ],
  "evidence_strength_score": 8,
  "evidence_strength_explanation": "Strong documentary proof including appointment letter, resignation acceptance, and clearance certificate, though bank statements and formal demand notices would further solidify the claim.",
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
  "plain_language_standing": "Your right to receive final settlement and relieving documents upon leaving a job is legally protected under Indian law. Under Section 17(2) of the Code on Wages, 2019, your unpaid wages must be paid within two working days of your resignation or removal. This is fundamentally a civil employment dispute rather than a criminal matter, meaning you should pursue remedies through proper statutory forums rather than filing police complaints.\n\nKey statutory rule: Section 17(2) mandates payment within two working days of leaving.\nImmediate takeaway: Send a formal demand notice to your employer and prepare to approach the competent labor authority if they fail to comply.",
  "governing_laws": [
    {
      "act_name": "Code on Wages, 2019",
      "section": "Section 17(2)",
      "relevance": "Mandates that the wages of an employee who resigns must be paid within two working days of that event."
    },
    {
      "act_name": "[unverified reference removed]",
      "section": "Civil vs. Criminal Boundary",
      "relevance": "Clarifies that withholding wages or breach of employment contracts are civil disputes and not criminal offenses unless initial fraudulent intent is proven.",
      "status": "unverified reference removed"
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Send a Formal Demand Notice",
      "timeline": "Suggested 15 days (customary pre-litigation practice)",
      "details": "Send a formal written demand email and notice to your employer citing Section 17(2) of the Code on Wages, 2019, requesting the immediate release of your unpaid wages and relieving documents within two working days."
    },
    {
      "step_number": 2,
      "title": "Approach the Competent Labor Authority",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "If the employer fails to settle your dues, approach the competent labour authority (confirm locally) for formal proceedings and recovery. Note: You can contact the District Legal Services Authority (DLSA) / NALSA Helpline 15100 for free legal aid and guidance only; it is never a forum for hearings or proceedings against an employer."
    },
    {
      "step_number": 3,
      "title": "Pursue Formal Conciliation and Adjudication",
      "timeline": "Timeline varies by state (confirm locally)",
      "details": "Participate in labor conciliation proceedings initiated through the labor authority to secure your full and final settlement and experience certificates."
    }
  ],
  "real_lawyer_needed": true,
  "real_lawyer_guidance": "Because this involves complex employment recovery and employer pushback impacting a new job offer, consulting a licensed advocate or utilizing free legal aid through the District Legal Services Authority (DLSA / NALSA Helpline 15100) is strongly advised.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
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
[Company Email Address, if known] 

---

### **SUBJECT: LEGAL DEMAND NOTICE FOR RELEASE OF UNPAID SALARY, LEAVE ENCASHMENT, RELIEVING LETTER, AND EXPERIENCE CERTIFICATE TOTUMING TO RS. 1,65,000**

Dear Sir/Madam,

I, am serving this Legal Demand Notice upon you from myself as an aggrieved ex-employee, to demand the immediate settlement of my pending dues and the issuance of my statutory relieving documents.

I hereby state and submit as under:

1. That for 18 months prior to August 2024, I worked as a Frontend Developer at your IT consultancy firm located in Cyber City, Gurugram, drawing a monthly salary of Rs. 70,000.
2. That on 1st August 2024, I formally submitted my resignation and diligently served the 60-day notice period as required by my employment terms.
3. That 30th September 2024 marked my last working day, on which I successfully completed all project handovers, returned all company assets in good condition, and duly received an asset clearance certificate from your authorized representatives.
4. That post 30th September 2024 (past 50 days), my salary for August 2024, salary for September 2024, and 15 days of encashable leave—totaling an amount of Rs. 1,65,000—have remained unpaid. Furthermore, HR has delayed responding with excuses of client payment delays while wrongfully withholding my Relieving Letter and Experience Certificate, thereby severely jeopardizing my new job offer.
5. That your withholding of my statutory dues and essential employment documents is in direct violation of applicable Indian employment laws, including Section 17(2) of the Code on Wages, 2019, which mandates that the wages of an employee who resigns must be paid promptly.

### **DEMAND FOR RECTIFICATION**

I hereby call upon you to clear my full and final settlement of **Rs. 1,65,000** and issue my Relieving Letter and Experience Certificate within **15 days** of receiving this notice. 

Payment must be remitted directly to my salary bank account on record. 

### **WARNING OF LEGAL ACTION**

If you fail to comply with this demand within the stipulated 15-day rectification window, I shall be constrained to initiate formal legal proceedings against your firm before the competent labour authority (confirm locally) for the recovery of my dues and statutory compensation, without any further notice to you. 

*(Note: For free legal aid, guidance, or information regarding your rights, you may contact the District Legal Services Authority (DLSA) / NALSA Toll-Free Helpline at 15100).*

Sincerely / Yours faithfully,

*(Signature)* 
[Your Name] 
Frontend Developer (Ex-Employee)

---

### **ANNEXURE INVENTORY**
1. Copy of Appointment Letter
2. Copy of Resignation Acceptance Email
3. Copy of Signed Asset Clearance Form
4. Copies of Emails with HR regarding payment delays

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under employment laws, full and final dues must be cleared timely and withholding my relieving letter violates my right to livelihood. If my Rs 1,65,000 and relieving letter are not issued within 3 days, I will file a formal complaint with the District Labor Commissioner."*
- **Opponent Reaction:** Arre, listen! Don't give me all these big threats about District Labor Commissioner and right to livelihood. Read your employment agreement—clearance pending hai, internal audits are going on, and exit formalities take time according to company policy. ₹1,65,000 is not small money, and relieving letter needs HR head's final signature which is delayed. Don't unnecessarily create tension over email!
- **Coach Feedback:**
```json
{
  "strength_rating": "Moderate",
  "what_went_well": "You clearly stated the exact total amount (₹1,65,000) and gave a firm timeline of 3 days.",
  "what_to_improve": "You mentioned 'employment laws' generally and threatened a labor commissioner. Make sure to ground your argument strictly in statutory provisions regarding timely wage payment and unauthorized withholding of dues without citing unsourced or restricted acts.",
  "suggested_next_counter": "My notice period ended on September 30, 2024, and assets were cleared; withholding earned wages and my relieving letter directly violates statutory wage provisions under the Code on Wages, 2019."
}
```

---

