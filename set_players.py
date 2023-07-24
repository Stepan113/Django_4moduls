import sqlite3 as sq


def set_and_player(surname):
    def check(cursor: sq.Cursor):
        command = """
        SELECT surname FROM users WHERE surname=?
        """
        return cursor.execute(command, (surname,))

    def set_player(cursor: sq.Cursor):
        command = """
        INSERT INTO users (surname) VALUES (?)
        """
        return cursor.execute(command, (surname,))

    with sq.connect('name_players.db') as con:
        cur = con.cursor()
        # print(check(cur).fetchall())
        if len(check(cur).fetchall()) != 0:
            return False
        else:
            set_player(cur)
            return True
