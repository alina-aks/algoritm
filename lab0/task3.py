f = open("input.txt")
n = int(f.readline())
f1,f2 = 0,1
for i in range(2,n+1):
    f1,f2=f2, (f1+f2)%10
k = open("output.txt", "w")
k.write(str(f2))
print(f2)
