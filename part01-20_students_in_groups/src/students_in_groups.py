# Write your solution here
students_on_course = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))


groups_formed = students_on_course // group_size

if students_on_course > group_size:
    if groups_formed % 2 == 0:
        print(f"Number of groups formed: {groups_formed}")
    elif groups_formed % 2 == 1:
        print(f"Number of groups formed: {groups_formed + 1}")
else: 
    print(f"Error try again")