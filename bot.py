from flask import Flask, request
import re

app = Flask(__name__)

# ==============================================================================
# 🛠️ SETTINGS SECTION
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

    # Message ko saaf karna (Lowercase aur spaces hatana)
    msg = re.sub(r'[^a-zA-Z0-9]', '', raw_msg).lower()
    
    # --- 1. RATES (Keywords: 1, rate, price, kitna, paisa) ---
    if any(x in msg for x in ['1', 'rate', 'price', 'kitna', 'cost', 'estimate']):
        return (
            "╔══════════════════════╗\n"
            "   📊  *RATE LIST & ESTIMATE*\n"
            "╚══════════════════════╝\n\n"
            "Hamari latest rate list download karein:\n\n"
            f"📥 *LINK:* {RATE_PDF_LINK}\n\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖"
        )

    # --- 2. COLORS (Keywords: 2, color, shade, paint, catalogue) ---
    elif any(x in msg for x in ['2', 'color', 'shade', 'paint', 'design', 'catalogue']):
        return (
            "╔══════════════════════╗\n"
            "   🎨  *CHOOSE YOUR COLOUR*\n"
            "╚══════════════════════╝\n\n"
            "🏠 *Asian Paints:* https://bit.ly/AsianPaints-Catalogue\n"
            "🏢 *Nerolac:* https://bit.ly/Nerolac-Shades\n\n"
            "*✨YE COMPANY KA ONLINE FANTAK FOR COLOUR CONFORMATION✨" 
            "➖➖➖➖➖➖➖➖➖➖➖➖"
        )

    # --- 3. CONTACT & PAYMENT (Keywords: 3, contact, payment, upi, gpay, phonepe, call, number) ---
    elif any(x in msg for x in ['3', 'contact', 'payment', 'upi', 'gpay', 'phonepe', 'call', 'number', 'pay']):
        return (
            "╔══════════════════════╗\n"
            "   📞  *CONTACT DETAILS*\n"
            "╚══════════════════════╝\n"
            "👤 *Markandey Pandey*\n"
            "📱 *Direct Call/Chat:* https://wa.me/917046769047\n"
            "📱 *Office:* https://wa.me/919016721639\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "╔══════════════════════╗\n"
            "   💸  *PAYMENT INFO*\n"
            "╚══════════════════════╝\n"
            "🔹 *Click to Pay:* \n"
            "https://upilinks.in/payment-button/7046769047@ybl \n\n"
            "👆 _Upar link par click karke GPay/PhonePe chunein_\n\n"
            "✅ *Payment ke baad screenshot bhejein.*"
        )

    # --- 🏠 MAIN MENU (Keywords: hi, hello, menu, start, ya kuch aur) ---
    else:
        return (
            "✨ *WELCOME TO PANDEY COLOURS* ✨\n"
            "   _Premium Interior & Exterior Finishes_\n\n"
            f"{FINAL_CARD_LINK}\n"
            "━━━━━━━━━━━━━━━━━━━━━━━\n"
            "👤 **Prop:** Markandey Pandey\n"
            "━━━━━━━━━━━━━━━━━━━━━━━\n"
            "👇 *Krupaya ek option chunein:*\n\n"
            "1️⃣  📊  **Rates & Estimate**\n"
            "2️⃣  🎨  **Color Selection**\n"
            "3️⃣  📞  **Contact & Payment**\n\n"
            "👉 _Reply with 1, 2 or 3_"
        )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
