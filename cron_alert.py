import requests
from cleaner_bot_script import cleaner_bot_alert
#import json

# crontab rule
# 0 13 * * * python3 /home/dvasilev/projects/telegram_bots/cleaner_bot/cron_alert.py

chat_id = -37549110
SCRIPT_PATH     = '/home/dvasilev/projects/telegram_bots/cleaner_bot/'
with open(SCRIPT_PATH+'token.key','r') as file:
    token=file.read().replace('\n', '')
    file.close()

message_text = cleaner_bot_alert(SCRIPT_PATH,'dish')

def send_message(token, chat_id, message_text):
    # proxy = {'https': 'socks5h://user:password@IP:1080'}
    URL = 'https://api.telegram.org/bot' + token + '/sendMessage'
    #reply_markup ={ "keyboard": [["Yes", "No"], ["Maybe"], ["1", "2", "3"]], "resize_keyboard": True}
    #data = {'chat_id': chat_id, 'text': message_text, 'reply_markup': json.dumps(reply_markup)}
    data = {'chat_id': chat_id, 'text': message_text}
    # r = requests.post(URL, data=data, proxies=proxy)
    r = requests.post(URL, data=data)
    #print(r.json())

send_message(token, chat_id, message_text)
message_text = cleaner_bot_alert(SCRIPT_PATH,'garbage')
send_message(token, chat_id, message_text)
