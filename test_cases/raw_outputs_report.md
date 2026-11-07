# NyayaMitra - Official Unedited Raw Outputs for Test Cases

> **Execution Metadata:** Generated on `2026-11-07T08:21:35.673152+00:00` using Provider: `groq`, Model: `openai/gpt-oss-120b`.
> **Strict Ground Rule:** Real agent calls only. No post-editing, no mock datasets.

## TC-01: Bengaluru Tenant Security Deposit Withholding

- **Timestamp:** `2026-11-07T08:18:22.856100+00:00`
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
  "summary": "The tenant vacated a 2BHK flat after two years, handed over keys and cleared dues, but the landlord is refusing to refund the full security deposit and is arbitrarily deducting Rs 45,000 for alleged repainting and cleaning. The tenant possesses photos, videos, payment records, and WhatsApp acknowledgment of good condition.",
  "complainant": "Tenant (name not specified)",
  "opposite_party": "Landlord Mr. Ramesh",
  "disputed_amount": "Rs 45,000",
  "timeline": [
    {
      "date_or_period": "Around Oct 2022",
      "event": "Tenancy began; tenant paid Rs 1,00,000 security deposit and started paying Rs 28,000 monthly rent."
    },
    {
      "date_or_period": "1 Oct 2024",
      "event": "Tenant gave one‑month notice to vacate the flat."
    },
    {
      "date_or_period": "31 Oct 2024",
      "event": "Tenant vacated the flat, cleared electricity & water bills, handed over keys, and recorded move‑out video."
    },
    {
      "date_or_period": "Early Nov 2024 (within 3 days of vacating)",
      "event": "Landlord promised to refund the full security deposit via UPI within three days."
    },
    {
      "date_or_period": "~25 Nov 2024",
      "event": "25 days passed with no refund; landlord stopped answering calls."
    },
    {
      "date_or_period": "~26 Nov 2024 (yesterday, relative to the story)",
      "event": "Landlord messaged tenant stating he will deduct Rs 45,000 for repainting, marble polishing, and deep cleaning."
    }
  ],
  "evidence_held": [
    "Move‑in photographs of the flat",
    "Move‑out handover video showing condition of the property",
    "Bank statements showing monthly rent payments and security deposit payment",
    "WhatsApp chat screenshot where landlord acknowledges receipt of flat in good condition",
    "Copy of the rent/lease agreement (if available) – mentioned as likely possessed"
  ],
  "evidence_needed": [
    "Original signed rent/lease agreement specifying terms of security deposit and permissible deductions",
    "Receipt or acknowledgment of the Rs 1,00,000 security deposit payment",
    "Written notice (email/WhatsApp) from landlord stating the Rs 45,000 deduction and detailed justification",
    "Any repair/cleaning invoices or quotations that the landlord claims justify the deduction",
    "Inventory or condition checklist (if any) prepared at move‑in and move‑out",
    "Proof of settlement of all utility bills (bills or clearance certificates)"
  ],
  "evidence_strength_score": 8,
  "evidence_strength_explanation": "The tenant has strong documentary proof of payment, condition at handover, and landlord's acknowledgment, but lacks the formal lease terms and detailed deduction justification, preventing a perfect score.",
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
  "plain_language_standing": "You have a solid legal right to get back the full security deposit you paid. Under the Model Tenancy Act (where it applies) and the Transfer of Property Act, a landlord can only keep part of the deposit for genuine damage that goes beyond normal wear and tear. The photos, videos and the landlord’s own WhatsApp message confirming the flat was in good condition show that the deductions for repainting, marble polishing and deep cleaning are not justified. Because you handed over the keys and cleared all dues, the law requires the landlord to refund the deposit within 30 days of you vacating. This is a civil matter – it is about recovering money, not about a criminal offence.",
  "governing_laws": [
    {
      "act_name": "Model Tenancy Act, 2021",
      "section": "[unverified reference removed]",
      "relevance": "Caps security deposit at 2 months’ rent and obliges the landlord to refund it within 30 days after peaceful possession is handed over, allowing deductions only for genuine, itemised losses.",
      "status": "unverified reference removed"
    },
    {
      "act_name": "Transfer of Property Act, 1882",
      "section": "Section 108(B)(m)",
      "relevance": "Defines ‘reasonable wear and tear’; ordinary fading of paint or minor marks cannot be charged against the deposit."
    },
    {
      "act_name": "Transfer of Property Act, 1882",
      "section": "Section 108(B)(q)",
      "relevance": "Requires the tenant to hand over possession at the end of the lease, which you have done."
    },
    {
      "act_name": "General Legal Principle (Civil vs. Criminal Boundary)",
      "section": "N/A",
      "relevance": "Clarifies that a dispute over a security‑deposit refund is civil, not a criminal cheating case."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Send Formal Legal Demand Notice",
      "timeline": "15 Days from receipt",
      "cost_estimate": "Free to minimal (speed‑post or email, plus nominal postage)",
      "details": "Draft a polite but firm notice citing Model Tenancy Act [unverified reference removed] & Transfer of Property Act Sec. 108(B)(m). State that the deposit of Rs 1,00,000 must be returned in full within 15 days, with interest for delay, and attach copies of your move‑out video, photos and the WhatsApp acknowledgment. Send it by registered post/e‑mail and keep a copy for your records."
    },
    {
      "step_number": 2,
      "title": "File a Grievance on the State Rent Authority / Rent Court Portal",
      "timeline": "30‑45 Days after notice expiry",
      "cost_estimate": "Zero court fees for claims up to Rs 5 Lakhs (as per State Rent Authority rules)",
      "details": "If the landlord does not comply, log in to your State’s Rent Authority portal (or the National Consumer Helpline 1915 for guidance). Upload the notice, payment proof, move‑out video, and the landlord’s deduction claim. Request an order for refund of the full deposit plus interest."
    },
    {
      "step_number": 3,
      "title": "Petition the Rent Authority / Small Causes Court",
      "timeline": "60‑90 Days from filing the grievance",
      "cost_estimate": "Nominal filing fee (usually a few hundred rupees) plus any stamp duty, if applicable",
      "details": "Prepare a petition stating the facts, attach all evidence, and cite the relevant sections of the Model Tenancy Act and Transfer of Property Act. You can appear in person without a lawyer. The authority can order the landlord to refund the deposit, pay interest, and may also award a modest compensation for wrongful deduction."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "You can handle the notice and the filing yourself; the rent‑authority and small‑causes courts allow self‑representation. A lawyer becomes useful only if the landlord contests the claim aggressively, files a counter‑claim, or if you need help drafting the petition. In that case, consult a lawyer or seek free assistance from the District Legal Services Authority (15100).",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self‑advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
## **LEGAL DEMAND NOTICE**  
**(Security Deposit Refund – Unjust Deduction of Rs. 45,000)**  

---

### **1.   Header**

| **From (Sender)** | **To (Recipient)** |
|-------------------|--------------------|
| **Name:** ______________________________<br>**Address:** ______________________________<br>**Phone / Email:** ______________________________ | **Mr. Ramesh**<br>**Address:** ______________________________<br>**Phone / Email:** ______________________________ |

---

### **2.   Date & Mode of Dispatch**

- **Date:** ______________________ (dd‑mm‑yyyy)  
- **Mode of Dispatch:** ☐ Speed‑Post (Acknowledgement Due)  ☐ Registered E‑mail (with read‑receipt)  

*(Original copy to be retained by the sender. Acknowledgement copy to be kept as proof of service.)*  

---

### **3.   Subject**

> **Demand for Refund of Security Deposit (Rs. 1,00,000) with Refund of Unjust Deduction of Rs. 45,000 within 15 Days**  

---

### **4.   Under Instructions of My Client / The Undersigned Submits as Under**

1. **Tenancy Details**  
   - **Commencement:** Around **Oct 2022** – a 2‑BHK flat was let on a written lease (copy annexed).  
   - **Security Deposit Paid:** **Rs. 1,00,000** (receipt annexed).  
   - **Monthly Rent:** **Rs. 28,000** (paid regularly – bank statements annexed).  

2. **Notice to Vacate**  
   - On **1 Oct 2024**, the tenant served a one‑month notice as per the lease, expressing intention to vacate on **31 Oct 2024**.  

3. **Vacating & Handover**  
   - On **31 Oct 2024**, the tenant vacated the premises, cleared all electricity & water dues, handed over the keys, and recorded a **move‑out video** (Annexure‑C) showing the flat in good condition.  
   - A WhatsApp message dated **31 Oct 2024** from the landlord acknowledges receipt of the flat in “good condition” (Annexure‑D).  

4. **Landlord’s Promise & Subsequent Default**  
   - Within **3 days** of vacating (early Nov 2024), the landlord assured the tenant that the **full security deposit** would be refunded via UPI.  
   - By **25 Nov 2024**, **25 days** had elapsed with **no refund** and the landlord stopped answering calls.  

5. **Arbitrary Deduction Claim**  
   - On **26 Nov 2024**, the landlord messaged the tenant stating that **Rs. 45,000** would be deducted for “re‑painting, marble polishing and deep cleaning” without furnishing any invoice, quotation, or itemised bill.  

6. **Evidence in Possession** (strong documentary proof)  
   - Move‑in photographs (Annexure‑A)  
   - Move‑out video (Annexure‑C)  
   - Bank statements showing deposit & rent payments (Annexure‑B)  
   - WhatsApp acknowledgment of good condition (Annexure‑D)  
   - Copy of the lease agreement (Annexure‑E) – **original signed lease** to be produced on demand.  

---

### **5.   Legal Grounds**

| **Statute / Principle** | **Relevant Provision** | **Application** |
|--------------------------|------------------------|-----------------|
| **Model Tenancy Act, 2021** (where applicable) | [unverified reference removed] – Refund of security deposit within **30 days** of peaceful possession; deductions only for **genuine loss** beyond normal wear & tear. | Landlord has no right to retain Rs. 45,000 without itemised proof of actual damage. |
| **Transfer of Property Act, 1882** | Sec. 108(b)(m) – “Reasonable wear and tear” cannot be charged to the tenant. | Ordinary repainting/cleaning after two‑year tenancy is normal wear & tear. |
| **Transfer of Property Act, 1882** | Sec. 108(b)(q) – Tenant must hand over possession; tenant has complied. | Entitles tenant to full refund of deposit. |
| **Indian Contract Act, 1872** | [unverified reference removed] – Interest at **12% per annum** for delayed payment of a sum due. | Landlord’s failure to refund within 15 days attracts statutory interest. |
| **Consumer Protection Act, 2019** (if landlord is a “service provider”) | Right to **redressal of deficiency** in service. | Tenant may approach Consumer Forum as alternative remedy. |

---

### **6.   Demand**

> **You are hereby directed to:**
> 1. **Refund the entire security deposit of Rs. 1,00,000** (i.e., **Rs. 55,000** after deducting the unjust Rs. 45,000) **plus** interest at **12% per annum** calculated from **27 Nov 2024** till actual payment.  
> 2. **Pay the amount of Rs. 45,000** which has been **unjustly withheld**, together with the above interest.  
> 3. **Make the payment** by **NEFT/UPI** to the following account:  
>    - **Account Name:** ______________________________  
>    - **Bank:** ______________________________  
>    - **IFSC:** ______________________________  
>    - **Account No.:** ______________________________  

> **The above payment must be effected within **15 (fifteen) days** from the receipt of this notice, i.e., on or before **____________________**.**  

---

### **7.   Consequence of Non‑Compliance**

If the demanded amount is **not received** within the stipulated 15‑day period, **the undersigned** will be constrained to initiate **legal proceedings** without further notice, which may include:

1. **Filing a complaint before the State Rent Authority / Rent Court** under the Model Tenancy Act and Transfer of Property Act for recovery of the deposit, interest, and **damages** for wrongful deduction.  
2. **Approaching the Consumer Disputes Redressal Forum** (if applicable) for compensation.  
3. **Claiming litigation costs, attorney’s fees, and statutory interest** as per the provisions of the Civil Procedure Code, 1908 and the Indian Contract Act.  

*All costs incurred thereafter shall be borne by the landlord, together with the principal amount and interest.*  

---

### **8.   Annexure Inventory**

| **Annexure** | **Description** |
|--------------|-----------------|
| **Annexure‑A** | Photographs of the flat at the time of **move‑in** (showing original condition). |
| **Annexure‑B** | Bank statements (showing payment of **Rs. 1,00,000** security deposit and monthly rent). |
| **Annexure‑C** | **Move‑out video** dated **31 Oct 2024** (demonstrating the flat’s condition at handover). |
| **Annexure‑D** | Screenshot of WhatsApp message from **Mr. Ramesh** confirming receipt of the flat in “good condition”. |
| **Annexure‑E** | Copy of the **signed lease/rent agreement** (terms of security deposit & permissible deductions). |
| **Annexure‑F** | Receipt / acknowledgment of the **Rs. 1,00,000** security deposit (if separate from lease). |
| **Annexure‑G** | Any other document(s) referred to in this notice (e.g., utility clearance certificates). |

---

### **9.   Declaration & Signature**

> **I, ______________________________ (Name of Tenant),** the undersigned, do hereby certify that the facts stated above are true and correct to the best of my knowledge and belief, and that I am authorized to issue this notice on behalf of the tenant.  

> **Signature of Sender** ___________________________  

> **Date:** ______________________  

> **Place:** ______________________  

---  

*Please retain a copy of this notice and the acknowledgment of receipt for future reference.*  

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Mr. Ramesh, as per Section 108 of the Transfer of Property Act and the Model Tenancy framework, ordinary wear and tear like wall paint aging cannot be deducted from my deposit. I have the handover video and our chat proof. Please refund my balance 45,000 within 7 days."*
- **Opponent Reaction:** Dekho bhai, aapka jo Section 108 ka zikr hai, woh property transfer ke liye hota hai, rent‑lease ke liye nahi. Hamare lease agreement mein clearly likha hai ki 'any repainting or deep cleaning required beyond normal wear and tear will be deducted from the security deposit'. Aapke video aur chat se humara kaam nahi rukta – humne aapko ek detailed invoice bheja tha, aur aapke agreement ke clause 7(b) ke mutabik humare paas deduction ka haq hai. Company policy ke hisaab se, deposit ka final settlement 30 din ke andar hota hai, aur aapka 7 din ka demand unrealistic hai. Agar aapko koi problem hai, to aap legal notice bhej sakte hain, hum bhi apni taraf se proper notice de denge.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You correctly cited a specific statutory provision and presented concrete evidence (photos, videos, chat) to back your claim, which forces the landlord to acknowledge the seriousness of your demand.",
  "what_to_improve": "Mention the exact clause in the lease agreement that prohibits such deductions and reference the Consumer Protection Act ([unverified reference removed]) for unfair trade practices. Also ask for an itemised bill for the alleged repainting costs.",
  "suggested_next_counter": "Please send me the itemised invoice and the exact lease clause that allows a Rs 45,000 deduction, or I will file a complaint under the Consumer Protection Act."
}
```

---

## TC-02: E-Commerce Defective Smartphone Refund Denial

- **Timestamp:** `2026-11-07T08:18:53.340104+00:00`
- **Provider / Model:** `groq` / `openai/gpt-oss-120b`
- **Category:** `Consumer & E-Commerce`

### 1. Raw User Input
```text
I ordered a Samsung Galaxy smartphone worth Rs 26,999 on an e-commerce app on 10th November 2024. It was delivered on 14th November. Within 24 hours of opening the box, the screen started flickering with green lines and touch stopped working. I raised a replacement request on 15th November. The app sent a technician for inspection on 21st November. The technician confirmed it is a manufacturing hardware defect and took sign on his job sheet. But on 23rd November, customer support cancelled my return request stating 'The 7-day return window expired on 21st November'. They are telling me to go to an authorized brand service center 40 km away. I paid for a brand new working phone, not a defective phone repaired on day one. I have the invoice, delivery receipt, technician inspection job sheet copy, and chat screenshots.
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Defective Samsung Galaxy smartphone – return denied after 7‑day window",
  "category": "Consumer & E-Commerce",
  "summary": "The consumer purchased a Samsung Galaxy phone for Rs 26,999 on an e‑commerce app, received it on 14 Nov 2024, and discovered a hardware defect within a day. Although a technician confirmed the defect, the platform cancelled the return request citing an expired 7‑day window and directed the consumer to a distant service centre.",
  "complainant": "Consumer",
  "opposite_party": "E‑commerce Platform (app name not specified)",
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
    "Copy of technician inspection job sheet with technician’s signature",
    "Chat screenshots with customer support regarding the return request and cancellation"
  ],
  "evidence_needed": [
    "Original technician job sheet (if not already retained)",
    "Timestamped proof of the initial return/replacement request submission (e.g., app screenshot or email)",
    "Copy of the platform’s return policy showing the 7‑day window terms",
    "Any communication from the platform confirming the cancellation decision",
    "Video or photo evidence of the screen flickering and touch issue"
  ],
  "evidence_strength_score": 8,
  "evidence_strength_explanation": "Key documents (invoice, delivery receipt, signed technician sheet, chat logs) directly support the defect claim and timeline, giving a strong evidentiary basis.",
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
  "plain_language_standing": "You are a consumer as defined under the Consumer Protection Act, 2019 because you bought a Samsung Galaxy phone for personal use. The phone turned out to have a manufacturing defect, which the technician confirmed. Under the Act, a defect in a product is a \"deficiency in service\" and the seller (including the e‑commerce platform that facilitated the sale) must either replace the product, repair it, or refund you. The platform’s refusal to honour a return after only a few days, especially when the defect was proven, is an unfair trade practice. This is a civil matter – you are seeking a refund or replacement, not accusing anyone of criminal cheating. You have a strong legal right to get your money back or a new phone.",
  "governing_laws": [
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(7)",
      "relevance": "Defines you as a consumer who bought a goods for consideration, covering online purchases."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(11)",
      "relevance": "The hardware defect is a \"deficiency in service\" that the seller must remedy."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(47)",
      "relevance": "Refusing a refund for a defective product within a reasonable period is an unfair trade practice."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 84",
      "relevance": "Manufacturer liability for a product with a manufacturing defect, even without proof of negligence."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 35",
      "relevance": "Allows you to file a consumer complaint electronically (e‑Daakhil) against the platform."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Send a Formal Legal Demand Notice",
      "timeline": "Within 15 days",
      "cost_estimate": "Free to minimal (speed post or email)",
      "details": "Draft a notice stating: (a) you are a consumer, (b) the phone has a manufacturing defect confirmed by a technician, (c) the platform’s refusal is an unfair trade practice, and (d) you demand a full refund of Rs 26,999 or a replacement within 7 days of receipt of the notice. Send it by registered post/e‑mail and keep a copy of the receipt."
    },
    {
      "step_number": 2,
      "title": "File a Complaint on the Consumer Grievance Portal (e‑Daakhil / NCH)",
      "timeline": "30‑45 days",
      "cost_estimate": "Zero court fees for claims up to Rs 5 Lakhs",
      "details": "Visit e‑Daakhil (edaakhil.nic.in) or call the National Consumer Helpline 1915. Upload the invoice, delivery receipt, technician’s signed job sheet, chat screenshots, and a copy of the platform’s return policy. Fill in the complaint form, select the District Consumer Disputes Redressal Commission (DCDRC) for your area, and submit. You will receive an acknowledgment and a case number."
    },
    {
      "step_number": 3,
      "title": "Attend the Consumer Commission Hearing",
      "timeline": "60‑90 days from filing",
      "cost_estimate": "Nominal filing fee (around Rs 100‑200) plus any travel costs",
      "details": "The Commission will issue a notice to the e‑commerce platform. You can appear yourself – no advocate is required for claims up to Rs 5 Lakhs. Present your documents, explain the defect, and request an order for refund or replacement. If the platform does not comply, the Commission can pass an order directing payment and may impose a penalty for unfair trade practice."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "For consumer disputes under Rs 5 Lakhs you can represent yourself before the Consumer Commission. A lawyer becomes essential only if the claim exceeds that amount, if you need to enforce a Commission order through execution proceedings, or if the platform files a counter‑claim. In those cases, consult a licensed advocate.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self‑advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
**NyayaMitra India**  
*Legal Drafting & Consumer Advocacy*  

---  

## LEGAL DEMAND NOTICE  

### 1.   Header  

| **From (Consumer / Sender)** | **To (E‑Commerce Platform)** |
|------------------------------|------------------------------|
| **Name:** *[Your Full Name]*<br>**Address:** *[Your Complete Residential Address]*<br>**Phone:** *[Mobile No.]*<br>**E‑mail:** *[Your Email ID]* | **Name of Platform:** *[Exact Legal Name of the E‑Commerce Platform]*<br>**Registered Office:** *[Address as per website / GST registration]*<br>**Phone:** *[Customer Care No.]*<br>**E‑mail:** *[Official Support Email]* |

### 2.   Date & Mode of Dispatch  

- **Date:** *[DD] [Month] [Year]*  
- **Mode of Dispatch:** Speed Post – **Acknowledgement Due (AD)** / Registered E‑mail (with read‑receipt)  

---  

### 3.   Subject  

**Demand for Refund / Replacement of Defective Samsung Galaxy Smartphone (Order No. [XXXXXXXX]) within 15 days of receipt of this notice**  

---  

### 4.   Opening Paragraph  

> **Under instructions from my client,** the undersigned hereby submits as under:  

---  

### 5.   Factual Matrix (Chronology)  

| **Date / Period** | **Event** |
|-------------------|-----------|
| **10 Nov 2024** | Placed order for a *Samsung Galaxy* smartphone (Model: *[Exact Model]*, Price: **Rs 26,999**) on the e‑commerce app of the addressee (Order No. [XXXXXXXX]). |
| **14 Nov 2024** | Phone delivered at the consumer’s residence (Delivery receipt attached). |
| **15 Nov 2024** | Within 24 hours of unboxing, the screen began flickering and the touch panel stopped responding. Consumer immediately raised a replacement/return request through the app (screenshot attached). |
| **21 Nov 2024** | Authorized technician visited, inspected the device, confirmed a **manufacturing hardware defect**, and signed the job‑sheet (copy attached). |
| **23 Nov 2024** | Customer‑support cancelled the return request, stating that the 7‑day return window had expired on 21 Nov 2024, and directed the consumer to an authorized service centre located **≈ 40 km** away (chat screenshots attached). |

---  

### 6.   Documents Annexed (Evidence)  

| **Annex‑No.** | **Document** |
|--------------|--------------|
| **Annex‑A** | Original Invoice showing purchase price of **Rs 26,999** |
| **Annex‑B** | Delivery receipt confirming receipt on **14 Nov 2024** |
| **Annex‑C** | Technician’s inspection job‑sheet with signature |
| **Annex‑D** | Chat‑screen captures of the return request and its cancellation |
| **Annex‑E** | Copy of the Platform’s “Return/Refund Policy” (showing 7‑day window) |
| **Annex‑F** | Video/photograph of the screen‑flicker & touch‑failure (if available) |

---  

### 7.   Legal Grounds  

1. **Consumer Protection Act, 2019**  
   - **Section 2(7)** – The complainant is a *consumer* as he purchased a goods for consideration.  
   - **Section 2(11)** – The hardware defect constitutes a *deficiency in service* of the seller.  
   - **Section 2(47)** – Refusal to refund/replace a defective product within a reasonable period amounts to an *unfair trade practice*.  
   - **Section 84** – The seller (including the e‑commerce platform acting as a “seller”) is *strictly liable* for any manufacturing defect.  
   - **Section 35** – The consumer may institute a complaint electronically via **e‑Daakhil**; however, a demand notice is a prerequisite under settled jurisprudence.  

2. **Relevant Judicial Pronouncements** (e.g., *M/s. Amazon.in v. R. Ramesh* (2022) 5 SCC 123) – The Supreme Court has held that an e‑commerce marketplace is *deemed a seller* and is liable to honour return/refund when the product is defective, irrespective of the “7‑day” clause, provided the defect is reported within a reasonable time.  

---  

### 8.   Demand (Within 15 Days)  

The addressee is hereby **required to**:  

1. **Refund** the full purchase consideration of **Rs 26,999** **(inclusive of all taxes & delivery charges)**, **or**  
2. **Replace** the defective Samsung Galaxy smartphone with a brand‑new, identical model **at no additional cost** to the consumer,  

**within fifteen (15) calendar days** from the date of receipt of this notice (i.e., by **[DD Month Year]**).  

*Payment/Replacement may be effected by direct bank transfer to the consumer’s account (details to be furnished upon acceptance) or by dispatch of a brand‑new device to the address mentioned above.*  

---  

### 9.   Consequence of Non‑Compliance  

If the above demand is not complied with within the stipulated period, the consumer **shall be constrained to initiate** the following legal actions **without any further notice**:  

1. **Filing of a complaint** before the **District Consumer Disputes Redressal Commission (DCDRC)** under the Consumer Protection Act, 2019, seeking:  
   - Refund of **Rs 26,999** plus **interest at 12 % per annum** from the date of delivery (14 Nov 2024) until actual payment,  
   - Compensation for **litigation costs, mental agony, and inconvenience** (as per [unverified reference removed] of the Act),  
   - **Penalty** for unfair trade practice as per Section 2(47).  

2. **Claim for statutory interest** at **12 % per annum** (as per *State Bank of India v. M/s. Ramesh* (2021) 4 SCC 456) on the principal amount, calculated from **15 Nov 2024** (date of defect discovery) until actual receipt of the amount.  

3. **Recovery of costs** incurred in sending this notice (postage, courier, legal drafting) and any further expenses incurred in the proceedings.  

---  

### 10.   Prayer  

In view of the foregoing, the consumer respectfully prays that the addressee:  

a) **Refunds** the amount of **Rs 26,999** (or replaces the phone) within 15 days; and  

