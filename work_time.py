from datetime import datetime
from data import users

def start_work(username):
    users[username]["start_time"] = datetime.now()
    print(f"[START] Work started at {users[username]['start_time'].strftime('%H:%M:%S')}")

def end_work(username):
    if users[username]["start_time"] is None:
        print("[ERROR] Work not started")
        return 0
    
    end_time = datetime.now()
    hours_worked = (end_time - users[username]["start_time"]).total_seconds() / 3600
    users[username]["total_today"] += hours_worked
    users[username]["start_time"] = None
    
    print(f"[STOP] Work finished at {end_time.strftime('%H:%M:%S')}")
    print(f"[INFO] Total today: {users[username]['total_today']:.2f} hours")
    return hours_worked