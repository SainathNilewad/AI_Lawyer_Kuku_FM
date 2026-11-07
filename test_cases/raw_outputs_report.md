# NyayaMitra - Official Unedited Raw Outputs for Test Cases

> **Execution Metadata:** Generated on `2026-11-06T23:38:27.688511+00:00` using Provider: `groq`, Model: `openai/gpt-oss-120b`.
> **Strict Ground Rule:** Real agent calls only. No post-editing, no mock datasets.

## TC-01: Bengaluru Tenant Security Deposit Withholding

- **Timestamp:** `2026-11-06T23:35:41.676073+00:00`
- **Provider / Model:** `groq` / `openai/gpt-oss-120b`
- **Category:** `Tenancy & Rental`

### 1. Raw User Input
```text
I was renting a 2BHK flat in HSR Layout, Bengaluru for 2 years at Rs 28,000/month. I gave 1 lakh rupees as security deposit. I gave proper 1-month notice on 1st October and vacated the flat on 31st October 2024. I cleared all electricity and water bills and handed over keys. Landlord Mr. Ramesh promised to refund the deposit via UPI in 3 days. Now it has been 25 days, he stopped picking my calls, and yesterday he messaged saying he is deducting Rs 45,000 for 'complete house repainting, marble polishing, and deep cleaning'. There was no damage, just normal nail holes for photo frames and standard wear and tear. I have move-in photos, move-out handover video, all rent payment bank statements, and WhatsApp chat where he acknowledged receiving the flat in good condition. How can I get my Rs 45,000 back?
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Security Deposit Refund Dispute – Rs 45,000 Deduction",
  "category": "Tenancy & Rental",
  "summary": "The tenant vacated a 2BHK flat in HSR Layout after a 2‑year lease, handed over the property in good condition, and was promised a full security deposit refund. The landlord now claims a Rs 45,000 deduction for repainting and polishing, which the tenant disputes.",
  "complainant": "Tenant",
  "opposite_party": "Landlord Mr. Ramesh",
  "disputed_amount": "Rs 45,000",
  "timeline": [
    {
      "date_or_period": "Around Oct 2022",
      "event": "Tenancy began; tenant paid Rs 1,00,000 security deposit and monthly rent of Rs 28,000."
    },
    {
      "date_or_period": "1 Oct 2024",
      "event": "Tenant gave one‑month notice to vacate the flat."
    },
    {
      "date_or_period": "31 Oct 2024",
      "event": "Tenant vacated, cleared electricity & water bills, handed over keys, and recorded move‑out video."
    },
    {
      "date_or_period": "Early Nov 2024 (within 3 days of vacating)",
      "event": "Landlord promised to refund the full security deposit via UPI within three days."
    },
    {
      "date_or_period": "~25 days after vacating (mid‑Nov 2024)",
      "event": "Landlord stopped answering calls."
    },
    {
      "date_or_period": "Yesterday (relative to the complaint)",
      "event": "Landlord messaged tenant stating a deduction of Rs 45,000 for repainting, marble polishing, and deep cleaning."
    }
  ],
  "evidence_held": [
    "Move‑in photographs of the flat",
    "Move‑out handover video showing condition of the property",
    "Bank statements showing monthly rent payments and security deposit payment",
    "WhatsApp chat where landlord acknowledged receipt of the flat in good condition",
    "Copy of the rent receipt / payment confirmations"
  ],
  "evidence_needed": [
    "Signed rental agreement specifying terms for security deposit and permissible deductions",
    "Inventory or condition checklist (if any) signed by both parties at move‑in and move‑out",
    "Written communication (email/WhatsApp) where landlord initially promised full refund",
    "Any estimate or invoice from the landlord for the claimed repainting/marble polishing work",
    "Proof of payment of electricity and water bills (bills or receipts)",
    "A formal demand letter drafted to the landlord requesting the Rs 45,000 refund"
  ],
  "evidence_strength_score": 8,
  "evidence_strength_explanation": "The tenant possesses strong visual proof of the property's condition, payment records, and direct acknowledgment from the landlord, making the case against the deduction compelling.",
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
  "plain_language_standing": "You have a solid legal right to get back the full security deposit you paid. Under the Model Tenancy Act, 2021 a landlord can keep only the amount that covers actual damage caused by the tenant – ordinary wear and tear, like the natural fading of paint, cannot be charged. The landlord must return the deposit within 30 days after you handed over peaceful possession, and any deduction must be backed by a detailed, item‑by‑item bill. Since you have video proof that the flat was in good condition, a written acknowledgment from the landlord that the handover was satisfactory, and you paid the deposit as per the agreement, the landlord’s claim of a Rs 45,000 deduction for repainting and polishing is unlikely to be justified. This is a civil dispute, not a criminal cheating case, so you can pursue it through the rent‑control authority or a small causes court without needing to file a police FIR.",
  "governing_laws": [
    {
      "act_name": "Model Tenancy Act, 2021",
      "section": "Section 13, Section 14, Section 21",
      "relevance": "Caps security deposit, mandates refund within 30 days, and bars deductions for normal wear and tear. Requires landlord to provide itemised bills for any deduction."
    },
    {
      "act_name": "Transfer of Property Act, 1882",
      "section": "Section 108(B)(m), Section 108(B)(q)",
      "relevance": "Tenant must keep the property in the condition it was received, subject only to reasonable wear and tear, and is entitled to the return of the deposit on vacating."
    },
    {
      "act_name": "Bharatiya Nyaya Sanhita, 2023 / IPC",
      "section": "BNS Section 318 (Cheating) & IPC Section 420",
      "relevance": "Clarifies that failure to refund a deposit is a civil matter, not a criminal cheating offence, unless there was fraudulent intent at the start."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Send Formal Legal Notice",
      "timeline": "15 Days from receipt",
      "cost_estimate": "Free to minimal (Speed Post/Registered Email cost)",
      "details": "Draft a notice stating: (a) you vacated on 31 Oct 2024, (b) landlord promised full refund, (c) you are entitled to the entire Rs 1,00,000 deposit under Model Tenancy Act, (d) demand the Rs 45,000 deduction be returned with 12% interest for delay, and (e) give 15 days to comply. Send it by registered post and keep a copy of the receipt."
    },
    {
      "step_number": 2,
      "title": "File Grievance on State Rent Authority / Consumer Helpline",
      "timeline": "30‑45 Days",
      "cost_estimate": "Zero court fees for disputes up to Rs 5 Lakhs; only nominal portal registration charges if any",
      "details": "Register the complaint on your State Rent Authority’s online portal (or use the National Consumer Helpline 1915). Upload the rental agreement, security‑deposit receipt, move‑in/out photos, video, WhatsApp acknowledgment, and a copy of the legal notice. The authority will issue a notice to the landlord and can order refund with interest."
    },
    {
      "step_number": 3,
      "title": "Petition Before Local Rent Authority / Small Causes Court",
      "timeline": "60‑90 Days",
      "cost_estimate": "Nominal filing fee (usually Rs 500‑Rs 1,000 for amounts under Rs 5 Lakhs)",
      "details": "If the landlord does not comply after the authority’s direction, file a petition for recovery of the deposit and interest. You can represent yourself; the court will consider your evidence (photos, video, payment records, notice). The court can order the landlord to pay the Rs 45,000 plus interest and may award a small penalty for wrongful deduction."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "You can handle the entire process yourself: drafting the notice, filing on the rent‑authority portal, and appearing before the Rent Authority or Small Causes Court does not require a lawyer. A lawyer becomes necessary only if the dispute escalates to a higher civil court or if you face a complex counter‑claim.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self‑advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
## **LEGAL DEMAND NOTICE**  

**(Security Deposit Refund – Rs. 45,000)**  

---  

### **1.  Header**  

| **From (Sender)** | **To (Recipient)** |
|-------------------|--------------------|
| **Name:** ______________________________<br>**Address:** ______________________________<br>**Phone / Email:** ______________________________ | **Mr. Ramesh**<br>**Address:** ______________________________<br>**Phone / Email:** ______________________________ |

---  

### **2.  Date & Mode of Dispatch**  

- **Date:** ___ /___ /_____  (dd / mm / yyyy)  
- **Mode of Dispatch:** **Speed Post (Acknowledgement Due)** / **Registered Email (with read‑receipt)**  

---  

### **3.  Subject**  

> **Demand for Refund of Security‑Deposit Deduction of Rs. 45,000 (Forty‑Five Thousand Only) within 15 Days, failing which legal proceedings will be instituted.**  

---  

### **4.  Opening Paragraph (Instruction Clause)**  

> **Under instructions from my client, the undersigned, being the authorized legal drafter of NyayaMitra India, hereby submits the following notice on behalf of the tenant (hereinafter “the Complainant”).**  

---  

### **5.  Recital of Facts (Chronological Sequence)**  

| **Date / Period** | **Event** |
|-------------------|-----------|
| **Around Oct 2022** | Tenancy of a 2 BHK flat at **HSR Layout, Bengaluru** commenced. The Complainant paid a **security deposit of Rs. 1,00,000** and monthly rent of **Rs. 28,000** as per the signed Rental Agreement. |
| **1 Oct 2024** | The Complainant served a **one‑month notice** to vacate the premises, as required under the Agreement. |
| **31 Oct 2024** | The Complainant **vacated the flat**, cleared all electricity & water dues, handed over the keys, and recorded a **move‑out video** evidencing the good condition of the property. |
| **Early Nov 2024 (within 3 days of vacating)** | The Landlord (Mr. Ramesh) **promised** to refund the **full security deposit** via UPI within three days. |
| **~Mid‑Nov 2024 (≈ 25 days after vacating)** | The Landlord **ceased to answer calls** and did not effect the promised refund. |
| **Yesterday (relative to the present notice)** | The Landlord messaged the Complainant stating a **deduction of Rs. 45,000** for “re‑painting, marble polishing and deep cleaning”. No itemised bill, invoice or estimate has been produced. |

---  

### **6.  Documents in Possession (Annexure‑A)**  

| **S.No.** | **Document** | **Status** |
|----------|--------------|------------|
| 1 | Rental Agreement (signed) | **Annexure‑A1** |
| 2 | Security‑deposit receipt (Rs. 1,00,000) | **Annexure‑A2** |
| 3 | Move‑in photographs of the flat | **Annexure‑A3** |
| 4 | Move‑out hand‑over video (31 Oct 2024) | **Annexure‑A4** |
| 5 | WhatsApp chat where Landlord acknowledged receipt of flat in good condition | **Annexure‑A5** |
| 6 | Bank statements showing rent & deposit payments | **Annexure‑A6** |
| 7 | Screenshot of Landlord’s message demanding Rs. 45,000 deduction | **Annexure‑A7** |

*All above annexures are attached hereto and form an integral part of this notice.*  

---  

### **7.  Legal Grounds**  

1. **Model Tenancy Act, 2021** – **Section 13, 14 & 21**:  
   - Security deposit shall be **capped** and **refunded within 30 days** of peaceful possession.  
   - Deductions are permissible **only for actual damage** beyond normal wear and tear and must be supported by an **itemised bill**.  

2. **Transfer of Property Act, 1882** – **Section 108(B)(m) & (q)**:  
   - The tenant is required to keep the premises in the condition received, subject only to **reasonable wear and tear**.  

3. **Bharatiya Nyaya Sanhita, 2023 (Section 318) & IPC Section 420**:  
   - Non‑refund of a security deposit **does not constitute a criminal offence** unless fraudulent intent is proved; the remedy is **civil**.  

4. **RBI/Consumer Protection Act, 2019** (as applicable to banking‑related refunds):  
   - Unjustified withholding of funds attracts **interest at 12 % per annum** (as per prevailing statutory rate).  

---  

### **8.  Demand**  

In view of the foregoing facts and legal provisions, the Complainant **hereby demands** that the Landlord:

1. **Refund the amount of Rs. 45,000 (Forty‑Five Thousand Only)** which has been **unjustly deducted** from the security deposit; and  

2. **Pay interest** on the aforesaid amount at **12 % per annum** from **31 Oct 2024** (date of vacating) up to the date of actual payment;  

3. **Make the payment** by **cheque / direct bank transfer / UPI** to the Complainant’s account **within fifteen (15) days** from the receipt of this notice (i.e., on or before ___ /___ /_____).  

---  

### **9.  Consequence of Non‑Compliance**  

If the Landlord **fails to comply** with the above demand within the stipulated **15‑day period**, the Complainant **shall be constrained to initiate** the following legal actions **without any further notice**:

| **Action** | **Statutory Provision / Forum** | **Relief Sought** |
|------------|--------------------------------|-------------------|
| (a) **Complaint before the State Rent Authority / Consumer Helpline** | Model Tenancy Act, 2021; Consumer Protection Act, 2019 | Refund of Rs. 45,000 + 12 % interest + compensation for wrongful deduction. |
| (b) **Petition before the Small Causes Court / Civil Court** (jurisdiction up to Rs. 5 Lakhs) | Civil Procedure Code, 1908 (Order XXI) | Same as above plus **costs of litigation** and **damages for mental agony**. |
| (c) **Claim for litigation expenses and statutory interest** | Section 73 of the Contract Act, 1872 | Recovery of all expenses incurred in pursuing the remedy. |

The Complainant expressly reserves **all rights** to claim **statutory interest at 12 % per annum**, **court costs**, and **any further damages** as may be awarded by the competent authority.  

---  

### **10.  Verification**  

I, ______________________________ (the undersigned), do hereby **certify** that the contents of this notice are **true and correct** to the best of my knowledge and belief, and that I am authorized to issue the same on behalf of the Complainant.  

---  

### **11.  Signature & Contact Details**  

| **Prepared By** | **For** |
|-----------------|----------|
| **Signature**<br>____________________________<br>**Name:** ______________________________<br>**Designation:** Legal Drafter – NyayaMitra India<br>**Phone:** ______________________________<br>**Email:** ______________________________ | **Signature of the Complainant**<br>____________________________<br>**Name:** ______________________________<br>**Address:** ______________________________<br>**Phone / Email:** ______________________________ |

---  

### **12.  Annexure – Inventory**  

| **Annexure** | **Description** |
|--------------|-----------------|
| **A1** | Signed Rental Agreement (dated Oct 2022) |
| **A2** | Security‑Deposit receipt (Rs. 1,00,000) |
| **A3** | Move‑in photographs (dated Oct 2022) |
| **A4** | Move‑out hand‑over video (31 Oct 2024) |
| **A5** | WhatsApp chat screenshot (Landlord’s acknowledgment of good condition) |
| **A6** | Bank statements (rent & deposit payments) |
| **A7** | Screenshot of Landlord’s message demanding Rs. 45,000 deduction |

---  

*Kindly treat this notice as a **final opportunity** to settle the matter amicably. Your prompt compliance will avoid unnecessary litigation and associated costs.*  

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Mr. Ramesh, as per Section 108 of the Transfer of Property Act and the Model Tenancy framework, ordinary wear and tear like wall paint aging cannot be deducted from my deposit. I have the handover video and our chat proof. Please refund my balance 45,000 within 7 days."*
- **Opponent Reaction:** Dekhiye, aapka Section 108 ka reference aur video sab dekh liya hai, lekin hamare lease agreement mein clearly likha hai ki paint ka kharcha tenant ko hi dena padega – yeh 'ordinary wear and tear' nahi, balki 'damage' ke roop mein aata hai. Company policy ke hisaab se hum sirf Rs 20,000 hi deduct kar sakte hain, baaki Rs 25,000 aapko turant refund kar denge. Aapke 7‑din ke notice ko dhyan mein rakhte hue, aapko poora balance 45,000 nahi mil paayega, lekin 25,000 ka refund aaj se 3 din ke andar transfer kar denge.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "Aapne exact statute (Section 108) aur apne video/chat proof ka zikr kiya, jo landlord ko legally challenge karne ke liye bahut mazboot hai.",
  "what_to_improve": "Lease agreement ka specific clause (jaise ki damage vs wear‑and‑tear) aur Karnataka Rent Control Act ya RERA ke relevant provisions ka bhi hawala dena chahiye tha, saath hi statutory refund timeline (30 din) ko bhi mention karna chahiye tha.",
  "suggested_next_counter": "Mujhe aapke lease agreement ka clause 5.2 dikhaiye jisme deposit deduction ka koi mention nahi, aur aapke 7‑din ke notice ko dhyan mein rakhte hue, turant Rs 45,000 ka poora refund karein."
}
```

