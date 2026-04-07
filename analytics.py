from data import users
from salary import calculate_salary

def show_analytics():
    workers = []
    salaries = []
    hours = []
    
    for username, data in users.items():
        if username != "admin":
            workers.append(username)
            work_hours = data["total_today"]
            hours.append(work_hours)
            salaries.append(calculate_salary(work_hours))
    
    if not workers:
        print("[ERROR] No data for analytics")
        return
    
    print("\n" + "="*40)
    print("ANALYTICS")
    print("="*40)
    print(f"Workers: {len(workers)}")
    print(f"Total hours: {sum(hours):.2f}")
    print(f"Total salary: {sum(salaries):.2f} units")
    print(f"Average salary: {sum(salaries)/len(workers):.2f} units")
    print(f"Max salary: {max(salaries):.2f} units ({workers[salaries.index(max(salaries))]})")
    print(f"Min salary: {min(salaries):.2f} units ({workers[salaries.index(min(salaries))]})")
    print("="*40)