from flask import request

#To convert the Task class as a resource we import from flask_restful Resource
from flask_restful import Resource
from flask import jsonify
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
  database="ToDo"
)
mycursor = mydb.cursor()
#This means that TAsk class is inherited from a Resource class so that Task class acts as a Resource
class TaskByID(Resource):
#get,post,put and delete are http methods
    def get(self,taskId):
        mycursor.execute("SELECT text, status FROM Tasks where id=2")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
        #pass statement is not ignored by the interpreter, but does nothing, useful when you haveto implement the function in future.

        return {"message": "inside get method of task by id. TAsk-id-{}".format(taskId)},200

    def post(self,taskId):




        # pass statement is not ignored by the interpreter, but does nothing, useful when you haveto implement the function in future.
        return {"message": "inside post method"}, 200

    def put(self,taskId):
        _json = request.get_json()
        _text = _json['text']
        _status = _json['status']

        sql = 'UPDATE Tasks SET text = %s,status = %s Where id=2'
        val = (_text, _status)

        mycursor.execute(sql, val)

        mydb.commit()
        return jsonify({"text": _text, "status": _status})
        # pass statement is not ignored by the interpreter, but does nothing, useful when you haveto implement the function in future.
        return {"message": "inside put method"}, 200

    def delete(self,taskId):
        sql = "DELETE FROM Tasks WHERE id = '1'"

        mycursor.execute(sql)

        mydb.commit()

        print(mycursor.rowcount, "record(s) deleted")
        # pass statement is not ignored by the interpreter, but does nothing, useful when you haveto implement the function in future.
        return {"message": "inside delete method"}, 200