import sqlite3

connection = sqlite3.connect("database1.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL);
   """)

for i in range(1, 11):
    cursor.execute('INSERT INFO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i}', f'example{i}@gmail.com', f'{i*10}', '1000'))

cursor.execute("UPDATE Users SET balance = ? WHERE id % 2 = ?",
               (500, 0))
cursor.execute("DELETE FROM Users WHERE id % 3 = ?", (0, ))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age = ?", (60, ))
users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()
