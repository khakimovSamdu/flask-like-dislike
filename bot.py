from flask import Flask, request
from keyboards import keyboard, inline_keyboard
from telegram import Bot, Update



from db import(
    is_user,
    add_user,
    get_user,
    inc_like,
    inc_dislike,
    clear,
    inc_inline_like,
    inc_inline_dislike,
    inc_inline_clear
    
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
    user = data['message']['chat']
    print(data)
    if data['message'].get('text')=='/start':
            add_user(chat_id=str(user['id']))
            bot.send_message(
            chat_id = user['id'],
            text=f'Hello, {user["first_name"]}! Press one of the buttons or photos',
            )
    if data['message'].get('text')!=None:
        if data['message']['text']=="👍":
            if not is_user(str(user['id'])):
                start(user=data['message']['chat'])
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
                    start(user=data['message']['chat'])
            inc_dislike(chat_id=str(user['id']))
            user_data = get_user(chat_id=str(user['id']))
            bot.send_message(
                chat_id = user['id'],
                text=f'🔥 likes: {user_data["likes"]}\n💣 dislikes: {user_data["dislikes"]}',
                reply_markup=keyboard
            )
        elif data['message']['text']=="🆑":
            if not is_user(str(user['id'])):
                start(user=data['message']['chat'])
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
            text=f'Please {user["first_name"]} send me the button. My function works based on the following buttons(👍, 👎, 🆑)',
                reply_markup=keyboard
            )
    elif data['message'].get('photo')!=None:
        update = Update(update_id=data['update_id'])
        db = update.callback_query.data

        if db=="inline_like":
            if not is_user(chat_id=str(user['id'])):
                start(user=data['message']['chat'])
            inc_inline_like(chat_id=str(user['id']))
            user_data = get_user(chat_id=str(user['id']))
            bot.send_photo(
                chat_id=user['id'],photo = data['message']['photo'][0]['file_id'], caption = f'🔥 inline likes: {user_data["inline_likes"]}\n💣 inline dislikes: {user_data["inline_dislikes"]}',
                reply_markup=inline_keyboard
            )
        elif db == "inline_dislike":
            if not is_user(chat_id=str(user['id'])):
                start(user=data['message']['chat'])
            inc_inline_dislike(chat_id=str(user['id']))
            user_data = get_user(chat_id=str(user['id']))
            bot.send_photo(
                chat_id=user['id'], photo=data['message']['photo'][0]['file_id'], caption=f'🔥 inline likes: {user_data["inline_likes"]}\n💣 inline dislikes: {user_data["inline_dislikes"]}',
                reply_markup=inline_keyboard

            )
        elif db == "inline_clear":
            if not is_user(chat_id=str(user['id'])):
                start(user=data['message']['chat'])
            inc_inline_clear(chat_id=str(user['id']))
            user_data = get_user(chat_id=str(user['id']))
            bot.send_photo(
                chat_id=user['id'], photo=data['message']['photo'][0]['file_id'], caption=f'🔥 inline likes: {user_data["inline_likes"]}\n💣 inline dislikes: {user_data["inline_dislikes"]}',
                reply_markup = inline_keyboard
            )
        else:
            bot.send_message(chat_id=user['id'], text=f'Please, {user["first_name"]}, you sent us the wrong request. Download from image inline keyboards to send for correct request.(👍, 👎, 🆑)')
        
    else:
        bot.send_message(
            chat_id = user['id'],
            text=f'Please {user["first_name"]} send me the text. My function works based on the following buttons.',
                reply_markup=keyboard
            )
    return "Hello programmer"


if __name__== "__main__":
    app.run(debug=True)