#123

reverse_num = 0
def reverse_num_Int(nm):
    global reverse_num   # user for reverse number because reverse_num define out of fuction
    if(nm > 0):
        Reminder = nm %10
        reverse_num = (reverse_num *10) + Reminder
        reverse_num_Int(nm //10)
    return reverse_num

nm = int(input("Please Enter any Value : "))
reverse_num = reverse_num_Int(nm)
print("reverse = %d" %reverse_num)