import sqlite3 as sq

with sq.connect("not_telegram.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Users")
    cur.execute("""CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL);
        """)

    for i in range(1, 11):
        cur.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                       (f'User{i}', f'example{i}@gmail.com', f'{i*10}', '1000'))

    cur.execute("UPDATE Users SET balance = 500 WHERE NOT id % 2 == 0")
    cur.execute("DELETE FROM Users WHERE id IN (1, 4, 7, 10)")
    cur.execute("DELETE FROM Users WHERE id == 6")
    cur.execute("SELECT SUM(balance) FROM Users")
    money = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Users")
    users = cur.fetchone()[0]

    cur.execute("SELECT username, email, age, balance FROM Users WHERE age = ?", (60, ))
    for user in cur:
        print(user)

    print(money / users)
