#This Api class from flask_restful module will create a new server.
from flask_restful import Api
#the app=flask(__name__) that is the flask instance created, we importit here .
from app import app
#We import from Task file the Task class
from .Task import Task
from .TaskByID import TaskByID
#Then we create the rest server using the flask_restful module
#And we pass Flasj instance that is app in it.
restServer=Api(app)
#we will add a resource TAsk and give a URl mapped to the resource
restServer.add_resource(Task,"/api/project/task")
restServer.add_resource(TaskByID,"/api/project/task/id/<int:taskId>")
