class ReportCard:
    def __init__(self, student, total, average):
        self.student = student
        self.total = total
        self.average = average

    def display(self):
        print("Report Card:")
        print("Name:", self.student["name"])
        print("Age:", self.student["age"])
        print("Total Marks:", self.total)
        print("Average Marks:", self.average)
