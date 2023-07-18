import random

if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")
    emp_full_time = 1

    emp_check = random.randint(0, 1)
    if emp_check == emp_full_time:
        print("Employee Present")
    else:
        print("Employee Absent")

