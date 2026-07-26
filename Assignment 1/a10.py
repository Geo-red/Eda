try:
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))

    result=a/b
    print(result)

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except ValueError:
    print("Enter valid numbers.")

except Exception as e:
    print("Unexpected error:",e)
