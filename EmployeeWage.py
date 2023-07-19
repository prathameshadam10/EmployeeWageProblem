import random

EMP_FULL_TIME = 1
EMP_PART_TIME = 2
EMP_WAGE_PER_HOUR = 20


def get_emp_hours(x):
    emp_hrs = 0
    if x == EMP_FULL_TIME:
        emp_hrs = 8
    elif x == EMP_PART_TIME:
        emp_hrs = 4
    else:
        emp_hrs = 0
    return emp_hrs


def find_daily_wage():
    y = get_emp_hours(random.randint(0, 2))
    daily_emp_wage = y * EMP_WAGE_PER_HOUR
    print('Emp Wage : ' + str(daily_emp_wage))


if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")
    find_daily_wage()