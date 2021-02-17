import math

number= int(input("enter number: "))
if number > 1:
    for i in range(2,number):
        if number % i == 0:
            print("it is not prime")
            break
    else:
        print(number, " is prime")

else:
    print(number, "not a prime")
