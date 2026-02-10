# Student Grade Calculator

name = input("Enter student name: ")
m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))

total = m1 + m2 + m3
average = total / 3

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

print("\n--- Result ---")
print("Name:", name)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)
