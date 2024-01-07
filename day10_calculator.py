def add(n1, n2):
    return n1  + n2

def subs(n1, n2):
    return n1 - n2

def multi(n1 , n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2


operations = {
    "+":  add,
    "-": subs,
    "*": multi,
    "/": divide,
}



def calculator():
    num1 = int(input("Enter number 1: "))
    for operators in operations:
        print(operators)

    # symbol = input("Enter the operation you want to perform: ")
    should_continue = True
    while should_continue:
        operation_symbol = input("Enter the next operation: ")
        num2 = int(input("Enter the next number: "))
        calc_func = operations[operation_symbol]
        answer = calc_func(num1 , num2)
        print(f"{num1} {operation_symbol} {num2} is {answer}.")

        if input(f"Type 'y' to continue with the {answer}  ").lower() == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()