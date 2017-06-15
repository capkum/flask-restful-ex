from flask import Flask
from flask_restful import Resource, Api

class Hi(Resource):
    def get(self):
        return {'hello': 'Hi'}

todo = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todo[todo_id]}
    
    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}