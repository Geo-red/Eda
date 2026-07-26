students={}
n=int(input("Enter number of students: "))

for i in range(n):
    name=input("Enter name: ")
    marks=int(input("Enter marks: "))
    students[name]=marks

highest=-1
topper=""

for name in students:
    if students[name]>highest:
        highest=students[name]
        topper=name

print(topper, highest)
