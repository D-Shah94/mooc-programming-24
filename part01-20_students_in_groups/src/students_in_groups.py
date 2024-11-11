# Write your solution here
students_enrolled = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

if (students_enrolled % group_size != 0):
    print(f"Number of groups formed: {(students_enrolled // group_size) + 1}")
else:
    print(f"Number of groups formed: {(students_enrolled // group_size)}")

'''Alternative approach
students = int(input("How many students on the course? "))

group_size = int(input("Desired group size? "))

 

groups = (students + group_size - 1) // group_size

 

print("Number of groups formed:", groups)

'''