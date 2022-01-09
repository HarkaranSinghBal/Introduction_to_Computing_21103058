#Assignment1:-
#Question1:-
print("Q.1.- Give any three integers: ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d=(a+b+c)/3
print("The average of these integers is ",d)

#Question2:-
print("\nQ.2.- Please give details for evaluating the amount of tax that you will receive: ")
#All taxpayers are charged a flat tax rate of 20%.
#All taxpayers are allowed a $10,000 standard deduction.
#For each dependent, a taxpayer is allowed an additional $3,000 deduction.
a = int(input("Gross income (in dollars): "))
b = int(input("Number of dependants : "))
c = a-10000-(b*3000)
d = c*(20/100)
print("The amount of tax is: ",d)

#Question3:-
print("\nQ.3.- Please enter your details below: ")
SID = int(input("Enter your SID: "))
name = input("Enter your name: ")
gender = input("Enter your gender, Use Gender values ‘F’, ‘M’, ‘U’ (For Unknown): ")
coursename = input("Enter your course name: ")
CGPA = float(input("Enter your CGPA: "))
a = [SID,name,gender,coursename,CGPA]
print('The list of the given details are: ',a)

#Question4:-
print("\nQ.4.- Enter the marks of 5 students below: ")
Student1 = int(input("Student1 = "))
Student2 = int(input("Student2 = "))
Student3 = int(input("Student3 = "))
Student4 = int(input("Student4 = "))
Student5 = int(input("Student5 = "))
a=[Student1,Student2,Student3,Student4,Student5]
a.sort()
print("The marks of the students in sorted manner is: ",a)

#Question5(a):-
color=['Red','Green','White','Black','Pink','Yellow']
print("\nQ.5.(a)- The list of given colors is: ",color)
color.remove('Black')
print("The new list of colors after removing black is: ",color)

#Question5(b):-
color=['Red','Green','White','Black','Pink','Yellow']
print('\nQ.5.(b)-The list of given colors is: ',color)
x = color[:3] + ['Purple'] + color[3+2:]
print('The new list of colors after replacing black and pink with purple is: ',x)
