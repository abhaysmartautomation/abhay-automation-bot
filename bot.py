from flask import Flask, request

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

@app.route("/whatsapp", methods=['GET', 'POST']) # Route badal kar /whatsapp kar diya
def bot():
    # User ka message lena (GET aur POST dono handle honge)
    if request.method == 'POST':
        incoming_msg = request.form.get('Body', '').lower().strip()
    else:
        incoming_msg = request.args.get('Body', '').lower().strip()
    
    response_text = ""

    # --- 🏠 MAIN MENU ---
    if incoming_msg in ['hi', 'hello', 'menu', 'start', 'namaste', 'hye']:
        response_text = (
            "✨ *Welcome to Pandey Colour* ✨\n"
            "_- Premium Interior & Exterior Finishes -_\n\n"
            "👤 **Prop:** Markandey Pandey\n"
            f"🪪 **Digital Card:** {VISITING_CARD_LINK}\n\n"
            "👇 *Krupaya ek option chunein:*\n\n"
            "1️⃣ 📊 **Rates & Estimate**\n"
            "2️⃣ 📞 **Contact Details**\n"
            "3️⃣ 🎨 **Color Selection** (Fantak)\n"
            "4️⃣ 🖼️ **Our Expertise & Album**\n"
            "5️⃣ 💸 **Payment Details**\n\n"
            "👉 _Reply with 1, 2, 3, 4 or 5_"
        )

    # --- 1. RATES ---
    elif incoming_msg == '1':
        response_text = (
            "📊 *Exclusive Rate List & Estimate*\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            f"📥 **Download Rate Card:**\n{RATE_PDF_LINK}\n\n"
            "🔹 _Plastic Paint_ | _Royal Play_ | _PU Polish_\n\n"
            "💡 *Note:* Final estimate site visit ke baad diya jayega."
        )

    # --- 2. CONTACT DETAILS ---
    elif incoming_msg == '2':
        response_text = (
            "📞 *Get in Touch* \n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "👷‍♂️ **Markandey Pandey**\n"
            "📱 +91 70467 69047\n"
            "📱 +91 90167 21639\n\n"
            "📍 **Address:** 211/-2 Krishnakunj Society, Palanpur Jakatnaka, Surat."
        )

    # --- 3. COLOR SELECTION ---
    elif incoming_msg == '3':
        response_text = (
            "🎨 *Color Shade Cards*\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "✨ **Asian Paints:** https://www.asianpaints.com/catalogue/colour-catalogue.html\n"
            "✨ **Nerolac:** https://www.nerolac.com/colour-palette-shade-card.html"
        )

    # --- 4. EXPERTISE & ALBUM ---
    elif incoming_msg == '4':
        response_text = (
            "🖼️ *Our Expertise & Portfolio* ✨\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "• Royal Play & Texture Designs\n"
            "• PU Polish & Lamination Work\n"
            "• Waterproofing Solutions\n"
            "• **All Type Contracts & Best Service**\n\n"
            f"📂 **View Our Album:** {ALBUM_LINK}"
        )

    # --- 5. PAYMENT ---
    elif incoming_msg == '5':
        response_text = (
            "💸 *Payment Information*\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "🏦 **UPI ID:** `7046769047@ybl`\n"
            "📱 **GPay / PhonePe:** 70467 69047\n\n"
            "✅ *Payment screenshot zaroor bhejein.*"
        )

    # --- ❌ ERROR ---
    else:
        response_text = "❌ Galat option. Main Menu ke liye *'Hi'* likh kar bhejein."

    # Seedha text return kar rahe hain MacroDroid ke liye
    return response_text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
