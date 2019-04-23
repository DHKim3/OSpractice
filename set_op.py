#!/usr/bin/python2.7

a=raw_input("Please enter the first list:")
b=raw_input("Please enter the second list:")
union=[]
inter=[]
i_a=[]
i_b=[]

a=a.replace("[","")
a=a.replace("]","")
a=a.replace(" ","")
b=b.replace("[","")
b=b.replace("]","")
b=b.replace(" ","")

a=a.split(',')
b=b.split(',')

for i in range(0,len(a)):
    i_a.append(int(a[i]))
for i in range(0,len(b)):
    i_b.append(int(b[i]))


s_a=set(i_a)
s_b=set(i_b)
s_i=s_a & s_b
s_u=s_a | s_b

union=list(s_u)
inter=list(s_i)
print("Union: ")
print(union)
print("Intersection: ")
print(inter)
