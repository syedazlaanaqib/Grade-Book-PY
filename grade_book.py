# grade_book.py
# A simple command-line grade book.

students = {}  # name -> list of marks


def show_menu():
    print("\n=== Grade Book ===")
<<<<<<< HEAD
    print("1. Show grades")
    print("0. Exit")


def calculate_grade(average):
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 55:
        return "C"
    elif average >= 40:
        return "D"
    return "F"


def show_grades():
    if not students:
        print("No students yet.")
        return

    for name, marks in students.items():
        average = sum(marks) / len(marks)
        print(
            f"{name}: average {average:.1f}, "
            f"grade {calculate_grade(average)}"
        )


=======
    print("1. Add Student")
    print("0. Exit")

def add_student(): 
    name = input("Student name: ") 
    marks = int(input("Marks separated by spaces: ") )
    students[name] = [int(m) for m in marks.split()] 
    print(f"Added {name}.")
    
>>>>>>> 68fb9bf72d8533e48adc85c177d28efcd939a9d7
def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            show_grades()
        else:
            add_student()


students = {"Ali": [78, 91, 66]}


if __name__ == "__main__":
    main()
