from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import datetime
import random 

app = Flask(__name__)

OWNER_PHONE = "+919016721639" 

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
    if incoming_msg in ['hi','hii', 'hello', 'start', 'menu', 'demo']:
        reply = (
            f"🤖 *{greet}! Ultimate Business Bot.*\n"
            "━━━━━━━━━━━━━━━━━━━\n"
            "Ab yeh data 'Google Sheet' mein bhi save karega (Demo Mode)!\n\n"
            "💪 *Type 'Gym'* (Try Membership Save)\n"
            "🍔 *Type 'Cafe'* (Try Order Save)\n"
            "🩺 *Type 'Dr'* (Try Patient Entry)\n\n"
            "_Option chunein._"
        )

    # =================================================
    # 💪 1. GYM MODE 
    # =================================================
    elif 'gym' in incoming_msg:
        reply = (
            "💪 *IRON FITNESS CLUB*\n"
            "1️⃣ Membership Plans 💰\n"
            "2️⃣ *Join Now (Save Data)* 📝\n"
            "_(Reply with 1 or 2)_"
        )
    elif incoming_msg == '1':
        reply = "💰 Monthly: ₹1500 | Yearly: ₹12,000"
    elif incoming_msg == '2':
        reply = "📝 Apna *Naam* aur *Mobile Number* likh kar bhejein."
    
    # --- FAKE SAVE LOGIC (GYM) ---
    elif len(incoming_msg) > 5 and any(char.isdigit() for char in incoming_msg): 
        # Agar message lamba hai aur usme number hai (Mano user ne details bheji)
        reply = (
            "✅ *Success!*\n"
            "Aapka Data *Google Sheet (New Joinees)* mein save ho gaya hai.\n"
            "Manager aapko call karenge."
        )

    # =================================================
    # 🍔 2. CAFE MODE
    # =================================================
    elif 'cafe' in incoming_msg:
        reply = (
            "🍔 *TASTY BITES CAFE*\n"
            "4️⃣ Menu Dekhein 📜\n"
            "5️⃣ *Book Table (Save Data)* 🪑\n"
            "_(Reply with 4 or 5)_"
        )
    elif incoming_msg == '4':
        reply = "📜 Menu: Pizza (₹200), Burger (₹100)."
    elif incoming_msg == '5':
        reply = "🪑 Kitne log hain? Example: *'Table for 4'* likh kar bhejein."
    
    # --- FAKE SAVE LOGIC (CAFE) ---
    elif 'table' in incoming_msg:
        token = random.randint(100, 999) # Random Ticket Number
        reply = (
            f"✅ *Booking Confirmed!*\n"
            f"Token No: *#{token}*\n"
            "Yeh entry *Cafe_Bookings_Sheet* mein add kar di gayi hai."
        )

    # =================================================
    # 🩺 3. CLINIC MODE
    # =================================================
    elif 'dr' in incoming_msg:
        reply = (
            "🩺 *CITY HOSPITAL*\n"
            "7️⃣ Appointment 📅\n"
            "8️⃣ Emergency 🚑\n"
            "_(Reply with 7 or 8)_"
        )
    elif incoming_msg == '7':
        reply = "📅 Appointment ke liye bas *'Book'* likh kar bhejein."
    
    # --- FAKE SAVE LOGIC (DOCTOR) ---
    elif 'book' in incoming_msg:
        reply = (
            "✅ *Appointment Saved!*\n"
            "Doctor ki *Daily Schedule Sheet* mein aapka naam add ho gaya hai.\n"
            "Number: 5th in Queue."
        )

    elif incoming_msg == '8':
        reply = f"🚑 *EMERGENCY:* Call {OWNER_PHONE}"

    else:
        reply = "🤖 *Smart Bot:* Samajh nahi aya.❤️ 'Hi' 'start' ya 'menu'  likhein. 
❤️"

    msg.body(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

