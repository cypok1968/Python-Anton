from flask import Flask, request, make_response, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('cookie_test')



@app.route('/cookie_test')
def cookie_test():
    visit_count = int(request.cookies.get('visit_count', 0)) # если ключ кукисов был найден, то переменная возвращает ноль

    if visit_count:
        res = make_response(f'Вы посетили эту страницу {visit_count} раз(а).')
        res.set.cookies('visit_count', str(visit_count + 1),
                        max_age=60 * 60 * 24 * 30) # определяем сколько времени будут жить кукисы
    else:
        res = make_response('Вы впервые тут у нас за этот месяц')
        res.set_cookie('visit_count', '1',
                        max_age=60 * 60 * 24 * 30)
        return res

if __name__ == '__main__':
    app.run(host='localhost', port=5000)