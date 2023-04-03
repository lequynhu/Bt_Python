string=input()
n=int(input())
m=[]
for i in range(n):
  m.append(input().lower())
for i in range(n):
  print(string.lower().count(m[i]))