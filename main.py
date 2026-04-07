from data import users
from auth import login
from work_time import start_work, end_work
from salary import show_salary
from reporting import show_report
from admin import register_user, reset_daily_data
from analytics import show_analytics
from storage import save_report_to_file

def user_menu(username):
    menu_actions = {
        "1": lambda: start_work(username),
        "2": lambda: end_work(username),
        "3": lambda: show_salary(username),
    }
    
    while True:
        print("\n" + "="*40)
        print(f"USER: {username}")
        print("="*40)
        print("1. Start work")
        print("2. Stop work")
        print("3. Show salary")
        print("4. Exit")
        
        choice = input("Select action (1-4): ")
        
        if choice == "4":
            if users[username]["start_time"]:
                end_work(username)
            print(f"Goodbye, {username}!")
            break
        
        action = menu_actions.get(choice)
        if action:
            action()
        else:
            print("[ERROR] Invalid choice")

def admin_menu(username):
    menu_actions = {
        "1": lambda: start_work(username),
        "2": lambda: end_work(username),
        "3": lambda: show_salary(username),
        "4": lambda: show_report(),
        "5": lambda: register_user(),
        "6": lambda: show_analytics(),
        "7": lambda: save_report_to_file(),
        "8": lambda: reset_daily_data(),
    }
    
    while True:
        print("\n" + "="*40)
        print(f"ADMIN: {username}")
        print("="*40)
        print("1. Start work")
        print("2. Stop work")
        print("3. Show salary")
        print("4. Show report")
        print("5. Add user")
        print("6. Analytics")
        print("7. Save report")
        print("8. Reset data")
        print("9. Exit")
        
        choice = input("Select action (1-9): ")
        
        if choice == "9":
            if users[username]["start_time"]:
                end_work(username)
            print(f"Goodbye, {username}!")
            break
        
        action = menu_actions.get(choice)
        if action:
            action()
        else:
            print("[ERROR] Invalid choice")

def main():
    print("\n" + "="*40)
    print("WORK TIME TRACKING SYSTEM")
    print("="*40)
    
    while True:
        username = login()
        if username:
            if users[username]["role"] == "admin":
                admin_menu(username)
            else:
                user_menu(username)
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()