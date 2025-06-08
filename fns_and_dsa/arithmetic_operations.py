def perform_operation(num1,num2,operation):
    num1 = float(num1)
    num2 = float(num2)

    if  operation == "add":
        return num1 + num2
    if operation == "subtract":
        return num1 - num2
    if operation == "multiply":
        return num1 * num2
    if operation == "divide" and num2 == 0:
        return 'Cannot divide by zero'
    return num1 / num2
