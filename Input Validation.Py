def validate_positive(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int) or arg <= 0:
                print("Error: All arguments must be positive integers.")
                return
        return func(*args)
    return wrapper

@validate_positive
def multiply(a, b):
    print("Product =", a * b)

multiply(5, 4)
multiply(-2, 3)
multiply(5, "10")