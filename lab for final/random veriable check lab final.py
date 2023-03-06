import random


def fx(x):
#fx(x) = int(input("rr"))
    return (x * x) - (5 * x) + 6


result = None
count = 0

while result != 0:
    # Generate a random number between -10 and 10
    num = random.randint(-10, 10)
    print("Generated number:", num)

    # Calculate the result of f(x)
    result = fx(num)
    print("f(x) result:", result)

    count += 1

print("Zero was generated after", count, "iterations.")
