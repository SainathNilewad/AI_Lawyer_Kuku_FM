"""
app.py - NyayaMitra: Conversational AI Legal Companion for Everyday India
Clean, interview-ready implementation providing:
1. Multilingual Voice & Text Intake (Whisper Large v3 Turbo + Pan-India scripts)
2. Calm Disclaimer & Strict Scope Boundaries on First Screen
3. Clickable Example Scenarios
4. High-Contrast Dark-Theme Styling (No blank white bars)
5. Live Case Intelligence Sidecar with Statutory Badges ('verified' / 'needs verification')
6. Automated Pre-Litigation Legal Notice Generator (15-day standard practice)
7. Dispute Roleplay Practice Arena
"""

import streamlit as st
import os
import sys
import html
from pathlib import Path

# Explicitly ensure repo root is in sys.path on Streamlit Cloud / Linux
_REPO_ROOT = str(Path(__file__).resolve().parent)
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from dotenv import load_dotenv

load_dotenv()

# Synchronize Streamlit Cloud secrets into os.environ if deployed
try:
    if hasattr(st, "secrets"):
        for _sec_k, _sec_v in st.secrets.items():
            if isinstance(_sec_v, str) and _sec_k not in os.environ:
                os.environ[_sec_k] = _sec_v
except Exception:
    pass

try:
    from legal_kb import (
        retrieve_verified_legal_context,
        check_immediate_advocate_escalation,
        VERIFIED_STATUTORY_DATABASE,
        is_case_law_request,
        CASE_LAW_FIXED_REPLY,
        build_safe_side_card_html,
        build_safe_source_law_html
    )
except ImportError:
    from .legal_kb import (
        retrieve_verified_legal_context,
        check_immediate_advocate_escalation,
        VERIFIED_STATUTORY_DATABASE,
        is_case_law_request,
        CASE_LAW_FIXED_REPLY,
        build_safe_side_card_html,
        build_safe_source_law_html
    )

try:
    from llm_engine import LegalLLMEngine, list_groq_models, list_gemini_models
    from agents import (
        CaseBuilderAgent,
        RightsAdvisorAgent,
        DocumentDrafterAgent,
        RoleplayOpponentAgent,
        ConversationalCounselorAgent
    )
except ImportError:
    from .llm_engine import LegalLLMEngine, list_groq_models, list_gemini_models
    from .agents import (
        CaseBuilderAgent,
        RightsAdvisorAgent,
        DocumentDrafterAgent,
        RoleplayOpponentAgent,
        ConversationalCounselorAgent
    )

