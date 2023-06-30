import json
import requests

def send_message(bot_id, chat_id, message):
    message_data = {
        "parse_mode" : "HTML",
        "chat_id": chat_id,
        "text": message,
    }
    return requests.post('https://api.telegram.org/bot{}/sendMessage'.format(bot_id),data=message_data).json()

def send_voice_message_with_button(bot_id, chat_id, message: str,word:str,voicelink):
    #message = message.replace(" ", "+")
    message_data = {
        "parse_mode" : "HTML",
        "chat_id": chat_id,
        "voice":voicelink,
        "caption": message,
    }
    return requests.post('https://api.telegram.org/bot{}/sendVoice'.format(bot_id),data=message_data).json()

def copy(bot_id, fromchatid,targetchatid, messageid):
    message_data = {
        "from_chat_id": fromchatid,
        "chat_id": targetchatid,
        "message_id": messageid,
    }
    return requests.post('https://api.telegram.org/bot{}/copyMessage'.format(bot_id),data=message_data).json()

def send_quiz(bot_id, chat_id, questionword, optionlist, correctindex):
    message_data = {
        "chat_id": chat_id,
        "question": questionword,
        "options": json.dumps(optionlist),
        "type": "quiz",
        "correct_option_id": correctindex
    }
    return requests.post('https://api.telegram.org/bot{}/sendPoll'.format(bot_id), data=message_data).json()

