import json
import pickle
filePath = 'C:/Users/bebid/Desktop/Projects/Projects/pyScraper/text.pickle'
dictVar = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5",
    "key6": "value6",
    "key7": "value7",
    "key8": "value8",
    "key9": "value9",
    "key10": "value10"
}
#creating function1:
def dictSaver(dictVar, filePath):
    with open(filePath,'w') as file:
        file.write(json.dumps(dictVar))
def dictLoader(filepath):
    dictList = []
    with open(filepath, 'r' ) as file:
        content = file.readlines()
        for dict in content:
            dictList.append(json.loads(dict))
    return dictList
def save_dict(dict_to_save, file_path):
    with open(filePath, 'wb') as file:
        pickle.dump(dict_to_save,file)

def lead_dict(file_path):
    with open(file_path,'rb') as file:
        return pickle.load(file)

#Schedule a function challenge
'''
U: Write a python function to shcedule another given function to execute at a specified time
    inputs: event time, function, anynumber of arguments
    example:
     schedule_func(time.time()+1,print,"Howdy!")

'''
import sched
import time

def schedule_function(event_time, function, *args):
    s = sched.scheduler(time.time,time.sleep)
    s.enterabs(event_time,1,function,argument=args)
    print(f"{function.__name__}() scheduled for {time.ctime(event_time)}")
    s.run()

print(schedule_function(time.time()+60,print,"HELLO WORLD"))