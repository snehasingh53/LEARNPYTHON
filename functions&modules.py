''' 
def greet(str1):
    print("good evening!!!!!")
    print(str1)
nm = input("Enter your name :" )
greet(nm)
'''


'''  
def calculation(num1,num2,operation) :
    if operation=="+":
        sum= num1+num2
        return sum 
    elif operation=="-":
        diff= num1-num2
        return diff
    elif operation=="*":
        mult = num1*num2
        return mult
    elif operation=="/":
        div = num1//num2
        return div
    else:
        print("operation not supported")
    
    
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation =input("Enter the operation to be performed  +,-,*,/:")
result=calculation(num1,num2,operation)
print(result)

'''


### for multiple retun use return add,sub,mul,div