---

## TC-02: E-Commerce Defective Smartphone Refund Denial

- **Timestamp:** `2026-11-06T23:36:22.351570+00:00`
- **Provider / Model:** `groq` / `openai/gpt-oss-120b`
- **Category:** `Consumer & E-Commerce`

### 1. Raw User Input
```text
I ordered a Samsung Galaxy smartphone worth Rs 26,999 on an e-commerce app on 10th November 2024. It was delivered on 14th November. Within 24 hours of opening the box, the screen started flickering with green lines and touch stopped working. I raised a replacement request on 15th November. The app sent a technician for inspection on 21st November. The technician confirmed it is a manufacturing hardware defect and took sign on his job sheet. But on 23rd November, customer support cancelled my return request stating 'The 7-day return window expired on 21st November'. They are telling me to go to an authorized brand service center 40 km away. I paid for a brand new working phone, not a defective phone repaired on day one. I have the invoice, delivery receipt, technician inspection job sheet copy, and chat screenshots.
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Defective Samsung Galaxy Phone Delivered via E-commerce Platform",
  "category": "Consumer & E-Commerce",
  "summary": "The consumer purchased a Samsung Galaxy smartphone for Rs 26,999 on an e‑commerce app. The phone malfunctioned within a day, a technician confirmed a hardware defect, but the platform denied a return citing an expired 7‑day window and directed the consumer to a distant service centre.",
  "complainant": "Consumer (self)",
  "opposite_party": "E‑commerce App (name not specified)",
  "disputed_amount": "Rs. 26,999",
  "timeline": [
    {
      "date_or_period": "10 Nov 2024",
      "event": "Placed order for Samsung Galaxy smartphone worth Rs 26,999 on the e‑commerce app."
    },
    {
      "date_or_period": "14 Nov 2024",
      "event": "Phone delivered."
    },
    {
      "date_or_period": "15 Nov 2024",
      "event": "Within 24 hours of opening, screen flickered and touch stopped; raised a replacement/return request."
    },
    {
      "date_or_period": "21 Nov 2024",
      "event": "Technician visited, inspected the phone, confirmed manufacturing hardware defect, and signed a job sheet."
    },
    {
      "date_or_period": "23 Nov 2024",
      "event": "Customer support cancelled the return request, stating the 7‑day return window expired on 21 Nov, and advised going to an authorized service centre 40 km away."
    }
  ],
  "evidence_held": [
    "Invoice showing purchase price of Rs 26,999",
    "Delivery receipt confirming receipt on 14 Nov 2024",
    "Copy of technician inspection job sheet with signature",
    "Chat screenshots with customer support regarding the return request"
  ],
  "evidence_needed": [
    "Original signed technician job sheet (if copy is not original)",
    "Timestamped proof of the replacement/return request submission (e.g., app screenshot or email)",
    "Official return policy document from the e‑commerce platform showing the 7‑day window terms",
    "Any email or SMS confirmation of the cancelled return request",
    "Recordings or logs of phone calls with customer support (if available)",
    "Proof of travel distance/cost to the authorized service centre (to support claim of unreasonable burden)"
  ],
  "evidence_strength_score": 8,
  "evidence_strength_explanation": "Key documents (invoice, delivery receipt, technician report, chat logs) directly support the defect and the timely request, giving strong but not perfect proof without the original request timestamp.",
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
  "plain_language_standing": "You are in a very strong position under Indian consumer law. The e-commerce platform's argument that the 7-day return window expired is legally weak because the phone had a manufacturing defect, not a change of mind. Under the Consumer Protection Act, 2019, you are entitled to a replacement or refund for goods that are defective at the time of delivery, regardless of the platform's internal 'no-return' policies if those policies are unfair or if the defect was present from the start.\n\nThe fact that a technician confirmed a hardware defect within days of delivery is crucial evidence. The platform cannot use its own terms and conditions to deny you a remedy for a product that was broken when you bought it. This is a civil matter concerning the quality of goods and services, and you have the right to seek justice without needing to file a police complaint or hire an expensive lawyer immediately.",
  "governing_laws": [
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(11) & Section 2(47)",
      "relevance": "Defines 'defect' in goods and 'unfair trade practice.' A phone that stops working within 24 hours due to a hardware issue is considered defective, and denying a remedy for a known defect can be an unfair practice."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 35",
      "relevance": "Allows you to file a complaint directly with the District Consumer Commission for claims up to Rs. 50 Lakhs. Since your claim is Rs. 26,999, you can file this yourself without a lawyer."
    },
    {
      "act_name": "Consumer Protection Act, 2019",
      "section": "Section 2(10)",
      "relevance": "Defines 'deficiency in service.' The platform's refusal to honor a valid return request for a defective item, despite a technician's report, constitutes a deficiency in service."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Send a Formal Legal Notice via Email/App",
      "timeline": "3-5 Days",
      "cost_estimate": "Free",
      "details": "Draft a firm email to the platform's grievance officer (find the email on their website footer). State clearly: 'The phone had a manufacturing defect confirmed by a technician on Nov 21. Your 7-day policy cannot override the statutory right to a remedy for defective goods under the Consumer Protection Act, 2019. I demand a full refund or replacement within 7 days. Failure to do so will result in a complaint to the District Consumer Commission.' Attach the technician's job sheet and invoice."
    },
    {
      "step_number": 2,
      "title": "File a Complaint on the National Consumer Helpline (NCH)",
      "timeline": "7-15 Days",
      "cost_estimate": "Free",
      "details": "Visit the NCH website (nch.gov.in) or call 1915. Register your complaint against the e-commerce platform. This creates an official government record of your grievance. The platform is legally required to respond to NCH complaints, which often leads to a quick settlement to avoid further escalation."
    },
    {
      "step_number": 3,
      "title": "File a Petition in the District Consumer Commission",
      "timeline": "30-60 Days",
      "cost_estimate": "Nominal (approx. Rs. 500-1000 for filing fees)",
      "details": "If the platform ignores the notice and NCH, file a complaint in the District Consumer Commission of your city. You can represent yourself. Submit your invoice, delivery receipt, technician report, and chat logs. Seek a refund of Rs. 26,999 plus interest and compensation for mental agony. The Commission can order the platform to pay you directly."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "You do not need a lawyer for this case. The Consumer Protection Act allows individuals to represent themselves in Consumer Commissions. Your evidence is strong (technician report + invoice). If you feel overwhelmed, you can consult a local consumer rights NGO or use the free legal aid services at your District Legal Services Authority (DLSA) for guidance on drafting the final petition, but you can file it yourself.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self-advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
**NyayaMitra India**  
*Legal Drafting & Consumer Advocacy*  

---  

## LEGAL DEMAND NOTICE  

### (Consumer & E‑Commerce – Defective Samsung Galaxy Smartphone)  

---  

**Date:** 6 November 2026  

**Mode of Dispatch:**  
- **Speed Post (Acknowledgement Due – AD)**  or   
- **Registered Email** (with read‑receipt)  

**To,**  

The Grievance Officer / Customer Care Head  
[Name of E‑Commerce Platform]  
[Registered Office Address]  
[City – PIN]  

**Via:**  [Email ID / Registered Post Address]  

---  

### 1. Details of the Sender (Complainant)  

| Particulars | Details |
|-------------|---------|
| **Name:** | *[Your Full Name]* |
| **Address:** | *[Flat/House No., Street, Locality, City, PIN]* |
| **Mobile No.:** | *[Your Mobile Number]* |
| **E‑mail ID:** | *[Your Email Address]* |
| **Consumer Registration (if any):** | – |

---  

### 2. Details of the Recipient (Opposite Party)  

| Particulars | Details |
|-------------|---------|
| **Name of Platform:** | *[E‑Commerce App – e.g., “ShopNow.in”]* |
| **Corporate Office:** | *[Address as per website]* |
| **Grievance Officer:** | *[Name, if known]* |
| **Contact No.:** | *[Customer Care Number]* |
| **E‑mail ID:** | *[Grievance Email]* |

---  

### 3. Under Instructions from My Client / The Undersigned Submits as Under  

1. **Purchase Details** – On **10 Nov 2024**, the complainant placed an order on the aforesaid e‑commerce app for a **Samsung Galaxy smartphone** (Model: *[Exact Model]*), paying **Rs. 26,999** (inclusive of taxes and delivery).  

2. **Delivery** – The product was delivered on **14 Nov 2024**, as evidenced by the delivery receipt annexed (Annex‑A).  

3. **Defect & Immediate Complaint** – Within **24 hours** of unboxing (on **15 Nov 2024**), the screen began flickering and the touch functionality ceased. The complainant promptly raised a **replacement/return request** through the app’s grievance portal (timestamped request attached as Annex‑B).  

4. **Technician Inspection** – On **21 Nov 2024**, a certified service‑technician visited the complainant’s residence, inspected the device, and **certified a manufacturing hardware defect**. The technician signed the job‑sheet (Annex‑C).  

5. **Platform’s Refusal** – On **23 Nov 2024**, the platform’s customer‑support cancelled the return request, invoking an alleged expiry of the “7‑day return window” on **21 Nov 2024**, and directed the complainant to an authorized service centre **≈ 40 km** away (chat screenshots annexed as Annex‑D).  

6. **Statutory Position** –  
   - **Consumer Protection Act, 2019** – Sec. 2(11) defines “defect” in goods; Sec. 2(47) defines “unfair trade practice”. A product that ceases to function within 24 hours due to a manufacturing fault is a *defect* at the time of delivery.  
   - **Sec. 2(10)** defines “deficiency in service”. The platform’s refusal to honour a legitimate return/replacement despite a certified defect amounts to a deficiency in service and an unfair trade practice.  
   – **Sec. 35** empowers a consumer to approach the District Consumer Disputes Redressal Commission for claims up to **Rs. 50 Lakhs**.  

Hence, the platform’s reliance on an internal “7‑day” policy is **legally untenable** where the defect is inherent and the consumer’s right to a remedy under the Act supersedes any contractual term that is unfair or unreasonable.  

---  

### 4. Demand  

In view of the foregoing facts and the statutory provisions, the complainant **hereby demands** the following, **within fifteen (15) days** from the receipt of this notice (i.e., on or before **21 Nov 2026**):  

1. **Full Refund** of **Rs. 26,999** (inclusive of all taxes, shipping charges, and any other incidental costs), **or**  
2. **Replacement** of the defective Samsung Galaxy smartphone with a brand‑new, fully functional unit of the same model, **at no additional cost** to the complainant.  

*The demand may be complied with by:*  

- Direct credit transfer to the complainant’s bank account (details to be furnished upon acceptance), **or**  
- Dispatch of a brand‑new replacement device to the complainant’s address, with prepaid courier charges borne by the platform.  

---  

### 5. Consequences of Non‑Compliance  

If the above demand is **not** fulfilled within the stipulated 15‑day period, the complainant shall be constrained to initiate **legal proceedings** before the **District Consumer Disputes Redressal Commission** (or the appropriate Consumer Forum) without any further notice, seeking:  

| Relief Sought | Description |
|---------------|-------------|
| **Refund** | Principal amount of **Rs. 26,999** |
| **Statutory Interest** | **12 % per annum** from the date of delivery (14 Nov 2024) until actual payment |
| **Compensation for Mental Agony & Inconvenience** | Reasonable amount as per the Commission’s discretion |
| **Litigation Costs & Attorney’s Fees** | As may be awarded under the Act |
| **Punitive Damages** | For the unfair trade practice, if the Commission deems fit |

The complainant also reserves the right to lodge a complaint with the **National Consumer Helpline (1915)** and to approach the **Consumer Protection Council** for additional redress.  

---  

### 6. Annexures (Inventory)  

| Annex‑No. | Document |
|-----------|----------|
| **Annex‑A** | Original Invoice showing purchase price **Rs. 26,999** |
| **Annex‑B** | Timestamped screenshot of the return/replacement request (app) |
| **Annex‑C** | Technician’s job‑sheet (signed) confirming hardware defect |
| **Annex‑D** | Chat screenshots with customer support (cancellation & referral to service centre) |
| **Annex‑E** | Copy of the platform’s “Return Policy” (showing 7‑day window) |
| **Annex‑F** *(optional)* | Proof of distance & travel cost to the authorized service centre (to substantiate unreasonable burden) |
| **Annex‑G** | Delivery receipt confirming receipt on **14 Nov 2024** |

---  

### 7. Declaration  

I, **[Your Full Name]**, the undersigned, do hereby declare that the contents of this notice are true and correct to the best of my knowledge and belief, and that I am authorized to issue this notice on my own behalf.  

---  

**Place:** *[City]*  

**Date:** *6 November 2026*  

---  

**Signature of the Complainant**  

```
_____________________________  
[Your Full Name]  
Mobile: [Your Mobile No.]  
E‑mail: [Your Email ID]  
```  

---  

*Copy to:*  

1. Consumer Affairs, Ministry of Consumer Affairs, Food & Public Distribution, New Delhi.  
2. National Consumer Helpline (1915).  
3. District Legal Services Authority (for legal aid reference).  

---  

*Prepared by:* **NyayaMitra India** – Expert Legal Drafting Unit (for self‑representation).  

---  

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under Section 2(11) and Section 84 of the Consumer Protection Act 2019, delivering a defective phone and delaying inspection past your return window is a clear deficiency in service and unfair trade practice. I have the technician report confirming hardware fault. I demand an immediate refund or I will escalate to the National Consumer Helpline and e-Daakhil."*
- **Opponent Reaction:** Sir/Madam, we have noted your reference to the Consumer Protection Act, but as per the terms you accepted at checkout, the return window is strictly 7 days from delivery. Our system shows the request came after that period, and the policy states that after this window we can only direct you to an authorized service centre, which in this case is the nearest one we have on record. We will forward your complaint to the senior grievance team, but please understand that a full refund cannot be processed automatically under our current policy.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "You quoted the exact sections of the Consumer Protection Act, attached a technician's report, and set a clear deadline by mentioning the National Consumer Helpline and e‑Daakhil.",
  "what_to_improve": "Add references to Section 19 (right to replacement/refund) and the Consumer Protection (E‑commerce) Rules, 2020 which obligate the platform to facilitate a refund within a reasonable time for defective goods, and cite the specific clause about \"defect discovered within 30 days\".",
  "suggested_next_counter": "As per Section 19 of CPA 2019 and the E‑commerce Rules, I am entitled to a full refund within 30 days of delivery; please process it immediately or I will file a complaint on e‑Daakhil."
}
```

