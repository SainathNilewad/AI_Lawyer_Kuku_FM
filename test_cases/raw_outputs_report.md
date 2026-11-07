# NyayaMitra - Official Unedited Raw Outputs for Test Cases

> **Execution Metadata:** Generated on `2026-11-07T19:37:31.167792+00:00` using Provider: `groq`, Model: `openai/gpt-oss-120b`.
> **Strict Ground Rule:** Real agent calls only. No post-editing, no mock datasets.

## TC-01: Bengaluru Tenant Security Deposit Withholding

- **Timestamp:** `2026-11-07T19:34:17.449671+00:00`
- **Provider / Model:** `groq` / `openai/gpt-oss-120b`
- **Category:** `Tenancy & Rental`

### 1. Raw User Input
```text
I was renting a 2BHK flat in HSR Layout, Bengaluru for 2 years at Rs 28,000/month. I gave 1 lakh rupees as security deposit. I gave proper 1-month notice on 1st October and vacated the flat on 31st October 2024. I cleared all electricity and water bills and handed over keys. Landlord Mr. Ramesh promised to refund the deposit via UPI in 3 days. Now it has been 25 days, he stopped picking my calls, and yesterday he messaged saying he is deducting Rs 45,000 for 'complete house repainting, marble polishing, and deep cleaning'. There was no damage, just normal nail holes for photo frames and standard wear and tear. I have move-in photos, move-out handover video, all rent payment bank statements, and WhatsApp chat where he acknowledged receiving the flat in good condition. How can I get my Rs 45,000 back?
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Security Deposit Refund Dispute – 2BHK HSR Layout",
  "category": "Tenancy & Rental",
  "summary": "The tenant vacated a 2BHK flat after a 2‑year lease, handed over the property in good condition, and was promised a full security deposit refund. The landlord now claims a Rs 45,000 deduction for repainting and cleaning, which the tenant disputes.",
  "complainant": "Tenant",
  "opposite_party": "Landlord Mr. Ramesh",
  "disputed_amount": "Rs 45,000",
  "timeline": [
    {
      "date_or_period": "Oct 2022 (approx)",
      "event": "Tenancy of 2BHK flat in HSR Layout, Bengaluru began at Rs 28,000/month with Rs 1,00,000 security deposit."
    },
    {
      "date_or_period": "1 Oct 2024",
      "event": "Tenant gave one‑month notice to vacate."
    },
    {
      "date_or_period": "31 Oct 2024",
      "event": "Tenant vacated the flat, cleared electricity and water bills, handed over keys, and recorded move‑out video."
    },
    {
      "date_or_period": "Early Nov 2024 (within 3 days of vacating)",
      "event": "Landlord promised to refund the full deposit via UPI within three days."
    },
    {
      "date_or_period": "~25 Nov 2024 (25 days after vacating)",
      "event": "No refund received; landlord stopped answering calls."
    },
    {
      "date_or_period": "26 Nov 2024 (yesterday)",
      "event": "Landlord messaged tenant stating a deduction of Rs 45,000 for repainting, marble polishing, and deep cleaning."
    }
  ],
  "evidence_held": [
    "Move‑in photographs of the flat",
    "Move‑out handover video showing condition of the property",
    "Bank statements showing monthly rent payments",
    "WhatsApp chat where landlord acknowledged receiving the flat in good condition",
    "UPI transaction history (showing no refund received)"
  ],
  "evidence_needed": [
    "Signed rent agreement/lease deed specifying security deposit terms and permissible deductions",
    "Receipt or written acknowledgment of the Rs 1,00,000 security deposit paid",
    "Copy of the one‑month notice sent on 1 Oct 2024",
    "Utility bill clearance receipts (electricity, water) for October 2024",
    "Any written estimate or invoice from landlord for repainting/marble polishing/cleaning",
    "Inventory or condition checklist (if any) signed by both parties at move‑in and move‑out"
  ],
  "evidence_strength_score": 8,
  "evidence_strength_explanation": "Strong visual and transactional proof of the flat's condition and payments, plus landlord's acknowledgment, but missing the formal lease and written notice documents which are crucial for a complete case.",
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
  "plain_language_standing": "You, as the tenant, have a solid legal footing to claim the full return of your security deposit. Under the Transfer of Property Act, 1882, a tenant is only liable for damage that goes beyond normal wear and tear (Section 108(B)(m)). The photographs and video you have taken show that the flat was handed back in good condition, and the landlord’s own WhatsApp message confirms this. Because the landlord has not provided any written estimate or invoice proving that the Rs 45,000 deduction is for actual damage, the deduction is not legally justified. \n\nSince the dispute is about a contract‑based monetary claim, it is a civil matter, not a criminal one. You can recover the amount through a simple pre‑litigation notice and, if needed, by approaching the Rent Authority or a Small Causes Court in Bengaluru. The process is straightforward, inexpensive, and you can represent yourself without hiring a lawyer.",
  "governing_laws": [
    {
      "act_name": "Transfer of Property Act, 1882",
      "section": "Section 108(B)(m)",
      "relevance": "Limits the landlord’s right to deduct from the deposit to damages beyond reasonable wear and tear. Your evidence shows only normal wear, so the deduction is unlawful."
    },
    {
      "act_name": "Transfer of Property Act, 1882",
      "section": "Section 108(B)(f)",
      "relevance": "Allows a tenant to make necessary repairs and deduct the cost only after giving the landlord a reasonable notice and receiving a written estimate. No such notice or estimate was given."
    },
    {
      "act_name": "Transfer of Property Act, 1882",
      "section": "Section 108(A)(c)",
      "relevance": "Guarantees the tenant’s right to quiet enjoyment and possession without arbitrary deductions, reinforcing your claim for a full refund."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Send a Formal Legal Notice to the Landlord",
      "timeline": "15 Days from receipt",
      "cost_estimate": "Free to minimal (Speed Post or email)",
      "details": "Draft a notice citing Section 108(B)(m) and Section 108(B)(f) of the Transfer of Property Act. State that the deposit must be returned in full because no proven damage beyond reasonable wear and tear exists. Attach copies of the move‑out video, photographs, rent payment statements, and the landlord’s WhatsApp acknowledgment. Demand payment of the full Rs 1,00,000 deposit within 15 days, failing which you will proceed to legal action."
    },
    {
      "step_number": 2,
      "title": "File a Complaint with the Local Rent Authority / Small Causes Court",
      "timeline": "30‑45 Days after notice expiry",
      "cost_estimate": "Zero court fees up to Rs. 5 Lakhs (Small Causes Court) + nominal filing fee",
      "details": "If the landlord does not comply, lodge an application before the Bengaluru Rent Authority (under Karnataka’s Rent Control Act) or file a suit for recovery of deposit in the Small Causes Court of Bangalore. Prepare the same documents used in the notice, plus a copy of the lease (if available) and the one‑month notice you sent. The court can order the landlord to refund the deposit with interest and may award costs."
    },
    {
      "step_number": 3,
      "title": "Approach the Consumer Forum (Optional)",
      "timeline": "60‑90 Days after filing in court",
      "cost_estimate": "Nominal (court fee based on claim value)",
      "details": "If the landlord continues to refuse payment, you may also file a complaint under the Consumer Protection Act, 2019 for unfair trade practice (Section 2(47)). Use the e‑Daakhil portal (edaakhil.nic.in) to submit the complaint with all evidence. The Consumer Commission can order a refund and may impose a penalty on the landlord."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "You can draft and send the legal notice yourself, and you are allowed to appear personally before the Rent Authority, Small Causes Court, or Consumer Forum. A lawyer becomes essential only if the case becomes complex (e.g., multiple parties, counter‑claims) or if you wish to file an appeal. For the steps outlined above, self‑representation is fully permissible.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self‑advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
## **LEGAL NOTICE**  
*(Demand for Refund of Security Deposit – 2BHK HSR Layout, Bengaluru)*  

---

### **Date:** 07‑11‑2026  

### **Mode of Dispatch:**  
- **Speed Post – Acknowledgement Due (AD)**  *(or)*  
- **Registered Email (with read‑receipt)**  

---

### **From (Sender / Claimant)**  

|  |  |
|---|---|
| **Name:** | **[Your Full Name]** |
| **Address:** | **[Flat No., Street, HSR Layout, Bengaluru – 560102]** |
| **Phone:** | **[Mobile No.]** |
| **E‑mail:** | **[your.email@example.com]** |

### **To (Recipient / Opposite Party)**  

|  |  |
|---|---|
| **Name:** | **Mr. Ramesh** |
| **Address:** | **[Landlord’s Complete Postal Address]** |
| **Phone / Email:** | **[If known]** |

---

## **Subject:**  
**Demand for Full Refund of Security Deposit (Rs. 1,00,000) within 15 Days of Receipt of this Notice**  

---

### **1.  Under instructions from my client, the undersigned hereby submits as under:**  

| Sr. No. | Date / Period | Event |
|---|---|---|
| 1 | **Oct 2022 (approx.)** | Tenancy of the 2 BHK flat (HSR Layout, Bengaluru) commenced on a month‑to‑month basis at **Rs 28,000 per month**. A **security deposit of Rs 1,00,000** was paid by the tenant to the landlord. |
| 2 | **1 Oct 2024** | Tenant served a **one‑month notice** to vacate the premises, as required under the lease. |
| 3 | **31 Oct 2024** | Tenant vacated the flat, cleared all electricity & water dues, handed over the keys, and recorded a **move‑out video** showing the flat in good condition. |
| 4 | **Early Nov 2024 (within 3 days of vacating)** | Landlord **promised** to refund the **full security deposit** via UPI **within three days**. |
| 5 | **~25 Nov 2024 (25 days after vacating)** | No refund was received; landlord stopped answering calls. |
| 6 | **26 Nov 2024** | Landlord messaged the tenant stating a **deduction of Rs 45,000** for repainting, marble polishing and deep cleaning. No written estimate, invoice or inspection report was furnished. |

---

### **2.  Documents/ Evidence in the possession of the tenant (Annexure‑A)**  

1. Move‑in photographs of the flat.  
2. Move‑out hand‑over video (showing condition of the property).  
3. Bank statements evidencing monthly rent payments.  
4. WhatsApp chat screenshot where landlord **acknowledged receipt of the flat in good condition**.  
5. UPI transaction history (showing **no refund** received).  

*(All the above are annexed hereto and form part of this notice.)*  

---

### **3.  Legal Grounds**  

| Provision | Act | Relevance |
|---|---|---|
| **Section 108(B)(m)** | Transfer of Property Act, 1882 | Allows deduction from security deposit **only for damage beyond normal wear and tear**. The tenant’s video & photographs demonstrate only ordinary wear; therefore the claimed Rs 45,000 is unlawful. |
| **Section 108(B)(f)** | Transfer of Property Act, 1882 | Requires the landlord to give **reasonable notice** and a **written estimate/invoice** for any deduction. No such notice or estimate has been provided. |
| **Section 108(A)(c)** | Transfer of Property Act, 1882 | Guarantees the tenant’s right to **quiet enjoyment and possession** without arbitrary deductions. |

---

### **4.  Demand**  

In view of the foregoing facts and legal provisions, the tenant **demands** that the landlord:

1. **Refund the entire security deposit of Rs 1,00,000 (Rupees One Lakh only)** **without any deduction**,  
2. **Within fifteen (15) days** from the date of receipt of this notice (i.e., by **22‑11‑2026**),  
3. Payment to be made by **UPI/Bank Transfer** to the following account:  
   - **Account Holder:** *[Your Name]*  
   - **Bank & IFSC:** *[Bank Details]*  
   - **UPI ID:** *[your.upi@bank]*  

**Failure to comply** with the above demand within the stipulated period will attract the following consequences **without any further notice**:

| Consequence | Legal Basis | Effect |
|---|---|---|
| **Interest** | [unverified reference removed] of the **Rural Debt Recovery Act, 1999** (as applied by courts) | Statutory interest at **12 % per annum** from the date of default (27 Nov 2024) until actual payment. |
| **Litigation Costs & Damages** | Civil Procedure Code, 1908 – Order II Rule 9 | Recovery of all court fees, attorney’s fees (if any), and **liquidated damages** for breach of contract. |
| **Legal Action** | Karnataka Rent Control Act, 1999 & Small Causes Court (Bengaluru) | Filing of a suit for recovery of the deposit with interest and costs before the **Bengaluru Rent Authority** or **Small Causes Court**. |
| **Consumer Protection** | Consumer Protection Act, 2019 – Section 2(47) (Unfair Trade Practice) | Parallel complaint before the **Consumer Disputes Redressal Commission** (District/State) for unfair deduction. |

---

### **5.  Annexure‑A (List of Documents attached)**  

| No. | Document |
|---|---|
| 1 | Move‑in photographs (dated Oct 2022) |
| 2 | Move‑out hand‑over video (31 Oct 2024) |
| 3 | Bank statements showing rent payments (Oct 2022 – Oct 2024) |
| 4 | WhatsApp chat screenshot (landlord’s acknowledgment) |
| 5 | UPI transaction history (no credit of Rs 1,00,000) |
| 6 | Copy of the one‑month notice dated 1 Oct 2024 (if available) |
| 7 | Utility bill clearance receipts (Electricity & Water – Oct 2024) |
| 8 | Any other relevant communication (e.g., landlord’s message of 26 Nov 2024) |

*(If any of the above documents are not in possession, the tenant shall procure them promptly and submit as part of the final pleading.)*  

---

### **6.  Verification**  

I, **[Your Full Name]**, the undersigned, do hereby **verify** that the contents of this notice are true to my knowledge and belief, and that no material fact has been concealed.

---  

**Signature of the Tenant**  

_____________________________  
**[Your Full Name]**  

**Date:** 07‑11‑2026  

---  

*Copy to:*  

1. **Self (for records)**  
2. **District Legal Services Authority (DLSA) – Bengaluru** (for legal aid reference)  
3. **E‑mail attachment (if sent by registered email)**  

---  

> **Important:** Retain the **Speed‑Post receipt with Acknowledgement Due (AD)** as proof of service. In case the landlord disputes receipt, the AD receipt will be admissible evidence before any forum.  

---  

*Prepared by:*  
**NyayaMitra India – Expert Legal Drafting Unit**  
*(Legal information and self‑advocacy tool – not a substitute for professional representation where required.)*  

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Mr. Ramesh, as per Section 108 of the Transfer of Property Act and the Model Tenancy framework, ordinary wear and tear like wall paint aging cannot be deducted from my deposit. I have the handover video and our chat proof. Please refund my balance 45,000 within 7 days."*
- **Opponent Reaction:** Dekhiye, aapka video aur chat humne dekha hai, lekin hamari company policy ke mutabik agar paint ki halat normal wear‑and‑tear se zyada kharab ho to uska kharcha deposit se liya ja sakta hai. Aapne Section 108 ka zikr kiya, lekin usmein bhi yeh likha hai ki ‘actual damage’ ke liye hi deduction ho sakta hai, na ki sirf purane hone ke liye. Isliye hum aapse ek formal notice maang rahe hain – aapke saboot aur hamare inspection report ko dekh kar hi hum final decision lenge. Agar aapko lagta hai ki hum galat hain, to aap consumer court ya Karnataka Rent Control Tribunal mein appeal kar sakte hain, lekin iske liye humein aapka written notice chahiye. Tab hum 7 din ke andar aapko final settlement amount batayenge.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "Aapne sahi tarah se Section 108 aur Model Tenancy framework ka hawala diya, saath hi video aur chat proof ka zikr karke apni baat ko mazboot banaya.",
  "what_to_improve": "Karnataka Rent Control Act ya Karnataka Rent Restriction Act ke specific clause (jaise ki [unverified reference removed] – deposit refund within 30 din) ka bhi zikr kar sakte the, aur actual repair estimate ya invoice attach karne se aapka case aur bhi pakka hota.",
  "suggested_next_counter": "Agar aapko 7 din mein refund nahi milta, to main Karnataka Rent Control Tribunal mein complaint file karunga aur aapke saboot ke saath consumer court ka bhi sahara lunga."
}
```

