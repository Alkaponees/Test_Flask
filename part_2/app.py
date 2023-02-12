import json
from flask import Flask, request, jsonify,render_template, url_for, redirect
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.flask_db
todos = db.todos

@app.route('/', methods=['GET'])
def query_record():
      output= []
      for q in todos.find():
        output.append({'CPU_Info': q.cpuUsage, 'Memory_Info':q.memUsage})
     #all_todos = todos.find()
     #return render_template('index.html', todos=all_todos)
      return jsonify({'result': output})
     
@app.route('/test', methods=['POST'])
def update_record():
    request_data = request.json()
    cpu_Usage=request_data['CPU_Usage']
    Memory_Usage = request_data['Memory_Usage']
    mydict={"CPU_Info":cpu_Usage, "Memory_Info": Memory_Usage}
    print(cpu_Usage)
    print(Memory_Usage)
    todos.insert_one({"CPU_Info":cpu_Usage, "Memory_Info": Memory_Usage})
    return redirect(url_for('index'))
    #x = mydb.insert_one(mydict)
@app.route('/update',methods=['PUT'])
def create_record():
    post_data=request.json()
    todos.insert_one(0, {
        'CPU_Info' : post_data['CPU_Usage'],
        'Memory_Info' : post_data['Memory_Usage']
     })
    return jsonify(post_data)
if __name__ == "__main__":
    app.run(Debug=True, host="0.0.0.0", port=8080) 
    