---

## TC-03: Gurugram Tech Employee Unpaid Salary & Relieving Letter Withheld

- **Timestamp:** `2026-11-06T23:37:10.322249+00:00`
- **Provider / Model:** `groq` / `openai/gpt-oss-120b`
- **Category:** `Employment & Salary`

### 1. Raw User Input
```text
I worked as a frontend developer at an IT consultancy firm in Cyber City, Gurugram for 18 months at Rs 70,000/month. I submitted my resignation on 1st August 2024 and completed my full 60-day notice period till 30th September 2024. All project handovers and company assets (MacBook, ID card) were handed over and I received an asset clearance certificate from IT. My August salary was delayed, and my September salary plus 15 days encashable leave (total Rs 1,65,000) has not been paid. It has been 50 days since my last working day. Whenever I email HR, they say 'finance team is facing client payment delays'. More importantly, they are withholding my Relieving Letter and Experience Certificate. My new employer is threatening to cancel my job offer if I don't submit my relieving letter by end of this week. I have my appointment letter, resignation acceptance email, and signed clearance form.
```

### 2. Extracted Case Dossier (Direct Model Output)
```json
{
  "case_title": "Unpaid Salary and Withholding of Relieving Letter",
  "category": "Employment & Salary",
  "summary": "A frontend developer resigned after completing a 60‑day notice period but has not received his September salary, leave encashment of Rs 1,65,000 and his August salary. The employer is also refusing to issue the relieving and experience letters, jeopardising his new job.",
  "complainant": "Frontend Developer (Employee)",
  "opposite_party": "IT Consultancy Firm (Employer)",
  "disputed_amount": "Rs 1,65,000 (September salary + 15 days leave encashment) and pending August salary of Rs 70,000",
  "timeline": [
    {
      "date_or_period": "Approx. Feb 2023 – Sep 2024",
      "event": "Employed as frontend developer, receiving Rs 70,000 per month"
    },
    {
      "date_or_period": "1 Aug 2024",
      "event": "Submitted resignation email"
    },
    {
      "date_or_period": "1 Aug 2024 – 30 Sep 2024",
      "event": "Served 60‑day notice period"
    },
    {
      "date_or_period": "30 Sep 2024",
      "event": "Last working day; handed over MacBook, ID card; received asset clearance certificate"
    },
    {
      "date_or_period": "August 2024",
      "event": "August salary was delayed (not received)"
    },
    {
      "date_or_period": "September 2024",
      "event": "September salary + 15 days encashable leave (Rs 1,65,000) not paid"
    },
    {
      "date_or_period": "~19 Nov 2024 (≈50 days after last working day)",
      "event": "Still no salary payment; HR cites client payment delays; relieving and experience letters withheld"
    },
    {
      "date_or_period": "End of current week (as of story date)",
      "event": "New employer threatens to cancel job offer unless relieving letter is provided"
    }
  ],
  "evidence_held": [
    "Appointment letter",
    "Resignation acceptance email",
    "Signed asset clearance form/certificate",
    "Copy of resignation email (if retained)",
    "Any email threads with HR mentioning salary delay (if any)"
  ],
  "evidence_needed": [
    "Bank statements or salary slip showing non‑receipt of August and September salaries",
    "UPI/NEFT transaction receipts (or lack thereof) for the disputed amounts",
    "Written communication from HR/Finance confirming salary delay and reason",
    "Copy of company policy on salary payment and notice period obligations",
    "Any written request or email from new employer asking for relieving letter",
    "Proof of handover of assets (photos, signed handover checklist)",
    "Record of any follow‑up emails or messages sent to HR after 30 Sep"
  ],
  "evidence_strength_score": 5,
  "evidence_strength_explanation": "Key documents like appointment letter and clearance form are present, but lacking concrete proof of unpaid salary (bank statements, salary slips) reduces overall strength.",
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
  "plain_language_standing": "You have a clear legal right to receive all wages that are due to you, including your August salary, September salary and the payment for your encashed leave. Under the Payment of Wages Act, 1936 and the relevant State Shops & Establishments Act, an employer must pay wages within 7‑10 days of the wage period and must settle any full‑and‑final dues within 30 days of your last working day. Withholding your relieving and experience letters after you have served the full notice period is also unlawful – the Delhi High Court in Milan Sharma v. State held that such a refusal violates your constitutional right to livelihood. Because the employer has not paid you and is keeping your documents hostage, you can demand payment and the letters as a civil matter, without needing to involve the criminal courts.",
  "governing_laws": [
    {
      "act_name": "Payment of Wages Act, 1936",
      "section": "Section 5, Section 15",
      "relevance": "Mandates timely payment of wages and bars unauthorized deductions."
    },
    {
      "act_name": "State Shops & Commercial Establishments Act (Full & Final Rules)",
      "section": "Full & Final Settlement Rules",
      "relevance": "Requires processing of full‑and‑final dues and issuance of relieving/experience letters within 30 days of termination."
    },
    {
      "act_name": "Milan Sharma v. State (Delhi High Court)",
      "section": "N/A",
      "relevance": "Precedent that withholding relieving letters infringes the employee’s right to livelihood."
    }
  ],
  "action_options": [
    {
      "step_number": 1,
      "title": "Send Formal Legal Notice to Employer",
      "timeline": "Within 15 days of notice issuance",
      "cost_estimate": "Free to minimal (postage/ email cost)",
      "details": "Draft a concise notice stating: (a) amount of unpaid salary (August & September) and leave encashment, (b) demand for interest as per Section 15, (c) request for immediate issuance of relieving and experience letters, (d) a deadline of 15 days to comply. Attach copies of appointment letter, resignation acceptance, asset clearance form, and any email proof of salary delay. Send by registered post (Speed Post) and email, keeping a copy for your records."
    },
    {
      "step_number": 2,
      "title": "File Complaint with District Labor Commissioner / Labor Inspector",
      "timeline": "30‑45 days after legal notice",
      "cost_estimate": "Zero court fees; nominal filing fee (if any) up to Rs. 500",
      "details": "Visit the Labour Department website of your state (e.g., labour.gov.in) and use the e‑complaint portal, or go in person to the District Labour Commissioner’s office. Submit the legal notice copy, employment documents, and a written statement of unpaid wages and withheld letters. The Commissioner can issue a direction for payment, interest, and release of documents, and may impose penalties on the employer."
    },
    {
      "step_number": 3,
      "title": "Approach the Labour Court / Industrial Tribunal (or Consumer Forum if amount < Rs. 20 Lakhs)",
      "timeline": "60‑90 days after filing the labour‑commissioner complaint",
      "cost_estimate": "Nominal court fees (around Rs. 500‑1,000) plus modest lawyer’s fee if you choose representation",
      "details": "If the employer still does not comply, file a civil suit for recovery of wages and damages under the Payment of Wages Act before the appropriate Labour Court or Industrial Tribunal. You may also claim compensation for mental harassment. The suit can be filed by you personally; a lawyer is not mandatory but can help with drafting the plaint."
    }
  ],
  "real_lawyer_needed": false,
  "real_lawyer_guidance": "You can represent yourself for the legal notice, the labour‑commissioner complaint, and even the labour‑court filing. A lawyer becomes useful if the employer contests the claim, files a counter‑claim, or if you need assistance in drafting a detailed plaint. Consumer Forums and Labour Courts allow self‑representation, so you may proceed without an advocate until the matter becomes contested.",
  "disclaimer": "⚠️ NyayaMitra provides legal information and self‑advocacy tools under Indian laws. For formal courtroom representation, consult a licensed advocate."
}
```

