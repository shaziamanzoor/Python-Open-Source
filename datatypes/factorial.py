def fact():
    num = int(input("Enter a Number: "))
    if num < 0:
        print("Negative number: cant find factorial")
    elif num == 0:
        print("Factorial of 0 is 1")
    else:
        result = 1
        while num != 1:
            result = result * num
            num = num - 1
    print(f"Factorial is {result}")
fact()     
        
    
    
