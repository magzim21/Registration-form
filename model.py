import json
import datetime

data_db = {}

def save_db():
    with open('db.json', 'w') as db:
        json.dump(data_db,db)


def read_db():
    with open('db.json') as db:
        global data_db
        data_db = json.load(db)

def reg_db(login, password, email):
    read_db()
    if not login or not password or not email:
        return False
    try:
        if login not in data_db:
            jsformat = {login: {"password": password, "email": email, "notes": []}}
            data_db.update(jsformat)
            save_db()
            return True
        else:
            return False
    except TypeError:
        print('Нужно передать 3 аргумента: login, password, email')
        return False

    else:
        print('Неизвестная ошибка при попытке добавления нового пользователя в БД')
        return False

def auth_db(login, password):
    read_db()
    return login in data_db and password == data_db[login]["password"]

    if login in data_db and password == data_db[login]["password"]:
        return True
    else:
        return False

def add_note_db(login, title, body):
    read_db()
    norm_datatime = str(datetime.datetime.now())[0:-7]
    note = {'title': title, 'body' : body, 'datetime' : norm_datatime}
    data_db[login]["notes"].append(note)
    save_db()


def del_note(login, num):
    read_db()
    del data_db[login]["notes"][int(num)-1]
    save_db()
    #return True

def show_notes(login):
    read_db()
    notes = []
    count = 0
    for note in data_db[login]["notes"]:
        count +=1
        notes.append(count)
        notes.append(note)
    return notes


def show_note(login,num):
    read_db()
    return data_db[login]["notes"][int(num)-1]




#del_note('max', 1)
