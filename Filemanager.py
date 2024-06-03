import json
import os
from Task import TaskEncoder
from Task import Task
from collections import namedtuple

path_file = 'tasks_reg.json'

def taskJsonDecod(taskDict):
    taskObj = Task.Task(**taskDict)
    return taskObj

def read_task_registers() :
    if not os.path.isfile(path_file) :
        with open( path_file ,'w') as file :
            json.dump([],file)
    
    readData = []
    with open(path_file ,  'r') as file :
        data = json.load(file)
        #conviriendo lectura str en obj(Task)
        if len(data) > 0:    
            for d in data :
                tareaObj = Task(**d)
                readData.append(tareaObj)

    return readData 

def write_task_registers( data ):
    with open(path_file , 'w') as file :
        json.dump( data , file , indent=4, cls=TaskEncoder)