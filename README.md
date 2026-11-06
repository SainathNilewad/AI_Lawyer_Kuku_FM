# ⚖️ NyayaMitra (न्यायमित्र) — AI Legal Partner for Everyday India

[![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-FF4B4B.svg)](https://streamlit.io)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![Gemini](https://img.shields.io/badge/Gemini-3.5%20Flash%20Lite-4285F4.svg)](https://deepmind.google/technologies/gemini/)
[![Groq](https://img.shields.io/badge/Groq-Whisper%20%2B%20Qwen-F55036.svg)](https://groq.com/)

> **Problem 2: Build an AI Lawyer**  
> *A genuine conversational AI that takes an ordinary person's legal dispute by voice or text, in the language they are comfortable with, and helps them act on it.*

---

## 🌟 What Makes NyayaMitra Conversational?

Instead of a rigid static form or batch report generator, **NyayaMitra** acts like a real legal counselor you can talk to directly:

1. **🎙️ Pan-India Multilingual (Voice & Text):**
   - Speak directly into your microphone or type in **11+ Indian languages**:
     - *Hindi (हिन्दी), Hinglish, Tamil (தமிழ்), Telugu (తెలుగు), Kannada (ಕನ್ನಡ), Bengali (বাংলা), Marathi (मराठी), Gujarati (ગુજરાતી), Malayalam (മലയാളം), Punjabi (ਪੰਜਾਬੀ), and English*.
   - Transcribed in real-time using Groq's high-speed **Whisper Large v3 Turbo** engine.
   - The AI responds authentically in your chosen mother tongue with culturally reassuring legal counsel.
2. **💬 Empathetic Legal Dialogue:**
   - The AI converses back in plain, accessible language without courtroom Latin jargon.
   - Gathers facts naturally and reassures the citizen about their rights.
3. **📊 Live Case Intelligence Sidecar:**
   - As you talk, a real-time side panel continuously updates your **Chronological Timeline**, **Case Dossier**, and **Evidence Strength Meter (1–10)**.
4. **📝 Instant Legal Notice Generator:**
   - With a single click, drafts a formal, ready-to-serve **15-Day Legal Demand Notice** or **Consumer Court (e-Daakhil) Complaint** with `.txt` download.
5. **🥊 Opponent Practice Arena (Roleplay):**
   - Toggle into roleplay mode right inside the chat! The AI plays the stubborn landlord or HR manager, lets you practice your arguments, and provides immediate **Coach Feedback** (rating, what worked, and a suggested counter-punch).

---

## 🛡️ Anti-Hallucination Guardrails

AI models frequently invent fake laws and sections. NyayaMitra avoids this through a **3-Layer Defense**:

1. **Closed Grounding Database (`legal_kb.py`):**
   - *Model Tenancy Act, 2021 & Transfer of Property Act Sec 108* (wear-and-tear protection).
   - *Consumer Protection Act, 2019 (Sections 2(7), 2(11), 35, 84 & e-Daakhil)*.
   - *Payment of Wages Act, 1936 & State Shops & Commercial Establishments Acts*.
2. **Negative Constraint Instructions:**
   - Strictly bars the LLM from manufacturing section numbers or citing unverified court judgments.
3. **Civil vs. Criminal Separation:**
   - Enforces Supreme Court precedent (*Dalip Kaur v. Jagnar Singh*): monetary/deposit breaches are civil matters, not criminal cheating (IPC 420 / BNS 318).
4. **Advocate Escalation Trigger:**
   - Automatically detects criminal offenses, bail, domestic violence, or high-value litigation (> ₹50 Lakhs) and routes the user to the **District Legal Services Authority (DLSA Helpline: 15100)**.

---

## 🚀 Quickstart Guide

### 1. Navigate to Project
```bash
cd "D:\Project\AI Lawyer"
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Conversational App
```bash
streamlit run app.py
```
Open **`http://localhost:8501`** in your browser.

---

## 📂 Repository Structure

```
D:\Project\AI Lawyer\
├── app.py                            # Conversational UI with Voice input & Live Intelligence Sidecar
├── legal_kb.py                       # Grounded Indian statutory knowledge base & escalation filter
├── agents.py                         # Specialized agents (CaseBuilder, RightsAdvisor, Drafter, Roleplay)
├── llm_engine.py                     # Model Engine supporting Gemini (3.5 Flash Lite) & Groq (Whisper + Qwen)
├── .env                              # Safe local storage for GEMINI_API_KEY and GROQ_API_KEY
├── .gitignore                        # Protects .env from git commits
├── requirements.txt                  # Minimal dependencies (streamlit, google-genai, groq, python-dotenv)
├── solution_doc.md                   # 2-Page Executive Solution Document
└── test_cases/                       # Unedited raw test case outputs
    ├── raw_outputs_report.md         # Full Markdown compilation of all raw test runs
    ├── tc_01_tenancy.json            # Bengaluru Landlord Deposit Dispute
    ├── tc_02_consumer.json           # Defective Smartphone Refund Denial
    └── tc_03_employment.json         # Unpaid Resignation Salary & Relieving Letter
```
