import json
from flask import Flask, request, jsonify,render_template, url_for, redirect
from pymongo import MongoClient
import bson

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.flask_db
todos = db.todos

@app.route('/', methods=['GET'])
def query_record():
      output= []
      for q in todos.find():
        output.append({'CPU_Info': q['CPU_Info'], 'Memory_Info':q['Memory_Info']})
     #all_todos = todos.find()
     #return render_template('index.html', todos=all_todos)
      return jsonify({'result': output})
#Workable
@app.route('/test', methods=['POST'])
def update_record():
    request_data = request.get_json()
    cpu_Usage=request_data['CPU_Usage']
    Memory_Usage = request_data['Memory_Usage']
    print(cpu_Usage)
    print(Memory_Usage)
    todos.insert_one({"CPU_Info":cpu_Usage, "Memory_Info": Memory_Usage})
    return jsonify(request_data)
#Unknown    
@app.route('/search/<ObjectId:info_id>',methods=['PUT'])
def create_record(info_id):
    post_data=request.json
    output=[]
    for q in todos.find({},{'__id':info_id}):
        output.append(q)    
    return jsonify({"result":output})
    
if __name__ == "__main__":
    app.run(Debug=True, host="0.0.0.0", port=8080)
