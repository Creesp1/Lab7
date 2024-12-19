import sqlite3
import pandas as pd

# Подключаемся к базе данных SQLite (если файл не существует, он будет создан)
conn = sqlite3.connect('gifts.db')

# Создаем таблицу, если её нет
conn.execute('''
CREATE TABLE IF NOT EXISTS gifts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    gift_name TEXT NOT NULL,
    price INTEGER NOT NULL,
    status TEXT NOT NULL
);
''')

# Вставляем данные в таблицу
data = [
    ('Иван Иванович', 'Санки', 2000, 'куплен'),
    ('Ирина Сергеевна', 'Цветы', 3000, 'не куплен'),
    ('Алексей Петрович', 'Ноутбук', 50000, 'не куплен'),
    ('Мария Константиновна', 'Книга', 500, 'куплен'),
    ('Сергей Александрович', 'Телефон', 15000, 'не куплен'),
    ('Наталья Дмитриевна', 'Палатка', 7000, 'куплен'),
    ('Дмитрий Владимирович', 'Курс по Python', 3000, 'не куплен'),
    ('Елена Юрьевна', 'Часы', 8000, 'куплен'),
    ('Ольга Васильевна', 'Сумка', 4000, 'не куплен'),
    ('Петр Степанович', 'Гарнитура', 3500, 'куплен')
]

# Вставляем данные в таблицу
conn.executemany('''
INSERT INTO gifts (full_name, gift_name, price, status)
VALUES (?, ?, ?, ?)
''', data)

# Подтверждаем изменения и закрываем соединение
conn.commit()

# Проверим содержимое таблицы с помощью SQL запроса
df = pd.read_sql_query("SELECT * FROM gifts", conn)
print(df)

conn.close()