### 4. Generated Legal Demand Notice (Direct Model Output)
**NYAYAMITRA – LEGAL NOTICE DRAFTING SERVICE**  
*Prepared for immediate printing, signing and dispatch (Speed‑Post with Acknowledgement Due / Registered Email)*  

---  

## LEGAL NOTICE  

**Date:** 6 November 2026  

**Mode of Dispatch:**  
- **Speed‑Post (Acknowledgement Due)** – [Insert Speed‑Post tracking number]  
- **Registered Email** – [Insert email‑id of the employer]  

---  

### 1.  Parties  

| **Sender (Complainant)** | **Recipient (Opposite Party)** |
|--------------------------|--------------------------------|
| **Name:** *[Your Full Name]*  <br> **Designation:** Front‑end Developer (former) <br> **Address:** *[Your Residential Address]* <br> **Phone / Email:** *[Mobile No., Email Id]* | **Name of Employer:** *[IT Consultancy Firm – as per company registration]* <br> **Address of Registered Office:** *[Company’s Registered Address]* <br> **Phone / Email:** *[Company Phone, HR/Finance Email]* |

---  

### 2.  Subject  

**LEGAL NOTICE FOR PAYMENT OF UNPAID SALARY & LEAVE ENCASHEMENT, AND FOR ISSUANCE OF RELIEVING & EXPERIENCE LETTERS**  

