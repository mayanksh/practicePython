#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# Complete the time_delta function below.
def time_delta(t1, t2):
    now= datetime.now()



    #for i in range(int(input())):
    t1 = datetime.strftime(input(), '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strftime(input(), '%a %d %b %Y %H:%M:%S %z')
    print(now.strftime("%c"))
    print(now.strftime("%x"))
    print(now.strftime("%X"))
    print(abs(int((t1-t2).total_seconds())))




    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        t = int(input())

        for t_itr in range(t):
            t1 = input()



            t2 = input()



            delta = time_delta(t1, t2)

            fptr.write(delta + '\n')

        fptr.close()
