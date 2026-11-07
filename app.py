"""
app.py - NyayaMitra: Real Conversational AI Lawyer for Everyday India
Supports:
1. Voice (Microphone via st.audio_input + Groq Whisper Large v3 Turbo)
2. Text Chat (Natural conversation in English, Hindi, or Hinglish)
3. Live Factual Case Dossier & Evidence Strength Tracker (updates dynamically)
4. Verified Statutory Grounding (No Hallucinations)
5. Instant Legal Notice Generator (15-Day formal notice)
6. Interactive Opponent Practice Arena (Roleplay negotiation)
"""

import streamlit as st
import os
import json
import io
from dotenv import load_dotenv

load_dotenv()

from legal_kb import retrieve_verified_legal_context, check_immediate_advocate_escalation
from llm_engine import LegalLLMEngine, list_groq_models, list_gemini_models
from agents import CaseBuilderAgent, RightsAdvisorAgent, DocumentDrafterAgent, RoleplayOpponentAgent, ConversationalCounselorAgent

st.set_page_config(
    page_title="NyayaMitra - Conversational AI Lawyer",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .chat-header {
        font-size: 2.1rem;
        font-weight: 800;
        color: #1a237e;
        margin-bottom: 2px;
    }
    .chat-sub {
        font-size: 1.05rem;
        color: #455a64;
        margin-bottom: 16px;
    }
    .side-card {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 14px;
        border-left: 4px solid #1a237e;
        margin-bottom: 12px;
    }
    .voice-box {
        background-color: #e8eaf6;
        border-radius: 8px;
        padding: 10px 14px;
        margin-bottom: 12px;
        border: 1px dashed #3f51b5;
    }
    .badge-statute {
        background-color: #e8f5e9;
        color: #2e7d32;
        padding: 3px 8px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# Supported Pan-India Languages & ISO Codes for Whisper
INDIAN_LANGUAGES = {
    "Auto-Detect / English": None,
    "Hindi (हिन्दी)": "hi",
    "Hinglish (Hindi in Roman script)": "hi",
    "Tamil (தமிழ்)": "ta",
    "Telugu (తెలుగు)": "te",
    "Kannada (ಕನ್ನಡ)": "kn",
    "Bengali (বাংলা)": "bn",
    "Marathi (मराठी)": "mr",
    "Gujarati (ગુજરાતી)": "gu",
    "Malayalam (മലയാളം)": "ml",
    "Punjabi (ਪੰਜਾਬੀ)": "pa",
}

# Helper: Transcribe Voice via Groq Whisper with Language Support
def transcribe_audio_file(audio_bytes, api_key: str, lang_code: str = None) -> str:
    try:
        from groq import Groq
        client = Groq(api_key=api_key)
        kwargs = {
            "file": ("voice_input.wav", audio_bytes),
            "model": "whisper-large-v3-turbo",
            "prompt": "Indian legal dispute conversation in Hindi, English, Tamil, Telugu, Kannada, Bengali, Marathi, Gujarati, Malayalam, Punjabi, or Hinglish",
        }
        if lang_code:
            kwargs["language"] = lang_code
        transcription = client.audio.transcriptions.create(**kwargs)
        return transcription.text.strip()
    except Exception as e:
        return f"[Voice Transcription Error: {e}]"

# Initialize Session State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "assistant",
            "content": (
                "**Namaste! I am your AI Legal Partner (NyayaMitra).**\n\n"
                "I am here to help you resolve everyday legal problems in India—like **a landlord withholding your security deposit**, "
                "**an e-commerce app refusing a refund for a broken product**, or **unpaid salary / withheld relieving letters** after resignation.\n\n"
                "🎙️ **Speak into your microphone** or 💬 **type your problem below** in your own words (English, Hindi, or Hinglish). Tell me what happened!"
            )
        }
    ]

if "case_dossier" not in st.session_state:
    st.session_state.case_dossier = None
if "rights_advice" not in st.session_state:
    st.session_state.rights_advice = None
