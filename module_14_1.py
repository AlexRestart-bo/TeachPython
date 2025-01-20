import sqlite3

connection = sqlite3.connect("database0.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS Users")
cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL);
   """)

for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', '1000'))

cursor.execute("UPDATE Users SET balance = 500 WHERE NOT id % 2 == 0")
cursor.execute("DELETE FROM Users WHERE id IN (1, 4, 7, 10)")

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age = ?", (60, ))
for user in cursor:
    print(user)

connection.commit()
connection.close()
