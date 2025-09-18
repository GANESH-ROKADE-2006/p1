def add(n1, n2):
    return n1 + n2
def sub(n1 ,n2):
    return n1 - n2
def multi(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operation={"+":add,"-":sub,"*":multi,"/":div}

def calculator():
    n1 = float(input("enter 1st no : "))
    should_accumulate = True

    while should_accumulate:
        for symbol in operation:
            print(symbol)
        operation_symbol=input("enter the operator")
        n2= float(input("enter 2st no : "))
        ans=operation[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {ans}")
        choice = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ")

        if choice == "y":
            n1 = ans
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()