if "notice_draft" not in st.session_state:
    st.session_state.notice_draft = None
if "practice_mode" not in st.session_state:
    st.session_state.practice_mode = False
if "practice_history" not in st.session_state:
    st.session_state.practice_history = []

@st.cache_data(ttl=3600)
def get_cached_groq_models(key: str):
    try:
        return [m for m in list_groq_models(key) if "whisper" not in m and "guard" not in m]
    except Exception:
        return []

@st.cache_data(ttl=3600)
def get_cached_gemini_models(key: str):
    try:
        models = list_gemini_models(key)
        return [m.replace("models/", "") for m in models if "embedding" not in m and "image" not in m and "preview" not in m]
    except Exception:
        return []

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3253/3253105.png", width=56)
    st.title("NyayaMitra AI")
    st.caption("Conversational Legal Partner for India")
    
    st.markdown("---")
    st.subheader("⚙️ Intelligence Settings")

    env_prov = os.getenv("LLM_PROVIDER", "groq").lower()
    default_p_idx = 0 if env_prov == "groq" else 1
    provider_choice = st.selectbox("LLM Provider:", ["Groq", "Gemini"], index=default_p_idx)
    prov_code = provider_choice.lower()

    groq_key = os.getenv("GROQ_API_KEY", "")
    gemini_key = os.getenv("GEMINI_API_KEY", "") or os.getenv("GOOGLE_API_KEY", "")
    active_key = groq_key if prov_code == "groq" else gemini_key

    if prov_code == "groq":
        default_model = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
        groq_models = get_cached_groq_models(groq_key) if groq_key else []
        if groq_models:
            m_idx = groq_models.index(default_model) if default_model in groq_models else 0
            model_name = st.selectbox("Model:", groq_models, index=m_idx)
        else:
            model_name = st.text_input("Model:", value=default_model)
    else:
        default_model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")
        gemini_models = get_cached_gemini_models(gemini_key) if gemini_key else []
        if gemini_models:
            m_idx = gemini_models.index(default_model) if default_model in gemini_models else 0
            model_name = st.selectbox("Model:", gemini_models, index=m_idx)
        else:
            model_name = st.text_input("Model:", value=default_model)

    if active_key:
        st.success(f"✅ {provider_choice} Connected ({model_name})")
    else:
        st.error(f"❌ {provider_choice} API Key missing in .env")

    if groq_key:
        st.success("🎙️ Voice Transcription (Whisper) Ready")

    st.markdown("---")
    st.subheader("🌐 Pan-India Language")
    selected_lang = st.selectbox("Preferred Language:", list(INDIAN_LANGUAGES.keys()))
    whisper_code = INDIAN_LANGUAGES[selected_lang]

    st.markdown("---")
    st.subheader("⚡ Quick Try Scenarios")
    demo_case = st.selectbox(
        "Load a sample scenario:",
        [
            "-- Free Conversation --",
            "Bengaluru Landlord ₹45k Deposit Withheld",
            "Defective Smartphone ₹26,999 Refund Refusal",
            "Gurugram Tech Employee ₹1.65L Salary Withheld"
        ]
    )

    DEMO_QUERIES = {
        "Bengaluru Landlord ₹45k Deposit Withheld": (
            "Mera landlord deposit return nahi kar raha. I was renting a flat in HSR Layout Bangalore. "
            "I gave 1 lakh deposit, vacated on 31st Oct after 1 month notice. Handed over keys with video proof. "
            "Now he deducted 45,000 saying painting and cleaning charges. Walls only had normal nail marks. How do I get my money back?"
        ),
        "Defective Smartphone ₹26,999 Refund Refusal": (
            "I ordered a phone for Rs 26,999 on Flipkart. The screen stopped working within 24 hours. "
            "I raised replacement immediately, but their technician took 6 days to visit. Technician signed job sheet confirming hardware defect, "
            "but customer care cancelled return saying 7-day return policy expired! They are refusing refund."
        ),
        "Gurugram Tech Employee ₹1.65L Salary Withheld": (
            "I resigned from my software job in Cyber City Gurugram. Completed full 60 days notice period and handed over company laptop on 30 Sept. "
            "It has been 50 days, company has not paid my September salary and leave encashment (total 1.65 Lakhs), and they are withholding my Relieving Letter. "
            "HR says client payment delay, but my new company will cancel my offer if I don't give relieving letter."
        )
    }

    if demo_case in DEMO_QUERIES:
        if st.button("📥 Insert into Chat"):
            st.session_state.pending_user_text = DEMO_QUERIES[demo_case]
            st.rerun()

    st.markdown("---")
    if st.button("🔄 Reset Conversation"):
        st.session_state.chat_history = [st.session_state.chat_history[0]]
        st.session_state.case_dossier = None
        st.session_state.rights_advice = None
        st.session_state.notice_draft = None
        st.session_state.practice_mode = False
        st.session_state.practice_history = []
        st.rerun()

