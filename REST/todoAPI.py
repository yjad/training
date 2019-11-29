#! todo-API using flask
from flask import Flask, jsonify, abort, make_response, request
from types import *
from DBhandling import *

app = Flask(__name__)

"""
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]
"""
@app.route('/todo/api/v1.0/get_all_tasks', methods = ['GET'])
def get_all_tasks():
    tasks, status = get_db_records("select * from todo")
    if status < 0:
        abort(400)
    else:
        return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['GET'])
def get_task(task_id):
    if task_id == None:
        abort(400)
    cmd = f"select * from todo where id = {task_id}"
    #task = list(filter(lambda t: t['id'] == task_id, tasks))
    tasks, status = get_db_records(cmd)
    if status < 0:
        abort(400)
    else:
        return jsonify({'tasks': tasks})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not Found'}), 404)


@app.route('/todo/api/v1.0/tasks', methods = ['POST'])
def create_task():
    print (request.json)
    print (request)
    if not request.json or not 'title' in request.json:
        abort(400)
    task =[
        request.json['title'],
        request.json.get('description', ''),
        None
        ]
    rec_id = add_todo_db_record(task)
    if rec_id < 0:
        abort(400)

    return jsonify({'rec_id' : rec_id}), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['PUT'])
def update_task(task_id):
    task, no_of_recs = get_db_records(f'select * from todo where ID={task_id}')
    if no_of_recs == 0:
        print('not found')
        abort(404)
    if not request.json:
        print ('no json')
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        print('title is not string')
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        print ('description not str')
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        print ('done is not bool')
        abort(404)
    tasks=[
        task_id,
        request.json.get('title', ''),
        request.json.get('description', ''),
        request.json.get('status', '')
        ]

    status = update_todo_db_record(tasks)
    if status < 0:
        abort(-1000+status)
    return jsonify( { 'task_id': task[0] } )

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['DELETE'])
def delete_task(task_id):
    status = delete_todo_db_record (task_id)
    if status <= 0:
        abort(404)  # not found

    return jsonify( { 'result': status } )


if __name__ == '__main__':
    app.run(debug = True)



