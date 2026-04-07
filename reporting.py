from data import users
from salary import calculate_salary

def show_report():
    print("\n" + "="*40)
    print("REPORT")
    print("="*40)
    
    for username, data in users.items():
        if username != "admin":
            salary = calculate_salary(data["total_today"])
            print(f"{username:15} - {salary:8.2f} units")
    print("="*40)