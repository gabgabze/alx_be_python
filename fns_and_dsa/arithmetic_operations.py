def perform_operation(num1,num2,operation):
    number1 = float(num1)
    number2 = float(num2)
    operation = str(operation)
    match operation:
        case 'add':
            return number1+number2
        case 'subtract':
            return number1-number2
        case 'multiply':
            return number1*number2
        case 'divide':
            if number1 > 0  and number2 == 0:
                return 'Cannot divide by zero'
            return number1/number2

"""    if operation == "+":
        return number1 + number2
    if operation == "-":
        return number1 - number2
    if operation == "*":
        return number1 * number2
    if operation == "/":
        if number1 > 0 and number2 == 0:
            return'Cannot divide by zero'
        
            return number1 / number2"""

print(perform_operations(1,3,"+"))