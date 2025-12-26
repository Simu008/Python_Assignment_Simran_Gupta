import datetime
import random

def generate_student_id():
    return random.randint(1000, 9999)

def current_date():
    return datetime.date.today()