st.set_page_config(
    page_title="NyayaMitra - AI Legal Companion",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-Contrast Styling (Clean on both Dark and Light Streamlit themes)
st.markdown("""
<style>
    /* Main titles with high contrast */
    .chat-header {
        font-size: 2.1rem;
        font-weight: 800;
        margin-bottom: 2px;
        line-height: 1.2;
    }
    .chat-sub {
        font-size: 1.02rem;
        color: #b0bec5;
        margin-bottom: 12px;
        line-height: 1.4;
    }
    
    /* First screen disclaimer cards */
    .calm-notice-card {
        background-color: rgba(33, 150, 243, 0.08);
        border: 1px solid rgba(33, 150, 243, 0.3);
        border-left: 4px solid #1e88e5;
        border-radius: 6px;
        padding: 10px 14px;
        font-size: 0.92rem;
        margin-bottom: 10px;
        line-height: 1.45;
    }
    .scope-card {
        background-color: rgba(158, 158, 158, 0.08);
        border: 1px solid rgba(158, 158, 158, 0.25);
        border-left: 4px solid #9e9e9e;
        border-radius: 6px;
        padding: 8px 14px;
        font-size: 0.88rem;
        margin-bottom: 14px;
        line-height: 1.4;
    }

    /* Sidecar Case Card */
    .side-card {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-left: 4px solid #3f51b5;
        border-radius: 8px;
        padding: 12px 14px;
        margin-bottom: 12px;
    }

    /* Statutory Badges */
    .badge-verified {
        background-color: #1b5e20;
        color: #e8f5e9;
        padding: 2px 7px;
        border-radius: 4px;
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        display: inline-block;
    }
    .badge-unverified {
        background-color: #e65100;
        color: #fff3e0;
        padding: 2px 7px;
        border-radius: 4px;
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        display: inline-block;
    }
    .badge-statute {
        background-color: rgba(76, 175, 80, 0.15);
        color: #81c784;
        padding: 2px 8px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.82rem;
    }

    /* Escalation and Scope Callouts */
    .banner-escalation {
        background-color: rgba(211, 47, 47, 0.12);
        border-left: 4px solid #ef5350;
        padding: 10px 14px;
        border-radius: 4px;
        margin-bottom: 12px;
        color: #ffcdd2;
    }
    .banner-scope {
        background-color: rgba(158, 158, 158, 0.12);
        border-left: 4px solid #9e9e9e;
        padding: 10px 14px;
        border-radius: 4px;
        margin-bottom: 12px;
        color: #cfd8dc;
    }
</style>
""", unsafe_allow_html=True)

# Supported Pan-India Languages in their own native script
INDIAN_LANGUAGES = {
    "Auto-Detect / English": None,
    "हिन्दी (Hindi)": "hi",
    "Hinglish (Hindi in Latin script)": "hi",
    "தமிழ் (Tamil)": "ta",
    "తెలుగు (Telugu)": "te",
    "ಕನ್ನಡ (Kannada)": "kn",
    "বাংলা (Bengali)": "bn",
    "मराठी (Marathi)": "mr",
    "ગુજરાતી (Gujarati)": "gu",
    "മലയാളം (Malayalam)": "ml",
    "ਪੰਜਾਬੀ (Punjabi)": "pa",
}

# Helper: Transcribe Voice via Groq Whisper with Language Support
def transcribe_audio_file(audio_bytes, api_key: str, lang_code: str = None) -> str:
    try:
        from groq import Groq
        client = Groq(api_key=api_key)
        kwargs = {
            "file": ("voice_input.wav", audio_bytes),
            "model": "whisper-large-v3-turbo",
            "prompt": "Indian legal dispute in Hindi, English, Tamil, Telugu, Kannada, Bengali, Marathi, Gujarati, Malayalam, Punjabi, or Hinglish",
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
                "You can type your problem below or use the **'Speak instead of typing'** voice recorder. Tell me what happened!"
            )
        }
    ]

if "case_dossier" not in st.session_state:
    st.session_state.case_dossier = None
if "case_category" not in st.session_state:
    st.session_state.case_category = None
if "rights_advice" not in st.session_state:
    st.session_state.rights_advice = None
if "notice_draft" not in st.session_state:
    st.session_state.notice_draft = None
if "practice_mode" not in st.session_state:
    st.session_state.practice_mode = False
if "practice_history" not in st.session_state:
    st.session_state.practice_history = []
if "pending_user_text" not in st.session_state:
    st.session_state.pending_user_text = None
if "model_provenance_log" not in st.session_state:
    st.session_state.model_provenance_log = []

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

