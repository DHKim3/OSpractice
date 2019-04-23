#!/bin/usr/python2.7

ejin = raw_input("INPUT EJIN NUMBER")

m=len(ejin)%4
hex=""
if m != 0 :
    if(m==1):
        ejin="000"+ejin
    elif(m==2):
        ejin="00"+ejin
    else:
        ejin="0"+ejin
n=int(len(ejin)/4)
for i in range(0,n) :
    if (i%4) ==0 :
        hex= " "+hex
    total =0
    temp = ejin[len(ejin)-(4*(i+1)):len(ejin)-(4*i)]

    for i in range(0,len(temp)) :
        temp=int(temp)
        store_mod = temp %10
        total = (store_mod *(2**i))+ total
        temp=int(temp/10)
    
    if total < 10 :
        hex=str(total)+hex
    else:
        if(total==10):
            hex="A"+hex
        elif(total==11):
            hex="B"+hex
        elif(total==12):
            hex="C"+hex
        elif(total==13):
            hex="D"+hex
        elif(total==14):
            hex="E"+hex
        else:
            hex="F"+hex

hex="0"+hex
print(hex)