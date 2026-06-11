x = int(input("var  "))
y = int(input("var  "))
z = int(input("var  "))
n = int(input("var  "))
newlist = []
for i in range(x+1):
  for j in range(y+1):
    for k in range(z+1):
     if i + j +k > n:
      newlist.append([i,j,k])
print(newlist)