from datetime import datetime
from data import users
from salary import calculate_salary

def save_report_to_file():
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"report_{date_str}.txt"
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("="*50 + "\n")
        file.write(f"REPORT FOR {datetime.now().strftime('%Y-%m-%d')}\n")
        file.write("="*50 + "\n\n")
        
        total_salary = 0
        for username, data in users.items():
            if username != "admin":
                salary = calculate_salary(data["total_today"])
                total_salary += salary
                file.write(f"{username:15} - {salary:8.2f} units (hours: {data['total_today']:.2f})\n")
        
        file.write("\n" + "-"*50 + "\n")
        file.write(f"TOTAL: {total_salary:.2f} units\n")
    
    print(f"[OK] Report saved to {filename}")