import sqlite3 as sq

link_input = input('Введите ссылку на партию: ')
surname_input = input("Введите фамилию шахматиста: ").capitalize()


def search_by_surname(cursor: sq.Cursor, surname):
    command = """
    SELECT row_id FROM users WHERE surname=? 
    """
    result = cursor.execute(command, (surname,))
    return result.fetchone()


def create_table(cursor: sq.Cursor, link, surname):
    command = f"""
    CREATE TABLE IF NOT EXISTS (?) (
    row_id INTEGER DEFAULT (?),
    link_on_game TEXT)"""
    return cursor.execute(command, (surname, link))


def set_game(cursor: sq.Cursor, link, surname):
    command = f"""
    INSERT INTO (?) VALUES (?) 
    """
    return cursor.execute(command, (surname, link))


with sq.connect('name_players.db') as con:
    cur = con.cursor()
    try:
        set_game(cur, surname_input, link_input)
    except TypeError:
        print("Такого игрока не существует!")
