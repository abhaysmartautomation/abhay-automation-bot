from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import datetime
import csv
import os

app = Flask(__name__)

# --- 🏢 BUSINESS DETAILS (Ye rahi tumhari details) ---
BUSINESS_NAME = "TechWizard Solutions"
OWNER_NAME = "Mr. Pandey"
OWNER_NUMBER = "+91 90167 21639"       # ✅ Tumhara Number Add Kar Diya
OWNER_EMAIL = "mk041982pandey@gmail.com" # ✅ Tumhara Email Add Kar Diya
LOCATION = "Surat, Gujarat"

# --- 📂 DATA SAVING SYSTEM (Excel) ---
def save_lead(mobile, category, message="N/A"):
    filename = "business_leads.csv"
    try:
        file_exists = os.path.isfile(filename)
        with open(filename, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Date", "Time", "Customer Mobile", "Category", "Message"])
            
            now = datetime.datetime.now()
            writer.writerow([now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), mobile, category, message])
            print(f"✅ Lead Saved: {mobile} -> {category}")
    except Exception as e:
        print(f"❌ Saving Error: {e}")

# --- 📅 TIME BASED GREETING ---
def get_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12: return "Good Morning ☀️"
    elif 12 <= hour < 18: return "Good Afternoon 🌤️"
    else: return "Good Evening 🌙"

@app.route("/whatsapp", methods=['POST'])
def bot():
    # 1. Message Processing
    incoming_msg = request.values.get('Body', '').strip()
    msg_lower = incoming_msg.lower()
    sender_number = request.values.get('From', '').replace('whatsapp:', '')
    
    # 2. Response Setup
    resp = MessagingResponse()
    msg = resp.message()
    
    # --- 🤖 MAIN MENU LOGIC ---

    # ➤ START / MENU
    if msg_lower in ['hi', 'hello', 'start', 'menu', 'hii','hey', 'help']:
        greeting = get_greeting()
        reply = (
            f"👋 *{greeting}, Welcome to {BUSINESS_NAME}!*\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "Hum premium IT & Automation services provide karte hain.\n\n"
            "👇 *Kripya ek seva (service) chunein:*\n"
            "1️⃣ *Web Scraping & Data* 🕷️\n"
            "2️⃣ *App & Game Development* 📱\n"
            "3️⃣ *Business Automation Bots* 🤖\n"
            "4️⃣ *Contact / Business Card* 📞\n\n"
            "_👉 Reply with a number (e.g. 1)_"
        )
    
    # ➤ OPTION 1: WEB SCRAPING
    elif msg_lower == '1' or 'scraping' in msg_lower:
        save_lead(sender_number, "Interest: Web Scraping")
        reply = (
            "🕷️ *Web Scraping Solutions*\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "Kisi bhi website se data nikal kar Excel/Database mein payein.\n"
            "✅ E-commerce Prices (Amazon/Flipkart)\n"
            "✅ Business Leads Extraction\n"
            "✅ Stock Market Data\n\n"
            "📞 *Order ke liye contact karein:*\n"
            "Whatsapp: https://wa.me/919016721639\n\n"
            "🔙 _Main Menu ke liye 'Menu' likhein._"
        )

    # ➤ OPTION 2: APP DEV
    elif msg_lower == '2' or 'app' in msg_lower:
        save_lead(sender_number, "Interest: App Dev")
        reply = (
            "📱 *App & Game Development*\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "Apna Dream App haqiqat banayein.\n"
            "✅ Android Apps (Business/Utility)\n"
            "✅ Hyper-Casual Games (Unity/Python)\n"
            "✅ Play Store Publishing Support\n\n"
            "📞 *Demo dekhne ke liye contact karein:*\n"
            "Whatsapp: https://wa.me/919016721639\n\n"
            "🔙 _Main Menu ke liye 'Menu' likhein._"
        )

    # ➤ OPTION 3: AUTOMATION
    elif msg_lower == '3' or 'bot' in msg_lower:
        save_lead(sender_number, "Interest: Automation")
        reply = (
            "🤖 *Business Automation*\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "Apne boring kaam humare Robots se karwayein!\n"
            "✅ WhatsApp Chatbots (24/7 Support)\n"
            "✅ Auto File Organizers\n"
            "✅ Bulk Email/Message Senders\n\n"
            "📞 *Setup karwane ke liye message karein:*\n"
            "Whatsapp: https://wa.me/919016721639\n\n"
            "🔙 _Main Menu ke liye 'Menu' likhein._"
        )

    # ➤ OPTION 4: CONTACT CARD (Ye raha tumhara Email/Phone)
    elif msg_lower == '4' or 'contact' in msg_lower:
        save_lead(sender_number, "Request: Contact Details")
        reply = (
            "📞 *Contact Information*\n"
            "━━━━━━━━━━━━━━━━━━\n"
            f"👤 *{OWNER_NAME}* (Owner)\n"
            f"📱 Mobile: *{OWNER_NUMBER}*\n"
            f"📧 Email: {OWNER_EMAIL}\n"
            f"📍 Location: {LOCATION}\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "💬 *Note:* Aap humein kabhi bhi WhatsApp kar sakte hain, hum jald hi reply karenge. 🚀"
        )

    # ➤ 🛑 SMART ERROR HANDLING (Professional Fallback)
    else:
        save_lead(sender_number, "Unknown Message", incoming_msg)
        greeting = get_greeting()
        reply = (
            f"🙏 *{greeting}!*\n"
            "Maaf kijiye, main samajh nahi paaya.\n\n"
            "🤔 *How can I help you?*\n"
            "Services dekhne ke liye type karein:\n"
            "👉 *Menu* ya *Hi*"
        )

    msg.body(reply)
    return str(resp)

if __name__ == "__main__":
    print("🚀 Professional Bot Started! (Mr. Pandey's Data Updated)")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)