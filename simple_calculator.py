def cal():
    a=float(input("Enter first number:"))
    b=float(input("Enter second number:"))
    print("-"*20)

    print("Simple Calculator")
    print("-"*20)
    print("select arithmatic operations:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Floor Division")
    choice=int(input("Enter choice (1/2/3/4/5/6):"))
    print("-"*20)
        
    if choice==1:
        print(f"Sum of {a} and {b} is: {a+b}")
    elif choice==2:
        print(f"Difference of {a} and {b} is: {a-b}")
    elif choice==3:
        print(f"Product of {a} and {b} is: {a*b}")
    elif choice==4:
         print(f"Division of {a} and {b} is: {a/b}")
    elif choice==5:
         print(f"Modulus of {a} and {b} is: {a%b}")  
    elif cjoice==6:    
         print(f"Floor Division of {a} and {b} is: {a//b}")       
    else:
        print("invalid choice :(")
    print("-"*20)                   
cal()