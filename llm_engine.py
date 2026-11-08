"""
llm_engine.py - Model Engine for NyayaMitra (Groq & Gemini)
Provides honest model connectivity, dynamic model listing, and transparent error handling.
"""

import os
import json
import re
from typing import Dict, Any, Optional, List
from dotenv import load_dotenv

load_dotenv()

def clean_json_string(raw_text: str) -> str:
    """Extracts JSON block from raw LLM text response."""
    raw_text = raw_text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", raw_text)
    if match:
        return match.group(1).strip()
    json_match = re.search(r"(\{[\s\S]*\}|\[[\s\S]*\])", raw_text)
    if json_match:
        return json_match.group(1).strip()
    return raw_text

def list_groq_models(api_key: Optional[str] = None) -> List[str]:
    """Fetches list of available models directly from Groq API."""
    key = api_key or os.getenv("GROQ_API_KEY")
    if not key:
        return []
    try:
        from groq import Groq
        client = Groq(api_key=key)
        models = client.models.list()
        return [m.id for m in models.data]
    except Exception as e:
        print(f"[Model List Error Groq]: {e}")
        return []

def list_gemini_models(api_key: Optional[str] = None) -> List[str]:
    """Fetches list of available models directly from Google Gemini API."""
    key = api_key or os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not key:
        return []
    try:
        from google import genai
        client = genai.Client(api_key=key)
        return [m.name for m in client.models.list()]
    except Exception as e:
        print(f"[Model List Error Gemini]: {e}")
        return []

class LegalLLMEngine:
    def __init__(self, provider: Optional[str] = None, model_name: Optional[str] = None, api_key: Optional[str] = None):
        self.provider = (provider or os.getenv("LLM_PROVIDER", "gemini")).lower()
        if self.provider == "gemini":
            self.api_key = api_key or os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
            self.model_name = model_name or os.getenv("GEMINI_MODEL", "gemini-3.5-flash")
        elif self.provider == "groq":
            self.api_key = api_key or os.getenv("GROQ_API_KEY")
            self.model_name = model_name or os.getenv("GROQ_MODEL", "qwen/qwen3.8-27b")
        else:
            self.api_key = api_key
            self.model_name = model_name or os.getenv("LLM_MODEL", "")
        self.last_used_provider = "Gemini" if self.provider == "gemini" else ("Groq" if self.provider == "groq" else self.provider)
        self.last_used_model = self.model_name

    def check_model_exists(self) -> tuple:
        """Verifies if self.model_name exists in the provider's active model catalog."""
        if not self.api_key:
            return False, []
        if self.provider == "groq":
            models = list_groq_models(self.api_key)
            return (self.model_name in models), models
        elif self.provider == "gemini":
            models = list_gemini_models(self.api_key)
            clean = [m.replace("models/", "") for m in models]
            exists = (self.model_name in clean) or (f"models/{self.model_name}" in models) or (self.model_name in models)
            return exists, clean
        return False, []

    def generate(self, system_prompt: str, user_prompt: str, temperature: float = 0.2) -> str:
        """Generates text completion without fake fallbacks or mock demo responses."""
        if not self.api_key:
            return "No model connected. Add an API key."

        # Provider 1: Groq
        if self.provider == "groq":
            try:
                from groq import Groq
                client = Groq(api_key=self.api_key)
                response = client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=temperature
                )
                self.last_used_provider = "Groq"
                self.last_used_model = self.model_name
                return response.choices[0].message.content
            except Exception as e:
                err_str = str(e)
                if ("429" in err_str or "rate_limit" in err_str) and self.model_name != "qwen/qwen3.8-27b":
                    try:
                        response = client.chat.completions.create(
                            model="qwen/qwen3.8-27b",
                            messages=[
                                {"role": "system", "content": system_prompt},
                                {"role": "user", "content": user_prompt}
                            ],
                            temperature=temperature
                        )
                        self.last_used_provider = "Groq"
                        self.last_used_model = "qwen/qwen3.8-27b"
                        return response.choices[0].message.content
                    except Exception:
                        pass
                # Secondary fallback to Gemini if Groq token limit is exhausted
                gem_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
                if gem_key and ("429" in err_str or "rate_limit" in err_str):
                    try:
                        from google import genai
                        from google.genai import types
                        g_client = genai.Client(api_key=gem_key)
                        g_resp = g_client.models.generate_content(
                            model="gemini-3.8-flash",
                            contents=user_prompt,
                            config=types.GenerateContentConfig(
                                system_instruction=system_prompt,
                                temperature=temperature,
                            )
                        )
                        if g_resp and g_resp.text:
                            self.last_used_provider = "Gemini (fallback)"
                            self.last_used_model = "gemini-3.8-flash"
                            return g_resp.text
                    except Exception:
                        pass
                return f"ERROR: [Groq Error: {e}]"

        # Provider: Gemini (Primary)
        if self.provider == "gemini":
            try:
                from google import genai
                from google.genai import types
                client = genai.Client(api_key=self.api_key)
                response = client.models.generate_content(
                    model=self.model_name,
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_prompt,
                        temperature=temperature,
                    )
                )
                if response and response.text:
                    self.last_used_provider = "Gemini"
                    self.last_used_model = self.model_name
                    return response.text
                return "ERROR: [Gemini Error: Empty response received from model]"
            except Exception as e:
                err_str = str(e)
                print(f"[Gemini Exception, attempting Groq fallback]: {err_str[:120]}")
                # Immediate fallback to Groq if Gemini hits any error (503, timeout, quota, etc.)
                groq_k = os.getenv("GROQ_API_KEY")
                if groq_k:
                    try:
                        from groq import Groq
                        g_client = Groq(api_key=groq_k)
                        g_resp = g_client.chat.completions.create(
                            model="qwen/qwen3.8-27b",
                            messages=[
                                {"role": "system", "content": system_prompt},
                                {"role": "user", "content": user_prompt}
                            ],
                            temperature=temperature
                        )
                        self.last_used_provider = "Groq (fallback)"
                        self.last_used_model = "qwen/qwen3.8-27b"
                        return g_resp.choices[0].message.content
                    except Exception as e2:
                        print(f"[Groq Fallback also failed]: {e2}")
                return f"ERROR: [Gemini Error: {e}]"

        return "ERROR: Unknown or unsupported provider configured."

    def generate_json(self, system_prompt: str, user_prompt: str) -> Dict[str, Any]:
        """Ensures structured JSON output from LLM."""
        raw = self.generate(system_prompt + "\nReturn ONLY valid JSON format. Do not include markdown preamble.", user_prompt, temperature=0.1)
        if raw.startswith("ERROR:") or "No model connected" in raw:
            return {
                "error": raw,
                "status": "error"
            }
        cleaned = clean_json_string(raw)
        try:
            return json.loads(cleaned)
        except Exception:
            match = re.search(r"(\{[\s\S]*\})", cleaned)
            if match:
                try:
                    return json.loads(match.group(1))
                except Exception:
                    pass
            return {
                "raw_text": raw,
                "status": "partial_json_parse_fallback"
            }
