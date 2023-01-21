#1+2+3+4+5.......nth

def fact(i):
    if i == 1:  #base case
        return 1
    return i+fact(i-1)

p = fact(5)
print(p)

