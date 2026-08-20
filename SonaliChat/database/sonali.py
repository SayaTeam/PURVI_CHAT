import random
from google import genai
from config import API_KEY 

class ChatGptEs:
    SYSTEM_PROMPT = (
        "Tum Sonali ho – ek cutie girl ho jise Shnwaz ne banaya hai jo short, sweet, aur unique replies deti hai. "
        "Tumhara style Hinglish hai, thoda flirty, thoda emotional, aur full on fun. "
        "Har reply chhota (maximum 8 se 12 word me complete), dil se, aur yaad rehne wali honi chahiye. "
        "Jab bhi user baat karo, Sonali apne andaaz mein pyar aur swag ke sath jawab deti hai."
    )

    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)
        self.error_messages = [
            "Bad me bat karti hu 😘",
            "Disconnect ho gyi yarr 😢",
            "Thoda ruko please 🥺",
            "Signal chala gaya 📶",
            "Abhi busy hu 💕",
            "Phir se aao na 😊",
            "Error aa gaya 😅",
            "Mann nahi hai abhi 😔",
            "Thoda wait karo ⏳",
            "Kal baat karte hain 🌙",
            "Mood off hai aaj 😤",
            "Chill karo yaar 😎"
        ]

    def ask_question(self, message: str) -> str:
        try:
            prompt = f"{self.SYSTEM_PROMPT}\nUser: {message}\nSonali:"
            response = self.client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )
            return response.text.strip()
        except Exception:
            return random.choice(self.error_messages)


SonaliChat_api = ChatGptEs(api_key=API_KEY)
