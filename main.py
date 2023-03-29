# ----------------------------------------------------------------
# Author: Mason Williams
# Date: 12/01/2021
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for. It also allows students to review the tuition
# # costs for their course roster.
# -----------------------------------------------------------------
import student

import billing


def main():
    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, in_state_list, course
    # list, max class size list and roster list.  It uses a loop to
    # serve multiple students. Inside the loop, ask student to enter
    # ID, and call the login function to verify student's identity.
    # Then let student choose to add course, drop course or list
    # courses. This function has no return value.
    # -------------------------------------------------------------
    student_id_list = ['1001', '1002', '1003', '1004']
    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444')]
    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False}

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': []}
    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}

    # class init section
    stu_obj_lst = {}
    bill_obj_lst = {}
    for i in range(len(student_id_list)):
        student_id = student_id_list[i]
        stu_obj_lst[student_id] = stu_obj_lst.get(student_id, student.Student(student_id, course_roster, course_max_size))
        bill_obj_lst[student_id] = bill_obj_lst.get(student_id, billing.Billing(student_id, course_roster, course_max_size, student_in_state,course_roster, course_hours))

    # Login section
    student_id = ""
    z = ""
    y = ""
    z = ""

    while True:
        x = ""
        x = input("Enter ID to log in, or 0 to quit: ")
        if x == "0":
            break
        else:
            student_id = x
            log = ""
            log = login(student_id, student_list)
            if log == "login success":
                pass
            else:
                continue

            while True:
                y = ""
                y = input("Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: ")
                if y == "0":
                    break
                elif y == "1":
                    stu_obj_lst[student_id].add_course()
                    print(course_roster)
                    y = False
                elif y == "2":
                    stu_obj_lst[student_id].drop_course()
                    y = False
                elif y == "3":
                    stu_obj_lst[student_id].list_courses()
                    y = False
                elif y == "4":
                    bill_obj_lst[student_id].calculate_hours_and_bill()
                    bill_obj_lst[student_id].display_hours_and_bill()
                    print(bill_obj_lst[student_id])
                    y = False


def login(student_id, s_list) -> str:
    s_id_check = student_id
    s_list = s_list

    z = ""

    user_pin = input("Please enter your student PIN number: ")

    if (s_id_check, user_pin) in s_list:
        print("login success")
        z = False
        return "login success"

        # return False
    else:
        print("ID or PIN incorrect")
        z = True
        return "ID or PIN incorrect"


main()






main()
