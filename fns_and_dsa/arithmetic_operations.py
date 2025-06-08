def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num1 > 0 and num2 == 0:
                return 'Cannot divide by zero'
            else:
                return num1 / num2


"""  if  operation == "add":
        return num1 + num2
    if operation == "subtract":
        return num1 - num2
    if operation == "multiply":
        return num1 * num2
    if operation == "divide" and num2 == 0:
        return 'Cannot divide by zero'
    return num1 / num2  """
