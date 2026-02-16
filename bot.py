from flask import Flask, request
import re

app = Flask(__name__)

# =========================================================
# ⚙️ BUSINESS SETTINGS (Pandey Ji VIP Config)
# =========================================================
BUSINESS_NAME  = "PANDEY COLOUR CONTRACTOR"
PRIMARY_PHONE  = "7046769047"
SECOND_PHONE   = "9016721639"
FULL_ADDRESS   = "202/-2krishnakunj, society palanpur jakaatnaka, Surat."
MAP_LINK       = "http://maps.google.com/?q=Suman+Chandan+Complex+Surat"
WHATSAPP_LINK  = f"https://wa.me/91{PRIMARY_PHONE}"

# 📷 DESIGN ALBUM (Pinterest - High Quality)
ALBUM_LINK     = "https://in.pinterest.com/search/pins/?q=royal%20play%20texture%20designs" 

@app.route('/whatsapp', methods=['GET'])
def whatsapp_reply():
    try:
        raw_msg = request.args.get('msg', '')
        if not raw_msg or not raw_msg.strip():
            return main_menu()

        msg = raw_msg.strip()
        msg_lower = msg.lower()

        # 🧠 SMART PATTERNS (Relatable words & Typos)
        # 1. Photos/Designs
        photo_pattern   = r"(photo|pic|image|design|color|colour|dekhna|portfolio|kaam|work|sample|album|catalogue|album|poto|fotto)"
        # 2. Rates/Price (VIP Treatment Branch)
        rate_pattern    = r"(rate|price|paisa|kitna|cost|kharcha|budget|estimate|bill|quotation|bhav|charges|money|pese|paisa|rait|prisce)"
        # 3. Address/Contact
        contact_pattern = r"(address|location|shop|office|contact|number|call|baat|milna|visit|jageh|loction|adrss|no|phone)"
        # 4. Greetings
        greet_pattern   = r"^(hi|hello|hii|hey|namaste|menu|start|helo|hy|yo|ram ram)$"

        # =====================================================
        # 👇 BRANCHING LOGIC (Professional & Attractive)
        # =====================================================

        # --- 1. RATE & PRICE (The "Qualify" Branch) ---
        if re.search(rate_pattern, msg_lower):
            return f"""💎 *BEST RATES & QUOTATION*
━━━━━━━━━━━━━━━━━━━
Namaste! 🙏

Sir/Ma'am, hum *Quality Work* mein believe karte hain. Sabse *Professional aur Best Rate* ke liye niche diye gaye number par message ya call karein.

📞 *Contact for Best Deal:*
👉 {PRIMARY_PHONE}
👉 {SECOND_PHONE}

💬 *WhatsApp:* {WHATSAPP_LINK}

*Hamari Team aapko jald hi contact karegi aur site visit ke liye time fix karegi.* ✨
━━━━━━━━━━━━━━━━━━━
🏠 *Menu ke liye 'Hi' likhein*"""

        # --- 2. PHOTOS & DESIGNS ---
        elif re.search(photo_pattern, msg_lower):
            return f"""🖼️ *DIGITAL DESIGN CATALOGUE*
━━━━━━━━━━━━━━━━━━━
Humare paas 500+ Latest Texture aur Colour Designs available hain.

🎨 *Design Gallery Dekhein:*
👇 *Click Here:*
🔗 {ALBUM_LINK}

(Jo design pasand aaye, uska screenshot lekar bhej dijiye)
━━━━━━━━━━━━━━━━━━━
🏠 *Menu ke liye 'Hi' likhein*"""

        # --- 3. CONTACT / ADDRESS ---
        elif re.search(contact_pattern, msg_lower):
            return f"""📞 *CONTACT & LOCATION*
━━━━━━━━━━━━━━━━━━━
👨‍🎨 *{BUSINESS_NAME}*

📍 *Office Address:*
{FULL_ADDRESS}

👇 *Google Map:*
🔗 {MAP_LINK}

📱 *Call Us:* {PRIMARY_PHONE} | {SECOND_PHONE}

🕒 *Time:* 9:00 AM - 8:00 PM
━━━━━━━━━━━━━━━━━━━
🏠 *Menu ke liye 'Hi' likhein*"""

        # --- 4. GREETINGS (Show Main Menu) ---
        elif re.search(greet_pattern, msg_lower):
            return main_menu()

        # --- 5. UNKNOWN/GIBBERISH FILTER (The "Sorry" Branch) ---
        else:
            # Check for random gibberish (e.g., "akjsax,k")
            # Pattern: No spaces and length > 12 OR no vowels and length > 4
            if (len(msg_lower) > 12 and " " not in msg_lower) or (len(msg_lower) > 4 and not any(v in msg_lower for v in 'aeiou')):
                sorry_msg = "❌ *SORRY!*\n━━━━━━━━━━━━━━━━━━━\nMujhe ye samajh nahi aaya. 😅\n\nPlease niche diye gaye options chuniye ya *Hi* likhein."
                return f"{sorry_text}\n\n{main_menu()}"
            else:
                # Basic unknown fallback
                return f"❌ *SORRY!*\nMujhe samajh nahi aaya. Kripya niche diye gaye options chuniye.\n\n{main_menu()}"

    except Exception:
        return main_menu()

# 🏛️ Function: Main Menu (Simple & Professional)
def main_menu():
    return f"""🏛️ *{BUSINESS_NAME}* 🏛️
━━━━━━━━━━━━━━━━━━━
👋 *Namaste! Welcome.*
Hum aapke ghar ko naya aur sundar roop dene ke liye taiyar hain. ✨

👇 *Jankari ke liye Option chuniye:*

🎨 *Latest Designs (Photos)*
(Type: 'Photo')

💎 *Check Best Rates*
(Type: 'Rate')

📍 *Address & Contact*
(Type: 'Contact')

📞 *Direct Call*
(Type: 'Call')

━━━━━━━━━━━━━━━━━━━
✨ *Quality Work. Trusted Name.*"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
