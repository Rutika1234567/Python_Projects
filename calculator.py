try:
    a=int(input("enter a first number: "))
    b=int((input("enter the second number:")))

    print("what kind of operation do you want to perform. press + for addition\nPress " 
    "- for subtration\nPress /for division\npress* for multiplication")

    o=input("Enter opertion: ")
    match o:
         case '+':
              print(f"The sum is {a+b}")
         case '-':
              print(f"The subtration is {a-b}")
         case '/':
              print(f"The division is {a/b}")
         case '*':
              print(f"The multiplication is {a*b}")
         case default:
              print(f"There is an Error")          
except  Exception as e:
      print("enter a valid value of a and b")











