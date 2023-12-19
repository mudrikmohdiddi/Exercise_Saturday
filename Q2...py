#2. (Diameter, Circumference and Area of a Circle) Write a program that reads in the radius of
# a circle as an integer and prints the circle’s diameter, circumference and area. Use the 
#constant value 3.14159 for π . Do all calculations in output statements.
f=4
while(f==4):
    try:
        r=int(input("\nPlease enter radius of circle:"))
        d=2*r
        π=3.14159
        c=2*π*r
        a=π*r**2
        print("\ncircle’s diameter is:",d)
        print("Circumference is:",c)
        print("Area of circle is:",a)
    except ValueError:
        print("\nYou enter wrong input, please try angain")
        




