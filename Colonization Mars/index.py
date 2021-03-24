from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def new_page():
    return '<h2>И на Марсе будут яблони цвести!</h2>'


@app.route('/promotion_image')
def promotion_page():
    return '''
    <!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" 
                    href="static/css/style.css">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src='static/img/mars.jpg' alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-danger" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 class='form_head'>Анкета претендента на участие в мессии</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" placeholder="Введите фамилию">
                                    <input type="text" class="form-control" placeholder="Введите имя">
                                    <br>
                                    <input type="email" class="form-control" placeholder="Введите адрес почты">
                                    <label for="classSelect">Какое у Вас образование?</label>
                                    <br>
                                    <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>Межпланетарное комплексное</option>
                                        </select>
                                    <label>Какие у Вас есть профессии?</label><br>
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">инженер-исследователь</label>
                                    <br>
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">пилот</label>
                                    <br>
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">строитель</label>
                                    <br>
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">Эллен Рипли</label>
                                    <br>
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">Чужой</label>
                                    <br>
                                    <label class="form-check-label" for="acceptRules">Укажите пол</label>
                                    <br>
                                    <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                    <label class="form-check-label" for="acceptRules">Мужской</label>
                                    <br>
                                    <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                    <label class="form-check-label" for="acceptRules">Женский</label>
                                    <br>
                                    <label class="form-check-label" for="acceptRules">Почему вы хотите принять участие в экспедиции?</label>
                                    <br>
                                    <textarea class="form-control" id="about" rows="3" name="about"></textarea><br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли вы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"

@app.route('/choice/Марс')
def welcome_mars():
    return f'''
    <!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" 
                    href="static/css/style.css">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: Марс</h1>
                    <img src='{url_for('static', filename='img/mars.jpg')}' alt="здесь должна была быть картинка, но не нашлась">
                    <h2>Эта планета близка к Земле;</h2>
                    <div class="alert alert-primary" role="alert">
                      <h2>На ней много необходимых ресурсов;</h2>
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      <h2>На ней есть вода и атмосфера;</h2>
                    </div>
                    <div class="alert alert-success" role="alert">
                      <h2>На ней есть небольшое магнитное поле;</h2>
                    </div>
                    <div class="alert alert-danger" role="alert">
                      <h2>Наконец, она просто красива!</h2>
                    </div>
                  </body>
                </html>'''

@app.route('/results/Mark/3/68.2')
def show_rating():
    return '''
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" 
                    href="static/css/style.css">
    <title>Результаты</title>
<h1>Результаты отбора</h1>
<h2>Претендента на участие в миссии Mark:</h2>
<div class="alert alert-success" role="alert">
<h2>Поздравляем! Ваш рейтинг после 3 этапа отбора</h2>
</div>
<h2>составляет 68.2!</h2>
<div class="alert alert-danger" role="alert">
                      <h2>Желаем удачи!</h2>
                    </div>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')