#Assignment5
#Question.1.-
from tkinter import *
root = Tk()
root.geometry('350x150')
root.title("Q.1.- GST Tax Finder")
original_price = IntVar()
net_price = IntVar()


def calculate():
    a = original_price.get()
    b = net_price.get()
    c = ((b-a)*100)/a
    print("The GST rate is", c)
    lbl.config(text="The GST rate is "+str(c))
    return c


lbl = Label(root, text="")
lbl.grid(row=3, column=0, sticky=W)
lb1 = Label(root, text="Enter the original price of the item")
lb1.grid(row=0, column=0, sticky=W)
lb2 = Label(root, text="Enter the net price of the item")
lb2.grid(row=1, column=0, sticky=W)
en1 = Entry(root, textvariable=original_price)
en1.grid(row=0, column=1, sticky=W)
en2 = Entry(root, textvariable=net_price)
en2.grid(row=1, column=1, sticky=W)
button = Button(root, text="Submit", command=calculate)
button.grid(row=2, column=1, sticky=W)
root.mainloop()



#Question.2.-
from tkinter import *
import calendar
win = Tk()
win.geometry("500x600")
win.title("Q.2.- Calender")
year = IntVar()


def fun1():
    c = calendar.calendar(year.get(), 2, 1, 6)
    label.config(text="The calendar is:"+str(c))
    return c


year_entry = Entry(win, textvariable=year)
year_entry.grid(row=0, column=1)
ask_user = Label(win, text="Enter the year here: ")
ask_user.grid(row=0, column=0)
year_button = Button(win, text="see the calendar", command=fun1)
year_button.grid(row=1, column=1)
label = Label(text="")
label.grid(row=2, column=1)
win.mainloop()



#Question.3.-
from tkinter import *
base = Tk()
base.geometry("263x150")
base.configure(background="light blue")
base.title("Q.3.- Basic calculator")
expression = ""


def collect(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def calc():
    try:
        global expression
        answer = str(eval(expression))
        equation.set(answer)
        expression = ""
    except:
        equation.set(" Error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


equation = StringVar()
expression_entry = Entry(base, textvariable=equation)
expression_entry.grid(columnspan=4, ipadx=70)
b7 = Button(base, text=" 7 ", fg="black", bg="light yellow", command=lambda: collect(7), height=1, width=8)
b7.grid(row=1, column=0)
b8 = Button(base, text=" 8 ", fg="black", bg="light yellow", command=lambda: collect(8), height=1, width=8)
b8.grid(row=1, column=1)
b9 = Button(base, text=" 9 ", fg="black", bg="light yellow", command=lambda: collect(9), height=1, width=8)
b9.grid(row=1, column=2)
b4 = Button(base, text=" 4 ", fg="black", bg="light yellow", command=lambda: collect(4), height=1, width=8)
b4.grid(row=2, column=0)
b5 = Button(base, text=" 5 ", fg="black", bg="light yellow", command=lambda: collect(5), height=1, width=8)
b5.grid(row=2, column=1)
b6 = Button(base, text=" 6 ", fg="black", bg="light yellow", command=lambda: collect(6), height=1, width=8)
b6.grid(row=2, column=2)
b1 = Button(base, text=" 1 ", fg="black", bg="light yellow", command=lambda: collect(1), height=1, width=8)
b1.grid(row=3, column=0)
b2 = Button(base, text=" 2 ", fg="black", bg="light yellow", command=lambda: collect(2), height=1, width=8)
b2.grid(row=3, column=1)
b3 = Button(base, text=" 3 ", fg="black", bg="light yellow", command=lambda: collect(3), height=1, width=8)
b3.grid(row=3, column=2)
b0 = Button(base, text=" 0 ", fg="black", bg="light yellow", command=lambda: collect(0), height=1, width=8)
b0.grid(row=4, column=1)
add = Button(base, text=" + ", fg="black", bg="light yellow", command=lambda: collect("+"), height=1, width=8)
add.grid(row=1, column=3)
subtract = Button(base, text=" - ", fg="black", bg="light yellow", command=lambda: collect("-"), height=1, width=8)
subtract.grid(row=2, column=3)
multiply = Button(base, text=" * ", fg="black", bg="light yellow", command=lambda: collect("*"), height=1, width=8)
multiply.grid(row=3, column=3)
divide = Button(base, text=" / ", fg="black", bg="light yellow", command=lambda: collect("/"), height=1, width=8)
divide.grid(row=4, column=3)
decimal = Button(base, text=" . ", fg="black", bg="light yellow", command=lambda: collect("."), height=1, width=8)
decimal.grid(row=4, column=0)
equal = Button(base, text=" = ", fg="black", bg="light yellow", command=calc, height=1, width=8)
equal.grid(row=4, column=2)
clear_all = Button(base, text=" C ", fg="black", bg="light yellow", command=clear, height=1, width=8)
clear_all.grid(row=5, column=0)
base.mainloop()



#Question.4.-
lst = input("Q.4.- Enter the list of marks of students(format example- 1, 2, 3): ")
lst = lst.split(", ")
lst1 = []


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(arr, compare=lambda x, y: x < y):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle], compare)
        right = merge_sort(arr[middle:], compare)
        return merge(left, right, compare)


print("The sorted list of marks of students is: ", merge_sort(lst))



#Question.5.-
#(a)
def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(arr, compare=lambda x, y: x < y):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle], compare)
        right = merge_sort(arr[middle:], compare)
        return merge(left, right, compare)


inp = input("Q.5.- (a) Enter the list to be sorted: ")
inp = inp.split(", ")
q = merge_sort(inp)
print("The sorted list is(using merge_sort function from Q4)): ", merge_sort(inp))


#(b)
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if int(arr[mid]) < x:
            low = mid + 1
        elif int(arr[mid]) > x:
            high = mid - 1
        else:
            return mid
    return -1


g = int(input("(b) Enter the number you wish to search in the sorted list: "))
z = binary_search(q, g)
if z != -1:
    print("Element is present at index", str(z))
else:
    print("Error, element is not present in array")

#(c)
count = 0
for w in inp:
    if int(w) == g:
        count = count + 1
print("(c) The number of occurrences of the searched number is:", count)
