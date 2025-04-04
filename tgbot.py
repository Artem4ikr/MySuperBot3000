import asyncio
import requests

TOKEN = '7742693696:AAEhuQEPL1rvlYsQreCyLuctyjov1kFCR_M'
URL = 'https://api.telegram.org/bot'

user_id = 5760976310

async def get_message():
    message = input('введите сообщение:')
    await send_message(message)

async def send_message(message):
    message_data = {
        'chat_id' : user_id,
        'text' : message
    }

    requests.post(URL + TOKEN + '/sendMassage', date=message_data)

loop = asyncio.new_event_loop()
loop.run_until_complete(get_message())