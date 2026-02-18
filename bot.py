from flask import Flask, request
import re

app = Flask(__name__)

# ==============================================================================
# 🛠️ SETTINGS SECTION
# ==============================================================================

# ✅ Aapka naya Google Drive Link (Maine yahan daal diya hai)
RAW_DRIVE_LINK = "https://drive.google.com/file/d/1NRm861WbxsTJFp_JyMsti_BsBg8ksESH/view?usp=sharing"

# Rate List Link
RATE_PDF_LINK = "https://drive.google.com/file/d/YOUR_PDF_ID_HERE/view?usp=sharing"

# Album Link
ALBUM_LINK = "https://wa.me/c/917046769047"

# ==============================================================================
# ⚙️ MAGIC ENGINE (Ye Link ko Image banayega - Isse mat chedhna)
# ==============================================================================
def get_direct_image(url):
    try:
        if "/d/" in url:
            # Link mein se ID nikal kar Direct Link banana
            file_id = url.split('/d/')[1].split('/')[0]
            # Ye 'uc' wala link WhatsApp par image dikhata hai
            return f"https://drive.google.com/uc?export=view&id={file_id}"
        return url
    except:
        return url

# Code start hote hi Link ko convert kar lega
FINAL_CARD_LINK = get_direct_image(RAW_DRIVE_LINK)

@app.route("/whatsapp", methods=['GET', 'POST'])
def bot():
    # MacroDroid se message lena
    if request.method == 'POST':
        raw_msg = request.form.get('Body', '')
    else:
        raw_msg = request.args.get('Body', '')

    # Message saaf karna
    cleaned_msg = re.sub(r'[^a-zA-Z0-9]', '', raw_msg).lower()
    response_text = ""

    # --- 🏠 MAIN MENU (Photo Sabse Upar) ---
    if any(word in cleaned_msg for word in ['hi', 'hello', 'menu', 'start', 'namaste']) or not cleaned_msg:
        response_text = (
            f"{FINAL_CARD_LINK}\n\n"  # 👈 Ye Card ki photo dikhayega
            "✨ *Welcome to Pandey Colour* ✨\n"
            "_- Premium Interior & Exterior Finishes -_\n\n"
            "👤 **Prop:** Markandey Pandey\n"
            "👇 *Krupaya ek option chunein:*\n\n"
            "1️⃣ 📊 **Rates & Estimate**\n"
            "2️⃣ 📞 **Contact Details**\n"
            "3️⃣ 🎨 **Color Selection**\n"
            "4️⃣ 🖼️ **Our Expertise & Album**\n"
            "5️⃣ 💸 **Payment Details**"
        )

    # --- OPTIONS ---
    elif '1' in cleaned_msg:
        response_text = f"📊 *Rate List & Estimate*\n\n📥 Download: {RATE_PDF_LINK}"

    elif '2' in cleaned_msg:
        response_text = (
            f"{FINAL_CARD_LINK}\n\n" # Yahan bhi card dikhega
            "📞 *Contact Details*\n"
            "👷‍♂️ **Markandey Pandey**\n📱 +91 70467 69047\n📍 211/-2 Krishnakunj Society, Surat."
        )

    elif '3' in cleaned_msg:
        response_text = "🎨 *Color Shade Cards*\n\nAsian Paints: https://www.asianpaints.com/catalogue/colour-catalogue.html"

    elif '4' in cleaned_msg:
        response_text = (
            "🖼️ *Our Expertise & Album* ✨\n\n"
            "• Royal Play & Texture Designs\n"
            "• PU Polish & Lamination\n"
            "• Waterproofing Solutions\n"
            "• **All Type Contracts**\n\n"
            f"📂 **Album:** {ALBUM_LINK}"
        )

    elif '5' in cleaned_msg:
        response_text = "💸 *Payment*\nUPI: `7046769047@ybl`\nGPay: 70467 69047"

    else:
        response_text = "❌ Galat option. Main Menu ke liye *'Hi'* bhejein."

    return response_text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
