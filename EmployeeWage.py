import random

if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")
    emp_full_time = 1
    emp_part_time = 2
    emp_wage_per_hour = 20
    emp_hrs = 0
    daily_emp_wage = 0

    emp_check = random.randint(0, 2)
    if emp_check == emp_full_time:
        emp_hrs = 8
        print("Employee Full-time Present")
    elif emp_check == emp_part_time:
        emp_hrs = 4
        print("Employee Part-time Present")
    else:
        emp_hrs = 0
        print("Employee Absent")
    daily_emp_wage = emp_hrs * emp_wage_per_hour
    print('Emp Wage : ' + str(daily_emp_wage))

