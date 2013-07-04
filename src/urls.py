from flask import Flask
from flask import request
from service.user.register import RegisterService
from service.user.template import TemplateService

app = Flask(__name__)
app.debug = True

@app.route('/', methods = ['GET','POST'])
def hello_world():
	return 'Hello World!' + request.args.get('sdf')

@app.route('/register', methods = ['GET','POST'])
def register():
    return TemplateService(request).handle()

if __name__ == "__main__":
	app.run(port=8888)


