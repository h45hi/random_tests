from tkinter import *

root = Tk()

""" buttons """
# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)

# button1 = Button(topFrame, text="Button 1", fg="red")
# button2 = Button(topFrame, text="Button 2", fg="blue")
# button3 = Button(topFrame, text="Button 3", fg="green")
# button4 = Button(bottomFrame, text="Button 4", fg="purple")

# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)

"""responsive labels"""
# one = Label(root, text="one", bg="red", fg="white")
# one.pack()
# two = Label(root, text="two", bg="red", fg="white")
# two.pack(fill=X)
# three = Label(root, text="three", bg="red", fg="white")
# three.pack(side= LEFT, fill=Y)

""" grids """
# label1 = Label(root,text='Name')
# label2 = Label(root,text='Password')
# entry1 = Entry(root)
# entry2 = Entry(root)
#  sticky =North/East/West/South
# label1.grid(row=0,sticky=E)
# label2.grid(row=1,sticky=E)
# entry1.grid(row=0,column=1)
# entry2.grid(row=1,column=1)

# c= Checkbutton(root, text="Keep me logged in")
# c.grid(columnspan=2)

"""bind button to function and print op to console"""
# def printName(event):
#     print("Nisit")
# button1 = Button(root, text = 'Print Name', command = printName)
# button1.pack()
# button1 = Button(root, text = 'Print Name')
# button1.bind('<Button-1>', printName)
# button1.pack()

"""one widget multiple events"""
# def leftClick(event):
#     print('left')

# def middleClick(event):
#     print('middle')

# def rightClick(event):
#     print('right')

# frame = Frame(root, height=200, width= 350)
# frame.bind('<Button-1>', leftClick)
# frame.bind('<Button-2>', middleClick)
# frame.bind('<Button-3>', rightClick)

# frame.pack()

"""class based approach"""
# class nisitButtons:
#     def __init__(self,master):
#         frame = Frame(master,height = 200, width = 350)
#         frame.pack()

#         self.button = Button(frame, text = "Print Message", command = self.printMessage)
#         self.button.pack(side = LEFT)

#         self.button1 = Button(frame, text = "Quit", command = frame.quit)
#         self.button1.pack(side = LEFT)

#     def printMessage(self):
#         print("wow ! It worked !!!")

# n = nisitButtons(root)

def doNewProj():
    print("New Project Clicked")

def doNewFile():
    print("New File Clicked")

def quitProg():
    print("Quit Clicked")

def doCut():
    print("Cut Clicked")

menu = Menu(root)
root.config(menu = menu)

fileMenu = Menu(menu)
menu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label= "New Project", command = doNewProj)
fileMenu.add_command(label= "New File", command = doNewFile)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = quitProg)

editMenu = Menu(menu)
menu.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Cut", command = doCut)

root.mainloop()
