# NyayaMitra (न्यायमित्र) — AI Legal Companion Solution Document
**Problem Statement:** Problem 2: Build an AI Lawyer  

---

## 1. Problem Choice & Framing
### Why Everyday Disputes?
Every year in India, millions of citizens abandon legitimate claims—withheld rental security deposits (₹30,000–₹80,000), rejected e-commerce refunds (₹5,000–₹40,000), and unpaid wages upon resignation (₹50,000–₹2,00,000). People give up because formal legal consultation feels expensive, legal jargon is intimidating, and procedural steps are unclear.

### Conversational Design
Rather than a static web form, NyayaMitra provides a conversational intake workflow:
1. **Multilingual Intake (Voice + Text across 11 Languages):** Transcribes voice via Whisper Large v3 Turbo or accepts text in Hindi, Hinglish, Tamil, Telugu, Kannada, Bengali, Marathi, Gujarati, Malayalam, Punjabi, and English.
2. **Empathetic Dialogue & Fact Extraction:** Organizes unstructured explanations into a factual dossier with dates, monetary claims, and documentary proofs.
3. **Live Intelligence Sidecar:** Real-time side panel displaying the case timeline, evidence checklist, and statutory provisions.
4. **Actionable Outputs:** Generates a structured 15-day formal Legal Demand Notice (established pre-litigation practice to establish a clear paper trail, not a statutory mandate) and provides an interactive Dispute Practice Arena for mock negotiation.

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
1. **No Invented Precedents:** Judicial case citations were intentionally eliminated from the database to prevent manufactured citations. In addition, an upstream regex intercept catches any prompt soliciting court precedents (e.g., "which Supreme Court case") and serves a deterministic refusal directing users to DLSA (15100).
2. **Code-Level Section & Act Guard:** Verifies every statutory section cited against a whitelist extracted exclusively from verified entries in the local knowledge base, and bans repealed/unverified Act names (Payment of Wages Act, Minimum Wages Act, Payment of Bonus Act, Equal Remuneration Act, Indian Penal Code, IPC, CrPC) replacing them with `[unverified reference removed]`.
3. **Repealed Statute Removal & Triggered Relevance:** The repealed Payment of Wages Act, 1936 was replaced with the Code on Wages, 2019. Furthermore, specific sections are gated behind trigger words: Section 18 (deductions) is only injected if deduction/fine keywords appear, preventing the model from hallucinating Section 18 in simple withheld-salary disputes.
4. **Automated Verification Suite (`verify_test_suite.py`):** Runs 28 benchmark test cases (10 core civil scenarios + 18 adversarial queries covering invented sections, repealed statutes, criminal threats, maintenance disambiguation, case-law interception, date integrity, provision relevance, and notice facts), achieving a pass count of **28/28 passed (0 failed)**, logged verbatim to `test_cases/verification_run.txt`.
   - **Evaluated Model:** Google Gemini 3.5 Flash Lite (`gemini-3.5-flash-lite`, free tier) for statutory reasoning; Groq for Whisper Large v3 Turbo voice transcription.
   - **Execution Metrics:** 28/28 passed (0 failed) across 42 LLM calls to `gemini-3.5-flash-lite` (0 fallback calls, 0 quota errors) under `EVAL_STRICT=1` with 12 req/min rate throttling.
   - **What the Suite Measures:** (a) Code-level section and banned Act guards, (b) Immediate advocate escalation triggers, (c) Honest out-of-scope refusal, (d) Upstream precedent interception, and (e) Fact and provision relevance.
   - **Note on Answer Correctness:** Full answer correctness was checked only on cases where the user filled in `expected_answer_verified_by_me`.
   - **Raw Model Output Reduction:** Across raw model outputs (TC-01 to TC-03), unverified section references were reduced from before fix: 7 unverified sections (2 in TC-01, 0 in TC-02, 5 in TC-03) to after fix: 0 unverified sections, and all banned Act citations were successfully intercepted.

---

## 4. One Place the AI Tools Got It Wrong
During initial testing with unconstrained frontier models on our employment wage-recovery scenario (TC-03), the LLM exhibited three critical legal hallucinations:
1. **Hallucinating Repealed Legislation & Phantom Sections:** It cited the repealed *Payment of Wages Act, 1936* (specifically Sections 5 and 15), advising the employee to approach the Payment of Wages Authority with a 12-month limitation period that does not apply under contemporary central labor codes.
2. **Statutory Distortion (Section 18 Mischaracterization):** When prompted with the modern *Code on Wages, 2019*, the model cited Section 18(3) and erroneously claimed that *"Section 18 prohibits employers from withholding wages"*. In reality, Section 18 strictly governs *permissible deductions* (fines, absence from duty, damage to goods) and caps total deductions at 50% of wages; it does not govern the withholding of full-and-final settlement upon resignation (which is covered under Section 17(2)).
3. **Manufactured Judicial Precedents:** When asked for precedent awarding interest on delayed wages, the model hallucinated fake Supreme Court citations (e.g., `(2000) 4 SCC 68`). Similarly, in a tenancy deposit scenario (TC-01), the model inappropriately cited criminal cheating provisions (Section 420 IPC / Section 318 BNS) for a purely contractual civil dispute.

**How NyayaMitra Solved It:**
- Replaced open-ended RAG with a hand-verified, closed statutory knowledge base (`legal_kb.py`).
- Implemented **Provision-Relevance Gating** (`filter_employment_entry`): Section 18 is completely withheld from prompts unless the user explicitly mentions deductions, fines, or pay cuts.
- Implemented **Deterministic Upstream Interception**: Case-law requests and criminal violence triggers bypass the LLM entirely, returning verified guidance and helpline 15100.
- Implemented a post-generation **Regex Section Whitelist Guard** that strips unverified section numbers and banned acts automatically.

---

## 5. Honest Limitations
- **Model Law Enforceability:** The Model Tenancy Act, 2021 is a central model law; it only binds states that have formally enacted it. Local state rent control legislations govern non-adopting states.
- **State-Specific Employment Rules:** Timelines for full-and-final settlement under state Shops & Establishments Acts vary across jurisdictions.
- **Crude Regex Scanner:** The code-level section guard uses regular expressions. While effective against standard formats (e.g., "Section 17"), it does not recognize spelled-out numbers ("Section seventeen"), Roman numerals, or cross-act section mismatches.
- **Restricted Coverage (3 Topics Only):** Only tenancy, consumer disputes, and wage claims are supported. Family law, criminal defense, motor accidents, and corporate litigation are outside scope.
- **No Live Case-Law Search:** NyayaMitra does not search live court judgment databases or cite active bench precedents.
- **Static Knowledge Base:** The local statutory database is small, hand-curated, and marked with verification statuses (`needs_my_verification` / `verified`), source URLs, and verification dates.
- **Information Only:** NyayaMitra provides pre-litigation structuring and information; it is not a licensed advocate and cannot represent individuals in court.
