from data import users

def login():
    print("\n" + "="*40)
    print("AUTHORIZATION")
    print("="*40)
    
    username = input("Login: ")
    password = input("Password: ")
    
    if username in users and users[username]["password"] == password:
        print(f"[OK] Welcome, {username}!")
        return username
    
    print("[ERROR] Invalid login or password")
    return None