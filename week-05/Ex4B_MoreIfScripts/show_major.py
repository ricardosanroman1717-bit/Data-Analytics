# Exercise 4.B Lab 5 - Show Student Major

# Starting values
student_name = "Alex Rivera"
student_major = "ENG"

# Determine major and office location
if student_major == "BIOL":
    major_name = "Biology"
    location = "Science Bldg, Room 310"

elif student_major == "CSCI":
    major_name = "Computer Science"
    location = "Sheppard Hall, Room 314"

elif student_major == "ENG":
    major_name = "English"
    location = "Kerr Hall, Room 201"

elif student_major == "HIST":
    major_name = "History"
    location = "Kerr Hall, Room 114"

elif student_major == "MKT":
    major_name = "Marketing"
    location = "Westly Hall, Room 310"

else:
    major_name = "<unknown>"
    location = ""

# Display results
print(f"Student: {student_name}")
print(f"Major: {major_name}")

if location:
    print(f"Office: {location}")