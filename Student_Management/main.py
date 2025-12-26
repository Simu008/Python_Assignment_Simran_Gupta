
import student.student_data as sd
from student.attendance import mark_attendance
from student.marks import calculate_total, calculate_average
from student.fees import pay_fee
from report.report_card import ReportCard
from utils import helpers


student_id = helpers.generate_student_id()
print("Generated Student ID:", student_id)
print("Date:", helpers.current_date())

sd.add_student(student_id, "Simran", 22)
student = sd.get_student(student_id)

mark_attendance(student_id, 85)
pay_fee(student_id, 50000)

marks = [80, 85, 90]
total = calculate_total(marks)
average = calculate_average(marks)

report = ReportCard(student, total, average)
report.display()

import student.student_data as module_info
print("Module Properties:")
print("name:", module_info.__name__)
print("file:", module_info.__file__)
print("dict_keys:", list(module_info.__dict__.keys()))
