from flask import request
#To convert the Task class as a resource we import from flask_restful Resource
from flask_restful import Resource

#new code

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
  database="ToDo"
)
mycursor = mydb.cursor()


#This means that TAsk class is inherited from a Resource class so that Task class acts as a Resource
class Task(Resource):
#get,post,put and delete are http methods
    def get(self):
        mycursor.execute("SELECT text, status FROM Tasks")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
        #pass statement is not ignored by the interpreter, but does nothing, useful when you haveto implement the function in future.
        print ("inside get method")
        return {"message": "inside get method"},200

    def post(self):
        _json = request.get_json()
        _text = _json['text']
        _status = _json['status']

        sql = ' INSERT INTO Tasks (text,status) VALUES (%s, %s)'
        val = (_text, _status)

        mycursor.execute(sql, val)

        mydb.commit()
        # pass statement is not ignored by the interpreter, but does nothing, useful when you haveto implement the function in future.
        return {"message": "inside post method"}, 200

    def put(self):
        # pass statement is not ignored by the interpreter, but does nothing, useful when you haveto implement the function in future.
        return {"message": "inside put method"}, 200

    def delete(self):
        # pass statement is not ignored by the interpreter, but does nothing, useful when you haveto implement the function in future.
        return {"message": "inside delete method"}, 200