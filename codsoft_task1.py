print("+")
print("-")
print("*")
print("/")
x = input("choose an operation: ")
if x in ["+","-","*","/"]:
    number1 = int(input("Enter num1 :"))
    number2 = int(input("Enter num2 :"))
    if (x == ("+")):
        print(number1+number2)
    elif (x ==("-")):
        print(number1-number2)
    elif (x == ("*")):
        print(number1 * number2)
    elif (x == ("/")):
        print(number1 / number2)
else:
    print("invalid entery")
    