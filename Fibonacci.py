#!/usr/bin/python

f1 = 1
f2 = 1
temp =0
f3=1
n = input("INPUT NUMBER OF TIMES?")
n=int(n)

if (n>=3) :
    for i in range(n-2):
        temp=f3
        f1=f2
        f2=temp
        f3=f1+f2
    print("{}".format(f3))
else:
    print("{}".format(f3))
