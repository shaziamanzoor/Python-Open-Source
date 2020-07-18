def area_calculator():
    print("Calculate area of square\n")
    x = input("Enter the length of square ? ")
    x = int(x)
    areaOfSquare = x * x
    print(f"The area of square is {areaOfSquare}")

    print("Calculate the area of rectangle\n")
    length = input("Enter the length of rectangle ? ")
    length = int(length)
    breadth = input("Enter the breadth of rectangle ? ")
    breadth = int(breadth)
    print(f"The area of Rectangle = {length * breadth}")
area_calculator()
