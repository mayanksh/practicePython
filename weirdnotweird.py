#!/bin/python3

import math
import os
import random
import re
import sys

def m(i):

    #n = int(input("enter any number b/w 1 and 100: "))

    if (1 <= i <= 100):
        if i%2 != 0:
            print("weird")
        elif (2<= i <=5 and i%2 == 0):
            print("not weird")
        elif 6<= i <=20 and i%2 == 0:
            print("weird")
        elif 20<= i <=100 and i%2 == 0:
            print("not weird")
    else:
     print("out of range")



if __name__ == '__main__':

    n = int(input("enter any number b/w 1 and 100: ").strip())
    m(n)
