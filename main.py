from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app = FastAPI()

class Student(BaseModel):
    name: str
    email: str
    age: str
    Roll_number: str
    Department: str
    
    class StudentResponse(BaseModel):
        name: str
        email: str
        age: str
        Roll_number: str
        Department: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

def create_student(student: Student):
    return student

def read_students(id:int):
    return StudentResponse(id=id, **student.dict())

    def update_student(id:int,student:Student):
        return studentResponse(id=id, **student.dict())

        def delete_student(id:int):
               return studentResponse(id=id, **student.dict())


@app.post("/students")
def create_student(student: Student):
    return create_student(student)

@app.get("/students/{id}")
def read_students(id:int):
    return read_students(id)

@app.put("/students/{id}")
def update_student(id:int,student:Student):
    return update_student(id,student)

@app.delete("/students/{id}")
def delete_student(id:int):
    return delete_student(id)