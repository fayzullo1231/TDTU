# telegram_utils.py

import os
import requests
from django.conf import settings

BOT_TOKEN = '8052192015:AAHtR8f8i3qu2TSkuQjnu8921bW-k2Hx1BI'
CHANNEL_ID = '-1002530734318'

def send_news_to_telegram(news):
    if news.for_telegram is True:
        caption = f"🟢 <b>{news.title.upper()}</b>\n\n{news.content[:1000]}"
        payload = {
            'chat_id': CHANNEL_ID,
            'caption': caption,
            'parse_mode': 'HTML',
        }
        if news.image:

            url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto'
            image_path = os.path.join(settings.MEDIA_ROOT, news.image.name)
            with open(image_path, 'rb') as photo:
                files = {'photo': photo}
                response = requests.post(url, data=payload, files=files)
        else:
            url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
            payload['text'] = caption
            response = requests.post(url, data=payload)

        return response.json()
    return None