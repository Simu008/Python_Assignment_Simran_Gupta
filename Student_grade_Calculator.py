students = {
    "Simran": [85, 90, 88],
    "Pallavi": [72, 68, 75],
    "Barsha": [95, 92, 94],
    "Rohit": [60, 58, 62],
    "Mohit": [40, 55, 50]
}

def calculate_average(marks):
    return sum(marks) / len(marks)

def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"

top_student = ""
top_average = 0



for name, marks in students.items():
    avg = calculate_average(marks)
    grade = assign_grade(avg)

    print(f"Name: {name}, Average Marks: {avg:.2f}, Grade: {grade}")

    if avg > top_average:
        top_average = avg
        top_student = name

print("Top Scorer:")
print(f"Name: {top_student}, Average Marks: {top_average:.2f}")
