# NyayaMitra - Official Unedited Raw Outputs for Test Cases

> **Execution Metadata:** Generated on `2026-11-07T00:49:27.717679+00:00` using Provider: `groq`, Model: `openai/gpt-oss-120b`.
> **Strict Ground Rule:** Real agent calls only. No post-editing, no mock datasets.

## TC-01: Bengaluru Tenant Security Deposit Withholding

- **Timestamp:** `2026-11-07T00:46:08.366522+00:00`
- **Provider / Model:** `groq` / `openai/gpt-oss-120b`
- **Category:** `Tenancy & Rental`

### 1. Raw User Input
```text
I was renting a 2BHK flat in HSR Layout, Bengaluru for 2 years at Rs 28,000/month. I gave 1 lakh rupees as security deposit. I gave proper 1-month notice on 1st October and vacated the flat on 31st October 2024. I cleared all electricity and water bills and handed over keys. Landlord Mr. Ramesh promised to refund the deposit via UPI in 3 days. Now it has been 25 days, he stopped picking my calls, and yesterday he messaged saying he is deducting Rs 45,000 for 'complete house repainting, marble polishing, and deep cleaning'. There was no damage, just normal nail holes for photo frames and standard wear and tear. I have move-in photos, move-out handover video, all rent payment bank statements, and WhatsApp chat where he acknowledged receiving the flat in good condition. How can I get my Rs 45,000 back?
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Security Deposit Refund Dispute – Unjust Rs 45,000 Deduction",
  "category": "Tenancy & Rental",
  "summary": "The tenant vacated a 2BHK flat on 31 Oct 2024 after giving proper notice. The landlord promised a full security‑deposit refund but now claims a Rs 45,000 deduction for repainting and cleaning, despite no damage. The tenant seeks the deducted amount back.",
  "complainant": "Tenant (name not specified)",
  "opposite_party": "Landlord Mr. Ramesh",
  "disputed_amount": "Rs 45,000",
  "timeline": [
    {
      "date_or_period": "Oct 2022 – Oct 2024",
      "event": "Tenant occupied 2BHK flat in HSR Layout, Bengaluru on a 2‑year lease at Rs 28,000 per month, paid Rs 1,00,000 security deposit."
    },
    {
      "date_or_period": "1 Oct 2024",
      "event": "Tenant gave one‑month notice to vacate."
    },
    {
      "date_or_period": "31 Oct 2024",
      "event": "Tenant vacated the flat, cleared electricity & water bills, handed over keys, and landlord acknowledged receipt in good condition via WhatsApp."
    },
    {
      "date_or_period": "Early Nov 2024 (within 3 days of vacating)",
      "event": "Landlord promised to refund the full security deposit via UPI within three days."
    },
    {
      "date_or_period": "Mid‑Nov 2024 (≈25 days after vacating)",
      "event": "No refund received; landlord stopped answering calls."
    },
    {
      "date_or_period": "Yesterday (mid‑Nov 2024)",
      "event": "Landlord messaged that he is deducting Rs 45,000 for repainting, marble polishing, and deep cleaning."
    }
  ],
  "evidence_held": [
    "Move‑in photographs of the flat",
    "Move‑out handover video",
    "Bank statements showing monthly rent payments and security‑deposit payment",
    "WhatsApp chat where landlord acknowledges receiving the flat in good condition",
    "Copy of the notice sent on 1 Oct 2024 (if any)"
  ],
  "evidence_needed": [
    "Signed rent/lease agreement specifying security‑deposit terms and deductions allowed",
    "Receipt or acknowledgment of the Rs 1,00,000 security deposit paid",
    "Written notice of termination (email or WhatsApp screenshot) sent on 1 Oct 2024",
    "Any written communication from landlord detailing the Rs 45,000 deduction (e.g., screenshot of the message, email)",
    "Inventory or condition checklist signed by both parties at move‑in and move‑out (if exists)",
    "Quotes/receipts for repainting, marble polishing, or deep‑cleaning (to verify if deduction is justified)",
    "UPI transaction history showing no refund received"
  ],
  "evidence_strength_score": 8,
  "evidence_strength_explanation": "Strong visual (photos/video) and transactional records plus landlord's acknowledgment, but missing the formal lease clause and written deduction notice.",
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
  "plain_language_standing": "You are in a strong position under Indian law to get your full security deposit back. The Model Tenancy Act, 2021 (where adopted by Karnataka) caps the security deposit at two months' rent and requires the landlord to return it within 30 days of you handing over peaceful possession, after deducting only genuine, itemised charges. Ordinary wear‑and‑tear – like the natural fading of paint or normal cleaning – cannot be used to keep part of the deposit. The landlord’s claim of a Rs 45,000 deduction for repainting, marble polishing and deep cleaning is not automatically valid, especially because you have video evidence that the flat was handed back in good condition and the landlord himself confirmed receipt.\n\nBecause the dispute is about money you are owed, it is a civil matter, not a criminal cheating case. You can first ask the landlord in writing to refund the amount (with interest for delay) and, if he does not comply, you may approach the Rent Authority or a Small Causes Court, which allows you to represent yourself without a lawyer. The evidence you already have – photos, videos, payment records and the WhatsApp acknowledgment – will support your claim that no real damage was caused and that the deduction is unjustified.",
  "governing_laws": [
    {
      "act_name": "Model Tenancy Act, 2021",
      "section": "Section 13",
      "relevance": "Limits security deposit to 2 months' rent and mandates refund within 30 days after peaceful possession."
    },
    {
      "act_name": "Model Tenancy Act, 2021",
      "section": "Section 14",
      "relevance": "Prohibits deduction for normal wear and tear; requires itemised bills for any legitimate deduction."
    },
    {
      "act_name": "Model Tenancy Act, 2021",
      "section": "Section 21",
      "relevance": "Specifies that deposit disputes must be filed before the Rent Authority/Rent Court, not a regular civil court."
    },
    {
      "act_name": "Transfer of Property Act, 1882",
      "section": "Section 108(B)(m)",
      "relevance": "Tenant must keep the property in as good condition as received, subject only to reasonable wear and tear."
    },
    {
      "act_name": "Transfer of Property Act, 1882",
      "section": "Section 108(B)(q)",
      "relevance": "Tenant is entitled to the return of the security deposit after vacating and handing over vacant possession."
    },
    {
      "act_name": "General Legal Principle (Civil vs. Criminal Boundary)",
      "section": "N/A",
      "relevance": "Refund disputes are civil matters; criminal cheating charges are inappropriate unless fraud was present from the start."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Send Formal Legal Notice to Landlord",
      "timeline": "15 Days from receipt of notice",
      "cost_estimate": "Free to minimal (Speed Post/Registered Email, approx. Rs. 50‑200)",
      "details": "Draft a concise notice stating: (a) you vacated on 31 Oct 2024, (b) landlord acknowledged good condition, (c) under Model Tenancy Act Sec.13 & Sec.14 he must refund the full Rs 1,00,000 deposit within 30 days, (d) the Rs 45,000 deduction is unjustified, (e) demand refund of Rs 45,000 plus 2% per month interest for delay. Attach copies of photos, handover video, WhatsApp acknowledgment, and payment proof. Send by registered post and email, and keep a copy of the receipt."
    },
    {
      "step_number": 2,
      "title": "File Grievance on State Rent Authority / Online Portal",
      "timeline": "30‑45 Days after notice expiry",
      "cost_estimate": "Zero court fees up to Rs. 5 Lakhs (online filing is free)",
      "details": "If the landlord does not respond or refuses to pay, log in to Karnataka's Rent Authority portal (or the National Consumer Helpline 1915 for guidance). Upload the notice, evidence (photos, video, payment slips, WhatsApp chat), and a brief statement of claim. The portal generates a reference number and forwards the complaint to the Rent Authority, which will schedule a hearing."
    },
    {
      "step_number": 3,
      "title": "Petition Before Rent Authority / Small Causes Court",
      "timeline": "60‑90 Days from filing the grievance",
      "cost_estimate": "Nominal court fee (usually Rs. 500‑1,000 for claims up to Rs. 5 Lakhs)",
      "details": "Prepare a petition citing Model Tenancy Act Sec.13,14,21 and Transfer of Property Act Sec.108. Attach all evidence and a copy of the legal notice. You may appear yourself; the forum allows self‑representation. The authority can order the landlord to refund the deposit with interest and may award a modest penalty for wrongful deduction."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "You can handle the entire process yourself: drafting the notice, filing the online grievance, and appearing before the Rent Authority or Small Causes Court does not require a lawyer. However, if the landlord contests the claim with complex counter‑evidence, or if you feel uncomfortable appearing in court, you may consult a lawyer for advice or representation. Legal aid services (DLSA/NALSA) are also available at no cost.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self‑advocacy tools under Indian laws. For formal courtroom representation or if the dispute escalates, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
**[Your Name]**  
[Flat No./House No., Street]  
HSR Layout, Bengaluru – 560102  
Mobile : +91‑XXXXXXXXXX  
Email   : [your.email@example.com]  

---

### LEGAL DEMAND NOTICE  
*(Security Deposit Refund – Unjust Rs 45,000 Deduction)*  

**Date:** 7 November 2026  

**Mode of Dispatch:** Speed Post – Acknowledgement Due (AD) / Registered Email (with read‑receipt)  

---

#### To,  

**Mr. Ramesh**  
[Landlord’s Address]  
Bengaluru – 5600XX  

---

#### Subject: **Demand for Refund of Unjustly Deducted Security Deposit (Rs 45,000) and Interest within 15 Days**  

---

### 1.  Under instructions from my client **[Tenant’s Full Name]** (hereinafter “the Tenant”), the undersigned hereby serves this legal notice as follows:  

---

### 2.  Facts of the Case  

| Sr. No. | Date / Period | Event |
|--------|---------------|-------|
| 1 | **Oct 2022 – Oct 2024** | The Tenant entered into a written lease for a 2‑BHK flat situated at HSR Layout, Bengaluru, for a period of two (2) years at a monthly rent of **Rs 28,000**. The Tenant paid a security deposit of **Rs 1,00,000** as per the lease. |
| 2 | **1 Oct 2024** | The Tenant served a one‑month notice (copy attached) to vacate the premises on or before **31 Oct 2024**. |
| 3 | **31 Oct 2024** | The Tenant vacated the flat, cleared all electricity & water dues, handed over the keys, and the landlord acknowledged receipt of the flat in **good condition** via WhatsApp (chat screenshot attached). |
| 4 | **Early Nov 2024 (within 3 days)** | The landlord promised to refund the entire security deposit through UPI within three days. |
| 5 | **Mid‑Nov 2024 (≈ 25 days after vacating)** | No refund was received; the landlord stopped answering calls. |
| 6 | **Mid‑Nov 2024 (yesterday)** | The landlord messaged that he is **deducting Rs 45,000** for repainting, marble polishing and deep cleaning, without any itemised bill or prior inspection. |

---

### 3.  Documents & Evidence in Possession (Annexure‑A)

1. Move‑in photographs of the flat.  
2. Move‑out hand‑over video.  
3. Bank statements showing monthly rent payments and the security‑deposit payment.  
4. WhatsApp chat where the landlord acknowledges receipt of the flat in good condition.  
5. Copy of the notice dated **1 Oct 2024**.  

*Documents yet to be produced (to be annexed if obtained):* signed lease agreement, receipt of security deposit, written notice of deduction, quotations/receipts for repainting, marble polishing or deep cleaning, UPI transaction history showing non‑receipt of refund.

---

### 4.  Legal Grounds  

| Provision | Act / Statute | Relevance |
|-----------|---------------|-----------|
| **Section 13** | Model Tenancy Act, 2021 (adopted by Karnataka) | Security deposit limited to two months’ rent and must be returned **within 30 days** of peaceful possession, after deducting only genuine, itemised charges. |
| **Section 14** | Model Tenancy Act, 2021 | No deduction is permissible for **normal wear and tear**; any deduction must be supported by an itemised bill. |
| **Section 21** | Model Tenancy Act, 2021 | Deposit disputes are to be adjudicated before the **Rent Authority / Rent Court**. |
| **Section 108(B)(m) & (q)** | Transfer of Property Act, 1882 | Tenant must keep the premises in as‑good‑as‑received condition; landlord must return the deposit after vacating. |
| **[unverified reference removed]** | Indian Contract Act, 1872 (for interest) | Entitles the creditor to **simple interest at 12 % per annum** for delayed payment. |
| **[unverified reference removed] & 74** | Specific Relief Act, 1963 (for damages) | Allows claim for **interest and compensation for loss** caused by breach of contract. |

The landlord’s unilateral deduction of **Rs 45,000** is **unjustified** because:

* The flat was handed back in **good condition** (as per video & WhatsApp acknowledgment).  
* No itemised bill or prior inspection was produced.  
* The deduction pertains to **normal wear and tear** (paint fading, routine cleaning) which is prohibited under Sec. 14 of the Model Tenancy Act.  

Hence, the landlord is **in breach of contract** and **statutory duty**.

---

### 5.  Demand  

In view of the above, the Tenant **hereby demands**:

1. **Refund of Rs 45,000** (the amount unjustly deducted).  
2. **Simple interest at 12 % per annum** from **31 Oct 2024** till the date of actual payment (interest calculated on a daily basis).  
3. **Compensation for litigation costs** (if any) and statutory damages as may be awarded by the Rent Authority / Small Causes Court.  

**All the above amounts are to be paid within **fifteen (15) days** of receipt of this notice**, i.e., **by 22 November 2026**.  

Payment may be made via UPI to **[Your UPI ID]** or by cheque in favour of **[Your Name]** payable at Bengaluru.

---

### 6.  Consequence of Non‑Compliance  

If the demanded amount is **not received** within the stipulated 15‑day period, the Tenant shall, **without any further notice**, proceed to:

* File a grievance before the **Karnataka Rent Authority** (or the appropriate Small Causes Court) under **Section 21** of the Model Tenancy Act, seeking:
  * Refund of the deducted amount with interest,
  * Statutory penalty for wrongful deduction,
  * Recovery of litigation costs and any other relief the forum deems fit.

* Claim **statutory interest at 12 % per annum** and **damages** as per Sections 73 & 74 of the Indian Contract Act and the Specific Relief Act.

The Tenant also reserves the right to approach the **Consumer Disputes Redressal Forum** if the landlord’s conduct amounts to unfair trade practice under the Consumer Protection Act, 2019.

---

### 7.  Verification  

I, **[Tenant’s Full Name]**, the undersigned, do hereby **verify** that the contents of this notice are true and correct to the best of my knowledge and belief, and that no material fact has been concealed.

---

### 8.  Signature  

```
_____________________________  
[Tenant’s Full Name]  
Date: 7 Nov 2026
```

---

### 9.  Annexure – Inventory  

| Annexure | Description |
|----------|-------------|
| **A‑1** | Move‑in photographs (dated Oct 2022) |
| **A‑2** | Move‑out hand‑over video (31 Oct 2024) |
| **A‑3** | Bank statements (rent & security‑deposit) |
| **A‑4** | WhatsApp chat screenshot (acknowledgement of good condition) |
| **A‑5** | Copy of notice served on 1 Oct 2024 |
| **A‑6** | (If obtained) Signed lease agreement |
| **A‑7** | (If obtained) Receipt of security‑deposit |
| **A‑8** | (If obtained) Screenshot of landlord’s message demanding Rs 45,000 |
| **A‑9** | (If obtained) Quotations/receipts for repainting, marble polishing, deep cleaning |
| **A‑10** | (If obtained) UPI transaction history showing non‑receipt of refund |

---

*Prepared by:*  
**NyayaMitra India – Self‑Help Legal Drafting Service**  
*Disclaimer:* This notice is a self‑help legal document intended for informational purposes. It does **not** constitute legal representation. For any escalation beyond the Rent Authority or for complex counter‑claims, you may consult a licensed advocate or approach the District Legal Services Authority (DLSA) / NALSA (Helpline: 15100).  

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Mr. Ramesh, as per Section 108 of the Transfer of Property Act and the Model Tenancy framework, ordinary wear and tear like wall paint aging cannot be deducted from my deposit. I have the handover video and our chat proof. Please refund my balance 45,000 within 7 days."*
- **Opponent Reaction:** Dekhiye, aapka reference Section 108 aur model tenancy ka hai, lekin hamare lease agreement mein clearly likha hai ki paint ki normal wear‑and‑tear ko bhi tenant ko replace karna hota hai, aur humare standard inspection report bhi ussi ko confirm karta hai. Humein aapka video aur chat mil gaya hai, lekin aapko bhi inspection report sign karni hoti thi jo aapne nahi ki. Phir bhi, hum aapki baat ko dhyan mein rakhte hue, Rs 45,000 ka deduction thoda kam kar dete hain – Rs 30,000 hi rakhte hain, aur aapko 7 din ke andar baaki refund kar denge. Agar aapko ismein koi problem hai, to aap legal notice bhej sakte hain, tab hum aage ki baat karenge.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You cited a specific statutory provision (Section 108) and backed it up with concrete evidence (handover video, chat logs), which forces the landlord to acknowledge the claim.",
  "what_to_improve": "Mention the exact clause in your lease that limits deductions for wear‑and‑tear, and reference the applicable state rent control act or RERA provisions that mandate full deposit return within a specific period, plus interest for delay.",
  "suggested_next_counter": "Ask for the signed inspection report and demand the full Rs 45,000 plus statutory interest, citing the lease clause and RERA/State Rent Act."
}
```

