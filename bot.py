from flask import Flask, request
import logging
from difflib import get_close_matches

app = Flask(__name__)

# --- LOGS SETUP ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- 🖼️ IMAGE LINK ---
CARD_IMAGE_URL = "https://raw.githubusercontent.com/abhaysmartautomation/abhay-automation-bot/main/Screenshot_17-2-2026_0613_.jpeg"

# --- SPELLING CHECKER ---
def is_match(user_message, keywords):
    user_words = user_message.split()
    for word in user_words:
        matches = get_close_matches(word, keywords, n=1, cutoff=0.8)
        if matches:
            return True
    return False

# --- 👇 IMPORTANT: GET AUR POST DONO ALLOW KIYE ---
@app.route("/bot", methods=['GET', 'POST'])
def bot():
    try:
        # MacroDroid 'msg' bhejta hai
        incoming_msg = request.values.get('msg', '').lower().strip()
        
        # Agar msg khali hai to body check karo (Backup)
        if not incoming_msg:
            incoming_msg = request.values.get('Body', '').lower().strip()

        logger.info(f"📩 Input: {incoming_msg}")
        response_text = ""

        # --- 1. MENU ---
        if is_match(incoming_msg, ['hi', 'hello', 'hey', 'start', 'namaste', 'menu']):
            menu_text = (
                "🎨 *PANDEY COLOUR* 🎨\n"
                "_Premium Interior & Exterior Finishes_\n"
                "----------------------------------\n"
                "👤 *Markandey Pandey* (Senior Contractor)\n"
                "📞 +91 70467 69047\n"
                "📞 +91 90167 21639\n"
                "----------------------------------\n"
                "👇 *Kripya ek option type karein:*\n"
                "📋 *Rate List* - Rates dekhne ke liye\n"
                "💸 *Payment* - Bank Details ke liye\n"
                "📍 *Address* - Shop Address ke liye"
            )
            response_text = f"{CARD_IMAGE_URL}\n\n{menu_text}"

        # --- 2. PAYMENT ---
        elif is_match(incoming_msg, ['payment', 'pay', 'upi', 'bank']):
            response_text = (
                "💸 *Payment Details* 💸\n\n"
                "📱 *Mobile:* `9016721639`\n"
                "🏦 *UPI ID:* `7046769047@ybl`\n"
                "✅ Screenshot bhejna na bhulein!"
            )

        # --- 3. RATE LIST ---
        elif 'list' in incoming_msg and is_match(incoming_msg, ['rate', 'price']):
            response_text = (
                "📋 *Standard Rate List (Per Sq. Ft.)*\n"
                "------------------------------\n"
                "🔸 *Plastic Paint:* ₹12 - ₹15\n"
                "🔸 *Royal Shine:* ₹22 - ₹25\n"
                "🔸 *Texture Work:* ₹50 se shuru\n"
                "🔸 *Putty Work:* ₹8 - ₹10\n"
                "------------------------------\n"
                "⚠️ *Best Rate Guaranteed*"
            )

        # --- 4. ADDRESS ---
        elif is_match(incoming_msg, ['address', 'location', 'shop', 'contact']):
            response_text = (
                "📍 *Pandey Colour*\n"
                "211/-2 Krishnakunj Society,\n"
                "Palanpur Jakatnaka, Surat."
            )
        
        # --- 5. FALLBACK ---
        else:
            response_text = "Maaf karein, samajh nahi aaya. Type: Rate List, Payment, or Address."

        return response_text

    except Exception as e:
        logger.error(f"❌ Error: {str(e)}")
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
