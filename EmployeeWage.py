import random

EMP_FULL_TIME = 1
EMP_PART_TIME = 2
EMP_ABSENT = 0
EMP_WAGE_PER_HOUR = 20
NUM_OF_WORKING_DAYS_IN_MONTH = 20


def get_emp_daily_hours():
    switcher = {
        EMP_FULL_TIME: 8,
        EMP_PART_TIME: 4,
        EMP_ABSENT: 0
    }
    emp_hrs = switcher.get(random.randint(0, 2))

    return emp_hrs


def get_monthly_emp_hours():
    emp_hrs = 0
    for day in range(1, NUM_OF_WORKING_DAYS_IN_MONTH + 1):
        emp_hrs += get_emp_daily_hours()
    return emp_hrs


def find_emp_wage():
    emp_hrs = get_emp_daily_hours()
    daily_emp_wage = get_emp_daily_hours() * EMP_WAGE_PER_HOUR
    print('Daily Emp Wage : ' + str(daily_emp_wage))
    monthly_emp_wage = get_monthly_emp_hours() * EMP_WAGE_PER_HOUR
    print('Monthly Emp wage :', monthly_emp_wage)


if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")

    find_emp_wage()