---

## TC-02: E-Commerce Defective Smartphone Refund Denial

- **Timestamp:** `2026-11-07T19:35:00.493335+00:00`
- **Provider / Model:** `groq` / `openai/gpt-oss-120b`
- **Category:** `Consumer & E-Commerce`

### 1. Raw User Input
```text
I ordered a Samsung Galaxy smartphone worth Rs 26,999 on an e-commerce app on 10th November 2024. It was delivered on 14th November. Within 24 hours of opening the box, the screen started flickering with green lines and touch stopped working. I raised a replacement request on 15th November. The app sent a technician for inspection on 21st November. The technician confirmed it is a manufacturing hardware defect and took sign on his job sheet. But on 23rd November, customer support cancelled my return request stating 'The 7-day return window expired on 21st November'. They are telling me to go to an authorized brand service center 40 km away. I paid for a brand new working phone, not a defective phone repaired on day one. I have the invoice, delivery receipt, technician inspection job sheet copy, and chat screenshots.
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Defective Samsung Galaxy Phone Delivered by E-commerce Platform",
  "category": "Consumer & E-Commerce",
  "summary": "The consumer purchased a Samsung Galaxy smartphone for Rs 26,999 on an e‑commerce app. The phone malfunctioned within a day, a technician confirmed a hardware defect, but the platform denied a return citing an expired 7‑day window and directed the consumer to a distant service centre.",
  "complainant": "Consumer (Buyer)",
  "opposite_party": "E‑commerce platform (name not specified)",
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
      "event": "Raised a replacement/return request after the screen flickered and touch stopped within 24 hours of opening."
    },
    {
      "date_or_period": "21 Nov 2024",
      "event": "Technician visited, inspected the phone, confirmed manufacturing hardware defect, and signed a job sheet."
    },
    {
      "date_or_period": "23 Nov 2024",
      "event": "Customer support cancelled the return request, stating the 7‑day return window expired on 21 Nov and advised going to an authorized service centre 40 km away."
    }
  ],
  "evidence_held": [
    "Invoice showing purchase price of Rs 26,999",
    "Delivery receipt confirming receipt on 14 Nov 2024",
    "Copy of technician inspection job sheet with signature",
    "Chat screenshots with customer support regarding the return request and cancellation"
  ],
  "evidence_needed": [
    "Original signed technician job sheet (if copy is not sufficient)",
    "Timestamped confirmation/email of the replacement/return request submitted on 15 Nov 2024",
    "Record of the 7‑day return policy terms as displayed on the app at the time of purchase",
    "Any email or SMS notification of the cancellation decision dated 23 Nov 2024",
    "Proof of the authorized service centre’s distance and any additional costs that may be incurred"
  ],
  "evidence_strength_score": 8,
  "evidence_strength_explanation": "Key documents (invoice, delivery receipt, signed job sheet, chat logs) directly support the claim, giving the evidence a strong but not perfect rating.",
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
  "plain_language_standing": "You are a consumer as defined by the Consumer Protection Act, 2019 because you bought a Samsung Galaxy phone online for personal use. The phone turned out to be defective within a day, and a qualified technician confirmed a manufacturing fault. Under the Act, a defect in goods and a deficiency in the service (the e‑commerce platform’s refusal to honour a return despite the defect) give you a clear right to a replacement, repair, or refund. The platform’s claim that the 7‑day window has expired, even though the defect was reported within that period and the law requires a refund or replacement within 30 days of delivery for defective goods, is an unfair trade practice. This is a civil dispute, not a criminal offence, so you can seek redress through the consumer forum without needing to file a police FIR.",
  "governing_laws": [
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(7)",
      "relevance": "Defines you as a consumer because you purchased the phone online for personal use."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(10)",
      "relevance": "Covers the hardware defect in the phone as a \"defect in goods\"."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(11)",
      "relevance": "Treats the platform’s refusal to replace/repair the defective phone as a \"deficiency in service\"."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(47)",
      "relevance": "Identifies the platform’s denial of refund/replacement after a defect as an unfair trade practice."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 35",
      "relevance": "Allows you to file a consumer complaint electronically via e‑Daakhil."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 84",
      "relevance": "Makes the product manufacturer liable for manufacturing defects, supporting your claim for a refund or replacement."
    },
    {
      "act_name": "General Legal Principle (Civil vs. Criminal)",
      "section": "N/A",
      "relevance": "Clarifies that this is a civil matter, not a criminal cheating case."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Send a Formal Legal Demand Notice",
      "timeline": "Within 15 days from today",
      "cost_estimate": "Free to minimal (postage or email cost)",
      "details": "Draft a concise notice stating: (a) you are a consumer under CPA 2019, (b) the phone has a manufacturing defect confirmed by a technician, (c) the e‑commerce platform is violating Section 2(47) by refusing a refund/replacement, and (d) you demand a full refund of Rs 26,999 or a replacement within 7 days of receipt of the notice. Send it by registered post or email and keep a copy of the receipt."
    },
    {
      "step_number": 2,
      "title": "File an Electronic Complaint on e‑Daakhil",
      "timeline": "Within 30‑45 days",
      "cost_estimate": "Zero court fee for claims up to Rs 5 Lakhs",
      "details": "Register on edaakhil.nic.in. Upload the following documents: purchase invoice, delivery receipt, technician’s signed job sheet, chat screenshots, and a copy of the demand notice. Choose the District Consumer Disputes Redressal Commission (DCDRC) as the forum. Pay the nominal filing fee (if any) online and note the complaint number for future reference."
    },
    {
      "step_number": 3,
      "title": "Attend the Consumer Forum Hearing / Seek Enforcement",
      "timeline": "Typically 60‑90 days after filing",
      "cost_estimate": "Nominal (travel, copying documents)",
      "details": "The forum will issue a notice to the e‑commerce platform. You can appear yourself (self‑representation is allowed) and present the evidence you have. If the forum orders a refund or replacement and the platform still does not comply, you can file for execution of the order through the district court."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "The Consumer Disputes Redressal Commissions allow you to represent yourself, so a lawyer is not mandatory. You may consult a lawyer for advice on drafting the demand notice or if the platform files a counter‑claim, but you can comfortably handle the filing and hearing on your own.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self‑advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
## **LEGAL DEMAND NOTICE**  
*(Consumer & E‑Commerce – Defective Samsung Galaxy Phone)*  

---

### **1.   Header**

| **From (Sender)** | **To (Recipient)** |
|-------------------|--------------------|
| **Name:** *[Your Full Name]*  <br> **Address:** *[Your Complete Residential Address]*  <br> **Mobile:** *[Your Mobile No.]*  <br> **E‑mail:** *[Your Email ID]* | **Name:** *[E‑Commerce Platform – Legal/Customer Service Department]*  <br> **Address:** *[Registered Office / Corporate Address as per website]*  <br> **E‑mail:** *[Official Support Email]* |

---

### **2.   Date & Mode of Dispatch**

- **Date:** *[Insert Date – e.g., 7 November 2026]*  
- **Mode of Dispatch:** **Speed Post – Acknowledgement Due (AD)** / **Registered E‑mail (with read‑receipt)**  

*(Both copies are being sent – one by Speed Post and one by registered e‑mail for redundancy and proof of service.)*  

---

### **3.   Subject**

> **Demand for Refund / Replacement of Defective Samsung Galaxy Smartphone (Order No. [XXXX]) purchased for Rs 26,999**  

---

### **4.   Opening Paragraph (Instruction Clause)**  

> **Under instructions from my client, the undersigned hereby submits as under:**  

---

### **5.   Statement of Facts (Chronological Sequence)**  

| **Date / Period** | **Event** |
|-------------------|-----------|
| **10 Nov 2024** | Placed an order for a *Samsung Galaxy* smartphone (Model: *[Exact Model]*, Price: **Rs 26,999**) on the e‑commerce app of *[Platform Name]* (Order No. [XXXX]). |
| **14 Nov 2024** | Phone was delivered to the above‑stated residential address; delivery receipt attached (Annexure‑B). |
| **15 Nov 2024** | Within 24 hours of unboxing, the screen began flickering and the touch panel stopped responding. A replacement/return request was lodged through the app’s “Return/Replace” facility (timestamped copy attached – Annexure‑D). |
| **21 Nov 2024** | A certified technician from *[Authorized Service Provider]* visited, inspected the device, diagnosed a **manufacturing hardware defect**, and signed the job‑sheet confirming the same (Annexure‑C). |
| **23 Nov 2024** | Customer‑support executive cancelled the return request, stating that the 7‑day return window had expired on 21 Nov 2024 and directed the consumer to an authorized service centre located **≈ 40 km** away (chat screenshots attached – Annexure‑D). |

---

### **6.   Documents Annexed (Evidence)**  

| **Annexure** | **Description** |
|--------------|-----------------|
| **Annexure‑A** | Original invoice showing purchase price **Rs 26,999**. |
| **Annexure‑B** | Delivery receipt confirming receipt on **14 Nov 2024**. |
| **Annexure‑C** | Technician’s inspection job‑sheet (signed) confirming a manufacturing defect. |
| **Annexure‑D** | Chat‑screen captures with customer‑support showing the return request, its cancellation, and the 7‑day window claim. |
| **Annexure‑E** *(optional)* | Screenshot of the platform’s “7‑day return policy” as displayed at the time of purchase. |

---

### **7.   Legal Grounds**

1. **Consumer Protection Act, 2019**  
   - **Section 2(7)** – Defines the complainant as a *consumer* (purchase for personal use).  
   - **Section 2(10)** – The hardware defect constitutes a *defect in goods*.  
   - **Section 2(11)** – The platform’s refusal to replace/repair amounts to a *deficiency in service*.  
   - **Section 2(47)** – Denial of refund/replacement after a confirmed defect is an *unfair trade practice*.  
   *Reference:* *Consumer Protection (Consumer Protection) Rules, 2020* – Rule 3 (right to replacement/repair within 30 days of delivery for defective goods).  

2. **Statutory Interest & Compensation**  
   - Under **[unverified reference removed]** of the CPA, the consumer is entitled to **interest at the rate of 12 % per annum** on the amount due, calculated from the date of default (i.e., from **23 Nov 2024**).  
   - The consumer may also claim **damages for loss of enjoyment and inconvenience** as per **[unverified reference removed](2)**.

---

### **8.   Demand (15‑Day Rectification Window)**  

> **You are hereby directed to effect either:**  

1. **A full refund of Rs 26,999 (Rupees Twenty‑Six Thousand Nine Hundred Ninety‑Nine only)**, **or**  
2. **A brand‑new replacement of the same model (Samsung Galaxy – identical specifications)**  

> **within **_**fifteen (15) calendar days**_** from the receipt of this notice (i.e., on or before **[Date + 15 days]**).**  

> The refund/replacement must be credited to the bank account **[Your Bank Details]** or the replacement dispatched to the address mentioned above, at **no additional cost** to the consumer.

---

### **9.   Consequence of Non‑Compliance**

- **Failure to comply** within the stipulated 15‑day period will compel the consumer to **file a complaint before the District Consumer Disputes Redressal Commission (DCDRC)** under the Consumer Protection Act, 2019, seeking:
  1. **Refund of Rs 26,999** with **statutory interest at 12 % per annum** from 23 Nov 2024 till actual payment.  
  2. **Compensation for inconvenience and mental agony** (as deemed fit by the Commission).  
  3. **Recovery of litigation costs, postage, and any other expenses** incurred.  

- The consumer also reserves the right to **approach the appropriate consumer forum for execution of the award** and to **report the unfair trade practice** to the **Competition Commission of India** and **State Consumer Protection Council**.

---

### **10.   Legal Disclaimer**

> This notice is issued **without prejudice** to any other rights or remedies available to the consumer under the law. The consumer expressly reserves all such rights.

---

### **11.   Signature & Verification**

| **Signature of the Consumer** | **Date** |
|-------------------------------|----------|
| _____________________________ | __________ |

*The consumer affirms that the facts stated herein are true and correct to the best of his/her knowledge and belief.*

---

### **12.   Service Confirmation (for Speed Post)**  

| **Speed Post Receipt No.** | **Date of Dispatch** |
|----------------------------|----------------------|
| __________________________ | ____________________ |

*(Retain the receipt as proof of service.)*  

---  

**Prepared by:** *[Your Full Name]* – Consumer (Self‑Represented)  

**Contact:** *[Mobile No.]* | *[Email ID]*  

---  

*Please acknowledge receipt of this notice within 2 working days.*  

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under Section 2(11) and Section 84 of the Consumer Protection Act 2019, delivering a defective phone and delaying inspection past your return window is a clear deficiency in service and unfair trade practice. I have the technician report confirming hardware fault. I demand an immediate refund or I will escalate to the National Consumer Helpline and e-Daakhil."*
- **Opponent Reaction:** Look, I have already explained our stance. We operate strictly by our terms and policies, so I cannot agree to this right now.
- **Coach Feedback:**
```json
{
  "strength_rating": "Moderate",
  "what_went_well": "You maintained a clear and determined position.",
  "what_to_improve": "Quote the exact 15-day timeline and statutory liability under Indian law.",
  "suggested_next_counter": "Remind them that persistent refusal attracts 12% statutory interest in formal court proceedings."
}
```

---

## TC-03: Gurugram Tech Employee Unpaid Salary & Relieving Letter Withheld

- **Timestamp:** `2026-11-07T19:36:14.344302+00:00`
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
  "summary": "The employee resigned on 1 Aug 2024, completed the 60‑day notice, but the employer has not paid the September salary and leave encashment of Rs 1,65,000, delayed the August salary, and is refusing to issue the relieving and experience letters, jeopardising the new job offer.",
  "complainant": "Frontend Developer (Employee)",
  "opposite_party": "IT Consultancy Firm (Employer)",
  "disputed_amount": "Rs 1,65,000",
  "timeline": [
    {
      "date_or_period": "Feb 2023 (approx)",
      "event": "Joined the IT consultancy as a frontend developer with a salary of Rs 70,000 per month."
    },
    {
      "date_or_period": "1 Aug 2024",
      "event": "Submitted resignation letter."
    },
    {
      "date_or_period": "1 Aug – 30 Sep 2024",
      "event": "Served 60‑day notice period, handed over assets (MacBook, ID card) and received asset clearance certificate."
    },
    {
      "date_or_period": "Aug 2024",
      "event": "Salary for August was delayed/not received."
    },
    {
      "date_or_period": "30 Sep 2024",
      "event": "Last working day; handover completed."
    },
    {
      "date_or_period": "Oct 2024 (post‑last day)",
      "event": "September salary plus 15 days encashable leave (Rs 1,65,000) remains unpaid."
    },
    {
      "date_or_period": "~Mid‑Nov 2024 (≈50 days after last day)",
      "event": "No salary paid; HR cites client payment delays; relieving and experience letters withheld."
    },
    {
      "date_or_period": "End of week (early Nov 2024)",
      "event": "New employer threatens to cancel job offer if relieving letter is not provided."
    }
  ],
  "evidence_held": [
    "Appointment letter",
    "Resignation acceptance email",
    "Signed asset clearance form/certificate",
    "Email records of resignation submission"
  ],
  "evidence_needed": [
    "Salary slips for August and September 2024",
    "Bank statements or UPI/NEFT transaction records showing non‑receipt of salary",
    "Complete email/WhatsApp thread with HR/Finance regarding salary delay and relieving letter request",
    "Copy of the company's policy on notice period salary payment and leave encashment",
    "Written acknowledgment from employer about pending dues (if any)",
    "Any internal communication confirming the withholding of relieving/experience letters"
  ],
  "evidence_strength_score": 5,
  "evidence_strength_explanation": "Key documents like appointment letter and clearance form are present, but lacking direct proof of unpaid salary and communications that show the employer's refusal.",
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
  "plain_language_standing": "You have a clear legal right to receive the salary and leave encashment that were due for August and September 2024, and also to get your relieving and experience letters. Under the Code on Wages, 2019, an employer must pay all wages within two working days after an employee resigns (Section 17(2)). The amount you are owed (Rs 1,65,000) is a wage, so the employer’s delay is a breach of that law. The matter is a civil dispute – it is about unpaid wages and a contract breach, not a criminal offence. Because the employer is also refusing to give you the relieving documents, you can claim those as part of the same wage claim, and the labour authorities can order the employer to issue them.",
  "governing_laws": [
    {
      "act_name": "Code on Wages, 2019",
      "section": "Section 17(2)",
      "relevance": "Requires the employer to pay all wages within two working days of resignation, dismissal or removal."
    },
    {
      "act_name": "Code on Wages, 2019",
      "section": "Section 18(3)",
      "relevance": "Limits any deductions to 50% of wages, ensuring the full amount you are owed cannot be arbitrarily reduced."
    },
    {
      "act_name": "General Legal Principle (Civil vs. Criminal Boundary)",
      "section": "N/A",
      "relevance": "Clarifies that non‑payment of salary is a civil matter, not a criminal cheating case."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Send Formal Legal Notice (Email / Registered Post)",
      "timeline": "Within 7‑10 days from notice date",
      "cost_estimate": "Free to minimal (postage or email cost)",
      "details": "Draft a concise notice stating: (a) you resigned on 1 Aug 2024 and completed the 60‑day notice; (b) under Section 17(2) of the Code on Wages, the employer must pay all pending wages within two working days of resignation; (c) you are owed August salary, September salary and leave encashment totalling Rs 1,65,000; (d) you also require the relieving and experience letters; (e) you demand payment and issuance of the letters within 7 days, failing which you will approach the labour authorities. Attach copies of your appointment letter, resignation acceptance, asset clearance form, and any email proof of the resignation."
    },
    {
      "step_number": 2,
      "title": "File a Grievance on the Labour Department Portal (e‑Daakhil / State Labour Commissioner)",
      "timeline": "Within 30 days of sending the notice",
      "cost_estimate": "Zero court fees for claims up to Rs 5 Lakhs; nominal filing fee if any",
      "details": "Register on the e‑Daakhil portal (https://e-daakhil.gov.in) or the respective State Labour Commissioner’s website. Upload the legal notice, supporting documents (appointment letter, resignation email, asset clearance, salary slips if available), and a brief statement of claim. The portal will generate a reference number and forward the complaint to the Labour Commissioner, who will issue a notice to the employer to comply."
    },
    {
      "step_number": 3,
      "title": "Approach the Labour Court / Industrial Tribunal",
      "timeline": "60‑90 days from filing the grievance, depending on the authority’s schedule",
      "cost_estimate": "Nominal court fee (around Rs 500‑1,000 for claims up to Rs 2 Lakhs); possible free legal aid from DLSA",
      "details": "If the employer does not comply with the Labour Commissioner’s order, file a plaint in the District Labour Court or Industrial Tribunal having jurisdiction over the employer’s location. You can represent yourself, but a lawyer can help draft the plaint and argue the case. Attach all evidence, including the employer’s response (or lack thereof). The court can order payment of the pending wages, interest, and direct the employer to issue the relieving and experience letters."
    }
  ],
  "real_lawyer_needed": true,
  "real_lawyer_guidance": "You can start the process yourself – sending the notice and filing the online grievance do not require a lawyer. However, filing a petition before the Labour Court or Industrial Tribunal usually benefits from legal representation, especially to ensure the claim is framed correctly and to handle any defence the employer raises. If you cannot afford a lawyer, approach the District Legal Services Authority (DLSA) for free legal aid (Helpline 15100).",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self‑advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
**[Your Letterhead – Optional]**  

---

## LEGAL DEMAND NOTICE  

**Date:** 7 November 2026  

**Mode of Dispatch:**  
- **Speed Post (Acknowledgement Due)** – No. _________________  
- **Registered Email** – to: ___________________________ (Read‑Receipt requested)  

---

### 1. PARTIES  

| **Sender (Complainant)** | **Recipient (Employer)** |
|--------------------------|--------------------------|
| **Name:** *[Your Full Name]*<br>**Designation:** Front‑end Developer (former)<br>**Address:** *[Your Residential Address]*<br>**Phone / Email:** *[Mobile No., Email ID]* | **Name of Firm:** *[IT Consultancy Firm’s Registered Name]*<br>**Address of Registered Office:** *[Employer’s Registered Address]*<br>**Attention:** *[HR Manager / Managing Director]*<br>**Phone / Email:** *[Employer’s Contact Details]* |

---

### 2. UNDER INSTRUCTIONS FROM MY CLIENT  

The undersigned, *[Your Full Name]*, acting on his own behalf, hereby serves this notice to *[Employer’s Name]* (hereinafter “the Employer”) as follows:

---

### 3. FACTUAL MATRIX  

| **Date / Period** | **Event** |
|-------------------|-----------|
| **Feb 2023 (approx.)** | Joined the Employer as a Front‑end Developer with a gross monthly salary of **Rs 70,000**. |
| **1 Aug 2024** | Submitted resignation letter (copy annexed – **Annexure‑A**). |
| **1 Aug – 30 Sep 2024** | Served the contractual 60‑day notice period, handed over all assets (MacBook, ID card) and obtained an **Asset Clearance Certificate** (copy annexed – **Annexure‑B**). |
| **Aug 2024** | Salary for August was **delayed / not received** (no salary slip – request attached as **Annexure‑C**). |
| **30 Sep 2024** | Last working day; hand‑over completed. |
| **Oct 2024 (post‑last day)** | September salary **plus** encashable leave (15 days) amounting to **Rs 1,65,000** remains unpaid (no salary slip – request attached as **Annexure‑D**). |
| **Mid‑Nov 2024 (~ 85 days after last day)** | HR communicated that payment is pending due to client‑payment delays and **refused to issue relieving & experience letters** (email thread attached – **Annexure‑E**). |
| **Early Nov 2024** | New employer has issued a **final notice** threatening cancellation of the job offer unless the relieving letter is produced. |

---

### 4. LEGAL BASIS  

1. **Code on Wages, 2019 – Section 17(2)**  
   *Mandates that an employer shall pay all wages within **two working days** of the employee’s resignation, dismissal or removal.*  

2. **Code on Wages, 2019 – Section 18(3)**  
   *Restricts any deduction to a maximum of **50 % of wages**, thereby precluding arbitrary withholding of the full salary and leave encashment.*  

3. **General Principle of Contractual Obligation**  
   *The employment contract obliges the Employer to pay earned wages and to furnish relieving/experience letters upon termination of service.*  

The Employer’s failure to pay the August & September salaries and the encashable leave, and its refusal to issue the relieving and experience letters, constitute a **clear breach of statutory duty** and of the contractual terms, giving rise to a civil claim for recovery of dues, interest, and damages.

---

### 5. DEMAND  

In view of the above, the Employer is **hereby required** to:

1. **Pay the pending wages and leave encashment** amounting to **Rs 1,65,000** (Rupees One Lakh Sixty‑Five Thousand only).  
2. **Issue the Relieving Letter** and **Experience Certificate** addressed to the undersigned, on the Employer’s official letterhead, within **fifteen (15) calendar days** from the receipt of this notice (i.e., by **22 November 2026**).  

**Payment** may be made by direct credit to the undersigned’s bank account (details provided below) or by any other mutually acceptable mode, and the letters may be dispatched by speed post or emailed in PDF format.

**Bank Details (for salary credit):**  
- **Account Holder:** *[Your Name]*  
- **Bank & Branch:** *[Bank Name, Branch]*  
- **Account No.:** *[XXXXXX]*  
- **IFSC Code:** *[XXXXXX]*  

---

### 6. CONSEQUENCES OF NON‑COMPLIANCE  

Should the Employer fail to comply with the above demands **within the stipulated 15‑day period**, the undersigned will be compelled to initiate the following actions **without any further notice**:

1. **File a grievance before the State Labour Commissioner / e‑Daakhil portal** under the provisions of the Code on Wages, 2019.  
2. **Approach the District Labour Court / Industrial Tribunal** for a definitive decree for:  
   - Payment of the outstanding amount **Rs 1,65,000**;  
   - **Statutory interest at 12 % per annum** (simple interest calculated from 1 Oct 2024 till actual payment);  
   - **Compensation for mental agony and loss of future employment** (estimated at **Rs 25,000**); and  
   - **Costs of the proceedings** (including court fees, attorney’s fees, and postage).  

The above reliefs are in accordance with Section 17(2) & Section 18(3) of the Code on Wages, 2019 and the principles of equity.

---

### 7. ANNEXURES  

| **Annexure** | **Description** |
|--------------|-----------------|
| **A** | Copy of Resignation Letter (dated 1 Aug 2024) |
| **B** | Asset Clearance Certificate (signed by HR) |
| **C** | Request for August 2024 salary slip (email) |
| **D** | Request for September 2024 salary slip & leave encashment statement (email) |
| **E** | Email/WhatsApp thread with HR/Finance refusing salary payment & relieving letters |
| **F** | Appointment Letter (Feb 2023) |
| **G** | New Employer’s conditional job‑offer email (showing urgency) |

*(All annexures are attached herewith and form an integral part of this notice.)*

---

### 8. DECLARATION  

I, *[Your Full Name]*, the undersigned, affirm that the contents of this notice are true and correct to the best of my knowledge and belief, and that I am entitled to the reliefs claimed herein.

---

**Signature of the Complainant**  

_____________________________  
*[Your Full Name]*  

**Date:** 7 November 2026  

---  

*Copy to:*  

1. Labour Commissioner, *[State]* – via e‑Daakhil portal (for information)  
2. District Legal Services Authority (DLSA) – for possible legal aid  
3. Personal records (file)  

---  

*Prepared by:*  
*NyayaMitra India – Expert Legal Drafting Unit*  

---  

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under employment laws, full and final dues must be cleared timely and withholding my relieving letter violates my right to livelihood. If my Rs 1,65,000 and relieving letter are not issued within 3 days, I will file a formal complaint with the District Labor Commissioner."*
- **Opponent Reaction:** Dekhiye, humare HR policies aur internal clearance process ke bina hum koi bhi final settlement ya relieving letter issue nahi kar sakte. Aapka resignation acceptance abhi tak HR ke system mein update nahi hua hai, isliye salary aur encashment hold par hai. Company ke standard operating procedure ke mutabik, aapko sabhi pending project deliverables aur asset return ka clearance form sign karna hoga. Jab tak yeh sab complete nahi hota, hum koi payment ya letter release nahi kar sakte. Aapka complaint bhi samajh rahe hain, lekin humare paas bhi apni internal audit ka schedule hai, jo agle hafte tak poora hoga.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "Aapne specific statutory right (full and final dues) aur deadline (3 din) ka zikr kiya, jo aapke claim ko majboot banata hai.",
  "what_to_improve": "Aapko relevant act ka exact section (jaise [unverified reference removed], [unverified reference removed]) ya labour law ka citation dena chahiye, aur apne resignation acceptance email ya receipt attach karna chahiye.",
  "suggested_next_counter": "Mujhe meri resignation acceptance ka email (1 Aug 2024) aur [unverified reference removed] of the [unverified reference removed] ka reference dijiye, aur turant Rs 1,65,000 ka payment aur relieving letter release karne ko kahun."
}
```

---

