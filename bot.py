from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    # User ka message small letters mein convert karte hain
    incoming_msg = request.values.get('Body', '').lower().strip()
    
    # Response object
    resp = MessagingResponse()
    msg = resp.message()

    # --- BRANCHING LOGIC ---

    # 1. PAYMENT WALA BRANCH (New Add Kiya Hai)
    if any(word in incoming_msg for word in ['payment', 'pay', 'upi', 'bank', 'paise']):
        response_text = (
            "💸 **Payment Details** 💸\n\n"
            "Aap niche diye gaye UPI ID par payment kar sakte hain:\n\n"
            "📱 **UPI ID:** `7046769047@ybl`\n\n"
            "✅ *Payment karne ke baad screenshot zaroor bhejein!*"
        )
        msg.body(response_text)

    # 2. RATE LIST WALA BRANCH
    elif 'list' in incoming_msg and any(word in incoming_msg for word in ['rate', 'price', 'bhav']):
        response_text = (
            "📋 **Standard Rate List (Per Sq. Ft.)**\n\n"
            "🔹 **Plastic Paint:** ₹12 - ₹15\n"
            "🔹 **Royal Shine:** ₹22 - ₹25\n"
            "🔹 **Texture Work:** ₹50 se shuru\n"
            "🔹 **Putty Work:** ₹8 - ₹10\n\n"
            "⚠️ *Rates area aur condition ke hisaab se change ho sakte hain.*"
        )
        msg.body(response_text)

    # 3. CONTACT / GENERAL RATE INQUIRY
    elif any(word in incoming_msg for word in ['rate', 'price', 'contact', 'call', 'number', 'baat']):
        response_text = (
            "📞 **Contact Us** 📞\n\n"
            "Best rates aur professional work ke liye humari team se direct baat karein:\n\n"
            "📱 **Mobile:** +91-98XXXXXXXX\n"
            "🏠 **Address:** Adajan, Surat, Gujarat.\n\n"
            "✨ *Hum jald hi aapko reply karenge!*"
        )
        msg.body(response_text)

    # 4. FANTAK / COLOUR CARD BRANCH
    elif any(word in incoming_msg for word in ['fantak', 'card', 'shade', 'colour', 'color']):
        response_text = (
            "🎨 **Colour Shade Card (Fantak)**\n\n"
            "Apna pasandida shade choose karein:\n\n"
            "1️⃣ **Asian Paints Royale**\n"
            "2️⃣ **Berger Silk**\n"
            "3️⃣ **Texture Designs**\n\n"
            "📷 Koi photo hai toh yahan share karein."
        )
        msg.body(response_text)

    # 5. DEFAULT (ATTRACTIVE WELCOME MENU)
    else:
        msg.body(
            "🏠 **Welcome to pandey colour paint!** 🎨\n\n"
            "Namaste! 🙏 Main aapki kya madad kar sakta hu?\n"
            "Kripya ek option type karke bhejein:\n\n"
            "📋 **'Rate List'** - Rates dekhne ke liye\n"
            "🎨 **'Fantak'** - Colour Card ke liye\n"
            "💸 **'Payment'** - Bank/UPI details ke liye\n"
            "📞 **'Contact Us'** - Humse baat karne ke liye"
        )

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
