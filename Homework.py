
print("BASIC STUDENT MENAGEMENT SYSTEM")

StudentName = str(input("Please you enter your Name: "))
StudentSurmame = str(input("Please you enter your Surname: "))
UsersName = str(StudentName) + str(StudentSurmame)

for StudentName in range(3):
    StudentName = input("Please you enter UsersName: ")    
    if UsersName == StudentName:
        print("Welcome")
        True
        break
    else:
        print("Wrong UsersNames!!")
else:
    print("Try again later")
    exit()

Lessons_of_Chosen = ["Math" , "Geographics" , "History" , "Physics" , "Turkısh"]
print("Your chosen all lessons: " , "Math - " , "Geographics - " , "History - " , "Physics - " , "Turkısh")
user_lessons = []
lessons_numbers = 0
def chosenLesson():
    global lessons_numbers
    while True:
        answer = str(input("Do you want to take a lesson?(Yes/No): "))
        if answer == "Yes":
            course = str(input("Please enter a lesson name: "))
            lessons_numbers +=1
            print(f"{course} is saved to system.")
            user_lessons.append(course)
            break
        elif answer == "No":
            print("contınue")
            break
    else:
        pass
    
chosenLesson()
chosenLesson()
chosenLesson()
chosenLesson()
chosenLesson()
print(user_lessons)

def controlOfLessonNumber():
    if lessons_numbers < 3:
        print("You failed in class.")
        exit()
    elif 3 <= lessons_numbers <= 5:
        return "You should choose a course exam."
        
print(controlOfLessonNumber())

Math =                      {"MidtermExam" : 80,
                             "Final Exam"  : 90,
                             "Project"     : 90}
    
Geographics =               {"MidtermExam" : 80,
                             "FinalExam"   : 90,
                             "Project"     : 90}
       
History =                   {"MidtermExam" : 80,
                             "FinalExam"   : 90,
                             "Project"     : 90}
    
Physics =                   {"MidtermExam" : 80,
                             "FinalExam"   : 90,
                             "Project"     : 90}
    
Turkısh =                   {"MidtermExam" : 80,
                             "FinalExam"   : 90,
                             "Project"     : 90}
x = list(Turkısh.values())
ExamOfLessons = str(input("Please choose a exam lesson: "))
AverageCourse = int(x[0] * 0.3) + int(x[1] * 0.5) + int(x[2] * 0.2)
print(f"You taked midterm exam {x[0]} , final exam {x[1]} and project {x[2]}.")
print(f"You average grade is {AverageCourse}. Congratulations!")

if AverageCourse > 90:
    print("GradeAverage: AA")

elif 70 < AverageCourse < 90:
    print("GradeAverage: BB")

elif 50 < AverageCourse < 70:
    print("GradeAverage: CC")

elif 30 < AverageCourse < 50:
    print("GradeAverage: DD")

else:
    print("GradeAverage: FF")
    print("You failed course!!")

