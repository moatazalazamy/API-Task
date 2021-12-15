from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.getcwd()

app = Flask(__name__)

# connect to database by SQLalchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{basedir}/example.db"
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    status = db.Column(db.String)

    def to_json(self):
        return {"id":self.id, "title":self.title, "status":self.status}

@app.route('/')
def hello_world():
    return ("hello, worlds!")


@app.route('/tasks')
def getTasks():
    data =[]
    tasks = Task.query.all()
    for task in tasks:
        data.append(task.to_json())
    return jsonify(data)

#create task
@app.route('/tasks',methods=['POST'])
def add_task():
    data = request.json
    title = data['title']
    status = data['status']
    if  status not in ["draft","active","done","archived"]:
        return jsonify({"meessage":'Status should be draft, active, done or archived',"isSuccess":False}),400
    if  not Task.query.filter_by(title=title).first():
        task = Task(title=title,status=status)
        db.session.add(task) # to save in db
        db.session.commit()
        return jsonify({"title":task.title,"status":task.status,"id":task.id}),201
    else:
        return jsonify({"meessage":f"This task with title:{title} exists","isSuccess":False}),400

#get task
@app.route('/tasks/<id>',methods=['GET'])
def get_task(id):
    task = Task.query.filter_by(id=id).first()
    if task:
        return jsonify({"title":task.title,"status":task.status,"id":task.id}),201
    return "Not Found",404

@app.route('/tasks/<id>/<status>', methods=['PUT'])
def update_status(id, status):
    
    if  status not in ["draft","active","done","archived"]:
        return jsonify({"meessage":'Status should be draft, active, done or archived',"isSuccess":False}),400
    task = Task.query.filter_by(id=id).first()
    if task:
        if task.status=='draft' and status=='done':
            return jsonify({"meessage":'Status can not move from draft to done',"isSuccess":False}),400
        if  status !='archived' and task.status =='archived':
            return jsonify({"meessage":'Status can not move from archived backward.',"isSuccess":False}),400
        if  (task.status=='active' or task.status=='done') and status =='draft':
            return jsonify({"meessage":'Status can not move back to draft.',"isSuccess":False}),400
        
        task.status = status
        db.session.add(task)
        db.session.commit()
        return jsonify({"title":task.title,"status":task.status,"id":task.id}),201
    return "Not Found",404


@app.route('/tasks/<id>', methods=['DELETE'])
def delete_tasks(id):
    task = Task.query.filter_by(id=id).first()
    if task:
        db.session.delete(task)
        db.session.commit()
        return "",204

    return "Not Found",404


if __name__ =='__main__':
    db.create_all()
    app.run(debug=True)