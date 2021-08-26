def calculator(a, b, operator):
    if (operator == "+"):
        output = a + b

    elif operator == '-':
        output = a - b

    elif operator == '*':
        output = a * b

    elif operator == '/':
        output = a / b
    else:
        output = 0

    return output


print(" The result is:")
print(calculator(10, 3, "-"))
