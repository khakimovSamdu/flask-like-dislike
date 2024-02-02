from flask import Flask, request
from keyboards import keyboard
from telegram import Bot
from db import(
    is_user,
    add_user,
    get_user,
    inc_like,
    inc_dislike,
    clear,
    
)
def start(user: str):
    if not is_user(chat_id=str(user['id'])):
        add_user(chat_id=str(user['id']))
        bot.send_message(
        chat_id = user['id'],
        text=f'Hello, {user["first_name"]}! Press one of the buttons.',
            reply_markup=keyboard
        )
    else:
        user_data = get_user(chat_id=str(user['id']))
        bot.send_message(
        chat_id = user['id'],
        text=f'🔥 likes: {user_data["likes"]}\n💣 dislikes: {user_data["dislikes"]}',
            reply_markup=keyboard
        )
    return
app = Flask(__name__)
TOKEN = "6984427979:AAGZ08mIUVwcSgiOzPpS7QZX31uP-_XWyE8"
bot = Bot(TOKEN)
url = "https://allamurodxakimov.pythonanywhere.com/"
@app.route('/', methods=['POST'])
def main():
    data = request.get_json()
    user = data['message']['from']
    print(data)
    if data['message'].get('text')!=None:
        if data['message'].get('text')=='/start':
            add_user(chat_id=str(user['id']))
            bot.send_message(
            chat_id = user['id'],
            text=f'Hello, {user["first_name"]}! Press one of the buttons.',
                reply_markup=keyboard
            )
        elif data['message']['text']=="👍":
            if not is_user(str(user['id'])):
                start(user=data['message']['from'])
            inc_like(chat_id=str(user['id']))
            user_data = get_user(chat_id=str(user['id']))
            bot.send_message(
                chat_id = user['id'],
                text=f'🔥 likes: {user_data["likes"]}\n💣 dislikes: {user_data["dislikes"]}',
                reply_markup=keyboard
            )
        elif data['message']['text']=="👎":
            if not is_user(str(user['id'])):
                if not is_user(str(user['id'])):
                    start(user=data['message']['from'])
            inc_dislike(chat_id=str(user['id']))
            user_data = get_user(chat_id=str(user['id']))
            bot.send_message(
                chat_id = user['id'],
                text=f'🔥 likes: {user_data["likes"]}\n💣 dislikes: {user_data["dislikes"]}',
                reply_markup=keyboard
            )
        elif data['message']['text']=="🆑":
            if not is_user(str(user['id'])):
                start(user=data['message']['from'])
            clear(chat_id=str(user['id']))
            user_data = get_user(chat_id=str(user['id']))
            bot.send_message(
                chat_id = user['id'],
                text=f'🔥 likes: {user_data["likes"]}\n💣 dislikes: {user_data["dislikes"]}',
                reply_markup=keyboard
            )
        else:
            bot.send_message(
            chat_id = user['id'],
            text=f'Please {user["first_name"]} send me the button. My function works based on the following buttons',
                reply_markup=keyboard
            )
    else:
        bot.send_message(
            chat_id = user['id'],
            text=f'Please {user["first_name"]} send me the button. My function works based on the following buttons',
                reply_markup=keyboard
            )
    return "Hello programmer"
bot.set_webhook(url)
bot.get_webhook_info()

if __name__== "__main__":
    app.run(debug=True)