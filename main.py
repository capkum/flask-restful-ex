from base import app, db

from flask_restful import Api
from sample.sample import Todo, TodoList
from auth.auth import CreateUser

api = Api(app)
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(CreateUser, '/user')

if __name__ == '__main__':
    with app.app_context():
        from base import models  # noqa
        db.create_all()
    app.run(debug=True)
