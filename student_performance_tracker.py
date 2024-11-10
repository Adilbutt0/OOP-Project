class Student:
    def __init__(self,name: str,scores:list[int]):
        self.name = name
        self.scores = scores
    def calculate_average(self):
        average_marks = sum(self.scores) / len(self.scores)
        print(f"Student Average Marks {average_marks}")

    def is_passing(self):
        marks_pass = self.calculate_average()
        if marks_pass <= 40:
            print("Congratulation Pass!")
        else:
            print("Sorry But Your Fail!")
class PerformanceTracker(Student):
    def __init__(self):
        self.students = {}
    def calculate_class_average(self):
        total_score = 0
        student_count = len(self.students)
        
        for student in self.students.values():
            total_score += student.calculate_average()
        
        if student_count > 0:
            class_average = total_score / student_count
            print(f"Class Average: {class_average}")
        else:
            print("No students to calculate the average.")
    def display_student_performance(self):
        total_score = 0
        student_count = len(self.students)
        for student_count in self.students:
            total_score += student_count.calculate_average()
        if student_count > 0:
            disaplay_class_perfomance = total_score / student_count
            if disaplay_class_perfomance <= 40:
                print(f"Each Student Perfomance Status: Pass")
            else:
                print("Each Student Perfomance Status: Fail")
        else:
            print("No students to calculate the average.")
        
    def add_students(self):
        new_student_name = input("Enter Student Name: ")
        new_subjects = ["Maths","Science","Computer"]
        new_marks = []
        for subj in new_subjects:
            while True:
                try:
                    new_scores = int(input("Enter Subject Number: "))
                    if new_scores <0:
                        print("Give Positive Number: ")
                    else:
                        new_marks.append(new_scores)
                        break
                except Exception as e:
                    print(str(e))
        new_student = Student(new_student_name,new_scores)
        user = self.students[new_student] = new_student
        print("Successfully added user")
name = input("Enter Your Name: ")
marks = []
subjects = ["Computer","Maths","Science"]
for subj in subjects:
    while True:
        try:
            scores = int(input("Enter subject numbers: "))
            if scores < 0:
                print("Wrong number")
            else:
                marks.append(scores)
        except Exception as e:
            print(str(e))
        break
print("Welcome To Library Management: ")
print(f"Press 1 If You Want To See Student Average: \nPress 2 If You Want To Find Student Is Passing Or Not\nPress 3 If You Want To See Class Average\nPress 4 If You Want To See Whole Class Perfomance\nPress 5 If You Want To Add Student In The List")
choice = int(input("Enter choice: "))
obj2 = PerformanceTracker()
obj1 = Student(name,marks)
if choice == 5:
    obj2.add_students()
elif choice == 3:
    obj2.calculate_class_average()
elif choice == 4:
    obj2.display_student_performance()
elif choice == 1:
    obj1.calculate_average()
elif choice == 2:
    obj1.is_passing()
else:
    print("Invalid Choice!")
