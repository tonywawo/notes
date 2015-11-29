from flask import Flask, render_template
from flask.ext.script import Manager,Server

app = Flask(__name__)

manager = Manager(app)
manager.add_command("runserver", Server(
    host = '0.0.0.0')
)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    manager.run()

