import sqlite3
import random
import string

# Создаем подключение к базе данных
conn = sqlite3.connect('магазин.db')
cursor = conn.cursor()

# Создаем таблицу "Товары"
cursor.execute('''
    CREATE TABLE Goods (
        ID INTEGER PRIMARY KEY,
        Name TEXT,
        Category TEXT,
        Price REAL,
        Quantity INTEGER,
        Manufacturer TEXT,
        Date DATE
    )
''')

# Заполняем таблицу случайными данными
for i in range(100000):
    name = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    category = random.choice(['Products', 'Clothes', 'Electronics'])
    price = round(random.uniform(1.0, 100.0), 2)
    quantity = random.randint(1, 100)
    manufacturer = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    date = f'2023-12-{random.randint(1, 31)}'

    cursor.execute('''
        INSERT INTO Goods (Name, Category, Price, Quantity, Manufacturer, Date)
        VALUES (name, category, price, quantity, manufacturer, date)
    ''', (name, category, price, quantity, manufacturer, date))

conn.commit()
conn.close()
