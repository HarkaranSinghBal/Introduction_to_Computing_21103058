#Assignment2
#Question.1.-
print("Q.1.- Python is a case sensitive language.")
data = "Python is a case sensitive language."
print("(a) The length of input data is ",len(data),"\n")

data1 = data[::-1]
print("(b) The string in reverse order is: ",data1,"\n")

a = slice(10,26)
print('(c) substring stored using the slice function is ','"'+data[a]+'"',"\n")

data3 = data[:9] + " object oriented " + data[27:]
print("(d) The new string after we replace “a case sensitive” with “object oriented” is: ",data3,"\n")

x = data.find("a")
print("(e) The index of substring \"a\" int the given string is ",x,"\n")

data4 = data.replace(" ","")
print("(f) The new string with no white spaces is: ",data4, "\n")

#Question.2.-
print("Q.2.- Enter your details below:\n")
name = input("Name: ")
SID = input("SID: 2110")
dpt_name = input("Department name: ")
cgpa = (input("CGPA: "))
print("Hey, " + name + " here!\nMy SID is 2110" + SID + "\nI am from " + dpt_name + " department and my CGPA is " + cgpa + "\n")

#Question.3.-
print("Q.3.- Given a = 56 and b = 10, the operations applied are as follows:")
a, b = 56, 10
print("(a) a&b =", a & b)
print("(b) a|b =", a | b)
print("(c) a^b =", a ^ b)
print("(d) Left shift both a and b with 2 bits =", a << 2, ",", b << 2)
print("(e) Right shift a with 2 bits and b with 4 bits =", a >> 2, ",", b >> 2,  "and", a >> 4, ",", b >> 4, "\n")

#Question.4.-
print("Q.4.- Give any three numbers below:")
a = input("1st number = ")
b = input("2nd number = ")
c = input("3rd number = ")
print("The greatest number of the given three numbers is:")
if a>b and a>c:
    print(a,"\n")
elif b>a and b>c:
    print(b,"\n")
else:
    print(c,"\n")

#Question.5.-
print("Q.5.- 'My name is Harkaran Singh Bal.' Is the word 'name' present in string?\n")
x = "My name is Harkaran Singh Bal."
y = x.find("name")
if y == -1:
    print("No\n")
else:
    print("Yes\n")

#Question.6.-
print("Q.6.- Give any 3 numbers below to check whether a triangle can be formed with these numbers:")
a = float(input("1st number: "))
b = float(input("2nd number: "))
c = float(input("3rd number: "))
print("Is a triangle possible?")
if a<b+c or b<a+c or c<a+b:
    print("Yes")
else:
    print("No")
