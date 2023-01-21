def fibonacci(Number):
    if (Number == 0):
        return 0
    elif Number == 1:
        return 1
    else:
        return fibonacci(Number - 2) + fibonacci(Number - 1)


Number = int(input("Please Enter the Fibonacci Number Range = "))
Sum = 0

for Num in range(Number):
    print(fibonacci(Num), end='  ')
    Sum = Sum + fibonacci(Num)

print("\nThe Sum of Fibonacci Series Numbers = %d" % Sum)