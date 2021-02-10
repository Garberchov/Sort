from tkinter import *

root = Tk()
root.title("Number Sorter")
root.geometry('200x200')
list = []

e = Entry(root, width=100)
e.pack()

f = Entry(root, width=100)
f.pack()

g = Entry(root, width=100)
g.pack()

h = Entry(root, width=100)
h.pack()

j = Entry(root, width=100)
j.pack()

def myClick():
    list.append(int(e.get()))
    list.append(int(f.get()))
    list.append(int(g.get()))
    list.append(int(h.get()))
    list.append(int(j.get()))
    sorted_list = quick_sort(list)
    print(list)
    label2 = Label(root, text="And Your Sorted Lsit Is:")
    myLabel = Label(root, text=sorted_list)
    label2.pack()
    myLabel.pack()


def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        
        else:
            items_lower.append(item)
    
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)





myButton = Button(root, text="Enter Your Numbers", command=myClick)
myButton.pack()

root.mainloop()