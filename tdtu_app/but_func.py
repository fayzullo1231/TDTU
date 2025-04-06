import requests

TELEGRAM_BOT_TOKEN = '8052192015:AAHtR8f8i3qu2TSkuQjnu8921bW-k2Hx1BI'
CHANNEL_ID = '-1002530734318'

def send_channel_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHANNEL_ID,
        'text': text,
        'parse_mode': 'HTML'  # optional: supports HTML/Markdown
    }
    response = requests.post(url, data=payload)
    print(response.text)
    return response.json()