# multiple outputs in same line(nested loops
n1=int(input())
n2=int(input())
n3=int(input())
if n1%2==0 and n2%2==0 and n3%2==0:
    print("n1,n2,n3 are even")
else:
    if n1%2==0 and n2%2!=0 and n3%2!=0:
        print("n1 is even,n2 and n3 are odd")
    elif n1%2==0 and n2%2==0 and n3%2!=0:
        print("n1,n2 is even,n3 are odd")
    elif n1%2==0 and n2%2!=0 and n3%2==0:
        print("n1,n2 is even,n3 are odd")
    elif n1%2!=0 and n2%2==0 and n3%2!=0:
        print("n1,n2 is even,n3 are odd")
    elif n1%2!=0 and n2%2==0 and n3%2==0:
        print("n1,n2 is even,n3 are odd")
    else:
        print("all are odd")
 #loops       
 # even or odd
lst=[1,2,3]
for i in lst:
    if i%2==0:
        print(i,"even")
    else:
        print(i,"odd")
print("program done")

# positive or negative

lst=[1,2,3,-0,-9,-4,-3]
for i in lst:
    if i>=0:
        print(i,"positive")
    else:
        print(i,"negative")
print("program done")

#range function
for i in range(1,21,1):
    print(i)
print("program done")
