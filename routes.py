from flask import Blueprint, request, jsonify
import requests

api_routes = Blueprint('api', __name__)

TELEGRAM_BOT_TOKEN = '7203672264:AAED9bhK2C9-ibys0A2s8Dv51YLD5HrP5gU'  # Replace with your bot token
CHAT_ID = '6744416532'  # Replace with your chat ID

@api_routes.route('/api/alert', methods=['POST'])
def send_alert():
    data = request.get_json()
    message = data.get('message', 'Emergency alert!')
    
    # Send message to Telegram
    send_telegram_message(message)
    
    return jsonify({'message': 'Emergency alert sent!'}), 200

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(url, json=payload)