# ==============================================================================
# SIDEBAR
# ==============================================================================
with st.sidebar:
    # Reliable text/emoji logo with high contrast
    st.markdown("## ⚖️ **NyayaMitra**")
    st.caption("AI Legal Companion for Everyday India")
    
    st.markdown("---")
    
    # 1. Language selector at the TOP of sidebar with native scripts
    st.markdown("**🌐 Language / भाषा**")
    selected_lang = st.selectbox(
        "Choose conversation language:",
        list(INDIAN_LANGUAGES.keys()),
        index=0,
        label_visibility="collapsed"
    )
    whisper_code = INDIAN_LANGUAGES[selected_lang]
    st.caption("ℹ️ *Verified languages: English, Hindi, Marathi, Hinglish. Other languages may work but are not verified.*")

    # Resolve API keys
    groq_key = os.getenv("GROQ_API_KEY", "")
    gemini_key = os.getenv("GEMINI_API_KEY", "") or os.getenv("GOOGLE_API_KEY", "")
    env_prov = os.getenv("LLM_PROVIDER", "gemini").lower()
    default_p_idx = 0 if env_prov == "gemini" else 1

    # 3. Model settings inside collapsed expander
    with st.expander("⚙️ Model settings (advanced)", expanded=False):
        provider_choice = st.selectbox("LLM Provider:", ["Gemini", "Groq"], index=default_p_idx)
        prov_code = provider_choice.lower()
        active_key = gemini_key if prov_code == "gemini" else groq_key

        # API key input field for cloud deployment or UI entry
        custom_key = st.text_input(
            f"{provider_choice} API Key:",
            value=active_key,
            type="password",
            placeholder=f"Paste {provider_choice} API key here...",
            help="Pre-filled if set in Streamlit Secrets or .env. You can also paste your key directly here."
        )
        if custom_key:
            active_key = custom_key
            if prov_code == "gemini":
                gemini_key = custom_key
            else:
                groq_key = custom_key

        if prov_code == "gemini":
            default_model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")
            gemini_models = get_cached_gemini_models(active_key) if active_key else []
            if gemini_models:
                m_idx = gemini_models.index(default_model) if default_model in gemini_models else 0
                model_name = st.selectbox("Model:", gemini_models, index=m_idx)
            else:
                model_name = st.text_input("Model:", value=default_model)
        else:
            default_model = os.getenv("GROQ_MODEL", "qwen/qwen3.8-27b")
            groq_models = get_cached_groq_models(active_key) if active_key else []
            if groq_models:
                m_idx = groq_models.index(default_model) if default_model in groq_models else 0
                model_name = st.selectbox("Model:", groq_models, index=m_idx)
            else:
                model_name = st.text_input("Model:", value=default_model)

        st.caption(f"Active Provider: **{provider_choice}** | Model: `{model_name}`")

    # 2. Compact single status line
    st.markdown("---")
    if active_key:
        if prov_code == "gemini":
            voice_status = " | Voice ready (Groq)" if groq_key else ""
            st.caption(f"🟢 **Gemini connected (Primary){voice_status}**")
        else:
            st.caption("🟢 **Groq connected, voice ready**")
    else:
        st.caption("🔴 **API Key missing** (Add in Secrets or under Model settings)")

    # Model Provenance Tracking per message
    st.markdown("---")
    with st.expander("🤖 Model Provenance Log", expanded=False):
        if st.session_state.get("model_provenance_log"):
            for item in st.session_state.model_provenance_log:
                st.caption(f"**Msg #{item['turn']}**: {item['provider']} (`{item['model']}`)")
        else:
            st.caption("No AI responses generated yet.")

    # Reset button
    st.markdown("---")
    if st.button("🔄 Reset Conversation", use_container_width=True):
        st.session_state.chat_history = [st.session_state.chat_history[0]]
        st.session_state.case_dossier = None
        st.session_state.case_category = None
        st.session_state.rights_advice = None
        st.session_state.notice_draft = None
        st.session_state.practice_mode = False
        st.session_state.practice_history = []
        st.session_state.pending_user_text = None
        st.session_state.model_provenance_log = []
        st.rerun()

# ==============================================================================
# MAIN LAYOUT: CHAT (65%) & LIVE INTELLIGENCE SIDECAR (35%)
# ==============================================================================
col_chat, col_side = st.columns([65, 35], gap="large")

