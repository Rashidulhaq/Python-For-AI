# palindrom check number 575

def pal(n,temp):
    if ( n == 0 ): # base case
        return temp

    temp = (temp * 10 ) + (n % 10)  #store
    return pal(n // 10, temp)

n = 575;
temp = pal(n , 0)


if (temp == n):
    print("yes")
else:
    print("No")