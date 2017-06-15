from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flaskext.mysql import MySQL
from sample.sample import Todo, TodoList
from auth.auth import CreateUser


app = Flask(__name__)
api = Api(app)

# mysql connect
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'flask'
app.config['MYSQL_DATABASE_PASSWORD'] = 'flask123'
app.config['MYSQL_DATABASE_DB'] = 'flask'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)

def abort_if_tod_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404,  message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(CreateUser, '/user')

if __name__ == '__main__':
    app.run(debug=True)