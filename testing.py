
def add (a , b):
    return(a+b)
def subtract (a,b):
    return (a-b)
def divide (a,b):
    return (a / b)
def multipy(a,b): 
    return (a*b )
def percent (a):
    return (a*100)
def square (a):
    return (a*a)
def cube (a):
    return (a*a*a)
while True: 
    print (""" 1.Menu 2. Addition 3. Subtraction 4. Division 5.Multiply 6.Percentage 7. Square 8. Cube 9. Exit""")
    choice= input ("choose from menu   ")
    if choice== "9": 
       print("exiting calculator")
       break
    if choice == "6" or choice== "7" or choice=="8":
        a= float(input("enter a number:"))
        if choice== "6":
            result= multipy(a,100)
            print("value is:", result)      
        if choice== "7":
            result= square(a)
            print ("value is:", result)
        if choice== "8": 
            result= cube(a)
            print ("value is:", result)
    else:
        a= float(input("enter your first number"))
        b= float(input("enter your second number"))
        if choice== "2":
            result= add(a,b)
            print ("value is:",result)
        if choice== "3":
            result= subtract (a, b )
            print ("value is:",result)
        if choice== "4":
            result=divide (a,b)
            print ("value is:",result)
        if choice== "5":
            result= multipy (a,b)
            print ("value is:",result)
     

    