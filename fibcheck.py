import math
print (" HELLO WORLD")
num1=int(input("THE CHECK NUMBER"));
x=((num1*num1)*5)-4
y=((num1*num1)*5)+4

z = int(math.sqrt(x));
a = int(math.sqrt(y));
if z*z == x or a*a == y:
    print ("Its a Fibonacci number :-) ")
else :
    print ("Its not a Fibonacci number :-( ")

#print(x)
#print(y)
#print(a)
#print(z);
