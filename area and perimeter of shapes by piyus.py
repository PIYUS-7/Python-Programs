#coded by Piyus 12'c'
def square (a):
    area = a * a
    perimeter = 4 * a
    print("Area: ",area)
    print("Perimeter: ",perimeter)

def rectangle (l,b):
    area = l * b
    perimeter = 2 * (l+b)
    print("Area: ",area)
    print("Perimeter: ",perimeter)

def triangle (b,h):
    area = (1/2) * b * h
    print("Area: ",area)

def circle (r):
    area = (22/7) * r * r
    perimeter = 2 * (22/7) * r
    print("Area: ",area)
    print("Perimeter: ",perimeter)

def trapezium (x,y,h):
    area = (1/2) * (x+y) * h
    print("Area: ",area)

print("\t\t ---> Area and Perimeter of Shapes <---")

while True:
    choice = int(input("\nDo you want to calculate: \n1.Yes \n2.No \nChoose the option (1/2) : "))
    if choice == 1:
        print("\n1.Triangle \n2.Square \n3.Rectangle \n4.Circle \n5.Trapezium")
        option = int(input("Enter a number between 1 to 5 to perform the operation : "))

        if option == 1:
            b = int(input("Enter the length of base : "))
            h = int(input("Enter the length of height : "))
            triangle(b,h)

        elif option == 2:
            a = int(input("Enter the length of side : "))
            square(a)

        elif option == 3:
            l = int(input("Enter the length of length : "))
            b = int(input("Enter the length of breadth : "))
            rectangle(l,b)

        elif option == 4:
            r = int(input("Enter the length of radius : "))
            circle(r)

        elif option == 5:
            x = int(input("Enter the length of 1st side : "))
            y = int(input("Enter the length of 2nd side : "))
            h = int(input("Enter the length of height : "))
            trapezium(x,y,h)

        else:
            print('Invalid input! ! ! \nPlease try again')
    else:
        print("Have a nice day! ! ! ")
        break