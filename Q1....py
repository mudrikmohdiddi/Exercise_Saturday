#1. Write a program that inputs three integers from the key-board and prints the sum, average, 
#product, smallest and largest of these numbers.

a=9
while(a==9):
    try:
        n1=int(input("\nPlease enter first integer:"))
        n2=int(input("\nPlease enter second integer:"))
        n3=int(input("\nPlease enter third integer"))
        s=n1+n2+n3
        av=s/3
        p=n1*n2*n3
        sm=min(n1,n2,n3)
        lg=max(n1,n2,n3)
        print("\nSum=",s)
        print("Average=",av)
        print("Smallest=",sm)
        print("Lagest=",lg)
    except ValueError:
        print("\nYou enter wrong input, please try angain")

        
        
    
