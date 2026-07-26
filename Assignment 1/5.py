text=input("Enter a string: ")

v=c=d=s=0

for ch in text:
    if ch.lower() in "aeiou":
        v+=1
    elif ch.isalpha():
        c+=1
    elif ch.isdigit():
        d+=1
    else:
        s+=1

print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("Special:",s)
