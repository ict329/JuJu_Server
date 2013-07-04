from flask import Flask
from flask import request
from service.user.register import RegisterService

app = Flask(__name__)
app.debug = True

@app.route('/', methods = ['GET','POST'])
def hello_world():
	return 'Hello World!' + request.args.get('sdf')

@app.route('/register', methods = ['GET','POST'])
def register():
    return RegisterService(request).handle()

if __name__ == "__main__":
	app.run(port=8888)


