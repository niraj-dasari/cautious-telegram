from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import bson.json_util as json_util

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://root:root@todocluster.dak741x.mongodb.net/todoSync'
mongo = PyMongo(app)


@app.route('/todos', methods=['POST'])
def create_todo():
    todo = request.json
    mongo.db.todos.insert_one(todo)
    return jsonify({'message': 'Todo created successfully'})


@app.route('/todos', methods=['GET'])
def get_all_todos():
    todos = list(mongo.db.todos.find())
    return json_util.dumps(todos)


@app.route('/todos/<title>', methods=['GET'])
def get_todo_by_id(title):
    todo = mongo.db.todos.find_one({'title': title})
    return json_util.dumps(todo)


@app.route('/todos/<id>', methods=['PUT'])
def update_todo(id):
    updates = request.json
    mongo.db.todos.update_one({'_id': id}, {'$set': updates})
    return json_util.dumps({'message': 'Todo updated successfully'})


@app.route('/todos/<id>', methods=['DELETE'])
def delete_todo(id):
    mongo.db.todos.delete_one({'_id': id})
    return json_util.dumps({'message': 'Todo deleted successfully'})
