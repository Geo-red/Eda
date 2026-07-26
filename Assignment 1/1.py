name = input("Enter student name: ")

total = 0
for i in range(1,6):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total += marks

average = total/5
percentage = average

print("Student Name:", name)
print("Total:", total)
print("Average:", average)
print("Percentage:", percentage,"%")
