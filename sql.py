import sqlite3
import datetime
import hashlib

db = sqlite3.connect('UserSave.db')

# Create Cursor
c = db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS data
            (userkey TEXT, mark TEXT, password TEXT, date TEXT)''')

def null_or_no():   # Эту фунцию можно использовать второй раз
    c.execute("SELECT userkey FROM data WHERE userkey IS NOT NULL")
    result = c.fetchone()
    if result:
        return result
    else:
        return 0



def add_userkey(key):
    # Хеширование пароля
    keyH = hashlib.sha256(key.encode()).hexdigest()
    c.execute('INSERT INTO data (userkey) VALUES (?)', (keyH,))
    db.commit()

def userkey_check(userkey):
    userkey_hash = hashlib.sha256(userkey.encode()).hexdigest()

    c.execute('SELECT userkey FROM data WHERE userkey = ?', (userkey_hash,))
    keyINbase = c.fetchone()
    if keyINbase is not None and keyINbase[0] == userkey_hash:
        return 1
    else:
        return 0

def add_data(title, password):
    a = null_or_no()
    keyHUY = None
    date_log = str(datetime.date.today())
    '''if a == 0:
        keyHUY = 
        c.execute('INSERT INTO data VALUES (?, ?, ?, ?)', (keyHUY, title, password, date_log))
        db.commit()
        return 0'''

    c.execute('INSERT INTO data VALUES (?, ?, ?, ?)', (keyHUY, title, password, date_log))
    db.commit()

def show_passwords():
    c.execute('SELECT mark, password, date FROM data WHERE mark is not NULL AND password is not null AND date is not null')
    rows = c.fetchall()
    #rows = rows[1:]
    print(rows)
    return rows
show_passwords()
