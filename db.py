import json

def read_db():
    with open("db.json") as f:
        data = f.read()
        try:
            return json.loads(data)
        except json.decoder.JSONDecodeError:
            return {}

def save_db(data: dict)->dict:
    with open("db.json", "w") as f:
        str_data = json.dumps(data, indent=4)
        f.write(str_data)

def is_user(chat_id):
    data = read_db()
    return chat_id in data.keys()


def get_user(chat_id: str):
    data = read_db()
    if not is_user(chat_id):
        return False
    return data[chat_id]

def add_user(chat_id: str):
    data = read_db()
    if not is_user(chat_id):
        data[chat_id] = {
            "likes":0,
            "dislikes":0,
            "inline_likes":0,
            "inline_dislikes":0
        }
    save_db(data)

def inc_like(chat_id: str):
    data = read_db()
    if not is_user(chat_id):
        return False
    data[chat_id]['likes']+=1
    save_db(data)


def inc_dislike(chat_id: str):
    data = read_db()
    if not is_user(chat_id):
        return False
    data[chat_id]['dislikes'] += 1
    save_db(data)

def clear(chat_id: str):
    data = read_db()
    if not is_user(chat_id):
        return False
    data[chat_id]['likes'] = 0
    data[chat_id]['dislikes'] = 0
    save_db(data)

def inc_inline_like(chat_id: str):
    data = read_db()
    if not is_user(chat_id):
        return False
    data[chat_id]['inline_likes']+=1
    save_db(data)

def inc_inline_dislike(chat_id: str):
    data = read_db()
    if not is_user(chat_id):
        return False
    data[chat_id]['inline_dislikes']+=1
    save_db(data)

def inc_inline_clear(chat_id: str):
    data = read_db()
    if not is_user(chat_id):
        return False
    data[chat_id]['inline_likes'] = 0
    data[chat_id]['inline_dislikes'] = 0
    save_db(data)
