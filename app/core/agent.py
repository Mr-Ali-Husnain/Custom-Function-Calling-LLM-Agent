import re
import json
from dotenv import load_dotenv
import os
import google.generativeai as genai
from datetime import datetime

# import tools
from app.tools import (
    tool_qr,
    tool_calculator,
    tool_search,
    tool_time,
    tool_weather,
)

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_KEY")
if not GEMINI_KEY:
    raise ValueError("Gemini Key missing in .env")

# configure Gemini
genai.configure(api_key=GEMINI_KEY)


class Agent:
    def __init__(self, model_name: str = "gemini-2.0-flash", temperature: float = 0.3):
        self.model_name = model_name
        self.temperature = temperature
        self.model = genai.GenerativeModel(self.model_name)
        # chat session object
        self.chat = self.model.start_chat(history=[])
    
 
    # ------------------------
    # detection helpers
    # ------------------------
    def _is_qr_request(self, msg: str):
        # robust regex to catch many variants
        return bool(re.search(r'\bqr\b|qrcode|qr bana|qr banao|make.*qr|generate.*qr', msg, flags=re.IGNORECASE))

    def _extract_url(self, msg: str):
        m = re.search(r'(https?://\S+|www\.\S+)', msg, flags=re.IGNORECASE)
        return m.group(0) if m else None

    def _extract_phone(self, msg: str):
        m = re.search(r'\b\d{7,15}\b', msg)
        return m.group(0) if m else None

    def _extract_email(self, msg: str):
        m = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', msg)
        return m.group(0) if m else None

    # ------------------------
    # main chat loop
    # ------------------------
    def start_chat(self):
        print(f"{self.model_name} Chat Started (type 'exit' to stop)\n")
        while True:
            try:
                user_input = input("You: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\nChat ended.")
                break

            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit", "bye", "end"]:
                print("Chat ended.")
                break

            msg = user_input.lower()

            # 1) QR detection & handling
            if self._is_qr_request(msg):
                phone = self._extract_phone(msg)
                if phone:
                    print("AI:", tool_qr(phone))
                    continue

                url = self._extract_url(msg)
                if url:
                    print("AI:", tool_qr(url))
                    continue

                email = self._extract_email(msg)
                if email:
                    print("AI:", tool_qr(email))
                    continue

                # fallback: remove qr words and use remaining text
                cleaned = re.sub(r'\bqr\b|qrcode', '', user_input, flags=re.IGNORECASE).strip()
                if cleaned:
                    print("AI:", tool_qr(cleaned))
                    continue

                # last fallback
                print("AI:", tool_qr(user_input))
                continue

            # 2) Calculator detection (simple)
            if any(op in msg for op in ["+", "-", "*", "/"]) and re.match(r'^[0-9+\-*/(). ]+$', msg):
                print("AI:", tool_calculator(msg))
                continue

            # 3) Search detection
            if any(k in msg for k in ["search", "google", "find"]):
                query = re.sub(r'\b(search|google|find)\b', '', user_input, flags=re.IGNORECASE).strip()
                if not query:
                    print("AI: What should I search for?")
                    continue
                print("AI:", tool_search(query))
                continue

            # 4) Weather detection
            if "weather" in msg or "mosam" in msg:
                parts = user_input.split()
                city = parts[-1] if len(parts) > 0 else ""
                if not city:
                    print("AI: Please tell me city. Example → weather Karachi")
                    continue
                print("AI:", tool_weather(city))
                continue

            # 5) Time detection
            if "time" in msg or "waqt" in msg:
                print("AI:", tool_time())
                continue

            # 6) Normal LLM conversation
            try:
                response = self.chat.send_message(
                    user_input,
                    generation_config={"temperature": self.temperature}
                )
                print("AI:", response.text)
            except Exception as e:
                print("AI Error:", str(e))