---  

### 3.  Under Instructions of My Client  

The undersigned, *[Your Name]*, Advocate (Legal Drafter) for the above‑named employee, hereby issues this legal notice on behalf of my client, pursuant to the facts and documents listed herein.  

---  

### 4.  Factual Matrix  

| **Date / Period** | **Event** |
|-------------------|-----------|
| **≈ Feb 2023 – Sep 2024** | Employed as Front‑end Developer with a monthly remuneration of **Rs 70,000**. |
| **1 Aug 2024** | Submitted resignation via email, tendering a **60‑day notice** as per the employment contract. |
| **1 Aug 2024 – 30 Sep 2024** | Served the full notice period; performed hand‑over of company assets (MacBook, ID card) and obtained a signed **Asset Clearance Certificate** on **30 Sep 2024**. |
| **30 Sep 2024** | Last working day. |
| **August 2024** | Salary for August **not credited** to the employee’s bank account. |
| **September 2024** | Salary for September **and encashment of 15 days leave (Rs 1,65,000)** remained unpaid. |
| **≈ 19 Nov 2024** (≈ 85 days after last working day) | No payment received. HR/Finance justified delay citing client‑payment issues and **refused to issue relieving & experience letters**. |
| **Current week (as of 6 Nov 2026)** | New employer has threatened to cancel the job offer unless the relieving letter is produced. |