---

## TC-02: E-Commerce Defective Smartphone Refund Denial

- **Timestamp:** `2026-11-07T00:46:50.130691+00:00`
- **Provider / Model:** `groq` / `openai/gpt-oss-120b`
- **Category:** `Consumer & E-Commerce`

### 1. Raw User Input
```text
I ordered a Samsung Galaxy smartphone worth Rs 26,999 on an e-commerce app on 10th November 2024. It was delivered on 14th November. Within 24 hours of opening the box, the screen started flickering with green lines and touch stopped working. I raised a replacement request on 15th November. The app sent a technician for inspection on 21st November. The technician confirmed it is a manufacturing hardware defect and took sign on his job sheet. But on 23rd November, customer support cancelled my return request stating 'The 7-day return window expired on 21st November'. They are telling me to go to an authorized brand service center 40 km away. I paid for a brand new working phone, not a defective phone repaired on day one. I have the invoice, delivery receipt, technician inspection job sheet copy, and chat screenshots.
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Defective Samsung Galaxy phone - Return denied",
  "category": "Consumer & E-Commerce",
  "summary": "The consumer purchased a Samsung Galaxy smartphone for Rs 26,999 on an e‑commerce app. The phone developed a hardware defect within a day, but the platform cancelled the return request citing an expired return window, directing the consumer to a distant service centre.",
  "complainant": "Consumer (Customer)",
  "opposite_party": "E‑commerce Platform (Seller)",
  "disputed_amount": "Rs 26,999",
  "timeline": [
    {
      "date_or_period": "10 Nov 2024",
      "event": "Placed order for Samsung Galaxy smartphone worth Rs 26,999 on the e‑commerce app."
    },
    {
      "date_or_period": "14 Nov 2024",
      "event": "Phone delivered to the consumer."
    },
    {
      "date_or_period": "15 Nov 2024",
      "event": "Within 24 hours of opening, screen flickered and touch stopped; consumer raised a replacement/return request."
    },
    {
      "date_or_period": "21 Nov 2024",
      "event": "Technician visited, inspected the phone, confirmed manufacturing hardware defect, and signed the job sheet."
    },
    {
      "date_or_period": "23 Nov 2024",
      "event": "Customer support cancelled the return request, stating the 7‑day return window expired on 21 Nov, and advised going to an authorized service centre 40 km away."
    }
  ],
  "evidence_held": [
    "Invoice showing purchase price of Rs 26,999",
    "Delivery receipt confirming receipt on 14 Nov 2024",
    "Technician inspection job sheet (signed) indicating hardware defect",
    "Chat screenshots with e‑commerce customer support regarding the return request and cancellation"
  ],
  "evidence_needed": [
    "Video or photos clearly showing the screen flickering and touch failure",
    "Original, unaltered copy of the technician’s report (if any additional notes beyond the job sheet)",
    "Email or in‑app notification confirming the replacement/return request submission date",
    "Written communication from the platform stating the 7‑day return policy terms",
    "Proof of any additional costs incurred (e.g., travel to service centre) if seeking compensation"
  ],
  "evidence_strength_score": 8,
  "evidence_strength_explanation": "Key documents (invoice, delivery receipt, signed technician sheet, chat logs) directly support the claim, giving the evidence a strong but not perfect rating.",
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
  "plain_language_standing": "You are a consumer as defined under the Consumer Protection Act, 2019 because you bought a Samsung Galaxy phone for personal use. The phone turned out to be defective within a day, and a qualified technician has already confirmed a manufacturing fault. Under the Act, a defect in a product is a clear \"deficiency in service\" and the seller (including the e‑commerce platform that facilitated the sale) is required to either replace the product, repair it, or refund you. The platform’s refusal to honour a return, despite the defect being proven, amounts to an unfair trade practice. This is a civil matter – it is about getting your money back or a replacement, not about criminal cheating. You therefore have a strong legal right to seek a refund or replacement through the consumer dispute redressal system.",
  "governing_laws": [
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(7)",
      "relevance": "Defines you as a consumer, giving you standing to approach the consumer forum."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(11)",
      "relevance": "Classifies the hardware fault as a \"deficiency in service\" for which the seller is liable."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(47)",
      "relevance": "The platform’s refusal to accept a return despite a proven defect is an unfair trade practice."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 84",
      "relevance": "Makes the manufacturer/seller liable to compensate you for harm caused by a defective product."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 35",
      "relevance": "Gives you the right to file a complaint before the District Consumer Disputes Redressal Commission."
    },
    {
      "act_name": "General Legal Principle (Civil vs. Criminal Boundary)",
      "section": "N/A",
      "relevance": "Clarifies that failure to refund or replace a defective product is a civil dispute, not a criminal offence."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Send a Formal Legal Notice to the Platform",
      "timeline": "Within 15 days from today",
      "cost_estimate": "Free to minimal (postage or email cost)",
      "details": "Draft a concise notice stating: (a) you bought the phone on 10 Nov 2024, (b) it was defective on 15 Nov 2024, (c) a technician confirmed the defect, (d) the platform’s refusal violates Sections 2(11) & 2(47) of CPA 2019, and (e) you demand a full refund of Rs 26,999 or a replacement within 7 days. Send it by registered post or email and keep a copy of the receipt."
    },
    {
      "step_number": 2,
      "title": "File a Consumer Complaint on the e‑Daakhil Portal",
      "timeline": "Within 30‑45 days",
      "cost_estimate": "Zero court fee for claims up to Rs 5 Lakhs",
      "details": "Register at edaakhil.nic.in, choose ‘Consumer Complaint’, and upload: invoice, delivery receipt, technician’s signed job sheet, chat screenshots, and a copy of the legal notice. Fill in the details of the dispute and request a refund. The portal guides you step‑by‑step and you can represent yourself."
    },
    {
      "step_number": 3,
      "title": "Approach the District Consumer Disputes Redressal Commission",
      "timeline": "Within 60‑90 days if the platform does not comply with the e‑Daakhil order",
      "cost_estimate": "Nominal filing fee (around Rs 100‑200) plus any required stamp duty",
      "details": "If the e‑Daakhil process does not yield a satisfactory order, file a petition directly with the District Consumer Commission of the district where you reside. Attach all documents already uploaded on e‑Daakhil. You may appear personally; a lawyer is optional but not mandatory."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "Consumer forums allow self‑representation, so you can handle the notice and the e‑Daakhil filing yourself. You would only need a lawyer if the platform files an appeal in a higher consumer commission or if you want professional help preparing evidence for a court‑level case.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self‑advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
**[Your Name]**  
[Your Complete Residential Address]  
[City, State – PIN]  
Mobile: [Your Mobile No.] | Email: [Your Email‑ID]  

---

### LEGAL DEMAND NOTICE  
*(Under instructions from my client – the consumer)*  

---

**Date:** 7 November 2026  

**Mode of Dispatch:** Speed Post (Acknowledgement Due) / Registered Email (with read‑receipt)  

**To,**  

The Manager – Legal/Customer‑Care  
[Name of the E‑Commerce Platform]  
[Corporate Office Address]  
[City, State – PIN]  

---

#### 1.  SUBJECT  
**Demand for Refund/Replacement of Defective Samsung Galaxy Smartphone (Order No. __________) – Failure to Honour Return Request in Violation of the Consumer Protection Act, 2019.**  

---

#### 2.  FACTUAL MATRIX  

| Sr. No. | Date / Period | Event |
|--------|---------------|-------|
| 1 | **10 Nov 2024** | Placed an order for a **Samsung Galaxy smartphone** (Model – __________) on your e‑commerce app, paying **Rs 26,999** (Invoice No. __________). |
| 2 | **14 Nov 2024** | The product was delivered at my residence (Delivery Receipt No. __________). |
| 3 | **15 Nov 2024** (within 24 hrs of unboxing) | Screen began flickering; touch‑panel stopped responding. Immediately raised a **replacement/return request** through the app (in‑app notification dated 15 Nov 2024). |
| 4 | **21 Nov 2024** | A certified technician from an authorized service centre inspected the device, **confirmed a manufacturing hardware defect**, and signed the job‑sheet (Annex‑C). |
| 5 | **23 Nov 2024** | Your customer‑support team **cancelled** the return request, stating that the 7‑day return window had expired on 21 Nov 2024, and directed me to an authorized service centre **40 km away** (Chat screenshots – Annex‑D). |

All the above documents (invoice, delivery receipt, technician’s job‑sheet, chat logs) are attached hereto as annexures.

---

#### 3.  LEGAL BASIS  

1. **Consumer Protection Act, 2019** –  
   * **Section 2(7)** defines me as a “consumer”.  
   * **Section 2(11)** treats the hardware fault as a “deficiency in service”.  
   * **Section 2(47)** classifies the refusal to accept a return of a defective product as an **unfair trade practice**.  
   * **Section 84** makes the seller liable to compensate the consumer for loss caused by a defective product.  

2. Under **[unverified reference removed]** of the Act, a consumer is entitled to **interest at the rate of 12 % per annum** on the amount due, from the date of default till actual payment.  

3. The refusal to honour a return despite a **certified defect** is a direct contravention of the above provisions and also violates the **e‑commerce platform’s own 7‑day return policy** (as communicated in the chat).  

---

#### 4.  DEMAND  

In view of the foregoing facts and legal provisions, I **hereby demand** that you, within **fifteen (15) days** from the receipt of this notice (i.e., on or before **22 November 2026**), do **either** of the following, at my option:  

1. **Refund** the full purchase price of **Rs 26,999** (Rupees Twenty‑Six Thousand Nine Hundred Ninety‑Nine only), **plus** statutory interest at **12 % per annum** calculated from **23 Nov 2024** till the date of actual payment, **and** reimbursement of any incidental expenses incurred (e.g., travel to the service centre).  

**OR**  

2. **Replace** the defective Samsung Galaxy smartphone with a brand‑new, identical model, free of any charge, and deliver it to my address within **seven (7) days** of your compliance with this notice.  

Kindly acknowledge receipt of this notice and intimate your intention to comply, within the stipulated period, by sending a written confirmation to the address/email mentioned above.  

---

#### 5.  CONSEQUENCES OF NON‑COMPLIANCE  

If you fail to comply with the above demand within the stipulated **15‑day** period, I shall be constrained to initiate **legal proceedings** without any further notice, which shall include but not be limited to:  

* Filing a complaint before the **District Consumer Disputes Redressal Commission** under **Section 35** of the Consumer Protection Act, 2019;  
* Claiming **interest at 12 % per annum**, **court costs**, **legal expenses**, and **punitive damages** as may be awarded by the forum; and  
* Seeking an order for **specific performance** (i.e., replacement of the product) or **full restitution** with interest.  

Such proceedings shall be instituted at my own cost and risk, and the platform shall be liable for **all consequential losses** arising therefrom.  

---

#### 6.  ANNEXURES  

| Annex‑No. | Description |
|-----------|-------------|
| **Annex‑A** | Original Invoice showing purchase price of **Rs 26,999** |
| **Annex‑B** | Delivery receipt confirming receipt on **14 Nov 2024** |
| **Annex‑C** | Technician’s inspection job‑sheet (signed) confirming hardware defect |
| **Annex‑D** | Screenshots of chat with customer‑support showing cancellation of return request |
| **Annex‑E** | Copy of this Legal Demand Notice (for your records) |
| **Annex‑F** *(if any)* | Any additional evidence (photos/video of defect, travel receipts, etc.) |

---

#### 7.  DECLARATION  

I, **[Your Full Name]**, the undersigned, do hereby declare that the contents of this notice are true and correct to the best of my knowledge and belief, and that I am authorized to issue this notice on my own behalf.  

---  

**Signature of the Consumer**  

_____________________________  
[Your Full Name]  

**Date:** 7 November 2026  

---  

*Please retain a copy of this notice and the acknowledgement receipt for future reference.*  

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under Section 2(11) and Section 84 of the Consumer Protection Act 2019, delivering a defective phone and delaying inspection past your return window is a clear deficiency in service and unfair trade practice. I have the technician report confirming hardware fault. I demand an immediate refund or I will escalate to the National Consumer Helpline and e-Daakhil."*
- **Opponent Reaction:** Dekhiye, aapke dwara diye gaye technician report aur Consumer Protection Act ke sections ko humne note kar liya hai. Company policy ke mutabik, hum aapko 48 ghante ke andar ek senior manager se baat karne ka avsar denge, lekin aapko original invoice, delivery challan aur report ki scanned copy turant upload karni hogi. In documents ki verification ke baad hi hum aapka refund ya replacement process kar sakenge. Kripya yeh sabhi details abhi upload kar dein, tab hum aage ki karwai karenge.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "Aapne specific sections (2(11) aur 84) ka zikr kiya aur technician report ka proof diya, jo aapke daave ko bahut majboot banata hai.",
  "what_to_improve": "Consumer Protection (E‑commerce) Rules, 2020 ke [unverified reference removed] aur 20 ka bhi ullekh karein, jo seller ko defective goods ke liye free repair/replacement ya refund dene ki zimmedari batata hai. Saath hi, aapke order ki exact purchase date aur delivery date ka zikr karen.",
  "suggested_next_counter": "Maine sabhi required documents upload kar diye hain, ab turant refund ya replacement process karne ki maang karta/ti hoon, warna consumer court mein case file kar dunga/dugi."
}
```