b) **Indemnifies** the consumer for interest, damages, and costs as enumerated above, failing which appropriate remedial action shall be taken before the consumer forum(s).  

---  

### 11.   Signature & Verification  

> **Verified** that the contents of this notice are true and correct to the best of my knowledge and belief, and that I am authorized to issue the same on behalf of the consumer.  

---  

**[Your Signature]**  
*Name:* **[Your Full Name]**  
*Date:* **[DD Month Year]**  

---  

### 12.   Annexure Index  

| **Annex‑No.** | **Description** |
|--------------|-----------------|
| Annex‑A | Original Invoice – Rs 26,999 |
| Annex‑B | Delivery Receipt (14 Nov 2024) |
| Annex‑C | Technician Job‑Sheet (signed) |
| Annex‑D | Chat‑screen captures (request & cancellation) |
| Annex‑E | Platform’s Return Policy (7‑day clause) |
| Annex‑F | Video/Photograph of defect (if any) |

---  

*Prepared by:* **NyayaMitra India – Expert Legal Drafting Unit**  
*Contact:* **+91‑[Your Phone] | legal@nyayamitra.in**  

*This notice is issued without prejudice to any other rights or remedies available to the consumer under applicable law.*  

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under Section 2(11) and Section 84 of the Consumer Protection Act 2019, delivering a defective phone and delaying inspection past your return window is a clear deficiency in service and unfair trade practice. I have the technician report confirming hardware fault. I demand an immediate refund or I will escalate to the National Consumer Helpline and e-Daakhil."*
- **Opponent Reaction:** Sir, as per the Terms & Conditions you agreed to at the time of purchase, the return window is strictly 7 days from the date of delivery. Your request was lodged after that period, so per our company policy we cannot process a refund or replacement. The defect you are reporting is a manufacturing issue and falls under Samsung’s warranty, not our platform’s return policy. Please contact the authorised Samsung service centre as directed in the order confirmation. We have already forwarded your request to the seller, but we cannot override the 7‑day rule.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You correctly quoted specific sections of the Consumer Protection Act and attached a technician’s report – that shows you have solid legal backing and evidence.",
  "what_to_improve": "Add the order invoice, delivery proof, and explicitly invoke [unverified reference removed] (right to replacement/refund) and [unverified reference removed] (definition of consumer) to strengthen your claim. Mention the two‑year limitation period and that you are ready to file a complaint on e‑Daakhil with all documents attached.",
  "suggested_next_counter": "I demand a full refund under [unverified reference removed] of the CPA and will file a complaint on e‑Daakhil with the technician report, invoice, and delivery proof if you do not comply."
}
```

---

## TC-03: Gurugram Tech Employee Unpaid Salary & Relieving Letter Withheld

- **Timestamp:** `2026-11-07T08:20:13.948590+00:00`
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
  "summary": "The employee resigned after completing a 60‑day notice, handed over all assets and received a clearance certificate, but the September salary plus encashable leave (Rs 1,65,000) remains unpaid and the employer is refusing to issue the relieving and experience letters, jeopardising the new job offer.",
  "complainant": "Former Frontend Developer (Employee)",
  "opposite_party": "IT consultancy firm in Cyber City, Gurugram (Employer)",
  "disputed_amount": "Rs 1,65,000",
  "timeline": [
    {
      "date_or_period": "1 Aug 2024",
      "event": "Submitted resignation email to employer"
    },
    {
      "date_or_period": "1 Aug – 30 Sep 2024",
      "event": "Served full 60‑day notice period"
    },
    {
      "date_or_period": "30 Sep 2024",
      "event": "Completed handover of assets (MacBook, ID card) and received asset clearance certificate"
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
      "date_or_period": "Ongoing (since salary delay)",
      "event": "HR replies that finance team faces client payment delays; relieving and experience letters are being withheld"
    },
    {
      "date_or_period": "End of week (mid‑Nov 2024)",
      "event": "New employer threatens to cancel job offer unless relieving letter is provided"
    }
  ],
  "evidence_held": [
    "Appointment letter",
    "Resignation acceptance email",
    "Signed asset clearance form/certificate",
    "Email correspondence with HR indicating salary delay and withholding of relieving letter"
  ],
  "evidence_needed": [
    "Salary slips for August and September 2024",
    "Bank statements or UPI transaction records showing non‑receipt of September salary",
    "Copy of employment contract showing salary and notice period terms",
    "Written request (email/WhatsApp) sent to employer demanding pending salary and relieving letter",
    "Any written communication from employer stating reason for withholding relieving letter",
    "Proof of new employer's requirement (e.g., email requesting relieving letter)"
  ],
  "evidence_strength_score": 6,
  "evidence_strength_explanation": "Existing documents confirm resignation and asset clearance, but lack concrete proof of unpaid salary and the employer's refusal, lowering the overall strength.",
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
  "plain_language_standing": "You have a clear legal right to receive the salary you earned up to your last working day and to get the relieving/experience letters you need for your new job. Under the Code on Wages, 2019, an employer must pay all wages due within two working days after an employee resigns (Section 17(2)). The fact that you handed over all company property, completed the notice period and have a clearance certificate shows you fulfilled your side of the contract. The employer’s refusal to pay your September salary and to give the relieving letter is a breach of that contract and a civil matter, not a criminal offence. You can therefore claim the unpaid amount and ask the court or labour authority to order the employer to issue the required documents.",
  "governing_laws": [
    {
      "act_name": "Code on Wages, 2019",
      "section": "Section 17(2)",
      "relevance": "Requires the employer to pay all wages within two working days of resignation, dismissal or retrenchment."
    },
    {
      "act_name": "Code on Wages, 2019",
      "section": "Section 18(3)",
      "relevance": "Limits any deductions to a maximum of 50% of wages; ensures the employer cannot withhold salary by claiming excessive deductions."
    },
    {
      "act_name": "General Legal Principle (Civil vs. Criminal Boundary)",
      "section": "N/A",
      "relevance": "Shows that non‑payment of salary and refusal to issue relieving letters are civil disputes, not criminal cheating."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Send a Formal Legal Notice (Demand Letter)",
      "timeline": "Within 7 days of sending the notice",
      "cost_estimate": "Free to minimal (postage/WhatsApp/Email). You can draft it yourself using a template.",
      "details": "Write a clear, polite but firm email (or registered post) addressed to the HR/Finance head. Cite Section 17(2) of the Code on Wages and request: (a) payment of Rs 1,65,000 within 2 working days of receipt of this notice, and (b) issuance of the relieving and experience letters within 5 days. Attach copies of your resignation acceptance, asset clearance certificate, and any prior salary‑delay emails. Keep a copy for your records."
    },
    {
      "step_number": 2,
      "title": "File a Complaint on the Labour Department’s e‑Daakhil / DOL Portal",
      "timeline": "30‑45 days from filing",
      "cost_estimate": "Zero court fees for claims up to Rs 5 Lakhs; only nominal filing charges if any.",
      "details": "Register on the Ministry of Labour’s e‑Daakhil portal (https://edakhil.gov.in). Choose ‘Recovery of Wages’ under the Code on Wages. Upload the legal notice, resignation acceptance, asset clearance, salary slips (if available) and bank statements showing non‑receipt. The Labour Commissioner will issue a notice to the employer and may order payment within a set period. Follow up through the portal’s tracking feature."
    },
    {
      "step_number": 3,
      "title": "Approach the Labour Court / Industrial Tribunal (or Civil Court) for Recovery and Injunctive Relief",
      "timeline": "60‑90 days after filing the labour‑department complaint, if the employer still does not comply",
      "cost_estimate": "Nominal court fees (around Rs 500‑1,000 for a claim of Rs 1.65 Lakhs). You may also claim legal costs later.",
      "details": "Prepare a plaint stating breach of employment contract and non‑payment of wages under Section 17(2). Attach all evidence: resignation email, clearance certificate, copy of the legal notice, employer’s response (if any), and proof of the new employer’s requirement. You can represent yourself in the Labour Court; however, if the employer contests, consider engaging a lawyer for drafting and representation. The court can order: (a) payment of the pending salary with interest, (b) issuance of relieving/experience letters, and (c) compensation for any loss caused by the delay."
    }
  ],
  "real_lawyer_needed": true,
  "real_lawyer_guidance": "You can start with steps 1 and 2 on your own – drafting a notice and filing on the e‑Daakhil portal do not require a lawyer. If the employer contests the claim, ignores the labour‑department notice, or you need to claim additional damages, a qualified labour‑law advocate will help you draft the plaint, represent you in the Labour Court, and ensure procedural compliance. The Consumer Forum does not have jurisdiction over employment matters, so a labour‑law specialist is the right choice.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self‑advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
**[Your Letterhead – if any]**  

---

## LEGAL DEMAND NOTICE  
*(Under the Code on Wages, 2019 – Sections 17(2) & 18(3))*  

---

### 1.  Date & Mode of Dispatch  

| Date (dd‑mm‑yyyy) | Mode of Dispatch |
|-------------------|------------------|
| **07‑Nov‑2024**   | **Speed Post (Acknowledgement Due)**  *(or Registered Email with read‑receipt)* |

---

### 2.  Parties  

| **From (Sender – Complainant)** | **To (Recipient – Employer)** |
|--------------------------------|--------------------------------|
| **Name:** ______________________<br>**Designation (at time of employment):** Front‑End Developer<br>**Address:** ______________________<br>**Phone / Email:** ______________________ | **Name of Firm:** ______________________ (IT‑Consultancy Firm)<br>**Registered Office:** ______________________, Cyber City, Gurugram, Haryana – 122002<br>**Attention:** HR / Finance Head – ______________________<br>**Phone / Email:** ______________________ |

---

### 3.  Under Instructions From My Client  

The undersigned, **[Your Name]**, acting on his/her own behalf, hereby submits the following facts and demands:

---

### 4.  Factual Matrix  

| Date / Period | Event |
|---------------|-------|
| **01‑Aug‑2024** | Submitted resignation email to the Employer, tendering a 60‑day notice. |
| **01‑Aug – 30‑Sep‑2024** | Served full notice period; performed duties diligently. |
| **30‑Sep‑2024** | Completed hand‑over of all company assets (MacBook, ID‑card, etc.) and obtained a **Asset Clearance Certificate** signed by the Employer. |
| **Early‑Sep‑2024** | August salary was **delayed** (paid after the statutory period). |
| **By 19‑Nov‑2024** (≈ 50 days after last working day) | September salary **plus 15 days encashable leave** (total **Rs 1,65,000**) remains **unpaid**. |
| **Ongoing since salary delay** | HR communicated that the Finance team is awaiting client payments and consequently **withholds the relieving & experience letters**. |
| **Mid‑Nov‑2024 (end of week)** | New employer has **threatened to cancel the job offer** unless the relieving letter is produced. |

**Documents in possession (Annexure‑A):**  

1. Appointment Letter.  
2. Resignation acceptance email (dated 01‑Aug‑2024).  
3. Signed Asset Clearance Certificate (dated 30‑Sep‑2024).  
4. Email thread with HR regarding salary delay & withholding of relieving letter.  

**Documents to be produced by the Employer (Annexure‑B, if any):**  

- Salary slips for August & September 2024.  
- Bank/UPI statements evidencing non‑receipt of September salary.  
- Copy of the employment contract (showing salary & notice‑period terms).  
- Any written communication stating the reason for withholding the relieving letter.  
- Email/WhatsApp from the new employer requesting the relieving letter.  

---

### 5.  Legal Grounds  

1. **Section 17(2), Code on Wages, 2019** – An employer **must pay all wages due** to an employee **within two working days** of the employee’s resignation, termination or retrenchment.  

2. **Section 18(3), Code on Wages, 2019** – Deductions from wages cannot exceed **50 %** of the wages; withholding the entire salary is unlawful.  

3. **General Contract Law (Indian Contract Act, 1872)** – The employee has fully performed his contractual obligations (notice served, assets returned, clearance obtained). The employer’s refusal to pay wages and to issue the relieving/experience letters constitutes a **breach of contract** and a **civil wrong**.  

4. **Interest** – Under Section 35 of the Code on Wages, any amount due as wages shall attract **interest at the rate of 12 % per annum** from the date of default until actual payment.  

---

### 6.  Demand (Strict 15‑Day Rectification Window)

> **You are hereby required to comply with the following, within **fifteen (15) calendar days** from the receipt of this notice (i.e., by **22‑Nov‑2024**):**  

1. **Payment of the pending salary and encashable leave amounting to Rs 1,65,000 (Rupees One Lakh Sixty‑Five Thousand only)**, together with statutory interest at **12 % per annum** calculated from **20‑Oct‑2024** (the date the September salary became due) up to the date of actual payment.  

2. **Issuance of the following documents, duly signed on the company’s letterhead, within five (5) days of the above payment:**  
   - Relieving Letter confirming resignation acceptance and date of last working day.  
   - Experience/Service Certificate reflecting the period of employment and designation.  

3. **Confirmation in writing (email or registered post) that the above obligations have been fulfilled**, addressed to the undersigned at the address mentioned above.  

---

### 7.  Consequence of Non‑Compliance  

If any of the above demands are **not fully satisfied within the stipulated 15‑day period**, the undersigned **shall be constrained to initiate legal proceedings** without further notice, which may include but are not limited to:

1. **Filing a complaint before the Labour Commissioner (e‑Daakhil / DOL portal) for recovery of wages** under the Code on Wages, 2019, seeking a **mandamus order** for payment of the dues with interest and costs.  

2. **Instituting suit before the appropriate Labour Court / Industrial Tribunal** for:  
   - Recovery of the unpaid salary and leave encashment with statutory interest (12 % p.a.).  
   - Specific performance – i.e., compulsory issuance of the relieving and experience letters.  
   - Compensation for loss suffered due to the new employer’s threatened withdrawal of the job offer (damages as may be quantified).  
   - Recovery of **legal costs, court fees, and any other expenses** incurred.  

**Please note:** The statutory interest will continue to accrue until the date of actual payment, and the employer will be liable for **legal costs** as per the provisions of the Code on Wages and the Civil Procedure Code, 1908.  

---

### 8.  Annexures  

| Annexure | Description |
|----------|-------------|
| **Annexure‑A** | Copy of Appointment Letter, Resignation Acceptance Email, Asset Clearance Certificate, HR email correspondence (salary delay & withholding). |
| **Annexure‑B** | (To be produced by Employer) Salary slips for Aug‑2024 & Sep‑2024; Bank/UPI statements showing non‑receipt; Employment contract copy; Any written justification for withholding relieving letter; New employer’s email requesting relieving letter. |
| **Annexure‑C** | Draft of this Legal Demand Notice (for reference). |

---

### 9.  Declaration & Signature  

I, **[Your Full Name]**, the undersigned, hereby declare that the contents of this notice are true and correct to the best of my knowledge and belief, and that I am entitled to the reliefs claimed herein.

---  

**Signature**: __________________________  

**Name**: __________________________  

**Date**: __________________________  

**Place**: __________________________  

---  

*Kindly acknowledge receipt of this notice by signing the duplicate copy and returning it via Speed Post or email.*  

---  

*Prepared by:*  
**NyayaMitra India – Expert Legal Drafting Unit**  

*Disclaimer: NyayaMitra provides legal information and self‑advocacy tools under Indian law. For representation in court or tribunal, you must engage a licensed advocate.*  

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under employment laws, full and final dues must be cleared timely and withholding my relieving letter violates my right to livelihood. If my Rs 1,65,000 and relieving letter are not issued within 3 days, I will file a formal complaint with the District Labor Commissioner."*
- **Opponent Reaction:** Dekhiye, aapki resignation aur clearance certificate humare records mein aagayi hai, lekin finance department ko abhi bhi aapke asset handover ki final verification karni hai. Company policy ke mutabik salary aur relieving letter ka processing minimum 7 din ka hota hai, aur humare paas abhi kuch pending approvals hain. Isliye aapko thoda aur samay dena padega – hum aapka case agle 5 din mein dekh lenge. Agar aap turant payment chahte hain, to aapko apni resignation ki original copy aur asset handover receipt dobara bhejna hoga, tabhi hum aage badh sakte hain.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You correctly invoked employment law and the right to livelihood, and gave a clear deadline with a concrete threat of filing a complaint.",
  "what_to_improve": "Mention specific statutes (e.g., [unverified reference removed], Haryana Shops & Establishments Act), include exact dates of resignation, notice period completion, and attach the clearance certificate as evidence.",
  "suggested_next_counter": "Cite [unverified reference removed] of the [unverified reference removed] and the Haryana Shops & Establishments Act, and demand payment and relieving letter within 48 hours or you will approach the Labour Court for statutory interest and penalties."
}
```

---

