import sqlite3 as sq
from set_players import set_and_player

surname_player = input("Введите фамилию игрока: ").capitalize()


def create_table(cursor: sq.Cursor):
    command = """
    CREATE TABLE IF NOT EXISTS users (
    row_id INTEGER PRIMARY KEY,
    surname TEXT NOT NULL)
    """
    return cursor.execute(command)


with sq.connect('name_players.db') as con:
    cur = con.cursor()
    create_table(cur)
    if set_and_player(surname_player):
        print('Шахматист успешно добавлен')
    else:
        print('Такой шахматист уже есть!')
