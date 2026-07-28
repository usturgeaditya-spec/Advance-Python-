# Login Authentication Decorator

logged_in = True  

def login_required(func):
    def wrapper():
        if logged_in:
            return func()
        else:
            print("Access Denied! Please log in first.")
    return wrapper

@login_required
def view_dashboard():
    print("Welcome to your Dashboard!")

view_dashboard()