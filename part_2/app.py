import json
from flask import Flask, request, jsonify,render_template, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
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
def create_record():
    request_data = request.get_json()
    cpu_Usage=request_data['CPU_Usage']
    Memory_Usage = request_data['Memory_Usage']
    mydict={"CPU_Info":cpu_Usage, "Memory_Info": Memory_Usage}
    print(cpu_Usage)
    print(Memory_Usage)
    todos.insert_one({"CPU_Info":cpu_Usage, "Memory_Info": Memory_Usage})
    return jsonify(request_data)
# Workable
@app.route('/update/<id>', methods=['PUT'])
def update_record(id):
    post_date=request.get_json()
    response = todos.update_one({'_id':ObjectId(id)},{'$set':{"CPU_Info":post_date['CPU_Usage'], "Memory_Info": post_date['Memory_Usage']}})
    if response.matched_count:
        message = "Data updated successfully !"
    else:
        message = "Data not found !"

    return jsonify({"result":message})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
#I tried to do this well
