# sum of even number in a range, and must be use two function,
# suppose 1-10 even number sum =30
# 

def num():
    num1 = int(input("enter 1st number :"))
    num2 = int(input("enter 2nd number :"))
    return num1, num2


def result(num1, num2):
    sum = 0
    for i in range(num1, num2+1):
        if i % 2 == 0:
            sum += i
    return sum
num1,num2 =num()
print(result(num1,num2))