from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>������ ����������� �����</h1>'


@app.route('/index')
def new_page():
    return '<h2>� �� ����� ����� ������ ������!</h2>'


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
                    <title>������, ����!</title>
                  </head>
                  <body>
                    <h1>��� ���, ����!</h1>
                    <img src='static/img/mars.jpg' alt="����� ������ ���� ���� ��������, �� �� �������">
                    <div class="alert alert-primary" role="alert">
                      ������������ ��������� �� �������.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      ������������ ���� ���� �������.
                    </div>
                    <div class="alert alert-success" role="alert">
                      �� ������� ���������� ������������ ���� �������.
                    </div>
                    <div class="alert alert-danger" role="alert">
                      � ������ � �����!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      �������������!
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
                            <title>����� �����������</title>
                          </head>
                          <body>
                            <h1 class='form_head'>������ ����������� �� ������� � ������</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" placeholder="������� �������">
                                    <input type="text" class="form-control" placeholder="������� ���">
                                    <br>
                                    <input type="email" class="form-control" placeholder="������� ����� �����">
                                    <label for="classSelect">����� � ��� �����������?</label>
                                    <br>
                                    <select class="form-control" id="classSelect" name="class">
                                          <option>���������</option>
                                          <option>�������</option>
                                          <option>������</option>
                                          <option>�������������� �����������</option>
                                        </select>
                                    <label>����� � ��� ���� ���������?</label><br>
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">�������-�������������</label>
                                    <br>
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">�����</label>
                                    <br>
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">���������</label>
                                    <br>
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">����� �����</label>
                                    <br>
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">�����</label>
                                    <br>
                                    <label class="form-check-label" for="acceptRules">������� ���</label>
                                    <br>
                                    <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                    <label class="form-check-label" for="acceptRules">�������</label>
                                    <br>
                                    <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                    <label class="form-check-label" for="acceptRules">�������</label>
                                    <br>
                                    <label class="form-check-label" for="acceptRules">������ �� ������ ������� ������� � ����������?</label>
                                    <br>
                                    <textarea class="form-control" id="about" rows="3" name="about"></textarea><br>
                                    <div class="form-group">
                                        <label for="photo">��������� ����������</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">������ �� �� �������� �� �����?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">���������</button>
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
        return "����� ����������"

@app.route('/choice/����')
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
                    <title>�������� ������</title>
                  </head>
                  <body>
                    <h1>��� �����������: ����</h1>
                    <img src='{url_for('static', filename='img/mars.jpg')}' alt="����� ������ ���� ���� ��������, �� �� �������">
                    <h2>��� ������� ������ � �����;</h2>
                    <div class="alert alert-primary" role="alert">
                      <h2>�� ��� ����� ����������� ��������;</h2>
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      <h2>�� ��� ���� ���� � ���������;</h2>
                    </div>
                    <div class="alert alert-success" role="alert">
                      <h2>�� ��� ���� ��������� ��������� ����;</h2>
                    </div>
                    <div class="alert alert-danger" role="alert">
                      <h2>�������, ��� ������ �������!</h2>
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
    <title>����������</title>
<h1>���������� ������</h1>
<h2>����������� �� ������� � ������ Mark:</h2>
<div class="alert alert-success" role="alert">
<h2>�����������! ��� ������� ����� 3 ����� ������</h2>
</div>
<h2>���������� 68.2!</h2>
<div class="alert alert-danger" role="alert">
                      <h2>������ �����!</h2>
                    </div>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')