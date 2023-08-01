import random

EMP_FULL_TIME = 1
EMP_PART_TIME = 2
EMP_ABSENT = 0
EMP_WAGE_PER_HOUR = 20


def get_emp_hours():
    switcher = {
        EMP_FULL_TIME: 8,
        EMP_PART_TIME: 4,
        EMP_ABSENT: 0
    }


    emp_hrs = switcher.get(random.randint(0, 2))

    return emp_hrs


def find_daily_wage():
    emp_hrs = get_emp_hours()
    daily_emp_wage = emp_hrs * EMP_WAGE_PER_HOUR
    print('Emp Wage : ' + str(daily_emp_wage))


if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")
    find_daily_wage()
