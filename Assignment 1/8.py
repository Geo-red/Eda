file=open("data.txt","w")

for i in range(5):
    file.write(input("Enter line: ")+"\n")
file.close()

file=open("data.txt","r")
content=file.readlines()

lines=len(content)
words=0
chars=0

for line in content:
    words+=len(line.split())
    chars+=len(line)

file.close()

print(lines)
print(words)
print(chars)
