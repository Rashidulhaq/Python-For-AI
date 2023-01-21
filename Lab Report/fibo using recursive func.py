# 0 1 1 2 3 5 8 13 fibonacci
def recur_fibo(n):
    if n<= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))

n = 8
if n >= 0:
    print("fibonacci sequence : ")
    for i in range(n):
        print(recur_fibo(i))