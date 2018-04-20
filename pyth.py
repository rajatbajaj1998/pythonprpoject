from tkinter import *
from tkinter import messagebox

m = Tk()
m.title("Phone Database")
m.configure(background="yellow")

a1=StringVar()
a2=StringVar()
a3=StringVar()
a4=StringVar()
a5=StringVar()
a6=StringVar()
count=0


def add():
    f=open("abc.txt",'a')
    a1=t1.get()
    a2=t2.get()
    a3=t3.get()
    a4=t4.get()
    a5=t5.get()
    if(a1=='' or a2=='' or a3=='' or a4=='' or a5==''):
        print("Invalid Entry")
        exit()
    f.writelines(a1.ljust(10)+a2.ljust(10)+a3.ljust(10)+a4.ljust(10)+a5.ljust(10)+"\n")
    print("Your record has been added")
    f.close()

def srch():
    fname = "abc.txt"

    aid=input("Enter the Name of the Model of the phone you want to search:")
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            if words[0]==aid:
                print(line)

def updt():
    fname = "abc.txt"

    aid=input("Enter the Name of the Model of the phone you want to search: ")
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            if words[0]==aid:
                print(line)
                asd=int(input("Enter the attribute you want to update 0: Name of the model     1: RAM     2: Storage Memory   3: Camera Quality(in pixels)   4: Price in India"))
                twitch = (input("Enter the new value : "))
                words[asd]=twitch
                line1 = ""
                for k in words:
                    line1 += k
                    line1 += "          "

                fname = "abc.txt"
                f2=open("xyz.txt",'w')

                with open(fname, 'r') as f:
                    for line in f:
                        words = line.split()
                        if words[0]!=aid:
                             f2.writelines(line)

                f2.close()

                f2=open("xyz.txt",'a')
                f2.writelines(line1)
                f2.close()


'''def dele():
    # f2=open("abc.txt",'r')
    # ctr=0
    # for line in f2:
    #     ctr=ctr+1
    # print(ctr)
    # f2.seek(0)
    # rl=f2.readlines()
    # l=list(rl)
    # print(l)
    # f2.close()
    # f2=open("abc.txt",'a')
    # i=0
    # aid=input("Enter the Name of the Model of the phone you want to delete:")
    # while(rl!="" and i<ctr):
    #     print(l[i][0])
    #     if(l[i][0]!=aid):
    #         f2.writelines(l[i][0].ljust(20)+l[i][1].ljust(20)+l[i][2].ljust(20)+l[i][3].ljust(20)+l[i][4].ljust(3)+"\n")
    #         print("Record has been deleted")
    #     i=i+1
    # f2.close()

    fname = "abc.txt"
    f2=open("xyz.txt",'w')
    aid=input("Enter the Name of the Model of the phone you want to delete:")
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            if words[0]!=aid:
                 f2.writelines(line)

    f2.close()
'''


def Del() :
    str = input("Enter the Name of the Model of the phone you want to delete:")
    with open("abc.txt",'r+') as f :
        f1=f.readlines()
        f.seek(0)
        for line in f1:
            if str not in line :
                f.write(line)
        f.truncate()
        print("Your record has been deleted")





def firstrecord():
    f3=open("abc.txt",'r')
    line = f3.readline()
    print(line)
    lp=line.split()
    a1.set(lp[0])
    a2.set(lp[1])
    a3.set(lp[2])
    a4.set(lp[3])
    a5.set(lp[4])
    f3.close()

def lastrecord():
    f4=open("abc.txt","r")
    lp=f4.readlines()
    leng=lp[len(lp)-1]
    print(leng)
    l12=leng.split()
    a1.set(l12[0])
    a2.set(l12[1])
    a3.set(l12[2])
    a4.set(l12[3])
    a5.set(l12[4])
    f4.close()


def Exit() :
        Exit = messagebox.askyesno("Quit System", "Do you want to quit?")
        if Exit > 0:
            m.destroy()
            return

def Next():
    global count
    f=open("abc.txt",'r')
    i=0
    while(i<=count):
        l=f.readline()
        i=i+1
    list1=l.split()
    if list1._len_() != 0:
        a1.set(list1[0])
        a2.set(list1[1])
        a3.set(list1[2])
        a4.set(list1[3])
        a5.set(list1[4])
        count = count + 1
    f.close()


def prev():
    global count
    if count!=1:
        f=open("abc.txt",'r')
        i=0
        count = count - 1
        while(i<count):
            l=f.readline()
            i=i+1
        list1=l.split()
        a1.set(list1[0])
        a2.set(list1[1])
        a3.set(list1[2])
        a4.set(list1[3])
        a5.set(list1[4])
        f.close()


l0=Label(m,text="",bg="yellow")
l0.grid(row=1,column=1)

l1=Label(m,text="Name of the model",bg="yellow",fg="blue")
l1.grid(row=2,column=1)

l2=Label(m,text="RAM",bg="yellow",fg="blue")
l2.grid(row=3,column=1)

l3=Label(m,text="Storage Memory",bg="yellow",fg="blue")
l3.grid(row=4,column=1)

l4=Label(m,text="Camera Quality(in pixels)",bg="yellow",fg="blue")
l4.grid(row=5,column=1)

l5=Label(m,text="Price in India",bg="yellow",fg="blue")
l5.grid(row=6,column=1)

l6=Label(m,text="",bg="yellow")
l6.grid(row=7,column=1)

t1=Entry(m,textvariable=a1)
t1.grid(row=2,column=3)
t2=Entry(m,textvariable=a2)
t2.grid(row=3,column=3)
t3=Entry(m,textvariable=a3)
t3.grid(row=4,column=3)
t4=Entry(m,textvariable=a4)
t4.grid(row=5,column=3)
t5=Entry(m,textvariable=a5)
t5.grid(row=6,column=3)

b1=Button(m,text="Save",fg="black",bg="red",width=20,command=add)
b1.grid(row=10,column=1)
b2=Button(m,text="Delete",fg="black",bg="red",width=20,command=Del)
b2.grid(row=10,column=2)
b3=Button(m,text="Search",fg="black",bg="red",width=20,command=srch)
b3.grid(row=10,column=3)
b4=Button(m,text="Update",fg="black",bg="red",width=20,command=updt)
b4.grid(row=10,column=4)

b5=Button(m,text="First record",fg="black",bg="red",width=20,command=firstrecord)
b5.grid(row=9,column=1)
b6=Button(m,text="|<",fg="black",bg="red",width=20,command=prev)
b6.grid(row=9,column=2)
b7=Button(m,text=">|",fg="black",bg="red",width=20,command=Next)
b7.grid(row=9,column=3)
b8=Button(m,text="Last Record",fg="black",bg="red",width=20,command=lastrecord)
b8.grid(row=9,column=4)

b9=Button(m,text="Exit",fg="black",bg="red",width=20,command=Exit)
b9.grid(row=11,column=3)


m.mainloop()
