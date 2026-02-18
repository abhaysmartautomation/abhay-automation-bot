from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# ==============================================================================
# 🛠️ SETTINGS SECTION (Apne Links Yahan Paste Karein)
# ==============================================================================

# 1. Naye Luxury Card ka Google Drive link yahan dalein
VISITING_CARD_LINK = "https://drive.google.com/file/d/YOUR_NEW_IMAGE_ID/view?usp=sharing"

# 2. Rate List PDF ka Google Drive link yahan dalein
RATE_PDF_LINK = "https://drive.google.com/file/d/YOUR_PDF_ID_HERE/view?usp=sharing"

# 3. WhatsApp Catalog ya Instagram Album ka link yahan dalein
ALBUM_LINK = "https://wa.me/c/917046769047"

# ==============================================================================

@app.route("/bot", methods=['POST'])
def bot():
    # User ka message lena
    incoming_msg = request.values.get('Body', '').lower().strip()
    resp = MessagingResponse()
    msg = resp.message()
    
    # --- 🏠 MAIN MENU ---
    if incoming_msg in ['hi', 'hello', 'menu', 'start', 'namaste', 'hye']:
        response_text = (
            "✨ *Welcome to Pandey Colour* ✨\n"
            "_- Premium Interior & Exterior Finishes -_\n\n"
            "👤 **Prop:** Markandey Pandey\n"
            f"🪪 **Digital Card:** {VISITING_CARD_LINK}\n\n"
            "👇 *Krupaya ek option chunein:*\n\n"
            "1️⃣ 📊 **Rates & Estimate** (Rate List PDF)\n"
            "2️⃣ 📞 **Contact Details** (Address & Call)\n"
            "3️⃣ 🎨 **Color Selection** (Fantak/Shades)\n"
            "4️⃣ 🖼️ **Our Expertise & Album** (Latest Designs)\n"
            "5️⃣ 💸 **Payment Details** (UPI/Bank)\n\n"
            "👉 _Reply with 1, 2, 3, 4 or 5_"
        )
        msg.body(response_text)

    # --- 1. RATES ---
    elif incoming_msg == '1':
        response_text = (
            "📊 *Exclusive Rate List & Estimate*\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "Hamare standard rates ki jankari ke liye PDF download karein:\n\n"
            f"📥 **Download Rate Card:**\n{RATE_PDF_LINK}\n\n"
            "🔹 _Plastic Paint_ | _Royal Play_ | _PU Polish_\n\n"
            "💡 *Note:* Final estimate site visit ke baad diya jayega."
        )
        msg.body(response_text)

    # --- 2. CONTACT DETAILS ---
    elif incoming_msg == '2':
        response_text = (
            "📞 *Get in Touch* \n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "👷‍♂️ **Markandey Pandey**\n"
            "📱 +91 70467 69047\n"
            "📱 +91 90167 21639\n\n"
            "📍 **Office Address:**\n"
            "211/-2 Krishnakunj Society, Palanpur Jakatnaka, Surat.\n\n"
            "🕒 *Timing:* 9:00 AM - 8:00 PM"
        )
        msg.body(response_text)

    # --- 3. COLOR SELECTION (FANTAK) ---
    elif incoming_msg == '3':
        response_text = (
            "🎨 *Choose Your Perfect Shade (Fantak)*\n"
            "━━━━━━━━━━━━━━━━━━━\n\n"
            "✨ **Asian Paints (Digital Card):**\n"
            "https://www.asianpaints.com/catalogue/colour-catalogue.html\n\n"
            "✨ **Nerolac (Shade Card):**\n"
            "https://www.nerolac.com/colour-palette-shade-card.html\n\n"
            "💡 *Tip:* Jo colour pasand aaye, uska screenshot humein bhejein!"
        )
        msg.body(response_text)

    # --- 4. EXPERTISE & ALBUM ---
    elif incoming_msg == '4':
        response_text = (
            "🖼️ *Our Expertise & Portfolio* ✨\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "Hum premium quality finishing mein expert hain:\n\n"
            "✅ **Pandey Colour Speciality:**\n"
            "• Royal Play & Texture Designs\n"
            "• PU Polish & Lamination Work\n"
            "• Waterproofing Solutions\n"
            "• **All Type Contracts & Best Service**\n\n"
            f"📂 **View Our Album:** {ALBUM_LINK}\n\n"
            "💡 *Tip:* Designs ke liye brand gallery bhi check karein!"
        )
        msg.body(response_text)

    # --- 5. PAYMENT ---
    elif incoming_msg == '5':
        response_text = (
            "💸 *Payment Information*\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "🏦 **UPI ID:** `7046769047@ybl`\n"
            "📱 **GPay / PhonePe:** 70467 69047\n\n"
            "✅ *Payment ke baad screenshot bhejna na bhulein.*"
        )
        msg.body(response_text)

    # --- ❌ ERROR HANDLING ---
    else:
        msg.body("❌ Galat option. Main Menu ke liye *'Hi'* likh kar bhejein.")

    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
