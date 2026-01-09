#conditional statements
#even or odd number
n=int(input("enter a number"))
if(n%2==0):
    print("given num is even number")
else:
    print("given num is odd number")
#positive or negative numbers
n=float(input("enter a number"))
if n>0:
    print("positive number")
elif n==0:
    print("neither positive nor negative")
else:
    print("negative number")
#check if num is zero or not
num=int(input("enter a number"))
if(num==0):
    print("it is zero")
else:
    print("it is not a zero")
#check the quadratic equation (finding roots)
a=int(input())
b=int(input())
c=int(input())
d=(b^2)-(4*a*c)
e=(-b+d)/2*a
f=(-b-d)/2*a
print(e,f)
#code
n=int(input())
if (n>0 and n%2==0):
    print("positive and even")
elif (n>0 and n%2!=0):
    print("positive and odd")
elif (n<0 and n%2!=0):
    print("negative and odd")
elif (n<0 and n%2==0):
    print("negative and even")
else:
    print("it is 0")
    
        
        
