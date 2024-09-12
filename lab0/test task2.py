import time
t_start = time.perf_counter()
def f(n):
    if (n <= 1):
        return n

    return f(n - 1) + f(n - 2)
k = open("input.txt")
n = int(k.readline())
y = open("output.txt", "w")
y.write(str(f(n)))
print(f(n))
print("Время работы: %s секунд" %  (time.perf_counter() - t_start))