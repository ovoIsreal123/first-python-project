num1 = float(input("put any number"))
num2 = float(input ("input another number"))
operator = input("input mathematical operand")
if operator == "+": 
    result = num1 + num2 
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "/":
    if num2 == 0:
        result = "input another number other than zero"
        print (result)
    elif num2 != 0:
        result = num1/num2
        print (result)
elif operator == "*":
    result = num1*num2
    print (result)
