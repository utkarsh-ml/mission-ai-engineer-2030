def get_numbers():
    while True:
        try:
            count = int(input("enter how many no do you want to operate?"))
            if count<2:
                print("please enter atleast two numbers")
                continue
            break
        except ValueError:
            print("please enter a valid whole number.")
    numbers =[]
    for i in range(count):
        while True:
            try:
                num = float(input(f"enter the numbers {i+1}:"))
                numbers.append(num)
                break
            except ValueError:
                print("please enter valid number.")
    return numbers
def calculate(numbers,operations):
    result = numbers[0]
    for num in numbers[1:]:
        if operations == "+":
            result += num
        elif operations == "-":
            result -= num
        elif operations == "*":
            result *= num
        elif operations == "/":
            if num == 0:
                return "error : division by zero"
            result /= num
    return result

def get_operations():
    valid_ops = ["+","-","*","/"]
    while True:
        op = input("choose an operation(+,-,*,/)")
        if op in valid_ops:
            return op
        print("invalid operations")

def main():
    print("="*50)
    print("simple calculator".center(50))
    print("="*50)
    while True:
        numbers = get_numbers()
        operations = get_operations()
        result = calculate(numbers,operations)
        print("Result =",result)
        while True:
            choice = input("do you want continue or exit?(c/e)").strip().lower()
            if choice in  ("c","continue"):
                print()
                break
            elif choice in ("e","exit"):
                print("good bye")
                return
            else:
                print("please type 'c' to continue or 'e' to exit.")

main()





      

                  