#Assignment4
#Question.1.-
print("Question.1.-")
def transfer(start, end):
    print(start, "→", end)


def hanoi(n, start, end):
    if n == 1:
        transfer(start, end)
    else:
        other = 6 - (start + end)
        hanoi(n - 1, start, other)
        transfer(start, end)
        hanoi(n - 1, other, end)


print("The transfer of 4 disks from 1st rod to 3rd rod is as follow:-")
hanoi(4, 1, 3)
print()


#Question.2.-
print("Question.2.-")
def triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        new_row = [1]
        last_row = triangle(n-1)
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
    return new_row


a = int(input("Enter the number of rows: "))
for h in range(0, a + 1):
    print(triangle(h))
print()


#Question.3.-
print("Question.3.-")
a = int(input("Dividend: "))
b = int(input("Divisor: "))
c, d = divmod(a, b)
lst1 = [a, b, c, d]
dict1 = {a: "dividend", b: "divisor", c: "quotient", d: "remainder"}
print("quotient: ", c, "\nremainder", d, "\n(a) whether callable or not:")
for e in dict1:
    print(dict1[e], ":", callable(e))
print("(b)whether zero or not:")


def zero(x):
    if x == 0:
        print("is zero")
    else:
        print("is non-zero")


print("dividend ", end="")
zero(a)
print("divisor ", end="")
zero(b)
print("quotient ", end="")
zero(c)
print("remainder ", end="")
zero(d)
lst2 = [4, 5, 6]
lst1.extend(lst2)
lst3 = []
for h in lst1:
    if h not in lst3:
        if h > 4:
            lst3.append(h)
print("(c)", lst3)
set1 = set(lst3)
print("(d)", set1)
set2 = frozenset(set1)
print("(e)", set2, "(after making the set immutable)")
print("(f) The max value in the set is", max(set2), "and its hash value is", hash(max(set2)), "\n")



#Question.4.-
print("Question.4.-")


class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        print(self.name, "'s data assigned.")

    def __del__(self):
        print(self.name, "'s data deleted.")


student = Student("Harkaran Singh Bal", 21103058)
print("Name:", student.name, "\nRoll Number:", student.roll_number, ";")
del student
print()


#Question.5.-
print("Question.5.-")


class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee1 = Employees("Mehak", 40000)
employee2 = Employees("Ashok", 50000)
employee3 = Employees("Viren", 60000)
lst = [employee1, employee2, employee3]
print("(a) The list of employees data created is:")
for i in lst:
    print(i.name, "-", i.salary)
employee1.salary = 70000
print("(b) The updated list of employees data created is:")
for i in lst:
    print(i.name, "-", i.salary)
del employee3
lst = [employee1, employee2]
print("(a) The updated list of employees data created is:")
for i in lst:
    print(i.name, "-", i.salary)
print()


#Question.6.-
print("Question.6.-")
from itertools import permutations
import enchant
d = enchant.Dict("en_US")
set_a = set()
q = str(input("Enter the word here: "))
letter = [x.lower() for x in q]
for p in range(3, len(q)+1):
    for y in list(permutations(letter, p)):
        z = "".join(y)
        if d.check(z):
            set_a.add(z)
print("The meaningful words from the given word are: ", set_a)
