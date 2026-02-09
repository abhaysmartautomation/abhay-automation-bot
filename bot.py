from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import datetime
import random

app = Flask(__name__)

# --- ⚙️ SETTINGS ---
OWNER_PHONE = "+919016721639" 

# --- 🕒 SMART GREETING ---
def get_greeting():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12: return "Good Morning ☀️"
    elif 12 <= hour < 17: return "Good Afternoon 🌤️"
    elif 17 <= hour < 22: return "Good Evening 🌆"
    else: return "Hello 👋"

@app.route('/whatsapp', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower().strip()
    resp = MessagingResponse()
    msg = resp.message()
    
    greet = get_greeting()

    # --- 🏠 MAIN MENU ---
    if incoming_msg in ['hi', 'hello', 'start', 'menu', 'demo']:
        reply = (
            f"🤖 *{greet}! Ultimate Business Bot.*\n"
            "━━━━━━━━━━━━━━━━━━━\n"
            "Yeh bot calculation aur games bhi khel sakta hai!\n\n"
            "💪 *Type 'Gym'* (Try BMI Calculator)\n"
            "🍔 *Type 'Cafe'* (Try Discount Game)\n"
            "🩺 *Type 'Dr'* (Try Symptom Check)\n\n"
            "_Ek option chunein._"
        )

    # =================================================
    # 💪 GYM MODE
    # =================================================
    elif 'gym' in incoming_msg:
        reply = (
            "💪 *IRON FITNESS CLUB*\n"
            "1️⃣ Membership Plans 💰\n"
            "2️⃣ *Check Your BMI* 🧮\n"
            "3️⃣ Diet Chart 🥗\n"
            "_(Reply with 1, 2, or 3)_"
        )
    elif incoming_msg == '1':
        reply = "💰 Monthly: ₹1500 | Yearly: ₹12,000 (With AC)"
    elif incoming_msg == '2':
        reply = "🧮 Apna BMI janne ke liye aise likhein:\n*BMI 70 1.75*\n_(Weight kg mein aur Height meters mein)_"
    elif 'bmi' in incoming_msg:
        try:
            parts = incoming_msg.split()
            weight = float(parts[1])
            height = float(parts[2])
            bmi = round(weight / (height * height), 1)
            reply = f"📊 *Result:*\nAapka BMI hai: *{bmi}*"
        except:
            reply = "❌ Format: *BMI 70 1.75*"
    elif incoming_msg == '3':
        reply = "🥗 *Diet:* Subah Oats, Dopahar Dal-Rice, Raat Salad."

    # =================================================
    # 🍔 CAFE MODE
    # =================================================
    elif 'cafe' in incoming_msg:
        reply = (
            "🍔 *TASTY BITES CAFE*\n"
            "4️⃣ Menu Dekhein 📜\n"
            "5️⃣ *Spin & Win Gift* 🎁\n"
            "6️⃣ Book Table 🪑\n"
            "_(Reply with 4, 5, or 6)_"
        )
    elif incoming_msg == '4':
        reply = "📜 Pizza (₹200), Burger (₹100), Coffee (₹80)."
    elif incoming_msg == '5':
        gifts = ["🎉 Free Cookie! 🍪", "🎉 10% Off! 🏷️", "😢 Try Again."]
        reply = random.choice(gifts)
    elif incoming_msg == '6':
        reply = "🪑 Table book karne ke liye naam bhejein."
    elif len(incoming_msg) > 3 and 'book' not in incoming_msg and 'gym' not in incoming_msg:
         # Fake Save Logic
         reply = "✅ *Saved!* Aapka data Google Sheet mein save ho gaya hai."

    # =================================================
    # 🩺 DOCTOR MODE
    # =================================================
    elif 'dr' in incoming_msg:
        reply = (
            "🩺 *CITY HOSPITAL*\n"
            "7️⃣ Appointment 📅\n"
            "8️⃣ *Symptom Checker* 🤒\n"
            "_(Reply with 7 or 8)_"
        )
    elif incoming_msg == '7':
        reply = "📅 Call karein: " + OWNER_PHONE
    elif incoming_msg == '8':
        reply = "🤒 Bukhar hai to *'Fever'* likhein, Sar dard hai to *'Headache'*."
    elif 'fever' in incoming_msg:
        reply = "💊 Paracetamol lein aur aaram karein."

    else:
        reply = "🤖 *Smart Bot:* Samajh nahi aya. 'Hi' likhein."

    msg.body(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

