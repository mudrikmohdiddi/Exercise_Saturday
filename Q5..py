#5. (Digits of an Integer) Write a program that inputs a five-digit integer, separates the integer 
#into its digits and prints them separated by three spaces each. [Hint: Use the integer division 
#and modulus operators.] For example, if the user types in 42339, the program should print:
#4 2 3 3 9
p=8
while(p==8):
    try:
        y=int(input("\nPlease enter five-digit integer:"))
        if(y>=10000 and y<100000):
            a=y//10000
            b=(y%10000)//1000
            c=(y%1000)//100
            d=(y%100)//10
            e=y%10
            sp=("   ")
            print(a,sp,b,sp,c,sp,d,sp,e)
        else:
            print("You enter wrong input, please try again")
    except ValueError:
        print("You enter wrong input, please try again")
        
            
            
