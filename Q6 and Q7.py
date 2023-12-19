#6. (Table) Using the techniques of this chapter, write a program that calculates the squares and
#7. cubes of the integers from 0 to 10. Use tabs to print the following neatly formatted table of 
#values:
n=0
print("integer ","square  ","cube")
while(n<=10):
    sq=n**2
    cb=n**3
    if(len(str(sq))==2):
        print(n,"      ",sq,"     ",cb)
    elif(len(str(sq))==3):
        print(n,"     ",sq,"    ",cb)
    else:
        print(n,"      ",sq,"      ",cb)
    n=n+1
    

