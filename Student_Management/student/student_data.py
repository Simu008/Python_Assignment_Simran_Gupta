students = {}

def add_student(roll, name, age):
    students[roll] = {
        "name": name,
        "age": age
    }

def get_student(roll):
    return students.get(roll)
