#relational operators
a=10
b=20
a=a>b
print(a)
b=a<b
print(b)
c=a>=b
print(c)
d=a<=b
print(d)
e=a==b
print(e)
f=a!=b
print(f)
#logical operators
c=30
g=a<b and b<c
print(g)
h=a>b or b<c
print(h)
i= not b<c
print(i)
#assignment operators
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a%=b
print(a)
a//=b
print(a)
a**=b
print(a)
#bitwise operators
a=10
b=20
a=a&b
print(a)
a=a|b
print(a)
a=a^b
print(a)
a=~b
print(a)
a=a<<2
print(a)
a=a>>2
print(a)
#identity operators
a=a is b
print(a)
a=a is not b
print(a)
#membership operators
l=[1,2,3]
b=[1,2]
c=b in l
print(c)
d=b not in l
print(d)
#type casting
#int to other datatypes
a=10
b=20
a=float(b)
print(a)
a=str(b)
print(a)
a=bool(b)
print(a)
#float to other datatypes
a=10.0
b=10.0
b=int(a)
print(b)
b=str(a)
print(b)
b=bool(a)
print(b)
#str to other datatypes
a="navya"
b="123"
b=int(b)
print(b)
b=float(int(b))
print(b)
#bool to other datatypes
a=bool(0)
print(a)
b=bool(1)
print(b)
b=bool(-1)
print(b)
#list to other datatypes
l1=[1,2,3]
a=str(l1)
print(a)
b=tuple(l1)
print(b)
c=set(l1)
print(c)
#tuple to other datatypes
t=(1,1,2,3)
a=list(t)
print(a)
a=str(t)
print(a)
c=set(t)
print(c)
#set to other datatypes
t={1,1,2,3}
a=list(t)
print(a)
a=str(t)
print(a)
c=set(t)
print(c)
c=tuple(t)
print(c)
#dictionary to other datatypes
t={1:'a',2:'b',3:'c'}
a=list(t)
print(a)
a=str(t)
print(a)
c=set(t)
print(c)
c=tuple(t)
print(c)

