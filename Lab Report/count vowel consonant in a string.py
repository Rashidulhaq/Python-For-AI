s = input("enter your string : ")

space = 0
vowel = 0
consonant = 0
l = len(s)

for i in range(0 , l):
    if (s[i] == " "):
        space +=1
    elif(s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u" or s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U" ):
        vowel +=1
    else:
        consonant +=1

print("total space",space)
print("total vowel",vowel)
print("total consonant",consonant)


