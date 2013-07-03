from flask import Flask
from flask import request
from service.handler import handle_request
from service.user_service.register_service import RegisterService

app = Flask(__name__)
app.debug = True

@app.route('/', methods = ['GET','POST'])
def hello_world():
	return 'Hello World!' + request.args.get('sdf')

@app.route('/register', methods = ['GET','POST'])
def register():
    return handle_request(request, RegisterService())

if __name__ == "__main__":
	app.run(port=8888)


