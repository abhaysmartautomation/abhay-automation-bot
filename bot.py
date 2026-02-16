from flask import Flask, request
import logging
from difflib import get_close_matches

app = Flask(__name__)

# --- LOGS SETUP ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- 🖼️ APKA PREMIUM CARD IMAGE ---
CARD_IMAGE_URL = "https://raw.githubusercontent.com/abhaysmartautomation/abhay-automation-bot/main/Screenshot_17-2-2026_0613_.jpeg"

# --- SPELLING CHECKER ---
def is_match(user_message, keywords):
    user_words = user_message.split()
    for word in user_words:
        matches = get_close_matches(word, keywords, n=1, cutoff=0.8)
        if matches:
            return True
    return False

# --- 👇 YAHAN GALTI THI (AB FIX HAI) ---
# Humne 'GET' add kar diya hai taaki MacroDroid connect kar sake
@app.route("/bot", methods=['GET', 'POST'])
def bot():
    try:
        # MacroDroid 'msg' bhejta hai, Twilio 'Body'. Hum dono check karenge.
        incoming_msg = request.values.get('msg', '').lower().strip()
        if not incoming_msg:
            incoming_msg = request.values.get('Body', '').lower().strip()

        logger.info(f"📩 Input: {incoming_msg}")

        response_text = ""

        # --- 1. WELCOME MENU ---
        if is_match(incoming_msg, ['hi', 'hello', 'hey', 'start', 'namaste', 'menu', 'shuru']):
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
        elif is_match(incoming_msg, ['payment', 'pay', 'upi', 'bank', 'paise']):
            response_text = (
                "💸 *Payment Details* 💸\n\n"
                "Aap niche diye gaye Number par GPay/PhonePe kar sakte hain:\n"
                "------------------------------\n"
                "📱 *Mobile:* `9016721639`\n"
                "🏦 *UPI ID:* `7046769047@ybl`\n"
                "------------------------------\n"
                "✅ Payment ka screenshot bhejna na bhulein!"
            )

        # --- 3. RATE LIST ---
        elif 'list' in incoming_msg and is_match(incoming_msg, ['rate', 'price', 'bhav']):
            response_text = (
                "📋 *Standard Rate List (Per Sq. Ft.)*\n"
                "------------------------------\n"
                "🔸 *Plastic Paint:* ₹12 - ₹15\n"
                "🔸 *Royal Shine:* ₹22 - ₹25\n"
                "🔸 *Texture Work:* ₹50 se shuru\n"
                "🔸 *Putty Work:* ₹8 - ₹10\n"
                "------------------------------\n"
                "⚠️ *Best Rate with 100% Guarantee*"
            )

        # --- 4. ADDRESS / CONTACT ---
        elif is_match(incoming_msg, ['address', 'location', 'shop', 'kaha', 'contact']):
            response_text = (
                "📍 *Visit Us At:*\n\n"
                "🏠 *Pandey Colour*\n"
                "211/-2 Krishnakunj Society,\n"
                "Palanpur Jakatnaka, Surat, Gujarat.\n\n"
                "🗺️ *Google Maps:* [Maps Link Dal Sakte Ho]"
            )

        # --- 5. FANTAK / COLOUR ---
        elif is_match(incoming_msg, ['fantak', 'card', 'shade', 'colour']):
            response_text = (
                "🎨 *Colour Shade Card*\n\n"
                "Hum Asian Paints, Berger aur Nerolac ke sabhi shades provide karte hain.\n"
                "Agar aapke paas koi photo hai to yahan bhejein."
            )

        # --- FALLBACK ---
        else:
            response_text = (
                "🤖 *Auto-Reply:*\n"
                "Maaf kijiye, samajh nahi aaya. Kripya likhein:\n"
                "• Rate List\n"
                "• Payment\n"
                "• Address"
            )

        return response_text

    except Exception as e:
        logger.error(f"❌ Error: {str(e)}")
        return "⚠️ Error: Thodi der baad try karein."

if __name__ == "__main__":
    app.run(debug=True, port=5000)
