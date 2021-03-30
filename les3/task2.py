import sqlite3
import hashlib

con = sqlite3.connect('sqlite.db')
cur = con.cursor()


def hash_password():
    user_password = input('Придумайте пароль: ')
    password_hash = hashlib.sha3_256(user_password.encode('utf-8'))
    hex_dig_password = password_hash.hexdigest()
    cur.execute('''CREATE TABLE IF NOT EXISTS passwords(
                passwd text
                )''')
    cur.executemany('INSERT INTO passwords VALUES (?)', hex_dig_password)
    user_password_try = input('Введите пароль который вы ввели: ')
    password_try_hash = hashlib.sha3_256(user_password_try.encode('utf-8'))
    hash_dig_password_try = password_try_hash.hexdigest()
    db_password_hash = cur.execute(f'SELECT * FROM passwords WHERE passwd = {hash_dig_password_try}')
    if hash_dig_password_try == db_password_hash:
        return 'Верный пароль'
    else:
        return 'Неверный пароль'


print(hash_password())