# Layout: 2 Columns (Main Chat Column 65%, Live Intelligence Sidecar 35%)
col_chat, col_side = st.columns([65, 35], gap="large")

with col_chat:
    st.markdown("<h1 class='chat-header'>⚖️ NyayaMitra AI Lawyer</h1>", unsafe_allow_html=True)
    st.markdown("<p class='chat-sub'>Talk by voice or text. Get plain-language advice, verified laws, legal notices, and practice your arguments.</p>", unsafe_allow_html=True)

    # Voice Input Box (Native Streamlit Audio Input)
    with st.container():
        st.markdown("<div class='voice-box'>", unsafe_allow_html=True)
        col_v1, col_v2 = st.columns([1, 4])
        with col_v1:
            st.markdown("🎙️ **Voice Message:**")
        with col_v2:
            st.caption("Click the mic to speak in English, Hindi, or Hinglish. Whisper will transcribe it instantly.")
        
        audio_prompt = st.audio_input("Record your problem by voice", label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)

    # Process Voice Input
    voice_transcribed_text = None
    if audio_prompt is not None:
        audio_bytes = audio_prompt.read()
        if "last_audio_bytes" not in st.session_state or st.session_state.last_audio_bytes != audio_bytes:
            st.session_state.last_audio_bytes = audio_bytes
            whisper_key = groq_key
            if not whisper_key:
                st.warning("⚠️ Voice transcription requires GROQ_API_KEY in .env.")
            else:
                with st.spinner("🎧 Transcribing your voice via Groq Whisper..."):
                    voice_transcribed_text = transcribe_audio_file(audio_bytes, whisper_key, lang_code=whisper_code)
                    if voice_transcribed_text and not voice_transcribed_text.startswith("[Voice Transcription Error"):
                        st.success(f"🗣️ Heard: *\"{voice_transcribed_text}\"*")
                    elif voice_transcribed_text:
                        st.warning(voice_transcribed_text)

    # Render Chat History
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"], avatar="🧑‍💼" if msg["role"] == "assistant" else "👤"):
            st.markdown(msg["content"])

    # Determine user input (Text Chat Input, Voice Transcription, or Preset Demo Insert)
    chat_text_input = st.chat_input("Type your message or ask a question...")
    
    incoming_message = None
    if voice_transcribed_text and not voice_transcribed_text.startswith("[Voice Transcription Error"):
        incoming_message = voice_transcribed_text.strip()
    elif chat_text_input and chat_text_input.strip():
        incoming_message = chat_text_input.strip()
    elif "pending_user_text" in st.session_state and st.session_state.pending_user_text:
        incoming_message = st.session_state.pending_user_text.strip()
        del st.session_state.pending_user_text

    # Handle incoming user message
    if incoming_message:
        # Append User Message
        st.session_state.chat_history.append({"role": "user", "content": incoming_message})
        
        # Check if in Opponent Practice Mode
        if st.session_state.practice_mode and st.session_state.case_dossier:
            engine = LegalLLMEngine(provider=prov_code, model_name=model_name, api_key=active_key)
            roleplay_agent = RoleplayOpponentAgent(engine)
            with st.spinner("Opponent is reacting to your argument..."):
                opp_eval = roleplay_agent.run(
                    st.session_state.case_dossier,
                    st.session_state.practice_history,
                    incoming_message,
                    language=selected_lang
                )
                opponent_reply = opp_eval.get("opponent_reply", "")
                coach = opp_eval.get("coach_evaluation", {})

                if opponent_reply.startswith("ERROR:") or "No model connected" in opponent_reply or "[Gemini Error" in opponent_reply or "[Groq Error" in opponent_reply or opp_eval.get("status") == "error":
                    err_msg = opp_eval.get("error", opponent_reply)
                    st.error(f"⚠️ {err_msg}")
                else:
                    st.session_state.practice_history.append({"role": "user", "content": incoming_message})
                    st.session_state.practice_history.append({"role": "assistant", "content": opponent_reply})

                    reply_markdown = f"""
**{st.session_state.case_dossier.get('opposite_party', 'Opposing Party')}:**  
*"{opponent_reply}"*

---
> **🥊 Coach Evaluation:**
> - **Rating:** `{coach.get('strength_rating', 'Moderate')}`
> - **What Worked:** {coach.get('what_went_well', '')}
> - **Tactical Tip:** {coach.get('what_to_improve', '')}
> - **💡 Powerful Counter:** *\"{coach.get('suggested_next_counter', '')}\"*
"""
                    st.session_state.chat_history.append({"role": "assistant", "content": reply_markdown})
                    st.rerun()

        # Conversational Legal Counselor Flow (Initial Case vs. Continuous Follow-ups)
        else:
            engine = LegalLLMEngine(provider=prov_code, model_name=model_name, api_key=active_key)
            
            # Scenario A: First Turn - Establishing the Case Dossier
            if st.session_state.case_dossier is None:
                case_builder = CaseBuilderAgent(engine)
                rights_advisor = RightsAdvisorAgent(engine)

                with st.spinner("🤔 NyayaMitra is listening, checking verified Indian statutes, and preparing guidance..."):
                    # 1. Build Case Dossier
                    dossier = case_builder.run(incoming_message, language=selected_lang)
                    if dossier.get("status") == "error" or "error" in dossier:
                        err_msg = dossier.get("error", "No model connected. Add an API key.")
                        st.error(f"⚠️ {err_msg}")
                    else:
                        st.session_state.case_dossier = dossier

                        # 2. Check escalation
                        esc = dossier.get("escalation_check", {})
                        
                        # 3. Retrieve verified laws & rights
                        rights = rights_advisor.run(dossier, language=selected_lang)
                        if rights.get("status") == "error" or "error" in rights:
                            err_msg = rights.get("error", "Error connecting to model.")
                            st.error(f"⚠️ {err_msg}")
                        else:
                            st.session_state.rights_advice = rights

                            # 4. Generate conversational response
                            standing_text = rights.get("plain_language_standing", "")
                            options = rights.get("action_options", [])
                            
                            response_content = f"{standing_text}\n\n"
                            
                            if esc.get("requires_real_lawyer", False):
                                response_content += f"⚠️ **IMPORTANT NOTICE:** This case touches upon high-risk matters ({', '.join(esc.get('reasons', []))}). I recommend consulting a practicing advocate immediately. You can reach the free National Legal Aid Helpline at **15100**.\n\n"
                            
                            if options:
                                response_content += "### 🎯 Your Immediate Action Steps:\n"
                                for opt in options[:2]:
                                    response_content += f"- **{opt.get('title')}:** {opt.get('details')} *(Timeline: {opt.get('timeline')}, Cost: {opt.get('cost_estimate')})*\n"
                            
                            response_content += "\n👉 **Take a look at the Live Intelligence panel on the right:** I've organized your case timeline and evidence checklist. You can ask me any follow-up questions, or click **Draft Legal Notice** anytime!"

                            st.session_state.chat_history.append({"role": "assistant", "content": response_content})
                            st.rerun()

            # Scenario B: Multi-Turn Follow-Up Question (Continuous Chat)
            else:
                counselor = ConversationalCounselorAgent(engine)
                with st.spinner("💬 NyayaMitra is thinking and preparing your legal answer..."):
                    answer = counselor.answer_followup(
                        st.session_state.chat_history,
                        st.session_state.case_dossier,
                        incoming_message,
                        language=selected_lang
                    )
                    
                    if answer.startswith("ERROR:") or "No model connected" in answer or "[Gemini Error" in answer or "[Groq Error" in answer:
                        st.error(f"⚠️ {answer}")
                    else:
                        # Also dynamically check if user mentioned new evidence/proofs to update the sidecar
                        msg_lower = incoming_message.lower()
                        evidence_keywords = ["bank statement", "receipt", "invoice", "photo", "video", "whatsapp", "email", "agreement", "cheque", "recording", "job sheet", "bill"]
                        found_ev = [w for w in evidence_keywords if w in msg_lower]
                        if found_ev and "evidence_held" in st.session_state.case_dossier:
                            for ev in found_ev:
                                entry_name = f"Additional mentioned proof: {ev.capitalize()}"
                                if entry_name not in st.session_state.case_dossier["evidence_held"]:
                                    st.session_state.case_dossier["evidence_held"].append(entry_name)
                                    curr_score = st.session_state.case_dossier.get("evidence_strength_score", 7)
                                    try:
                                        curr_score = int(curr_score)
                                    except Exception:
                                        curr_score = 7
                                    if curr_score < 10:
                                        st.session_state.case_dossier["evidence_strength_score"] = curr_score + 1

                        st.session_state.chat_history.append({"role": "assistant", "content": answer})
                        st.rerun()

