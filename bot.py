from flask import Flask, request
import re

app = Flask(__name__)

# ==============================================================================
# 🛠️ SETTINGS
# ==============================================================================
RAW_DRIVE_LINK = "https://drive.google.com/file/d/1NRm861WbxsTJFp_JyMsti_BsBg8ksESH/view?usp=sharing"
RATE_PDF_LINK = "https://drive.google.com/file/d/YOUR_PDF_ID_HERE/view?usp=sharing"

def get_direct_image(url):
    try:
        if "/d/" in url:
            file_id = url.split('/d/')[1].split('/')[0]
            return f"https://lh3.googleusercontent.com/d/{file_id}"
        return url
    except:
        return url

FINAL_CARD_LINK = get_direct_image(RAW_DRIVE_LINK)

@app.route("/whatsapp", methods=['GET', 'POST'])
def bot():
    if request.method == 'POST':
        raw_msg = request.form.get('Body', '')
    else:
        raw_msg = request.args.get('Body', '')

    msg = re.sub(r'[^a-zA-Z0-9]', '', raw_msg).lower()

    # --- 1. RATES ---
    if any(x in msg for x in ['1', 'rate', 'price', 'kitna', 'cost', 'estimate']):
        return (
            "📊 *RATES & ESTIMATES*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Review our standard pricing and project estimates.\n\n"
            "📥 *Download Latest Rate List:*\n"
            f"{RATE_PDF_LINK}\n\n"
            "_Note: Final estimates may vary based on site inspection._"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
        )

    # --- 2. COLORS ---
    elif any(x in msg for x in ['2', 'color', 'shade', 'paint', 'design', 'catalogue']):
        return (
            "🎨 *COLOR CATALOGUES*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Explore shade cards from premium brands:\n\n"
            "🔸 *Asian Paints:*\n"
            "🔗 https://bit.ly/AsianPaints-Catalogue\n\n"
            "🔸 *Kansai Nerolac:*\n"
            "🔗 https://bit.ly/Nerolac-Shades"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
        )

    # --- 3. CONTACT & PAYMENT ---
    elif any(x in msg for x in ['3', 'contact', 'payment', 'upi', 'gpay', 'phonepe', 'call', 'number', 'pay']):
        return (
            "📞 *CONTACT INFORMATION*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "👤 *Markandey Pandey* (Senior Contractor)\n"
            "▪️ *Chat / Call:* https://wa.me/917046769047\n"
            "▪️ *Direct Desk:* https://wa.me/919016721639\n\n"
            "💳 *SECURE PAYMENT*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "▪️ *UPI ID:* `7046769047@ybl`\n"
            "▪️ *1-Click Pay:* https://upilinks.in/payment-button/7046769047@ybl\n\n"
            "✅ _Kindly share a transaction screenshot once completed._"
        )

    # --- 🏠 MAIN MENU ---
    else:
        return (
            "🏢 *PANDEY COLOURS*\n"
            "_Premium Interior & Exterior Finishes_\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"visiting card »» {FINAL_CARD_LINK}\n\n"
            "Hello! Welcome to our digital desk.\n"
            "👤 *Prop:* Markandey Pandey\n\n"
            "Please select an option from our service menu below:\n\n"
            "1️⃣ 📊 *Rates & Estimates*\n"
            "2️⃣ 🎨 *Color Catalogues*\n"
            "3️⃣ 📞 *Contact & Secure Payment*\n\n"
            "💬 _Reply with 1, 2, or 3 to proceed._"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
        )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
