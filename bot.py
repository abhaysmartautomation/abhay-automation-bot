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

    # 1. RATE LIST WALA BRANCH (Specific List)
    # Agar user specifically "list" word use kare rate ke sath
    if 'list' in incoming_msg and any(word in incoming_msg for word in ['rate', 'price', 'bhav']):
        response_text = (
            "📋 **Standard Rate List (Per Sq. Ft.)**\n\n"
            "🔹 **Plastic Paint:** ₹12 - ₹15\n"
            "🔹 **Royal Shine:** ₹22 - ₹25\n"
            "🔹 **Texture Work:** ₹50 se shuru\n"
            "🔹 **Putty Work:** ₹8 - ₹10\n\n"
            "⚠️ *Note: Ye rates area aur condition ke hisaab se thoda upar-niche ho sakte hain.*"
        )
        msg.body(response_text)

    # 2. GENERAL RATE / PRICE INQUIRY (Professional Contact Msg)
    # Agar user sirf rate/price puche bina list mange
    elif any(word in incoming_msg for word in ['rate', 'price', 'paisa', 'cost', 'bhav', 'charge']):
        response_text = (
            "🎨 **Professional & Best Rates** 🎨\n\n"
            "Market mein sabse behtareen service aur professional rates ke liye, humari team se direct baat karein.\n\n"
            "📞 **Call/WhatsApp:** +91-98XXXXXXXX\n"
            "✨ *Hum aapko site visit karke best quotation denge!*"
        )
        msg.body(response_text)

    # 3. FANTAK / COLOR CARD WALA BRANCH
    elif any(word in incoming_msg for word in ['fantak', 'card', 'shade', 'colour', 'color']):
        response_text = (
            "🎨 **Colour Shade Card (Fantak)**\n\n"
            "Aap inmein se apna pasandida shade chun sakte hain:\n\n"
            "1️⃣ **Asian Paints Royale**\n"
            "2️⃣ **Berger Silk**\n"
            "3️⃣ **Nerolac Impressions**\n\n"
            "📷 Agar aapke paas koi photo hai design ki, toh yahan bhej dijiye."
        )
        msg.body(response_text)

    # 4. DEFAULT MESSAGE
    else:
        msg.body(
            "Namaste! 🙏\n"
            "Kripya inme se kuch likh kar bhejein:\n\n"
            "👉 **'Rate List'** - Rates ki list dekhne ke liye\n"
            "👉 **'Rate'** - Best offer ke liye contact karein\n"
            "👉 **'Fantak'** - Colour card dekhne ke liye"
        )

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
