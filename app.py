from flask import Flask

app = Flask(__name__)

# API가 있어야 한다, 아래 코드가 API
@app.route('/', methods = ['GET'])
def hello_world() :
    return 'Hello World hihihi'

if __name__ == '__mian__' :
    app.run()

