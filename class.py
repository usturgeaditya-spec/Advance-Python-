# 1.Required Argument
def student(name,roll):
    print("Required Argument:")
    print("Name:",name)
    print("Roll No:",roll)
    print()

    # 2.Keyword Argument
    def employee(name,salary):
        print("Keyword Argument:")
        print("Name:",name)
        print("Salary:",salary)
        print()

        # 3.Default Argument
        def student_default(Roll_no,name,classroom="SY-2"):
            print("Default Argument:")
            print("Roll no:",Roll_no)
            print("Name:",name)
            print("Class:",classroom)
            print()

            # 4.Variable length Argument
            def addition(*numbers):
                total=sum(numbers)
                print("Variable Length Arguments:")
                print("Numbers:",numbers)
                print("Sum=",total)
                print()

                student("Aditya",7)
                employee(salary=15000,name="Rahul")
                student(7,"Aditya","SY-2")
                addition(10,20)