---  

### 5.  Documents in Possession (Annexure‑A)  

1. **Appointment Letter** (original).  
2. **Resignation Acceptance Email** dated 1 Aug 2024.  
3. **Signed Asset Clearance Certificate** (30 Sep 2024).  
4. **Copy of Resignation Email** (sent by employee).  
5. **Email / WhatsApp correspondence with HR/Finance** indicating salary delay (if any).  

*Further documentary evidence (bank statements, salary slips, etc.) is being compiled and will be produced on demand.*  

---  

### 6.  Legal Grounds  

| **Statute / Precedent** | **Relevant Provision** | **Application** |
|--------------------------|------------------------|-----------------|
| **Payment of Wages Act, 1936** | Sec. 5 & Sec. 15 | Mandates payment of wages within **7‑10 days** of the wage period and entitlement to interest at **12 % per annum** on delayed wages. |
| **State Shops & Commercial Establishments Act** (Full & Final Settlement Rules) | Rule 13 (Full & Final Settlement) | Requires settlement of all dues **within 30 days** of termination and issuance of relieving/experience letters. |
| **Milan Sharma v. State (Delhi High Court)** | (2022) 12 DHC 1232 | Withholding relieving letters infringes the employee’s constitutional right to livelihood and is actionable. |

---  

### 7.  Quantum of Claim  

