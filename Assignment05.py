# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   JGraham,11/9/2026, Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.

# When the program starts, read the file data into a list of dictionaries (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("File not found.")
except Exception as e:
    print("An error occurred while attempting to open the JSON file.")
    print(e, e.__doc__)
finally:
# If error occurred, check if a file object exists and is still open
    if file is not None and file.closed == False:
        file.close()

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name can only contain letters.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name can only contain letters.")
        except ValueError as e:
            print("Student names can only contain letters.")
            continue
        course_name = input("Please enter the name of the course: ")
        student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "CourseName": course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name}"
              f" for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-" * 50)
        try:
            for student in students:
                print(f"Student {student['FirstName']} "
                      f"{student['LastName']}"
                      f" is enrolled in "
                      f"{student['CourseName']}.\n")
        except Exception as e:
            print("An error occurred while attempting to display"
                  " student data.")
            print(e, e.__doc__)
            continue

        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students,file,indent=2)
            file.close()
        except TypeError as e:
            print("Please ensure data is in JSON format.\n")
            print(e, e.__doc__)
        except Exception as e:
            print("An error occurred while writing to the file.\n")
            print(e, e.__doc__)
        finally:
            # If error occurred, check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()

        try:
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student['FirstName']} "
                      f"{student['LastName']} "
                      f"is enrolled in {student['CourseName']}.\n")
        except Exception as e:
            print("Data is saved. An error occurred displaying string.\n")
            print(e, e.__doc__)
            continue
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
