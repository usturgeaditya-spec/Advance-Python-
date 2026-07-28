def call_counter(func):
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        print(f"{func.__name__} has been called {count} time(s).")
        return func()

    return wrapper

@call_counter
def say_hello():
    print("Hello!")

say_hello()
say_hello()
say_hello()
