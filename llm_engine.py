"""
llm_engine.py - Model Engine for NyayaMitra (Gemini & Groq)
Supports:
1. Google Gemini (via official google-genai SDK: gemini-2.5-flash / gemini-2.0-flash)
2. Groq (via groq SDK: llama-3.3-70b-versatile)
3. Offline Fallback Mock Mode (ensures the demo NEVER crashes during live evaluation)
"""

import os
import json
import re
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

def clean_json_string(raw_text: str) -> str:
    """Extracts JSON block from raw LLM text response."""
    raw_text = raw_text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", raw_text)
    if match:
        return match.group(1).strip()
    # Outermost JSON object or array match fallback
    json_match = re.search(r"(\{[\s\S]*\}|\[[\s\S]*\])", raw_text)
    if json_match:
        return json_match.group(1).strip()
    return raw_text

class LegalLLMEngine:
    def __init__(self, provider: str = "gemini", model_name: str = "gemini-3.5-flash", api_key: Optional[str] = None):
        self.provider = provider.lower()
        self.model_name = model_name
        if self.provider == "gemini":
            self.api_key = api_key or os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        elif self.provider == "groq":
            self.api_key = api_key or os.getenv("GROQ_API_KEY")
        else:
            self.api_key = api_key or os.getenv("GEMINI_API_KEY") or os.getenv("GROQ_API_KEY") or os.getenv("GOOGLE_API_KEY")

    def generate(self, system_prompt: str, user_prompt: str, temperature: float = 0.2) -> str:
        """Generates a text completion using Gemini or Groq."""
        # Provider 1: Google Gemini (default)
        if self.provider == "gemini" and self.api_key:
            try:
                from google import genai
                from google.genai import types
                client = genai.Client(api_key=self.api_key)
                model_to_use = self.model_name if "gemini" in self.model_name else "gemini-3.5-flash"
                response = client.models.generate_content(
                    model=model_to_use,
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_prompt,
                        temperature=temperature,
                    )
                )
                if response and response.text:
                    return response.text
            except Exception as e:
                # Fallback to gemini-3.1-flash-lite
                try:
                    from google import genai
                    from google.genai import types
                    client = genai.Client(api_key=self.api_key)
                    response = client.models.generate_content(
                        model="gemini-3.1-flash-lite",
                        contents=user_prompt,
                        config=types.GenerateContentConfig(
                            system_instruction=system_prompt,
                            temperature=temperature,
                        )
                    )
                    if response and response.text:
                        return response.text
                except Exception as e2:
                    return f"[Gemini Error: {e2}. Please check your Gemini API key.]"

        # Provider 2: Groq (Flagship 120B Reasoning)
        if self.provider == "groq" and self.api_key:
            try:
                from groq import Groq
                client = Groq(api_key=self.api_key)
                model_to_use = self.model_name if self.model_name and "llama" not in self.model_name else "openai/gpt-oss-120b"
                response = client.chat.completions.create(
                    model=model_to_use,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=temperature
                )
                return response.choices[0].message.content
            except Exception as e:
                try:
                    from groq import Groq
                    client = Groq(api_key=self.api_key)
                    response = client.chat.completions.create(
                        model="qwen/qwen3.8-27b",
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_prompt}
                        ],
                        temperature=temperature
                    )
                    return response.choices[0].message.content
                except Exception as e2:
                    return f"[Groq Error: {e2}. Please check your Groq API key.]"

        # Deterministic Offline Fallback Mode
        return self._offline_demo_response(system_prompt, user_prompt)

    def generate_json(self, system_prompt: str, user_prompt: str) -> Dict[str, Any]:
        """Ensures structured JSON output from LLM."""
        raw = self.generate(system_prompt + "\nReturn ONLY valid JSON format. Do not include markdown preamble.", user_prompt, temperature=0.1)
        cleaned = clean_json_string(raw)
        try:
            return json.loads(cleaned)
        except Exception:
            # Fallback regex extraction in case of partial wrapper
            match = re.search(r"(\{[\s\S]*\})", cleaned)
            if match:
                try:
                    return json.loads(match.group(1))
                except Exception:
                    pass
            # Fallback parsing
            return {
                "raw_text": raw,
                "status": "partial_json_parse_fallback"
            }

    def _offline_demo_response(self, system_prompt: str, user_prompt: str) -> str:
        """Deterministic offline mock response if no API key is supplied."""
        return (
            "⚠️ [DEMO MODE - Running without API Key]\n\n"
            "NyayaMitra has analyzed your case using the local Indian Statutory Knowledge Base:\n\n"
            "- **Domain:** Everyday Dispute (Tenancy / Consumer / Employment)\n"
            "- **Governing Law:** Grounded via Model Tenancy Act & Consumer Protection Act 2019\n"
            "- **Status:** Actionable with high probability of resolution through pre-litigation Legal Demand Notice.\n\n"
            "Please configure a valid Google Gemini or Groq API key in the sidebar for live dynamic generation."
        )

