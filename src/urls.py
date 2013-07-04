from flask import Flask
from flask import request
from service.user.register import RegisterService

app = Flask(__name__)
app.debug = True


@app.route('/register', methods = ['GET','POST'])
def register():
    return RegisterService(request).handle()

if __name__ == "__main__":
	app.run(port=8888)


