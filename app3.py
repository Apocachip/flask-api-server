from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

@app.route('/add_two_nums', methods= ['POST'])
def add() :
    # 클라이언트로부터 두 수를 받는다.
    data = request.get_json()
    ret = data['x'] + data['y']
    result = {"result" : ret}


    # 웹브라우저는 항상 메소드가 GET으로 되어있다.
    # 웹브라우저는 GET 메소드로만 호출한다.
    # 우리가 요청한 URL은 GET메소드로 호출한것
    return jsonify(result)

if __name__ == '__main__' :
    app.run()