def safe_divide(numerator, denominator):
    try:
        final_value = float(numerator) / float(denominator)
        return f'The result of the division is {final_value}'
    except ZeroDivisionError:
        if denominator == 0:
            return 'Cannot divide by zero'
    except ValueError:
        if numerator.isalpha() or denominator.isalpha():
            return 'Error: Please enter numeric values only.'
