# ⚖️ NyayaMitra (न्यायमित्र) — AI Legal Companion for Everyday India

> **Problem 2: Build an AI Lawyer**  
> *A conversational AI that takes an ordinary person's legal dispute by voice or text, in the language they are comfortable with, and helps them act on it.*

---

## 🌟 What Makes NyayaMitra Conversational?

Instead of a rigid static form or batch report generator, **NyayaMitra** acts like an empathetic legal companion:

1. **🎙️ Pan-India Multilingual (Voice & Text):**
   - Speak directly into your microphone or type in **11 Indian languages**:
     - *Hindi (हिन्दी), Hinglish, Tamil (தமிழ்), Telugu (తెలుగు), Kannada (ಕನ್ನಡ), Bengali (বাংলা), Marathi (मराठी), Gujarati (ગુજરાતી), Malayalam (മലയാളം), Punjabi (ਪੰਜਾਬੀ), and English*.
   - Voice audio is transcribed using Groq's **Whisper Large v3 Turbo** engine.
2. **💬 Empathetic Legal Dialogue & Fact Intake:**
   - Listens to unstructured narratives, extracts chronological facts, and organizes claims.
3. **📊 Live Case Intelligence Sidecar:**
   - Real-time side panel continuously tracking your **Chronological Timeline**, **Case Dossier**, and **Documentary Proofs**.
4. **📝 15-Day Formal Legal Notice Generator:**
   - Drafts a ready-to-serve **15-Day Legal Demand Notice** or consumer complaint with 1-click `.txt` download.
5. **🥊 Opponent Practice Arena (Roleplay):**
   - Practice negotiating against a simulated opposing party with instant coach feedback (strength rating, critique, and counter-tactics).

---

## 🛡️ Anti-Hallucination Guardrails & Statutory Grounding

NyayaMitra strictly enforces that models never invent laws or court judgments:

1. **Closed Statutory Grounding (`legal_kb.py`):**
   - Grounded strictly in curated, verified Indian enactments:
     - *Model Tenancy Act, 2021 & Transfer of Property Act Sec 108*
     - *Consumer Protection Act, 2019*
     - *Code on Wages, 2019 (Sections 17(2), 17(4), 18(1), 18(3))*
   - Precedents were removed from the local knowledge base to eliminate fabricated court citations.
2. **Code-Level Section Guard:**
   - Deterministic regex engine that scans generated outputs for statutory section references and automatically strips unverified sections with a visible `[unverified reference removed]` flag.
3. **Advocate Escalation Filter:**
   - Whole-word regex checks immediately route criminal violence, assault, threats, and bodily harm to the **District Legal Services Authority (DLSA Helpline: 15100)**.
4. **Honest Out-of-Scope Fallback:**
   - Queries outside the 3 supported civil domains (such as divorce, child custody, property partition, or criminal defense) are refused honestly without guessing.

---

## ⚠️ Honest Limitations

- **Only 3 Core Topics:** Scoped exclusively to Tenancy, Consumer Disputes, and Wage Settlement. All other legal matters are outside scope.
- **Model Law Caveat:** The Model Tenancy Act, 2021 is a central model law binding only states that have formally adopted it. State-level rent control acts govern elsewhere.
- **State Employment Rules:** Timelines for full-and-final settlement under state Shops & Establishments Acts vary across states.
- **Crude Regex Scanner:** The section scanner uses regular expressions. It catches standard citations (e.g., "Section 17"), but does not parse spelled-out numbers, Roman numerals, or cross-act mismatches.
- **No Live Case-Law Search:** NyayaMitra does not query live case databases.
- **Small Hand-Checked Knowledge Base:** The statutory context is small and hand-checked with explicit `needs_my_verification` / `verified` statuses and source URLs.
- **Legal Information Only:** NyayaMitra provides informational guidance and pre-litigation structuring; it is not a licensed lawyer and cannot represent parties in court.

---

## 🧪 Verification & Benchmark Suite

NyayaMitra includes an automated benchmark suite (`verify_test_suite.py`) testing 14 distinct scenarios:
- **10 Core Civil Scenarios:** Spanning residential tenancy, consumer defects, and wage claims.
- **4 Adversarial Cases:**
  1. *Invented Section Injection (Section 999A)* -> Detected and sanitized by regex guard.
  2. *Repealed Statute Query (Payment of Wages Act 1936)* -> Correctly grounded in Code on Wages 2019.
  3. *Criminal Violence Threat* -> Escalation triggered to DLSA 15100.
  4. *Out-of-Scope Civil Query (Divorce / Custody)* -> Refused without guessing.

To run the verification suite:
```bash
python verify_test_suite.py
```

---

## 🚀 Quickstart Guide

### 1. Clone & Install Dependencies
```bash
git clone https://github.com/SainathNilewad/AI_Lawyer_Kuku_FM.git
cd AI_Lawyer_Kuku_FM
pip install -r requirements.txt
```

### 2. Configure Environment (`.env`)
Create a `.env` file with your API keys:
```env
GROQ_API_KEY=your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
LLM_PROVIDER=groq
GROQ_MODEL=openai/gpt-oss-120b
GEMINI_MODEL=gemini-3.5-flash
```

### 3. Run the Conversational App
```bash
streamlit run app.py
```
Open **`http://localhost:8501`** in your browser.

---

## 📂 Repository Structure

```
├── app.py                            # Conversational UI with Voice input & Live Intelligence Sidecar
├── legal_kb.py                       # Grounded statutory knowledge base, section whitelist & guard
├── agents.py                         # Modular agents (CaseBuilder, RightsAdvisor, Drafter, Roleplay)
├── llm_engine.py                     # Provider engine (Groq & Gemini) with model listing & error handling
├── verify_test_suite.py              # Automated 14-scenario benchmark & adversarial test runner
├── .env                              # API key configuration
├── .gitignore                        # Protects .env from git commits
├── requirements.txt                  # Minimal dependencies
├── solution_doc.md                   # 2-Page Executive Solution Document
├── solution_doc.html                 # Print-ready HTML version of solution document
└── test_cases/
    ├── benchmark_test_cases.json     # 14 benchmark & adversarial test cases
    ├── raw_outputs_report.md         # Full Markdown report of live model outputs
    ├── tc_01_tenancy.json            # Tenancy live output dossier
    ├── tc_02_consumer.json           # Consumer live output dossier
    └── tc_03_employment.json         # Employment live output dossier
```
