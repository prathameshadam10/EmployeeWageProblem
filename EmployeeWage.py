import random


def check_emp_present_absent():
    EMP_FULL_TIME = 1

    emp_check = random.randint(0, 1)
    if emp_check == EMP_FULL_TIME:
        print("Employee Present")
    else:
        print("Employee Absent")


if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")
    check_emp_present_absent()