# Sidecar Column: Live Case Intelligence & Actionable Tools
with col_side:
    st.markdown("### 📊 Live Case Intelligence")
    
    if st.session_state.case_dossier:
        dossier = st.session_state.case_dossier
        rights = st.session_state.rights_advice or {}

        # Dispute Card
        st.markdown(f"""
        <div class='side-card'>
            <b>📌 Case:</b> {dossier.get('case_title', 'Everyday Dispute')}<br/>
            <b>👤 Parties:</b> {dossier.get('complainant', 'You')} vs. {dossier.get('opposite_party', 'Opposing Party')}<br/>
            <b>💰 Disputed Sum:</b> {dossier.get('disputed_amount', 'N/A')}<br/>
            <b>📁 Category:</b> <span class='badge-statute'>{dossier.get('category', 'Civil')}</span>
        </div>
        """, unsafe_allow_html=True)

        # Evidence Strength Meter (Bounded 1-10)
        raw_score = dossier.get("evidence_strength_score", 7)
        try:
            score = int(raw_score)
        except Exception:
            score = 7
        score = max(1, min(10, score))
        
        st.markdown(f"**🛡️ Evidence Strength: `{score}/10`**")
        st.progress(float(score) / 10.0)
        st.caption(dossier.get("evidence_strength_explanation", ""))

        # Tabs for Details
        st_tab1, st_tab2, st_tab3 = st.tabs(["⏳ Timeline", "📜 Proof Checklist", "📚 Laws"])
        
        with st_tab1:
            timeline = dossier.get("timeline", [])
            if isinstance(timeline, list) and timeline:
                for t in timeline:
                    if isinstance(t, dict):
                        st.markdown(f"- **{t.get('date_or_period', 'Event')}:** {t.get('event', '')}")
                    else:
                        st.markdown(f"- {t}")
            else:
                st.caption("Tell me the dates to build your timeline.")

        with st_tab2:
            st.markdown("**Proof You Have:**")
            held = dossier.get("evidence_held", [])
            if isinstance(held, str):
                held = [held]
            for h in held:
                st.markdown(f"- ✅ {h}")
                
            st.markdown("**Proof You Still Need:**")
            needed = dossier.get("evidence_needed", [])
            if isinstance(needed, str):
                needed = [needed]
            for n in needed:
                st.markdown(f"- ⚠️ {n}")

        with st_tab3:
            laws = rights.get("governing_laws", [])
            if isinstance(laws, list) and laws:
                for l in laws:
                    if isinstance(l, dict):
                        is_verified = l.get("status") == "verified"
                        badge = "" if is_verified else " <span style='color:orange; font-size:0.8rem; font-weight:bold;'>[unverified]</span>"
                        st.markdown(f"- **{l.get('act_name', 'Statute')}** ({l.get('section', 'General Provisions')}){badge}: {l.get('relevance', '')}", unsafe_allow_html=True)
                    else:
                        st.markdown(f"- {l} <span style='color:orange; font-size:0.8rem; font-weight:bold;'>[unverified]</span>", unsafe_allow_html=True)
            else:
                st.caption("Statutory provisions will be listed here.")

        st.markdown("---")
        st.markdown("### ⚡ Action Center")

        # 1. Legal Notice Generator Button
        if st.button("📝 Draft Ready-to-Send Legal Notice", use_container_width=True, type="primary"):
            engine = LegalLLMEngine(provider=prov_code, model_name=model_name, api_key=active_key)
            drafter = DocumentDrafterAgent(engine)
            with st.spinner("Drafting 15-day formal legal notice..."):
                notice = drafter.run(dossier, rights)
                if notice.startswith("ERROR:") or "No model connected" in notice or "[Gemini Error" in notice or "[Groq Error" in notice:
                    st.error(f"⚠️ {notice}")
                else:
                    st.session_state.notice_draft = notice
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": f"📄 **I have generated your Formal Legal Demand Notice!**\n\nYou can review, copy, or download it from the Action Center on the right."
                    })
                    st.rerun()

        # Display Notice if Drafted
        if st.session_state.notice_draft:
            with st.expander("📄 View Generated Legal Notice", expanded=True):
                st.text_area("Legal Notice Text", value=st.session_state.notice_draft, height=220)
                st.download_button(
                    "📥 Download Notice (.txt)",
                    data=st.session_state.notice_draft,
                    file_name="Legal_Demand_Notice.txt",
                    mime="text/plain",
                    use_container_width=True
                )

        # 2. Practice Opponent Mode Toggle
        st.markdown("---")
        st.markdown("### 🥊 Opponent Practice Arena")
        st.caption("Roleplay and practice negotiating with the opposing party right in the chat.")
        
        practice_toggle = st.toggle("Enable Roleplay Opponent Mode", value=st.session_state.practice_mode)
        if practice_toggle != st.session_state.practice_mode:
            st.session_state.practice_mode = practice_toggle
            if practice_toggle:
                opp_name = dossier.get("opposite_party", "Opponent")
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": (
                        f"🥊 **PRACTICE ARENA ACTIVE!**\n\n"
                        f"I am now roleplaying as **{opp_name}**. "
                        f"Type or speak your counter-arguments in the chat. Let's see how firmly you can defend your rights!"
                    )
                })
            else:
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": "🤝 **Practice Arena Deactivated.** I am back as your AI Legal Counselor."
                })
            st.rerun()

    else:
        st.info("💡 **Your Case Intelligence will appear here** as soon as you speak or type your legal problem.")
        st.markdown("""
        **What NyayaMitra does:**
        1. 🎧 **Listens to your story** by voice or text.
        2. 📋 **Extracts facts & dates** into a verified dossier.
        3. ⚖️ **Cites real Indian laws** (*Model Tenancy Act, CPA 2019, Code on Wages 2019*).
        4. 📝 **Generates a 15-day Legal Notice**.
        5. 🥊 **Simulates the opponent** so you can practice negotiating.
        """)
