def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i+1)
    name = input("Name: ")
    roll = input("Roll No: ")

    m1 = int(input("Marks 1: "))
    m2 = int(input("Marks 2: "))
    m3 = int(input("Marks 3: "))

    total = m1 + m2 + m3
    avg = total / 3
    grade = calculate_grade(avg)

    students.append([name, roll, total, avg, grade])

print("\n----- Student Results -----")
for s in students:
    print("Name:", s[0])
    print("Roll:", s[1])
    print("Total:", s[2])
    print("Average:", s[3])
    print("Grade:", s[4])
    print("------------------------")