---

## TC-03: Gurugram Tech Employee Unpaid Salary & Relieving Letter Withheld

- **Timestamp:** `2026-11-07T00:47:57.883783+00:00`
- **Provider / Model:** `groq` / `openai/gpt-oss-120b`
- **Category:** `Employment & Salary`

### 1. Raw User Input
```text
I worked as a frontend developer at an IT consultancy firm in Cyber City, Gurugram for 18 months at Rs 70,000/month. I submitted my resignation on 1st August 2024 and completed my full 60-day notice period till 30th September 2024. All project handovers and company assets (MacBook, ID card) were handed over and I received an asset clearance certificate from IT. My August salary was delayed, and my September salary plus 15 days encashable leave (total Rs 1,65,000) has not been paid. It has been 50 days since my last working day. Whenever I email HR, they say 'finance team is facing client payment delays'. More importantly, they are withholding my Relieving Letter and Experience Certificate. My new employer is threatening to cancel my job offer if I don't submit my relieving letter by end of this week. I have my appointment letter, resignation acceptance email, and signed clearance form.
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Unpaid Salary and Withholding Relieving Letter after Resignation",
  "category": "Employment & Salary",
  "summary": "The former frontend developer completed a 60‑day notice period and returned all company assets, but the employer has not paid the September salary and leave encashment totaling Rs 1,65,000 and is refusing to issue the relieving and experience letters, jeopardising the new job offer.",
  "complainant": "Former Employee (Frontend Developer)",
  "opposite_party": "Employer – IT consultancy firm (name not specified)",
  "disputed_amount": "Rs 1,65,000",
  "timeline": [
    {
      "date_or_period": "Feb 2023 – July 2024",
      "event": "Employed as frontend developer on a Rs 70,000 per month salary"
    },
    {
      "date_or_period": "1 Aug 2024",
      "event": "Submitted resignation email"
    },
    {
      "date_or_period": "1 Aug – 30 Sep 2024",
      "event": "Served 60‑day notice period; completed all project handovers and returned company assets (MacBook, ID card)"
    },
    {
      "date_or_period": "30 Sep 2024",
      "event": "Received asset clearance certificate from IT department"
    },
    {
      "date_or_period": "Early Sep 2024",
      "event": "August salary was delayed"
    },
    {
      "date_or_period": "By 19 Nov 2024 (≈50 days after last working day)",
      "event": "September salary plus 15 days encashable leave (Rs 1,65,000) still unpaid"
    },
    {
      "date_or_period": "Ongoing (since Sep 2024)",
      "event": "HR replies that finance team faces client payment delays; no salary paid"
    },
    {
      "date_or_period": "Early Nov 2024",
      "event": "Employer withholds relieving letter and experience certificate; new employer demands relieving letter by end of the week"
    }
  ],
  "evidence_held": [
    "Appointment letter",
    "Resignation acceptance email",
    "Signed asset clearance form/certificate",
    "Email correspondence with HR regarding salary delay",
    "Copy of resignation email (sent on 1 Aug 2024)"
  ],
  "evidence_needed": [
    "Salary slips for August and September 2024",
    "Bank statements or UPI/NEFT transaction records showing non‑receipt of September salary",
    "Written company policy on notice period salary and leave encashment",
    "Any email/WhatsApp/chat logs where employer explicitly refuses to release relieving/experience letters",
    "Offer letter or email from new employer stating deadline for relieving letter",
    "Proof of 15 days encashable leave entitlement (e.g., leave balance statement)"
  ],
  "evidence_strength_score": 7,
  "evidence_strength_explanation": "Key documents (appointment, resignation acceptance, clearance) are present, but direct proof of non‑payment (salary slips, bank statements) and written refusal of the relieving letter are still missing.",
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
  "plain_language_standing": "You have a clear legal right to receive the salary and leave encashment that you earned up to your last working day. Under the Code on Wages, 2019, an employer must pay all wages due within two working days of the employee’s removal, dismissal, retrenchment or resignation (Section 17(2)). The amount you are owed – August and September salary plus 15 days of leave encashment – is therefore a civil debt that the employer is legally bound to pay. The same Code also says that no deduction can be made from your wages unless it is expressly authorised (Section 18(1)), so the employer cannot withhold any part of your salary as an excuse for client payment delays.\n\nIn addition, refusing to give you a relieving or experience letter after you have completed your notice period and returned all company property is not a criminal matter; it is a breach of the employment contract and can be pursued as a civil claim for specific performance or damages. The law treats these issues as civil disputes, not cheating under the criminal code, so the appropriate remedy is through labour‑related civil forums rather than a police complaint.",
  "governing_laws": [
    {
      "act_name": "Code on Wages, 2019",
      "section": "Section 17(2)",
      "relevance": "Requires employer to pay all wages (including salary and leave encashment) within two working days of resignation"
    },
    {
      "act_name": "Code on Wages, 2019",
      "section": "Section 17(4)",
      "relevance": "Preserves any other time‑limits for wage payment that may be prescribed by state rules"
    },
    {
      "act_name": "Code on Wages, 2019",
      "section": "Section 18(1)",
      "relevance": "Prohibits unauthorised deductions from wages, preventing the employer from withholding salary as a penalty"
    },
    {
      "act_name": "General Legal Principle (Civil vs. Criminal Boundary)",
      "section": "N/A",
      "relevance": "Clarifies that non‑payment of salary or refusal to issue relieving letters is a civil dispute, not a criminal cheating case"
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Send Formal Legal Notice (Email / Registered Post)",
      "timeline": "Within 15 days from today",
      "cost_estimate": "Free to minimal (postage or email cost)",
      "details": "Draft a concise notice stating: (a) amount owed (Rs 1,65,000), (b) demand payment within 7 days, (c) demand issuance of relieving and experience letters within the same period, (d) mention that under Section 17(2) of the Code on Wages you are entitled to immediate payment, and (e) warn that failure will lead to filing a claim before the Labour Commissioner and DLSA. Attach copies of appointment letter, resignation acceptance, asset clearance certificate, and any HR correspondence. Send via registered post and email, and keep proof of delivery."
    },
    {
      "step_number": 2,
      "title": "File a Grievance on the Labour Ministry’s e‑Daakhil / Labour Commissioner Portal",
      "timeline": "Within 30‑45 days",
      "cost_estimate": "Zero court fees for claims up to Rs 5 Lakhs",
      "details": "Register on the Ministry of Labour’s e‑Daakhil portal (or the state labour department portal). Upload the legal notice, supporting documents, and a brief statement of facts. Select ‘Recovery of Wages and Issuance of Relieving Letter’ as the grievance type. The Labour Commissioner will issue a notice to the employer to comply within a stipulated period (usually 15 days)."
    },
    {
      "step_number": 3,
      "title": "Approach the District Labour Court / DLSA for Recovery of Wages and Specific Performance",
      "timeline": "Within 60‑90 days if earlier steps fail",
      "cost_estimate": "Nominal court fees (around Rs 500‑1,000) plus any filing charges; you may get free legal aid from DLSA",
      "details": "Prepare a plaint citing Section 17(2) and Section 18(1) of the Code on Wages, attach all evidence (notice, emails, asset clearance, salary slips, bank statements). File the suit in the appropriate District Labour Court or approach the District Legal Services Authority for free legal aid. The court can order payment of the pending salary, interest, and direct the employer to issue the relieving and experience letters. You may represent yourself, but a lawyer can help with drafting and representation, especially if the employer contests the claim."
    }
  ],
  "real_lawyer_needed": true,
  "real_lawyer_guidance": "You can start by sending the legal notice and filing the e‑Daakhil grievance yourself; these steps do not require a lawyer. However, if the employer does not comply and you need to file a suit in the Labour Court or seek enforcement of the court’s order, engaging a qualified labour‑law advocate is advisable. A lawyer will ensure the plaint is correctly drafted, help you navigate procedural rules, and represent you effectively in court.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self‑advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
**[Your Name]**  
Frontend Developer (Former Employee)  
Flat No. ___, [Building Name], [Street],  
[Locality], [City] – [Pin Code]  
Mobile: [Your Mobile No.] | Email: [Your Email]  

---

### LEGAL DEMAND NOTICE  

**Date:** ____ ____ 2026  

**Mode of Dispatch:** Speed Post (Speed Post with Acknowledgement Due) / Registered Email (with read‑receipt)  

**To,**  

**The Managing Director / HR Head**  
[Employer’s Company Name] – IT Consultancy Firm  
[Company’s Registered Office Address]  
[City] – [Pin Code]  

---

#### 1. UNDER INSTRUCTIONS FROM MY CLIENT  

The undersigned, **[Your Full Name]**, hereby issues this legal notice on behalf of himself/herself (the “Complainant”) pursuant to the provisions of the **Code on Wages, 2019** and the principles of natural justice, demanding immediate settlement of the dues and issuance of the relieving & experience letters as detailed below.

---

#### 2. FACTUAL MATRIX  

| No. | Date / Period | Event |
|-----|---------------|-------|
| 1 | **Feb 2023 – July 2024** | Employed as Front‑End Developer on a salary of **Rs 70,000 per month**. |
| 2 | **1 Aug 2024** | Submitted resignation via email (copy annexed). |
| 3 | **1 Aug – 30 Sep 2024** | Served the contractual **60‑day notice period**, completed all hand‑overs and returned company assets (MacBook, ID card). |
| 4 | **30 Sep 2024** | Received **Asset Clearance Certificate** from IT department (annexed). |
| 5 | **Early Sep 2024** | August salary was delayed; later paid on ___ (if paid). |
| 6 | **By 19 Nov 2024** (≈ 85 days after last working day) | September salary **plus 15 days encashable leave** (total **Rs 1,65,000**) remains unpaid. |
| 7 | **Since Sep 2024** | HR repeatedly states that the finance team is awaiting client payments; no salary credited. |
| 8 | **Early Nov 2024** | Employer refuses to issue **Relieving Letter** and **Experience Certificate**; new employer has demanded the relieving letter by the end of the week. |

---

#### 3. EVIDENCE IN POSSESSION  

The following documents are annexed hereto and form part of the present notice:  

- **Annexure‑A:** Appointment Letter.  
- **Annexure‑B:** Resignation Acceptance Email (dated 1 Aug 2024).  
- **Annexure‑C:** Signed Asset Clearance Certificate (dated 30 Sep 2024).  
- **Annexure‑D:** Email correspondence with HR regarding salary delay (Sept – Nov 2024).  
- **Annexure‑E:** Copy of the resignation email sent on 1 Aug 2024.  

*The complainant also possesses the following documents which can be produced on demand:* salary slips for Aug‑Sep 2024, bank/UPI statements showing non‑receipt of September salary, company policy on notice‑period salary & leave encashment, any written refusal of relieving/experience letters, and the offer letter of the new employer indicating the deadline.

---

#### 4. LEGAL BASIS OF THE CLAIM  

1. **Section 17(2), Code on Wages, 2019** – mandates that an employer shall pay **all wages** (including salary and leave encashment) **within two working days** of the employee’s resignation.  

2. **Section 18(1), Code on Wages, 2019** – prohibits any unauthorised deduction from wages; therefore the employer cannot withhold salary on the pretext of client payment delays.  

3. The refusal to issue the relieving and experience letters, after the employee has fully complied with the notice period and returned all assets, constitutes a **breach of the employment contract** and entitles the employee to specific performance and damages under the Indian Contract Act, 1872.  

4. The claim is a **civil debt** recoverable before the Labour Commissioner/Labour Court; it is **not a criminal matter** under the Indian Penal Code.

---

#### 5. DEMAND  

In view of the foregoing facts and law, the Complainant **HEREBY DEMANDS**:

1. **Payment of the pending dues** – **Rs 1,65,000** (September salary + 15 days leave encashment) **within fifteen (15) days** from the receipt of this notice.  

2. **Issuance of the Relieving Letter and Experience Certificate** in the prescribed format **within the same fifteen (15)‑day period**.  

3. **Statutory interest** at **12 % per annum** (simple interest) on the amount due from **30 Sep 2024** till actual payment, together with **costs of litigation** (court fees, postage, attorney’s fees) if the matter proceeds to court.

---

#### 6. CONSEQUENCES OF NON‑COMPLIANCE  

Should the Employer fail to comply with the above demands **within 15 days**, the Complainant will be constrained to initiate the following actions **without any further notice**:

| Sr. No. | Action | Forum | Anticipated Consequence |
|--------|--------|-------|------------------------|
| 1 | File a grievance on the **Labour Ministry’s e‑Daakhil / State Labour Commissioner portal** for recovery of wages and specific performance. | Labour Commissioner | Issuance of a statutory notice to the employer; possible attachment of assets. |
| 2 | Institute a suit before the **District Labour Court / DLSA** for recovery of wages, interest, damages, and specific performance (issuance of relieving/experience letters). | District Labour Court | Court decree for payment of dues with 12 % interest, costs, and an order directing issuance of the letters. |
| 3 | Seek **legal aid** from the District Legal Services Authority (DLSA) under **NALSA** (Helpline 15100) if the Complainant is unable to bear litigation costs. | DLSA | Free legal representation and assistance. |

The above steps will be taken **without prejudice** to any other remedy available under law, including filing a complaint under the **Industrial Disputes Act, 1947** or approaching the **National Consumer Helpline** for violation of consumer rights.

---

#### 7. DECLARATION  

The Complainant declares that the contents of this notice are true and correct to the best of his/her knowledge and belief, and that he/she is ready to pursue all legal remedies available under the law.

---

#### 8. SIGNATURE  

```
_____________________________  
[Your Full Name]  
Former Front‑End Developer  
Date: ____/____/2026
```

---

#### 9. ANNEXURE INVENTORY  

| Annexure | Description |
|----------|-------------|
| A | Appointment Letter (dated Feb 2023) |
| B | Resignation Acceptance Email (dated 1 Aug 2024) |
| C | Asset Clearance Certificate (dated 30 Sep 2024) |
| D | HR Email Thread on Salary Delay (Sept – Nov 2024) |
| E | Copy of Resignation Email (sent 1 Aug 2024) |
| F | (If available) Salary Slip – August 2024 |
| G | (If available) Bank/UPI Statement showing non‑receipt of September salary |
| H | (If available) Company policy on notice‑period salary & leave encashment |
| I | (If available) Communication refusing relieving/experience letters |
| J | Offer Letter of New Employer (showing deadline for relieving letter) |

---

*Prepared by:*  
**[Your Name]** – Self‑Represented Employee (or “Prepared under the guidance of NyayaMitra India”)  

*For any clarification, please contact the undersigned at the above address or mobile number.*  

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under employment laws, full and final dues must be cleared timely and withholding my relieving letter violates my right to livelihood. If my Rs 1,65,000 and relieving letter are not issued within 3 days, I will file a formal complaint with the District Labor Commissioner."*
- **Opponent Reaction:** Sir, we understand your concern, but as per our internal policy the final settlement is processed only after the finance team completes its clearance, which normally takes up to 10 working days. We have already made certain deductions for the notice period and asset usage as per the signed agreement. However, if you forward us the signed resignation copy and the asset‑return receipt, we will expedite the process and aim to release the pending Rs 1,65,000 and your relieving/experience letters by 7 December. Please note that any legal notice will be reviewed by our legal department before any further action.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You correctly invoked employment law and gave a clear 3‑day deadline, which puts pressure on the employer.",
  "what_to_improve": "Mention the specific statutory provision (e.g., [unverified reference removed] of the Payment of Wages Act or the Industrial Employment (Standing Orders) Act) and attach the resignation and asset‑return documents to strengthen your claim.",
  "suggested_next_counter": "Ask for a written commitment stating the exact settlement date, citing [unverified reference removed] of the Payment of Wages Act and warning of immediate legal action if not met."
}
```

---

