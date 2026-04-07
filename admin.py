from data import users

def register_user():
    new_login = input("Enter new username: ")
    if new_login in users:
        print("[ERROR] User already exists")
        return
    
    new_password = input("Enter password: ")
    users[new_login] = {
        "password": new_password,
        "role": "user",
        "start_time": None,
        "total_today": 0
    }
    print(f"[OK] User {new_login} added")

def reset_daily_data():
    for username in users:
        if username != "admin":
            users[username]["total_today"] = 0
            users[username]["start_time"] = None
    print("[OK] Daily data reset")