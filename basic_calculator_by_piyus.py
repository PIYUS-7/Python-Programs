def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def power(x,y):
    return x**y

def task(x):
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if x == 1:
        result = add(a,b)
    elif x == 2:
        result = subtract(a,b)
    elif x == 3:
        result = multiply(a,b)
    elif x == 4:
        result = divide(a,b)
    elif x == 5:
        result = power(a,b)
    print('The result is:',result)
    last()

def last():
    last = int(input('''Do you want to calculate more ?
1.Yes
2.No
Enter the choice (1/2): '''))
    if last == 1:
        main()
    

def decision(x):
    if x in [1,2,3,4,5]:
        task(x)
    else:
        print("Choose the correct choice !")
        main()


def main():
    
    print("\t\t ---> Basic Calculator <---")
    choice = int(input('''
    1.Addition 
    2.Subtraction 
    3.Multiplication 
    4.Division 
    5.Power 
    Enter the choice between 1 to 5 :'''))
    decision(choice)

main()