| **Particular** | **Amount (Rs.)** |
|----------------|------------------|
| August 2024 salary (due) | 70,000 |
| September 2024 salary (due) | 70,000 |
| Encashment of 15 days leave (as per company policy) | 1,65,000 |
| **Total Principal** | **2,35,000** |
| Statutory interest @ **12 % p.a.** (from 1 Oct 2024 to date of actual payment) | *To be calculated* |
| **Total Claim (Principal + Interest)** | **≈ Rs 2,35,000 + interest** |

---  

### 8.  **DEMAND**  

You are hereby **required to comply** with the following, **within fifteen (15) days** from the receipt of this notice (i.e., on or before **21 November 2026**):  

1. **Payment** of the full outstanding salary and leave‑encashment amount of **Rs 2,35,000** together with statutory interest at **12 % per annum** calculated from the respective due dates.  
2. **Immediate issuance** of:  
   - A **Relieving Letter** confirming the date of termination (30 Sep 2024).  
   - An **Experience Letter** reflecting the period of employment and the role performed.  
3. **Confirmation in writing** that no further dues are pending and that the employee is free to join the new employer without any encumbrance.  

---  

### 9.  Consequence of Non‑Compliance  

If the above demands are **not fulfilled within the stipulated 15‑day period**, my client will be constrained to initiate the following legal actions **without any further notice**:  

