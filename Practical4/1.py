# Create List
student = ['Bhanwar Lal Choudhary', 19012011094, 19, 'CE', 'Pass']

# Call all Elements in List
print("Name :  ", student[0], "\nEnrollment Number :  ", student[1], "\nAge : ", student[2],
      "\nBranch : ", student[3], "\nResult : ", student[4])
print(student)

# Insert Element
print("\nInsert Element")
student.insert(3, 'xyz@gmail.com')
print(student)

# Remove Element
print("\nRemove Element")
student.remove('xyz@gmail.com')
print(student)

# Append Element
print("\nAppend Element")
student.append('O+ve')
print(student)

# Extend Element
print("\nExtend Element")
student1 = ['Ankit Choudhary', 19012011141, 20, 'IT', 'Fail']
student.extend(student1)
print(student)

# Update Element
print("\nUpdate Element")
student[2] = 20
print(student)