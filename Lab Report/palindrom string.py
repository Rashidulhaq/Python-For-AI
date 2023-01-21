# palindrom check number MOM
def pal(s):
    if len(s) <=1 :
        return True
    else:
        if s[0] == s[-1]:
            return pal(s[1 : -1])
        else:
            False

p=input("enter your string : ")
if pal(p) == True:
    print("Yes")
else:
    print("NO")