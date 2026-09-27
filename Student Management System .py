print("STUDENTS MANAGEMENT SYSTEM")
students = {}


def add_student():
    print("\n========== ADD STUDENT ==========")

    try:
        roll_no = int(input("Enter Roll Number: "))
    except ValueError:
        print("Please enter a valid roll number.")
        return

    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    branch = input("Enter Branch: ")

    try:
        age = int(input("Enter Age: "))
        python_marks = float(input("Enter Python Marks: "))
        maths_marks = float(input("Enter Mathematics Marks: "))
        english_marks = float(input("Enter English Marks: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    students[roll_no] = {
        "name": name,
        "branch": branch,
        "age": age,
        "python": python_marks,
        "maths": maths_marks,
        "english": english_marks
    }

    print("Student added successfully!")


def view_students():
    print("\n========== ALL STUDENTS ==========")

    if not students:
        print("No student records available.")
        return

    for roll_no, details in students.items():
        print("\nRoll Number :", roll_no)
        print("Name        :", details["name"])
        print("Branch      :", details["branch"])
        print("Age         :", details["age"])
        print("Python      :", details["python"])
        print("Mathematics :", details["maths"])
        print("English     :", details["english"])
        print("---------------------------------")


def search_student():
    print("\n========== SEARCH STUDENT ==========")

    try:
        roll_no = int(input("Enter Roll Number: "))
    except ValueError:
        print("Please enter a valid roll number.")
        return

    if roll_no in students:
        details = students[roll_no]

        print("\nStudent Found!")
        print("Roll Number :", roll_no)
        print("Name        :", details["name"])
        print("Branch      :", details["branch"])
        print("Age         :", details["age"])
        print("Python      :", details["python"])
        print("Mathematics :", details["maths"])
        print("English     :", details["english"])
    else:
        print("Student not found.")


def update_student():
    print("\n========== UPDATE STUDENT ==========")

    try:
        roll_no = int(input("Enter Roll Number: "))
    except ValueError:
        print("Please enter a valid roll number.")
        return

    if roll_no not in students:
        print("Student not found.")
        return

    name = input("Enter New Name: ")
    branch = input("Enter New Branch: ")

    try:
        age = int(input("Enter New Age: "))
        python_marks = float(input("Enter New Python Marks: "))
        maths_marks = float(input("Enter New Mathematics Marks: "))
        english_marks = float(input("Enter New English Marks: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    students[roll_no]["name"] = name
    students[roll_no]["branch"] = branch
    students[roll_no]["age"] = age
    students[roll_no]["python"] = python_marks
    students[roll_no]["maths"] = maths_marks
    students[roll_no]["english"] = english_marks

    print("Student details updated successfully!")


def delete_student():
    print("\n========== DELETE STUDENT ==========")

    try:
        roll_no = int(input("Enter Roll Number: "))
    except ValueError:
        print("Please enter a valid roll number.")
        return

    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def calculate_result():
    print("\n========== STUDENT RESULT ==========")

    try:
        roll_no = int(input("Enter Roll Number: "))
    except ValueError:
        print("Please enter a valid roll number.")
        return

    if roll_no not in students:
        print("Student not found.")
        return

    details = students[roll_no]

    total = (
        details["python"]
        + details["maths"]
        + details["english"]
    )

    percentage = total / 3

    print("\nStudent Name :", details["name"])
    print("Roll Number  :", roll_no)
    print("Total Marks  :", total)
    print("Percentage   :", round(percentage, 2), "%")

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    print("Grade        :", grade)

    if percentage >= 40:
        print("Result       : PASS")
    else:
        print("Result       : FAIL")


def find_topper():
    print("\n========== TOPPER ==========")

    if not students:
        print("No student records available.")
        return

    topper_roll = None
    highest_percentage = -1

    for roll_no, details in students.items():
        total = (
            details["python"]
            + details["maths"]
            + details["english"]
        )

        percentage = total / 3

        if percentage > highest_percentage:
            highest_percentage = percentage
            topper_roll = roll_no

    topper = students[topper_roll]

    print("\nTopper Details")
    print("----------------------------")
    print("Roll Number :", topper_roll)
    print("Name        :", topper["name"])
    print("Branch      :", topper["branch"])
    print("Percentage  :", round(highest_percentage, 2), "%")
    print("----------------------------")


def count_students():
    print("\n========== TOTAL STUDENTS ==========")
    print("Total Students:", len(students))


def main():
    while True:
        print("\n========================================")
        print("       STUDENT MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Result")
        print("7. Find Topper")
        print("8. Count Students")
        print("9. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            calculate_result()

        elif choice == "7":
            find_topper()

        elif choice == "8":
            count_students()

        elif choice == "9":
            print("\nThank you for using Student Management System!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1 to 9.")


main()