import random

NUM_OF_WORKING_DAYS_IN_MONTH = 20
EMP_WAGE_PER_HOUR = 20
MAX_HOURS_MONTH = 100


def get_emp_daily_hours(input_random_choice):
    '''
        EMP_FULL_TIME = 1
        EMP_PART_TIME = 2
        EMP_ABSENT = 0
    :param input_random_choice: int
    :return: emp_hrs
    '''
    switcher = {

        1: 8,
        2: 4,
        0: 0
    }
    emp_hrs = switcher.get(input_random_choice, "none")

    return emp_hrs


def get_monthly_emp_hours():
    '''
    Calculate Monthly Employee Wage based on given condition
    :return: Monthly emp_hrs
    '''
    emp_hrs = 0
    for _ in range(NUM_OF_WORKING_DAYS_IN_MONTH):
        emp_hrs += get_emp_daily_hours(random_choice)
    if emp_hrs >= MAX_HOURS_MONTH:
        return MAX_HOURS_MONTH
    else:
        return emp_hrs


def find_emp_wage():
    '''
    Calculation Of Daily And Monthly Employee Wage
    :return:
    '''
    daily_emp_wage = get_emp_daily_hours(random_choice) * EMP_WAGE_PER_HOUR
    print('Daily Emp Wage : ' + str(daily_emp_wage))
    monthly_emp_wage = get_monthly_emp_hours() * 20
    print('Monthly Emp wage :', monthly_emp_wage)


if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")
    random_choice = random.randint(0, 2)
    find_emp_wage()
