attendance = {}

def mark_attendance(roll, days_present):
    attendance[roll] = days_present

def get_attendance(roll):
    return attendance.get(roll, 0)
