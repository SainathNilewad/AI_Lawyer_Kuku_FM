# NyayaMitra (न्यायमित्र) — AI Legal Companion Solution Document
**Candidate Name:** [Your Name] | **Roll No:** [Your Roll No] | **Branch:** [Your Branch]  
**Problem Statement:** Problem 2: Build an AI Lawyer | **Repository / App Link:** [Streamlit App / GitHub Link]

---

## 1. Problem Choice & Framing
### Why Problem 2?
Every year in India, millions of ordinary citizens abandon legitimate claims—unreturned rental security deposits (₹30,000–₹80,000), e-commerce refund refusals (₹5,000–₹40,000), and withheld salaries upon resignation (₹50,000–₹2,00,000). People give up because hiring an advocate feels cost-prohibitive (₹15,000+), legal drafting is intimidating, and the procedural paperwork seems overwhelming.

### The True Conversational Solution
Rather than a rigid, static web form or offline batch report generator, **NyayaMitra is designed as a genuine, empathetic Conversational AI Legal Partner**:
1. **Pan-India Multimodal Intake (Voice + Text across 11+ Languages):** Takes voice input via browser microphone (transcribed via Whisper Large v3 Turbo) or text across *Hindi (हिन्दी), Hinglish, Tamil (தமிழ்), Telugu (తెలుగు), Kannada (ಕನ್ನಡ), Bengali (বাংলা), Marathi (मराठी), Gujarati (ગુજરાતી), Malayalam (മലയാളം), Punjabi (ਪੰਜਾਬੀ), and English*.
2. **Empathetic Dialogue:** Listens to the user's messy story, extracts key facts organically, and reassures them.
3. **Live Case Intelligence Sidecar:** As the conversation progresses, a real-time side panel continuously updates the **Case Dossier, Chronological Timeline, and Evidence Strength Score (1–10)**.
4. **Actionable Outputs:** Generates a ready-to-serve 15-day **Formal Legal Demand Notice** and provides a **Dispute Practice Arena** where the user can roleplay against the opposing party.

### Scoping the Problem (Depth over Superficial Breadth)
We explicitly scope NyayaMitra to the top 3 everyday civil and consumer disputes in India:
* **Tenancy & Rental Disputes** (*Model Tenancy Act 2021, Transfer of Property Act Sec 108*)
* **Consumer & E-Commerce Disputes** (*Consumer Protection Act 2019, e-Daakhil*)
* **Employment & Full-and-Final Dues** (*Payment of Wages Act 1936, State Shops & Establishments Acts*)

---

## 2. Approach, Architecture & Real-World Scale

```
[Voice Microphone / Text (Hindi, Hinglish, English)]
                      │
                      ▼
┌──────────────────────────────────────────────┐
│  Ingestion & Whisper Transcription Engine    │
└─────────────────────┬────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────┐
│  Conversational Counselor & Case Builder     │ ──► [Escalation Filter] ──► [Critical? DLSA 15100]
└─────────────────────┬────────────────────────┘
                      │
       ┌──────────────┴──────────────┐
       ▼                             ▼
┌───────────────────────────┐ ┌──────────────────────────────────────┐
│ Live Case Intelligence    │ │ Conversational Dialogue & Rights     │
│ • Chronological Timeline  │ │ • Plain Language Rights              │
│ • Evidence Strength (1-10)│ │ • Grounded in CPA 2019, MTA, Wages   │
│ • 1-Click Legal Notice    │ │ • Roleplay Negotiation Practice      │
└───────────────────────────┘ └──────────────────────────────────────┘
```

### What We Gave to AI vs. What We Kept as Deterministic Rules
* **Kept as Code / Deterministic Rules:**
  - **Escalation Boundary Filter:** Regex and keyword checks for physical violence, arrest, bail, and matrimonial disputes. If triggered, the AI immediately flags a warning and connects the user to the *District Legal Services Authority (DLSA Helpline: 15100)*.
  - **Statute Retrieval (Closed RAG):** Direct retrieval from curated, verified statutory text (*Model Tenancy Act*, *Consumer Protection Act 2019*, *Payment of Wages Act*) to ensure zero hallucinations.
  - **Evidence Scoring:** Rule-based verification matrix cross-referencing documentary proof (bank statements, chat logs, job sheets).
