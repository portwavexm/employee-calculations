from data import users

def calculate_salary(hours_worked, hourly_rate=10):
    return hours_worked * hourly_rate

def show_salary(username):
    hours = users[username]["total_today"]
    salary = calculate_salary(hours)
    print(f"\n[SALARY] {salary:.2f} units for {hours:.2f} hours")
    return salary