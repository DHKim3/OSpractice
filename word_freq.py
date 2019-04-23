#!/usr/bin/python2.7

import sys

dic ={}

fname= sys.argv[1]
n=int(sys.argv[2])
with open(fname,"r") as f:
    lines=f.readlines()
    for ln in lines:
        ln=ln.replace("\n","")
        word= ln.split(" ")
        for i in range(0,len(word)):
            if word[i] in dic:
                dic[word[i]]+=1
            else:
                dic[word[i]]=1

sortdic = sorted(dic.items(), key= lambda x: x[1] ,reverse=True)

for i in range(0,n):
    sortdic[i]=str(sortdic[i])
    sortdic[i]=sortdic[i].replace("(","")
    sortdic[i]=sortdic[i].replace(")","")
    sortdic[i]=sortdic[i].replace(",","        ")
    sortdic[i].strip()
    print(sortdic[i])
