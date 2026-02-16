from flask import Flask, request
import logging
from difflib import get_close_matches

app = Flask(__name__)

# --- LOGS SETUP ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- 🖼️ IMAGE LINK ---
# Yahan wo link dalna jo aapne Step 2 mein GitHub se copy kiya
CARD_IMAGE_URL = "https://raw.githubusercontent.com/username/repo/main/card.jpg" 

# --- SPELLING CHECKER ---
def is_match(user_message, keywords):
    user_words = user_message.split()
    for word in user_words:
        matches = get_close_matches(word, keywords, n=1, cutoff=0.8)
        if matches:
            return True
    return False

@app.route("/bot", methods=['GET', 'POST'])
def bot():
    try:
        incoming_msg = request.values.get('msg', '').lower().strip()
        logger.info(f"📩 Input: {incoming_msg}")

        response_text = ""

        # --- 1. WELCOME MENU (Pandey Colour Card Style) ---
        if is_match(incoming_msg, ['hi', 'hello', 'hey', 'start', 'namaste', 'menu']):
            
            # Ye Text bilkul aapke card jaisa design kiya hai
            menu_text = (
                "🎨 *PANDEY COLOUR* 🎨\n"
                "_Premium Interior & Exterior Finishes_\n"
                "----------------------------------\n"
                "👤 *Markandey Pandey* (Senior Contractor)\n"
                "📞 +91 70467 69047\n"
                "📞 +91 90167 21639\n"
                "----------------------------------\n"
                "✨ *Our Expertise:*\n"
                "🔹 Royal Play & Texture Designs\n"
                "🔹 PU Polish & Lamination Work\n"
                "🔹 Waterproofing Solutions\n"
                "🔹 Complete Project Management\n\n"
                "👇 *Kripya ek option type karein:*\n"
                "📋 *Rate List* - Rates dekhne ke liye\n"
                "💸 *Payment* - Bank Details ke liye\n"
                "📍 *Address* - Shop Address ke liye"
            )
            
            # Agar image link hai to image + text bhejo
            if "http" in CARD_IMAGE_URL and "your-image" not in CARD_IMAGE_URL:
                response_text = f"{CARD_IMAGE_URL}\n\n{menu_text}"
            else:
                response_text = menu_text

        # --- 2. PAYMENT BRANCH ---
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
