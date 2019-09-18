# while(1):
#     try:
#         num1=raw_input('chushu ')
#         num2=raw_input('beichushu')
#         result=int(num2)/int(num1)
#     except BaseException:
#         print('error')
#     else:
#         print('nomal')
# def sayhello(par):
#     print('hello, ',par)
#     return
# sayhello(5)
from Tkinter import *
root=Tk()
root.geometry('500x400')
root.title("hejiaman is a pig")

# buttn=Button(root,text="touch me!")
# buttn.pack()

#lable.config(text="hejiaman is a pig")
lable=Label(root)
lable.pack()
lable.config(text="hejiaman is clever")
textvar=StringVar()
entry=Entry(root,textvariable=textvar)
entry.pack()
text = Text(root)


listbox=Listbox(root,height=15)
listbox.pack()

def read():
    listbox.delete(0,END)
    import os
    dir=os.getcwd()
    list=os.listdir(dir)
    lable.config(text="read mode")
    if len(list)==0:
        lable.config(text="read mode \n"+" diary is emplty")
    for item in list:
        listbox.insert(0,item)
    listbox.bind('<Double-Button-1>',showDirary)
    entry.pack_forget()
    text.pack_forget()
    listbox.pack()
def showDirary(event):
    title=listbox.get(listbox.curselection())
    realtitle=title[:-5]
    textvar.set(realtitle)
    fileojb=open(title,'r+')
    content=fileojb.read()
    text.delete("0.0","end")
    text.insert("end",content)
    fileojb.close()
    listbox.pack_forget()
    entry.pack()
    text.pack()



def write():
    textvar.set("")
    text.delete("0.0","end")
    lable.config(text="write mode")
    listbox.pack_forget()
    entry.pack()
    text.pack()
    return

def save():
    titled=textvar.get()+".text"
    content=text.get("0.0","end")
    import os
    dir = os.getcwd()
    list = os.listdir(dir)


    if titled!=".text":
        titled=titled[0:-5]
        for item in list:
            if titled == item:
                titled = titled + "1"
                
        titled=titled+".text"

        fileojb=open(titled,'wb')
        fileojb.write(content)
        fileojb.close()
        lable.config(text="saved ready")
    else:
         lable.config(text="please add the title")



quitbuttn=Button(root,text="quit me ")
quitbuttn.pack(side=RIGHT,anchor='se')
readbutton=Button(root,text="read me!",command=read)
readbutton.pack(side=BOTTOM)
writebutton=Button(root,text="write me!",command=write)
writebutton.pack(side=BOTTOM)
savebuttn=Button(root,text="save me",command=save)
savebuttn.pack(side=LEFT, anchor='sw')



# list=["hejiaman", "hejiajun","fankeyi"]
# for people in list:
#     listbox.insert(0,people)
#
# text.pack()
# lable=Label(root)
# lable.pack()

def intdiary():
    import os
    dir=os.getcwd()
    list=os.listdir(dir)
    havediary=False
    for item in list:
        if item=="diary":
            havediary=True
    if havediary==False:
        os.mkdir("diary")
    os.chdir("./diary")
    return
intdiary()



root=mainloop()