import random
a=random.randint(0,50)
if a%2==0:
    print(a,"is an even number")
else:
    print(a,"is an odd number")
if a>=0:
    print(a,"is a positive number")
else:
    print(a,"is a negative number")
if a>1:
    for i in range(2,a):
        if a%i==0:   
            print(a,"is composite number")
            break
        else:
            print(a,"is prime number")
            break
elif a==0 or 1:
    print(a,"is not a prime number")