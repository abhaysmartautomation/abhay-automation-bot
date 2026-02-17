from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# ==============================================================================
# 🛠️ SETTINGS SECTION (Apne Links Yahan Paste Karein)
# ==============================================================================

# 1. Apni Rate List PDF ka Google Drive link yahan dalein
RATE_PDF_LINK = "https://drive.google.com/your-pdf-link-here"

# 2. Apni Digital Visiting Card ka link yahan dalein
VISITING_CARD_LINK = "https://your-visiting-card-link.com"

# 3. WhatsApp Catalog ya Instagram Album ka link yahan dalein
ALBUM_LINK = "https://wa.me/c/917046769047"

# 4. Color Shade Card Link (Asian Paints/Nerolac)
COLOR_LINK = "https://www.asianpaints.com/catalogue/colour-catalogue.html"

# ==============================================================================

@app.route("/bot", methods=['POST'])
def bot():
    # User ka message clean format mein lena
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
            "4️⃣ 🖼️ **Our Work Album** (Latest Designs)\n"
            "5️⃣ 💸 **Payment Details** (UPI/Bank)\n\n"
            "👉 _Reply with 1, 2, 3, 4 or 5_"
        )
        msg.body(response_text)

    # --- 1. RATES (PDF LINK) ---
    elif incoming_msg == '1':
        response_text = (
            "📊 *Exclusive Rate List & Estimate*\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "Hamare standard rates aur services ki jankari ke liye neeche di gayi PDF download karein:\n\n"
            f"📥 **Download Rate Card (PDF):**\n{RATE_PDF_LINK}\n\n"
            "🔹 _Plastic Paint_ | _Royal Play_ | _PU Polish_\n\n"
            "💡 *Note:* Final estimate site visit ke baad diya jayega."
        )
        msg.body(response_text)

    # --- 2. CONTACT DETAILS ---
    elif incoming_msg == '2':
        response_text = (
            "📞 *Get in Touch* \n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "👷‍♂️ **Markandey Pandey** (Senior Contractor)\n"
            "📱 +91 70467 69047\n"
            "📱 +91 90167 21639\n\n"
            "📍 **Office Address:**\n"
            "211/-2 Krishnakunj Society,\n"
            "Palanpur Jakatnaka, Surat, Gujarat.\n\n"
            "🕒 *Timing:* 9:00 AM - 8:00 PM"
        )
        msg.body(response_text)

    # --- 3. COLOR SELECTION ---
    elif incoming_msg == '3':
        response_text = (
