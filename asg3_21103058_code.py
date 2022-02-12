#Assignment_3
#Question.1.-
print("Question.1.-")
a = input("Enter some text(s): ")
x = a.split()
b = []
print()
if len(x) == 1:
    x = a
for d in x:
    # to prevent duplication
    if d not in b:
        b.append(d)
for d in range(0, len(b)):
    print('The frequency of ' + '"' + b[d] + '"' + ' is :', x.count(b[d]))
print("\n")

#Question.2.-
print("Question.2.-")
def condition(a, b, c):
    while True:
        print(a, end=" - ")
        aa = int((input()))
        if b <= aa <= c:
            break
        else:
            print("Wrong date format")
    return aa


#To take and check the input date
while True:
    x = condition("Day", 1, 31)
    y = condition("Month", 1, 12)
    z = condition("Year", 1800, 2025)
    if (y == 4 or y == 6 or y == 9 or y == 11) and x == 31:
        print("Wrong date format")
        continue
    elif (z % 4 == 0 and y == 2) and (x > 29):
        print("Wrong date format")
        continue
    elif (z % 4 != 0 and y == 2) and (x > 28):
        print("Wrong date format")
        continue
    else:
        break
print("The given date is:", x, "-", y, "-", z)
#Conditions to give the next date
if (y == 4 or y == 6 or y == 9 or y == 11) and x == 30:
    x = 1
    y += 1
elif y == 12 and x == 31:
    x, y = 1, 1
    z += 1
elif (y == 2 and z % 4 != 0) and x == 28:
    x, y = 1, 3
elif (y == 2 and z % 4 == 0) and x == 29:
    x, y = 1, 3
else:
    x += 1
print("The next date is", x, "-", y, "-", z)
print("\n")

#Question.3.-
print("Question.3.-")
a = int(input("Enter a value: "))
b = []
c = []
#Asking the user whether to give more input or not
while True:
    ask = input('Do you wish to give more values?(answer "Y" for Yes or "N" for No):\n')
    b.append(a)
    if ask == "Y":
        a = int(input("Enter a value: "))
        continue
    elif ask == "N":
        break
    else:
        print('Please use "Y" for Yes or "N" for No to answer.')

for i in b:
    b1 = i**2
    c.append(b1)
print("The list of the values and their squares is ", list(zip(b, c)))
print("\n")

#Question.4.-
print("Question.4.-")
while True:
    grade = float(input("Enter your grade: "))
    if grade < 4 or grade > 10:
        print("Error. Grade should lie between 4 and 10")
    else:
        break
grade1 = ["D", "C", "C+", "B", "B+", "A", "A+"]
pfm = ["Poor", "Below Average", "Average", "Good", "Very Good", "Excellent", "Outstanding"]
p = (int(grade//1)) - 4
print("Your Grade is '", grade1[p], "' and ", pfm[p], "performance.")
print("\n")

#Question.5.-
print("Question.5.-")
a = "ABCDEFGHIJK"
print("", a, end="")
for i in range(0, len(a), 2):
    print(" "*i, a[:-i])
print("\n")

#Question.6.-
print("Question.6.-")
SID = input("Enter the student's SID: ")
name = input("Enter the student's name: ")
dict1 = {SID: name}
while True:
    dict1[SID] = name
    ask = input("Do you wish to enter more data?(use 'Y' or 'N')?\n")
    if ask == "Y":
        SID = input("Enter the student's SID: ")
        name = input("Enter the student's name: ")
        continue
    elif ask == "N":
        print("(a) The dictionary of the given data is: ", dict1)
        dict2 = {k: v for k, v in sorted(dict1.items(), key=lambda v: v[1])}
        dict3 = {}
        for i in sorted(dict1):
            dict3[i] = dict1[i]
        print("(b) The dictionary with sorted names of the students is: ", dict2)
        print("(c) The dictionary with sorted SID of the students is: ", dict3)
        search = input("(d) Enter the SID of the Student: ")
        print("The name of the student is", dict1.get(search, "Not found"))
        break
    else:
        print("Please use 'Y' for Yes or 'N' for No to answer")
print("\n")

#Question.7.-
print("Question.7.-")
x = int(input("Enter the number of terms upto which you wish to find the fibbonaci sequence: "))
count, a, b = 0, 0, 1
c = a + b
print(a, ",", b, ",", c, end=" , ")
while count < x:
    count += 1
    a, b = b, c
    c = a + b
    print(c, end=" , ")
print()
avg = c / count
print("The average upto", count, "terms is: ", avg)
print("\n")

#Question.8.-
print("Question.8.-")
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
Set_a = Set1 ^ Set2
print("(a) : ", Set_a)
Set_b = Set1 ^ (Set2 | Set3)
print("(b) : ", Set_b)
Set_c = (Set1 & Set2) | (Set2 & Set3) | (Set3 & Set1)
print("(c) : ", Set_c)
Set_d = set()
for i in range(1, 10):
    Set_d.add(i)
Set_d1 = Set_d - Set1
print("(d) : ", Set_d1)
Set_e = Set_d - (Set1 | Set2 | Set3)
print("(e) : ", Set_e)