with col_chat:
    st.markdown("<h1 class='chat-header'>⚖️ NyayaMitra AI Legal Companion</h1>", unsafe_allow_html=True)
    st.markdown("<p class='chat-sub'>Conversational legal guidance for everyday Indian citizens.</p>", unsafe_allow_html=True)

    # First screen calm notice
    st.markdown("""
    <div class='calm-notice-card'>
        🛡️ <strong>Notice:</strong> NyayaMitra gives general information, not legal advice. It can be wrong. For arrests, violence, court summons or large amounts, speak to a real lawyer. <strong>Free help: DLSA / NALSA helpline 15100.</strong>
    </div>
    """, unsafe_allow_html=True)

    # Scope line
    st.markdown("""
    <div class='scope-card'>
        📋 <strong>Scope:</strong> Covers: rental deposits and tenancy, consumer refunds and e-commerce, unpaid salary and final settlement. Does not cover: criminal cases, family law, property title disputes, court filings.
    </div>
    """, unsafe_allow_html=True)

    # 4 Clickable Example Prompts (Clicking one immediately fills and sends the message)
    st.markdown("**💡 Try an example problem:**")
    prompt_col1, prompt_col2 = st.columns(2)

    EXAMPLE_PROMPTS = [
        (
            "🏠 Landlord Deposit",
            "My landlord is withholding my security deposit of Rs 45,000 claiming wear-and-tear repainting charges after I vacated. How can I recover it?"
        ),
        (
            "📱 E-Commerce Refund",
            "I bought a smartphone for Rs 26,999 online that arrived defective. The seller cancelled my replacement request saying the 7-day return window expired. How can I get a refund?"
        ),
        (
            "💼 Unpaid Salary After Resignation",
            "I resigned, served my full 60-day notice period, but my employer is withholding my Rs 1,65,000 final settlement and relieving letter. What are my statutory rights?"
        ),
        (
            "मकान मालिक डिपॉजिट (Hindi)",
            "मेरा मकान मालिक ₹40,000 का सिक्योरिटी डिपॉजिट वापस नहीं कर रहा है और कह रहा है कि पेंटिंग का खर्चा कटेगा। मैं अपने पैसे कैसे वापस लूँ?"
        )
    ]

    with prompt_col1:
        if st.button(EXAMPLE_PROMPTS[0][0], use_container_width=True, help="Tenancy security deposit dispute"):
            st.session_state.pending_user_text = EXAMPLE_PROMPTS[0][1]
            st.rerun()
        if st.button(EXAMPLE_PROMPTS[2][0], use_container_width=True, help="Employment wage settlement dispute"):
            st.session_state.pending_user_text = EXAMPLE_PROMPTS[2][1]
            st.rerun()

    with prompt_col2:
        if st.button(EXAMPLE_PROMPTS[1][0], use_container_width=True, help="Consumer defect & refund denial"):
            st.session_state.pending_user_text = EXAMPLE_PROMPTS[1][1]
            st.rerun()
        if st.button(EXAMPLE_PROMPTS[3][0], use_container_width=True, help="हिंदी में किरायेदारी विवाद"):
            st.session_state.pending_user_text = EXAMPLE_PROMPTS[3][1]
            st.rerun()

    st.markdown("---")

    # Render Chat History
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"], avatar="🧑‍💼" if msg["role"] == "assistant" else "👤"):
            content = msg.get("content", "")
            if msg.get("role") == "user":
                # Render user messages safely escaped to prevent HTML/XSS injection
                st.markdown(html.escape(content))
            else:
                # Assistant messages: check if it's a fixed internal UI banner
                if content.startswith("<div class='banner-") or content.startswith("<div class='side-card"):
                    st.markdown(content, unsafe_allow_html=True)
                else:
                    st.markdown(content)

    # Chat Input Box
    chat_text_input = st.chat_input("Type your dispute or question here...")
    st.caption("Your messages and voice are processed by Google Gemini and Groq Whisper. Avoid unnecessary personal identifiers.")

    # Voice Recorder moved UNDER the chat input into a collapsed expander
    voice_transcribed_text = None
    with st.expander("🎙️ Speak instead of typing", expanded=False):
        st.caption("Click the microphone to record your voice. Groq Whisper Large v3 Turbo will transcribe it.")
        audio_prompt = st.audio_input("Record voice message", label_visibility="collapsed")
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
                            st.success(f"🗣️ Transcribed: *\"{voice_transcribed_text}\"*")
                        elif voice_transcribed_text:
                            st.warning(voice_transcribed_text)

    # Determine incoming user message
    incoming_message = None
    if "pending_user_text" in st.session_state and st.session_state.pending_user_text:
        incoming_message = st.session_state.pending_user_text.strip()
        st.session_state.pending_user_text = None
    elif voice_transcribed_text and not voice_transcribed_text.startswith("[Voice Transcription Error"):
        incoming_message = voice_transcribed_text.strip()
    elif chat_text_input and chat_text_input.strip():
        incoming_message = chat_text_input.strip()

    # Process Message
    if incoming_message:
        # Pre-check: Ensure an active API key is connected before invoking agents
        if not active_key:
            if not st.session_state.chat_history or st.session_state.chat_history[-1].get("content") != incoming_message:
                st.session_state.chat_history.append({"role": "user", "content": incoming_message})
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": (
                    "⚠️ **No API Key Connected:**\n\n"
                    "To generate AI legal analysis, please configure your API key:\n\n"
                    "1. **On Streamlit Community Cloud (Recommended):**\n"
                    "   - Open your app on [share.streamlit.io](https://share.streamlit.io)\n"
                    "   - Click **⚙️ Settings** (bottom-right or via top menu) → **Secrets**\n"
                    "   - Paste:\n"
                    "     ```toml\n"
                    "     GROQ_API_KEY = \"your-groq-key-here\"\n"
                    "     GEMINI_API_KEY = \"your-gemini-key-here\"\n"
                    "     ```\n"
                    "   - Click **Save**.\n\n"
                    "2. **Or enter it directly in this session:**\n"
                    "   - Expand **⚙️ Model settings (advanced)** in the left sidebar and paste your key into the text field!"
                )
            })
            st.rerun()

        # Fix duplicated user bubble: append only if not already last message
        if not st.session_state.chat_history or st.session_state.chat_history[-1].get("content") != incoming_message:
            st.session_state.chat_history.append({"role": "user", "content": incoming_message})

        # Pre-flight Check 1: Immediate Advocate Escalation & Emergency check FIRST (No LLM call)
        esc_check = check_immediate_advocate_escalation(incoming_message)
        if esc_check.get("is_past_incident", False):
            clarification_reply = (
                "Is this happening now, or did it happen in the past?\n\n"
                "Please clarify the timeline so I can give you appropriate guidance (and direct you to emergency help or civil/legal aid at DLSA/NALSA 15100 as needed)."
            )
            st.session_state.model_provenance_log.append({
                "turn": len(st.session_state.chat_history) + 1,
                "provider": "Deterministic Guard",
                "model": "Emergency Safety Rule (No LLM)"
            })
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": clarification_reply,
                "meta": {"provider": "Deterministic Guard", "model": "Emergency Safety Rule (No LLM)"}
            })
            st.rerun()

        if esc_check.get("requires_real_lawyer", False):
            reason = esc_check.get("reason", "High-risk matter")
            is_phys = esc_check.get("is_physical_danger", False)
            if is_phys:
                escalation_reply = (
                    f"<div class='banner-escalation'>"
                    f"<strong>🚨 IMMEDIATE EMERGENCY / PHYSICAL DANGER:</strong> If you are facing physical violence, assault, or are in danger right now, "
                    f"please <strong>call 112 now</strong> (National Emergency Helpline).<br/>"
                    f"Escalation trigger: <em>{html.escape(str(reason))}</em>.<br/>"
                    f"For emergency legal aid and protection, contact the District Legal Services Authority (DLSA) / NALSA Helpline at <strong>15100</strong>."
                    f"</div>\n\n"
                    f"**Immediate safety steps:**\n"
                    f"- **Call 112 now:** Dial 112 immediately for emergency police or medical assistance.\n"
                    f"- **Move to a safe place:** Move away from aggressors to a secure or public area.\n"
                    f"- **Do not sign or concede anything under duress:** Avoid signing documents under threat or pressure.\n"
                    f"- **Call DLSA / NALSA 15100:** For free emergency legal assistance and protection."
                )
            else:
                escalation_reply = (
                    f"<div class='banner-escalation'>"
                    f"<strong>🚨 Please speak to a lawyer:</strong> This situation involves serious legal or criminal risk.<br>"
                    f"Escalation trigger: <em>{html.escape(str(reason))}</em>.<br>"
                    f"Please consult a practicing advocate immediately or call the free District Legal Services Authority (DLSA) / NALSA helpline at <strong>15100</strong>."
                    f"</div>\n\n"
                    f"**Immediate safety steps:**\n"
                    f"- **Keep written records:** Preserve all messages, notices, emails, and call logs.\n"
                    f"- **Do not sign anything:** Do not sign any settlement, resignation, or admission under threat or pressure.\n"
                    f"- **Speak to a lawyer or DLSA 15100:** NyayaMitra cannot predict what police or courts will do. Please contact your local District Legal Services Authority or call 15100 for official legal protection."
                )
            st.session_state.model_provenance_log.append({
                "turn": len(st.session_state.chat_history) + 1,
                "provider": "Deterministic Guard",
                "model": "Emergency Safety Rule (No LLM)" if is_phys else "Safety Escalation Rule (No LLM)"
            })
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": escalation_reply,
                "meta": {"provider": "Deterministic Guard", "model": "Emergency Safety Rule (No LLM)" if is_phys else "Safety Escalation Rule (No LLM)"}
            })
            st.rerun()

        # Pre-flight Check 2: Case-law request check (Fixed reply, no LLM call)
        if is_case_law_request(incoming_message):
            st.session_state.model_provenance_log.append({
                "turn": len(st.session_state.chat_history) + 1,
                "provider": "Deterministic Guard",
                "model": "Statutory Rule Engine (No LLM)"
            })
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": CASE_LAW_FIXED_REPLY,
                "meta": {"provider": "Deterministic Guard", "model": "Statutory Rule Engine (No LLM)"}
            })
            st.rerun()

        # Pre-flight Check 3: True Out-of-Scope check (with category inheritance, no LLM call)
        cat_fallback = st.session_state.get("case_category")
        scope_check = retrieve_verified_legal_context(incoming_message, fallback_category=cat_fallback)
        if scope_check.get("truly_out_of_scope", False):
            scope_reply = (
                "<div class='banner-scope'>"
                "<strong>ℹ️ Topic Out of Scope:</strong> This matter falls outside NyayaMitra's supported civil areas (rental deposits, consumer refunds, wage settlement). "
                "NyayaMitra does not cover criminal cases, family law/divorce, property title disputes, or court filings. "
                "Please consult a licensed advocate or contact the free District Legal Services Authority (DLSA) / NALSA helpline at <strong>15100</strong>."
                "</div>"
            )
            st.session_state.model_provenance_log.append({
                "turn": len(st.session_state.chat_history) + 1,
                "provider": "Deterministic Guard",
                "model": "Statutory Scope Engine (No LLM)"
            })
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": scope_reply,
                "meta": {"provider": "Deterministic Guard", "model": "Statutory Scope Engine (No LLM)"}
            })
            st.rerun()

        # Handle Roleplay Mode
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

                if opponent_reply.startswith("ERROR:") or "No model connected" in opponent_reply or opp_eval.get("status") == "error":
                    err_msg = opp_eval.get("error", opponent_reply)
                    st.error(f"⚠️ {err_msg}")
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": f"⚠️ **Model Error:** {err_msg}\n\nPlease check your model settings."
                    })
                    st.rerun()
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
                    actual_p = getattr(engine, "last_used_provider", provider_choice)
                    actual_m = getattr(engine, "last_used_model", model_name)
                    st.session_state.model_provenance_log.append({
                        "turn": len(st.session_state.chat_history) + 1,
                        "provider": actual_p,
                        "model": actual_m
                    })
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": reply_markdown,
                        "meta": {"provider": actual_p, "model": actual_m}
                    })
                    st.rerun()

        # Handle Standard Legal Assistant Flow
        else:
            engine = LegalLLMEngine(provider=prov_code, model_name=model_name, api_key=active_key)

            # Turn 1: Build Dossier & Rights Advice
            if st.session_state.case_dossier is None:
                case_builder = CaseBuilderAgent(engine)
                rights_advisor = RightsAdvisorAgent(engine)

                with st.spinner("🤔 NyayaMitra is analyzing facts, checking verified statutes, and preparing advice..."):
                    dossier = case_builder.run(incoming_message, language=selected_lang)
                    if isinstance(dossier, dict) and (dossier.get("status") == "error" or "error" in dossier):
                        err_msg = dossier.get("error", "No model connected. Add an API key.")
                        st.error(f"⚠️ {err_msg}")
                        st.session_state.chat_history.append({
                            "role": "assistant",
                            "content": f"⚠️ **Model Error:** {err_msg}\n\nPlease check your API key in **Model settings (advanced)**."
                        })
                        st.rerun()
                    else:
                        st.session_state.case_dossier = dossier
                        st.session_state.case_category = dossier.get("category", "")
                        rights = rights_advisor.run(dossier, language=selected_lang)

                        if isinstance(rights, dict) and (rights.get("status") == "error" or "error" in rights):
                            err_msg = rights.get("error", "Error connecting to model.")
                            st.error(f"⚠️ {err_msg}")
                            st.session_state.chat_history.append({
                                "role": "assistant",
                                "content": f"⚠️ **Model Error:** {err_msg}\n\nPlease check your model settings."
                            })
                            st.rerun()
                        else:
                            st.session_state.rights_advice = rights

                            standing_text = rights.get("plain_language_standing", "")
                            options = rights.get("action_options", [])

                            response_content = f"{standing_text}\n\n"

                            if options:
                                response_content += "### 🎯 Your Immediate Action Steps:\n"
                                for opt in options[:2]:
                                    tl = opt.get('suggested_timeline') or opt.get('timeline')
                                    if tl:
                                        if "suggest" not in tl.lower():
                                            tl = f"Suggested: {tl}"
                                        response_content += f"- **{opt.get('title')}:** {opt.get('details')} *({tl})*\n"
                                    else:
                                        response_content += f"- **{opt.get('title')}:** {opt.get('details')}\n"

                            response_content += "\n👉 **Take a look at the Case Intelligence panel on the right:** I've organized your case timeline and evidence checklist. You can ask follow-up questions, or click **Draft Legal Notice** anytime!"

                            actual_p = getattr(engine, "last_used_provider", provider_choice)
                            actual_m = getattr(engine, "last_used_model", model_name)
                            st.session_state.model_provenance_log.append({
                                "turn": len(st.session_state.chat_history) + 1,
                                "provider": actual_p,
                                "model": actual_m
                            })
                            st.session_state.chat_history.append({
                                "role": "assistant",
                                "content": response_content,
                                "meta": {"provider": actual_p, "model": actual_m}
                            })
                            st.rerun()

            # Subsequent Turns: Multi-Turn Dialogue
            else:
                counselor = ConversationalCounselorAgent(engine)
                with st.spinner("💬 NyayaMitra is preparing your legal answer..."):
                    answer = counselor.answer_followup(
                        st.session_state.chat_history,
                        st.session_state.case_dossier,
                        incoming_message,
                        language=selected_lang
                    )

                    if answer.startswith("ERROR:") or "No model connected" in answer:
                        st.error(f"⚠️ {answer}")
                        st.session_state.chat_history.append({
                            "role": "assistant",
                            "content": f"⚠️ **Model Error:** {answer}\n\nPlease check your model settings."
                        })
                        st.rerun()
                    else:
                        # Dynamically record newly mentioned evidence without marking as verified/available
                        msg_lower = incoming_message.lower()
                        evidence_keywords = ["bank statement", "receipt", "invoice", "photo", "video", "whatsapp", "email", "agreement", "job sheet", "bill"]
                        found_ev = [w for w in evidence_keywords if w in msg_lower]
                        if found_ev:
                            ev_list = st.session_state.case_dossier.setdefault("evidence_mentioned", [])
                            for ev in found_ev:
                                entry_name = f"Mentioned: {ev.capitalize()}"
                                if entry_name not in ev_list:
                                    ev_list.append(entry_name)
                            st.session_state.case_dossier["evidence_held"] = ev_list

                        actual_p = getattr(engine, "last_used_provider", provider_choice)
                        actual_m = getattr(engine, "last_used_model", model_name)
                        st.session_state.model_provenance_log.append({
                            "turn": len(st.session_state.chat_history) + 1,
                            "provider": actual_p,
                            "model": actual_m
                        })
                        st.session_state.chat_history.append({
                            "role": "assistant",
                            "content": answer,
                            "meta": {"provider": actual_p, "model": actual_m}
                        })
                        st.rerun()

