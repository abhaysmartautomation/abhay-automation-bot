from flask import Flask, request
import re  # Ye zaroori hai text saaf karne ke liye

app = Flask(__name__)

# ==============================================================================
# 🛠️ SETTINGS SECTION
# ==============================================================================

# 1. Aapka Premium Visiting Card Link (Maine add kar diya hai)
VISITING_CARD_LINK = "https://docs.google.com/document/d/1mIZxc63-QFQZDVHXA-AwpeYYnS06Nqj44Xt-or5Ixh0/edit?tab=t.0"

# 2. Rate List PDF Link (Isse aap baad mein apne Drive link se badal lena)
RATE_PDF_LINK = "https://drive.google.com/file/d/YOUR_PDF_ID_HERE/view?usp=sharing"

# 3. Album Link
ALBUM_LINK = "https://wa.me/c/917046769047"

# ==============================================================================

@app.route("/whatsapp", methods=['GET', 'POST'])
def bot():
    # Step 1: Message receive karna (Chahe GET ho ya POST)
    if request.method == 'POST':
        raw_msg = request.form.get('Body', '')
    else:
        raw_msg = request.args.get('Body', '')

    # Step 2: "SUPER CLEANING" Logic
    # Ye line message me se space, *, ., ! sab hata degi.
    # Agar user ne "*Hi*" bheja -> toh wo "hi" ban jayega.
    cleaned_msg = re.sub(r'[^a-zA-Z0-9]', '', raw_msg).lower()

    response_text = ""

    # --- 🏠 MAIN MENU ---
    # Agar message me 'hi', 'menu', 'start' jaisa kuch bhi ho
    menu_keywords = ['hi', 'hello', 'menu', 'start', 'namaste', 'hye', 'hey']
    
    # Check: Agar message khali hai YA inme se koi word hai
    if not cleaned_msg or any(word in cleaned_msg for word in menu_keywords):
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
    elif '1' in cleaned_msg:
        response_text = (
            "📊 *Exclusive Rate List & Estimate*\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            f"📥 **Download Rate Card:**\n{RATE_PDF_LINK}\n\n"
            "🔹 _Plastic Paint_ | _Royal Play_ | _PU Polish_\n\n"
            "💡 *Note:* Final estimate site visit ke baad diya jayega."
        )

    # --- 2. CONTACT ---
    elif '2' in cleaned_msg:
        response_text = (
            "📞 *Contact Details*\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "👷‍♂️ **Markandey Pandey**\n"
            "📱 +91 70467 69047\n"
            "📱 +91 90167 21639\n\n"
            "📍 **Address:** 211/-2 Krishnakunj Society, Palanpur Jakatnaka, Surat."
        )

    # --- 3. COLOR SELECTION ---
    elif '3' in cleaned_msg:
        response_text = (
            "🎨 *Color Shade Cards*\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "✨ **Asian Paints:** https://www.asianpaints.com/catalogue/colour-catalogue.html\n"
            "✨ **Nerolac:** https://www.nerolac.com/colour-palette-shade-card.html"
        )

    # --- 4. EXPERTISE ---
    elif '4' in cleaned_msg:
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
    elif '5' in cleaned_msg:
        response_text = (
            "💸 *Payment Information*\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "🏦 **UPI ID:** `7046769047@ybl`\n"
            "📱 **GPay / PhonePe:** 70467 69047\n\n"
            "✅ *Payment screenshot zaroor bhejein.*"
        )

    # --- ❌ ERROR HANDLING ---
    else:
        # Ye aapko batayega ki server ne kya receive kiya jo galat tha
        response_text = (
            f"❌ Option '{raw_msg}' samajh nahi aaya.\n"
            "Krupaya Main Menu ke liye *'Hi'* likh kar bhejein."
        )

    return response_text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

