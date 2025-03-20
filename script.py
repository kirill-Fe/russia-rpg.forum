from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/submit-complaint', methods=['POST'])
def submit_complaint():
    if request.method == 'POST':
        topic = request.form['complaint_topic']
        description = request.form['complaint_description']

        # Здесь нужно добавить код для обработки жалобы:
        # 1. Сохранить в базу данных.
        # 2. Отправить уведомление администратору.
        # 3. И т.д.

        print(f"Получена жалоба по теме: {topic}")
        print(f"Описание: {description}")

        return "Жалоба успешно отправлена!" # Или редирект на страницу подтверждения

    return "Что-то пошло не так!"

@app.route('/')
def index():
    return render_template('index.html')  # Замените 'index.html' на имя вашего HTML файла

if __name__ == '__main__':
    app.run(debug=True)