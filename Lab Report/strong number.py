def strong_number(number):
    number_str = str(number)


    factorial_sum = 0

    for i in number_str:
        i  = int(i)
        factorial = 1


        for j in range( 1, i+1):
            factorial *= j

        factorial_sum += factorial

    return factorial_sum == number

print(f"strong number is {strong_number(145)}")