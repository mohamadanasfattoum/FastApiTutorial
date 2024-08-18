from fastapi import FastAPI

app = FastAPI()

students = [
    {'name':'anas','age':30,'depatment': 'IT'},
    {'name':'Max', 'age':40,'depatment':'CH'},
    {'name':'Ali', 'age':50,'depatment':'MA'}]

@app.get("/root")

def root():
    return{'message':'hello'}



@app.get("/students")
def get_all_students():
    return students

@app.get("/students/{id}")
def get_student_by_id(id:int):
    return students[id]