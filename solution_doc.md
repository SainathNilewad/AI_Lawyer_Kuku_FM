# NyayaMitra (न्यायमित्र) — AI Legal Companion Solution Document
**Candidate Name:** Sainath Nilewad | **Problem Statement:** Problem 2: Build an AI Lawyer  
**Repository Link:** https://github.com/SainathNilewad/AI_Lawyer_Kuku_FM

---

## 1. Problem Choice & Framing
### Why Everyday Disputes?
Every year in India, millions of citizens abandon legitimate claims—withheld rental security deposits (₹30,000–₹80,000), rejected e-commerce refunds (₹5,000–₹40,000), and unpaid wages upon resignation (₹50,000–₹2,00,000). People give up because formal legal consultation feels expensive, legal jargon is intimidating, and procedural steps are unclear.

### Conversational Design
Rather than a static web form, NyayaMitra provides a conversational intake workflow:
1. **Multilingual Intake (Voice + Text across 11 Languages):** Transcribes voice via Whisper Large v3 Turbo or accepts text in Hindi, Hinglish, Tamil, Telugu, Kannada, Bengali, Marathi, Gujarati, Malayalam, Punjabi, and English.
2. **Empathetic Dialogue & Fact Extraction:** Organizes unstructured explanations into a factual dossier with dates, monetary claims, and documentary proofs.
3. **Live Intelligence Sidecar:** Real-time side panel displaying the case timeline, evidence checklist, and statutory provisions.
4. **Actionable Outputs:** Generates a structured 15-day formal Legal Demand Notice and provides an interactive Dispute Practice Arena for mock negotiation.

### Scoped Civil Domains
To maintain legal integrity, NyayaMitra is explicitly restricted to three everyday civil domains:
- **Tenancy & Rental Disputes** (*Model Tenancy Act 2021, Transfer of Property Act Sec 108*)
- **Consumer & E-Commerce Disputes** (*Consumer Protection Act 2019*)
- **Employment & Wage Settlement** (*Code on Wages 2019*)

---

## 2. Architecture & Implementation

```
[Voice / Text (Hindi, Hinglish, English, Regional)]
                      │
                      ▼
┌──────────────────────────────────────────────┐
│       Whisper Voice / Text Intake            │
└─────────────────────┬────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────┐
│  CaseBuilder & Escalation Boundary Filter    │ ──► [Emergency/Violence? DLSA 15100]
└─────────────────────┬────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────┐
│   Closed Statutory Retrieval & Regex Guard   │ ──► [Out-of-Scope? Refusal Fallback]
└─────────────────────┬────────────────────────┘
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
┌─────────────────────────┐ ┌──────────────────────────────────────┐
│ Live Case Intelligence  │ │ Conversational Guidance & Action     │
│ • Chronological Timeline│ │ • Plain-language rights advice       │
│ • Evidence Checklist    │ │ • 15-Day Formal Legal Demand Notice  │
│ • Statutory Provisions  │ │ • Roleplay Opponent Practice Arena   │
└─────────────────────────┘ └──────────────────────────────────────┘
```

### Deterministic Code vs. LLM Responsibilities
- **Deterministic Code:**
  - **Advocate Escalation Filter:** Whole-word regex checks for violence, assault, murder, arrest, and bail. Immediately directs high-risk situations to the *District Legal Services Authority (DLSA Helpline: 15100)*.
  - **Closed Statutory Grounding:** Only provisions present in the curated local statutory database are supplied to the model.
  - **Regex Section Guard:** Scans generated text against allowed section citations and strips unverified sections with a visible warning `[unverified reference removed]`.
  - **Honest Out-of-Scope Refusal:** Unmatched domains (e.g., divorce, criminal defense, property partition) trigger an immediate refusal without guessing.
- **LLM Responsibilities:**
  - Parsing conversational descriptions into timeline events and monetary claims.
  - Explaining statutory rights in accessible, conversational language.
  - Formatting formal legal notices and simulating opposing party counter-arguments in the practice arena.

---

## 3. Hallucination Defense & Quality Verification
1. **No Invented Precedents:** Judicial case citations were intentionally eliminated from the database to prevent manufactured citations.
2. **Code-Level Section Guard:** Verifies every statutory section cited against a whitelist extracted from the local knowledge base.
3. **Repealed Statute Removal:** The repealed Payment of Wages Act, 1936 was replaced with the Code on Wages, 2019 (Sections 17(2), 17(4), 18(1), 18(3)).
4. **Automated Verification Suite (`verify_test_suite.py`):** Runs 14 benchmark test cases (10 core domain scenarios + 4 adversarial queries covering invented sections, repealed statutes, criminal threats, and out-of-scope topics), achieving 100% pass rate with zero unverified sections.

---

## 4. One Place the AI Tools Got It Wrong
<!-- PLACEHOLDER: To be filled by candidate based on real testing experience -->
[Placeholder: Describe a specific instance where LLM tools gave an incorrect legal answer, invented a section, or gave flawed advice, and how NyayaMitra's verification guardrails handled it.]

---

## 5. Honest Limitations
- **Model Law Enforceability:** The Model Tenancy Act, 2021 is a central model law; it only binds states that have formally enacted it. Local state rent control legislations govern non-adopting states.
- **State-Specific Employment Rules:** Timelines for full-and-final settlement under state Shops & Establishments Acts vary across jurisdictions.
- **Crude Regex Scanner:** The code-level section guard uses regular expressions. While effective against standard formats (e.g., "Section 17"), it does not recognize spelled-out numbers ("Section seventeen"), Roman numerals, or cross-act section mismatches.
- **Restricted Coverage (3 Topics Only):** Only tenancy, consumer disputes, and wage claims are supported. Family law, criminal defense, motor accidents, and corporate litigation are outside scope.
- **No Live Case-Law Search:** NyayaMitra does not search live court judgment databases or cite active bench precedents.
- **Static Knowledge Base:** The local statutory database is small, hand-curated, and marked with verification statuses (`needs_my_verification` / `verified`), source URLs, and verification dates.
- **Information Only:** NyayaMitra provides pre-litigation structuring and information; it is not a licensed advocate and cannot represent individuals in court.
