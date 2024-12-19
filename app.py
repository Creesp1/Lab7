from flask import Flask, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)


# Функция для подключения к базе данных и извлечения данных
def get_gift_data():
    conn = sqlite3.connect('gifts.db')
    query = "SELECT * FROM gifts"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


@app.route('/')
def index():
    # Получаем данные из базы данных
    gift_data = get_gift_data()

    # Конвертируем данные в список словарей для отображения в шаблоне
    gift_list = gift_data.to_dict(orient='records')

    return render_template('index.html', gifts=gift_list)


if __name__ == '__main__':
    app.run(debug=True)