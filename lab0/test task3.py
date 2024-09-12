import time
t_start = time.perf_counter()
f = open("input.txt")
n = int(f.readline())
f1,f2 = 0,1
for i in range(2,n+1):
    f1,f2=f2, (f1+f2)
k = open("output.txt", "w")
k.write(str(f2%10))
print(f2%10)
print("Время работы: %s секунд" %  (time.perf_counter() - t_start))