a=input()
s=0
for i in a:
    if i.isdecimal():
        s+=int(i)
    else:
        print(i,end="")
print(s)