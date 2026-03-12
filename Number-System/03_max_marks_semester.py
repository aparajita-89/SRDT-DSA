n = int(input("Enter no of semester: "))

subjects = []

for i in range(n):
    s = int(input("Enter no of subjects in " + str(i+1) + " semester: "))
    subjects.append(s)

for i in range(n):

    marks = list(map(int, input("Marks obtained in semester " + str(i+1) + ": ").split()))

    if len(marks) != subjects[i]:
        print("You entered wrong number of marks.")
        exit()

    max_mark = marks[0]

    for m in marks:
        if m < 0 or m > 100:
            print("You have entered invalid mark.")
            exit()

        if m > max_mark:
            max_mark = m

    print("Maximum mark in", i+1, "semester:", max_mark)