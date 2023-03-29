# Mason Williams
# 12/05/2021
# This program allows the user to add, drop, and list classes
# to the class roster.


class Student:

    # The init class initializes the different variables that the
    # user will need to use to utilize each method of this program

    def __init__(self, student_id, c_roster, c_max_size):
        self.student_id = student_id
        self.c_roster = c_roster
        self.c_max_size = c_max_size

    # The add course method lets the user add a course if the course
    # intended meets the criteria of being in the roster, not full,
    # or not already enrolled into and prompts an error if these
    # conditions aren't met.

    def add_course(self):
        student_input = input("Enter the course you want to add: ")
        if student_input in self.c_roster:
            if len(self.c_roster[student_input]) < self.c_max_size[student_input]:
                if self.student_id not in self.c_roster[student_input]:
                    self.c_roster[student_input].append(self.student_id)
                    return self.c_roster
                else:
                    print('You are already enrolled in this class')
            else:
                print('This class has reached max capacity.')
        else:
            print('This class is not in our roster.')
        return self.c_roster

    # The drop course method allows the student to drop a class if the
    # class exists in the roster and the student is enrolled in it and
    # prompts an error if the criteria isn't met.

    def drop_course(self):
        student_input = input("Please enter the class you want to drop: ")
        if student_input in self.c_roster:
            if self.student_id in self.c_roster[student_input]:
                self.c_roster[student_input].remove(self.student_id)
            else:
                print("You are not enrolled in this class.")
        else:
            print("This class is not in our roster")

        return self.c_roster

    # This method allows the user to list the courses that they are enrolled into

    def list_courses(self):
        course_list = []
        for i in self.c_roster:
            if self.student_id in self.c_roster[i]:
                course_list.append(i)
                print(i)
                print(f'Courses registered {course_list}')  # only j cause only want course displayed
