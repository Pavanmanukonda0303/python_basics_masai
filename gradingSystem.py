print("This program will give the grade of a student based on the marks obtained")

marks = float(input("Please enter the marks obtained by the student: "))

if marks >= 90:
    grade = "Grade A"
elif marks >= 75:
    grade = "Grade B"
elif marks >= 50:
    grade = "Grade C"

else:
    grade = "Grade F"

print(f"The grade of the student is: {grade}")