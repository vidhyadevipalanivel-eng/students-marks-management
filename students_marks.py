
print("===== Student Marks Management System =====")

name = input("Enter student name: ")

marks = []

for i in range(1, 4):
    while True:
        try:
            mark = int(input(f"Enter mark for Subject {i} (0-100): "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter a mark between 0 and 100.")

        except ValueError:
            print("Invalid input! Enter a whole number.")

total = sum(marks)
average = total / len(marks)

print("\n----- Student Report -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", round(average, 2))

if all(mark >= 35 for mark in marks):
    print("Result: PASS")
else:
    print("Result: FAIL")