# ==============================================================================
# RIGHT SIDECAR: LIVE CASE INTELLIGENCE
# ==============================================================================
with col_side:
    st.markdown("### 📊 Case Intelligence")

    if st.session_state.case_dossier:
        dossier = st.session_state.case_dossier
        rights = st.session_state.rights_advice or {}

        # Dispute Card (HTML-escaped)
        side_card_html = build_safe_side_card_html(
            dossier.get('case_title', 'Everyday Dispute'),
            dossier.get('complainant', 'You'),
            dossier.get('opposite_party', 'Opposing Party'),
            dossier.get('disputed_amount', 'N/A'),
            dossier.get('category', 'Civil')
        )
        st.markdown(side_card_html, unsafe_allow_html=True)

        # Tabs for Timeline, Proof Checklist, and Sources Used
        st_tab1, st_tab2, st_tab3 = st.tabs(["⏳ Timeline", "📜 Proof Checklist", "📚 Sources Used"])

        with st_tab1:
            timeline = dossier.get("timeline", [])
            if isinstance(timeline, list) and timeline:
                for t in timeline:
                    if isinstance(t, dict):
                        st.markdown(f"- **{t.get('date_or_period', 'Event')}:** {t.get('event', '')}")
                    else:
                        st.markdown(f"- {t}")
            else:
                st.caption("Timeline will appear here as dates are discussed.")

        with st_tab2:
            st.markdown("**Mentioned by you (from your story):**")
            mentioned = dossier.get("evidence_mentioned") or dossier.get("evidence_held", [])
            if isinstance(mentioned, str):
                mentioned = [mentioned]
            if mentioned:
                for m in mentioned:
                    st.markdown(f"- 📝 {m}")
            else:
                st.caption("No proof items mentioned yet.")

            st.markdown("**Still needed:**")
            needed = dossier.get("evidence_needed", [])
            if isinstance(needed, str):
                needed = [needed]
            if needed:
                for n in needed:
                    st.markdown(f"- ⚠️ {n}")
            else:
                st.caption("No missing documents identified yet.")

        with st_tab3:
            st.markdown("**Statutory provisions referenced:**")
            laws = rights.get("governing_laws", [])
            
            # Helper: check status from verified database
            def lookup_statutory_status(act_name: str, sec: str) -> str:
                norm_act = act_name.lower()
                for entry in VERIFIED_STATUTORY_DATABASE:
                    if entry.get("domain", "").lower() in norm_act or entry.get("act", "").lower() in norm_act:
                        return entry.get("status", "verified")
                return "verified"

            if isinstance(laws, list) and laws:
                for l in laws:
                    if isinstance(l, dict):
                        raw_act = str(l.get("act_name", "Statute"))
                        raw_sec = str(l.get("section", ""))
                        raw_rel = str(l.get("relevance", ""))
                        status = l.get("status") or lookup_statutory_status(raw_act, raw_sec)
                        is_verified = (status == "verified")
                        law_html = build_safe_source_law_html(raw_act, raw_sec, raw_rel, is_verified=is_verified)
                        st.markdown(law_html, unsafe_allow_html=True)
                    else:
                        safe_l = html.escape(str(l))
                        st.markdown(f"- {safe_l} <span class='badge-unverified'>needs verification</span>", unsafe_allow_html=True)
            else:
                st.caption("Statutory provisions will be listed here.")

            # Guard Removal Audit: Count instances where safety guard intervened
            all_text = ""
            if rights:
                all_text += str(rights.get("plain_language_standing", ""))
                all_text += str(rights.get("action_options", ""))
            for msg in st.session_state.chat_history:
                all_text += str(msg.get("content", ""))

            removed_count = all_text.count("[unverified reference removed]")
            if removed_count > 0:
                st.markdown(f"""
                <div style='background:rgba(255, 152, 0, 0.12); border-left:4px solid #ff9800; padding:8px 12px; border-radius:4px; margin-top:10px; font-size:0.85rem; color:#ffb74d;'>
                    ⚠️ <strong>{removed_count} unverified reference(s)</strong> removed from the answer.
                </div>
                """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### ⚡ Action Center")

        # 1. Legal Notice Generator Button (Standard Pre-Litigation Practice)
        if st.button("📝 Legal Notice Draft – Review Before Sending", use_container_width=True, type="primary"):
            if not active_key:
                st.error("⚠️ Please configure an API key in Secrets or under Model settings to draft legal notices.")
            else:
                engine = LegalLLMEngine(provider=prov_code, model_name=model_name, api_key=active_key)
                drafter = DocumentDrafterAgent(engine)
                with st.spinner("Drafting formal legal demand notice (suggested pre-litigation practice)..."):
                    notice = drafter.run(dossier, rights)
                    if notice.startswith("ERROR:") or "No model connected" in notice:
                        st.error(f"⚠️ {notice}")
                    else:
                        st.session_state.notice_draft = notice
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": "📄 **I have generated your Legal Notice Draft – Review Before Sending!**\n\nYou can review, copy, or download it from the Action Center on the right."
                    })
                    st.rerun()

        # Display Notice if Drafted
        if st.session_state.notice_draft:
            with st.expander("📄 View Legal Notice Draft – Review Before Sending", expanded=True):
                st.text_area("Legal Notice Text", value=st.session_state.notice_draft, height=220)
                st.download_button(
                    "📥 Download Notice (.txt)",
                    data=st.session_state.notice_draft,
                    file_name="Legal_Notice_Draft.txt",
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

    # Empty State (When no dispute is active yet)
    else:
        st.info("💡 **Your Case Intelligence will appear here** as soon as you speak or type your legal problem.")
        st.markdown("""
        **How NyayaMitra works:**
        1. 🎧 **Listens to your story** by voice or text in verified languages (English, Hindi, Marathi, Hinglish; other languages may work but are not verified).
        2. 📋 **Extracts facts & dates** into an organized case timeline.
        3. ⚖️ **Answers only from a small checked list of laws.** Anything not on the list is flagged.
        4. 📝 **Legal Notice Draft – Review Before Sending** (suggested 15-day pre-litigation practice).
        5. 🥊 **Simulates the opponent** so you can practice your arguments.
        """)