* **Gave to AI (LLM):**
  - Parsing messy unstructured voice transcripts and Hinglish prose into chronological events.
  - Translating legal doctrine into compassionate, empowering advice.
  - Generating formal legal notices with structured prayer and demand clauses.
  - Dynamic opponent roleplay with tactical negotiation coaching.

### Economics & Token Cost at Scale
* **Voice Transcription (Whisper Large v3 Turbo):** ~$0.0004 per minute.
* **LLM Reasoning (Gemini 3.5 Flash / Groq Qwen):** ~2,400 tokens per full dispute intake ($\approx$ **< ₹0.10 / $0.0012**).
* Compared to a traditional advocate consultation (₹1,500–₹5,000), NyayaMitra achieves a **99.9% cost reduction**, running easily on standard free tiers.

---

## 3. Quality Checking & Hallucination Defense

### How Legal Models Hallucinate
Standard LLMs hallucinate in two dangerous ways:
1. **Inventing Fake Sections:** E.g., quoting *"IPC Section 73 for Breach of Contract"* (IPC 73 is solitary confinement; breach of contract is Contract Act Sec 73).
2. **Fabricating High Court Case Laws:** Manufacturing plausible-sounding bench citations that do not exist.

### NyayaMitra's 3-Layer Hallucination Defense
1. **Constrained Statutory Grounding (Closed RAG):** The Legal Advisor is bound to verified Indian enactments (*Model Tenancy Act, Consumer Protection Act 2019, Payment of Wages Act*).
2. **Negative Constraint System Prompts:** Agents are explicitly instructed: *"Never invent an Act or Section number. If a specific section is not confirmed in the verified context, state the legal principle in plain English without manufacturing a section."*
3. **Civil vs. Criminal Separation:** Prevents users from making frivolous criminal cheating (IPC 420 / BNS 318) threats for civil breaches, following Supreme Court precedent (*Dalip Kaur v. Jagnar Singh*).

---

## 4. The Prototype & Verification
* **Voice & Text Ingestion:** Tested on native microphone voice input in Hinglish and English.
* **Action Center:** Generates a ready-to-serve 15-day formal Legal Demand Notice with 1-click `.txt` download.
* **Practice Arena:** Tested live with counter-arguments against simulated landlords and customer support agents, receiving real-time coach feedback.

### Real Test Cases Executed (Saved in `test_cases/`):
1. **TC-01 (Tenancy):** Bengaluru landlord withholding ₹45,000 deposit for painting. *Applied Sec 108 TPA (wear & tear doctrine); notice drafted; landlord roleplay offered 66% refund.*
2. **TC-02 (Consumer):** E-commerce platform refusing refund on day-old defective smartphone (₹26,999). *Invoked CPA 2019 Sec 2(11) Deficiency in Service; roleplay escalated to senior operations manager.*
3. **TC-03 (Employment):** Gurugram IT firm withholding ₹1.65L salary and relieving letter for 50 days. *Grounded in Payment of Wages Act & Delhi HC Art. 21 livelihood precedent; notice drafted.*

---

## 5. Honest Limitations & Where the Solution Fails
* **State-Specific Rent Laws:** While the Model Tenancy Act provides national guidance, legacy rent control acts (e.g., Maharashtra Rent Control Act 1999) have localized procedural quirks.
* **Disputed Verbal Agreements:** When a user has zero written proof, rent agreement, or chat history, the AI can only recommend issuing an exploratory demand notice; it cannot manufacture proof.
* **Criminal Matters:** The AI will not assist in criminal bail, cross-examinations, or courtroom trials; it strictly enforces handoff to a human advocate.
