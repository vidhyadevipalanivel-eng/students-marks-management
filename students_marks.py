print("===== Student Marks Management System =====")

name = input("Enter student name: ")

mark1 = int(input("Enter mark for Subject 1: "))
mark2 = int(input("Enter mark for Subject 2: "))
mark3 = int(input("Enter mark for Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\n----- Student Report -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", round(average, 2))

if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
