import sqlite3

connection = sqlite3.connect("filmy.db")
cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS filmy (id INTEGER PRIMARY KEY, nazev_filmu TEXT, hodnoceni INTEGER)"
)

# Zapsání do databáze
film = "Titanic"
hodnoceni = 5

cursor.execute(
    'INSERT INTO filmy (nazev_filmu, hodnoceni) VALUES (?, ?)', (film, hodnoceni)
)
connection.commit()

# Vypisování hodnocení
cursor.execute(
    "SELECT * FROM filmy"
)

rows = cursor.fetchall()
for row in rows:
    print(*row)

connection.close()
