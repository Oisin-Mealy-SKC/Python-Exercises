Name = input("What is your name: ")

mark = int(input("What result did you get you get in ur exam: "))

print (mark)

if mark >= 90:
    print ("H1")
    print (Name,"this is some excellent work")
elif mark >= 80:
    print ("H2")
    print (Name,"this is some good work")
elif mark >= 70:
    print ("H3")
    print (Name,"keep this up")
elif mark >= 60:
    print ("H4")
    print ("Study Harder",Name)
elif mark >= 50:
    print ("H5")
elif mark >= 40:
    print ("H6")
    print ("Work Harder",Name)
elif mark >= 0:
    print ("FAIL")
    