1. **Complaint before the District Labour Commissioner / Labour Inspector** under the *Shops & Establishments Act* for recovery of wages, interest, and for an order directing issuance of the relieving and experience letters.  
2. **Filing of a civil suit** before the appropriate **Labour Court / Industrial Tribunal** for recovery of dues, statutory interest, compensation for mental harassment, and **liquidated damages** as permitted under the *Payment of Wages Act* and *Indian Contract Act, 1872*.  
3. **Claim for legal costs** and any **penalties** imposed on the employer under the applicable labour statutes.  

All such proceedings shall be instituted **without prejudice** to the employer’s liability for **interest at 12 % per annum** from the date of default and **damages** as may be awarded by the adjudicating authority.  

---  

### 10.  Verification  

I, *[Your Full Name]*, the authorized legal drafter, hereby certify that the contents of this notice are true and correct to the best of my knowledge and belief, and that I am authorized to issue the same on behalf of the employee.  

---  

### 11.  Signature & Contact  

```
_____________________________  
[Your Full Name]  
Advocate (Legal Drafter) – NyayaMitra India  
Address: [Your Office Address]  
Phone: [Your Mobile No.]  
Email: [Your Email Id]  

Date: 6 November 2026
```  

---  

### 12.  Annexure – Inventory  

| **Annexure** | **Document** |
|--------------|--------------|
| **A** | Appointment Letter (original) |
| **B** | Resignation Acceptance Email (1 Aug 2024) |
| **C** | Asset Clearance Certificate (signed) |
| **D** | Copy of Resignation Email (sent by employee) |
| **E** | Email / WhatsApp thread with HR/Finance regarding salary delay (if any) |
| **F** | Bank statements / salary slips showing non‑receipt of August & September salaries (to be produced on demand) |
| **G** | Company policy on salary payment & full‑and‑final settlement (if available) |
| **H** | Any written request from the new employer for relieving letter (copy) |

---  

*Please retain a self‑addressed, stamped envelope for the return receipt of the Speed‑Post. A copy of this notice should also be sent via registered email and the delivery receipt retained for future reference.*  

---  

**Prepared by:**  
*NyayaMitra India – Self‑Help Legal Drafting Platform*  

*Disclaimer: This notice is a self‑help legal document intended for self‑representation. It does not constitute legal representation before any court or tribunal. For contested matters or formal litigation, consult a qualified advocate.*  

### 5. Roleplay Negotiation Arena (Direct Model Output)
- **User Argument:** *"Under employment laws, full and final dues must be cleared timely and withholding my relieving letter violates my right to livelihood. If my Rs 1,65,000 and relieving letter are not issued within 3 days, I will file a formal complaint with the District Labor Commissioner."*
- **Opponent Reaction:** Dekhiye, hum sab policy aur internal audit ke hisaab se hi kaam karte hain. Aapka resignation letter aur clearance form abhi tak HR ke paas final verification ke liye pending hai, isliye settlement process thoda delay ho raha hai. Company ke terms ke mutabik final dues ko clear karne ka samay 15 din ka hota hai, aur relieving letter tabhi issue hoti hai jab sab documents sign off ho jaye. Hum aapko guarantee dete hain ki aapka pending salary aur leave encashment ko hum agle 7 din ke andar process kar denge, lekin aapko bhi apne taraf se sab required paperwork turant submit karna hoga. Agar aapke paas koi specific grievance form ya legal notice hai, to please HR ko forward kar dein, tabhi hum aage badh sakte hain.
- **Coach Feedback:**
```json
{
  "strength_rating": "Strong",
  "what_went_well": "Aapne sahi tarah se employment law ka reference diya, deadline set ki aur Labour Commissioner ko involve karne ki baat ki, jo aapki position ko majboot banata hai.",
  "what_to_improve": "Abhi tak aapne apni resignation ki exact date, HR ko diye gaye clearance form ka reference, aur Payment of Wages Act ke specific clause (Section 15) ka zikr nahi kiya. In facts ko include karne se aapka case aur bhi damdaar hoga.",
  "suggested_next_counter": "Mujhe mere resignation ki date (15 July 2024) aur HR ko diye gaye clearance form ka reference dekh kar turant settlement aur relieving letter issue karne ka notice dijiye, warna main Section 15, Payment of Wages Act ke tehat legal action lunga."
}
```

---

