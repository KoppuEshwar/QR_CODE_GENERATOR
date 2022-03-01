import qrcode
from tkinter import *
from tkinter.ttk import *
import os
from PIL import ImageTk,Image

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)


root = Tk()
root.title("QR CODE GENERATOR")
root.geometry("800x300")

new_window = Toplevel(root)
new_window.title("xyz")

canvas = Canvas(new_window, width=500, height=500)
canvas.grid(row=0,column=1)
new_window.destroy()

maindir = os.getcwd()
def show(dir):
    current = os.getcwd()
    os.chdir(dir)
    current2 = os.getcwd()

    global canvas

    with open("names.txt","r") as fobj:
        img_lst = []
        img_names = []
        for line in fobj:
            name = line
            name = name[0:len(line)-1]
            name+=".png"
            img_names.append(name)
            img = ImageTk.PhotoImage(Image.open(name))
            img_lst.append(img)

    new_window = Toplevel(root)
    new_window.title(img_names[0])

    canvas = Canvas(new_window, width=500, height=500)
    canvas.grid(row=0,column=1)
    img = PhotoImage(file=img_names[0])
    canvas.create_image(250, 250, anchor=CENTER, image=img)



    back_b = Button(new_window,text="<<",command=lambda:back(0))
    exit_b = Button(new_window, text="EXIT", command=new_window.destroy)
    next_b = Button(new_window, text=">>",command=lambda:forward(0))

    def back(i_no):
        if os.getcwd() != current2:
            os.chdir(current2)
        global canvas
        new_window.title(img_names[(i_no - 1)%(len(img_names))])
        img = PhotoImage(file=img_names[(i_no-1)%(len(img_names))])
        canvas.create_image(250, 250, anchor=CENTER, image=img)
        back_b = Button(new_window,text="<<",command=lambda:forward((i_no-1)%len(img_names)))
        next_b = Button(new_window, text=">>", command=lambda: forward((i_no + 1) % (len(img_names))))
        back_b.grid(row=1, column=0)
        exit_b.grid(row=1, column=1)
        next_b.grid(row=1, column=2)
        os.chdir(current)
        mainloop()


    def forward(i_no):
        if os.getcwd() != current2:
            os.chdir(current2)
        global canvas
        new_window.title(img_names[(i_no + 1)%(len(img_names))])
        img = PhotoImage(file=img_names[(i_no+1)%(len(img_names))])
        canvas.create_image(250, 250, anchor=CENTER, image=img)
        next_b = Button(new_window,text=">>",command=lambda:forward((i_no+1)%(len(img_names))))
        back_b = Button(new_window,text="<<",command=lambda:forward((i_no-1)%(len(img_names))))
        back_b.grid(row=1, column=0)
        exit_b.grid(row=1, column=1)
        next_b.grid(row=1, column=2)
        os.chdir(current)
        mainloop()

    back_b.grid(row=1,column=0)
    exit_b.grid(row=1,column=1)
    next_b.grid(row=1,column=2)
    os.chdir(current)
    mainloop()




menu = Menu(root)
root.config(menu=menu)
recordings = Menu(menu,tearoff=0)
menu.add_cascade(label='Recordings', menu=recordings)
recordings.add_command(label='Chemistry',command=lambda:show("Chemistry"))
recordings.add_command(label='OOPS',command=lambda:show("OOPS"))
recordings.add_command(label='DSA',command=lambda:show("DSA"))
recordings.add_command(label='DT&T',command=lambda:show("DT&T"))
recordings.add_command(label='WMP',command=lambda:show("WMP"))
recordings.add_command(label='EE',command=lambda:show("EE"))
recordings.add_command(label='Chemistry Lab',command=lambda:show("Chemistry Lab"))
recordings.add_command(label='OOPS Lab',command=lambda:show("OOPS Lab"))
recordings.add_command(label='DSA Lab',command=lambda:show("DSA Lab"))
recordings.add_command(label='DT&T Lab',command=lambda:show("DT&T Lab"))


submissions = Menu(menu,tearoff=0)
menu.add_cascade(label='Submissions', menu=submissions)
submissions.add_command(label='Chemistry')
submissions.add_command(label='OOPS')
submissions.add_command(label='DSA')
submissions.add_command(label='DT&T')
submissions.add_command(label='WMP')
submissions.add_command(label='EE')
submissions.add_command(label='Chemistry Lab')
submissions.add_command(label='OOPS Lab')
submissions.add_command(label='DSA Lab')
submissions.add_command(label='DT&T Lab')

help = Menu(menu,tearoff=0)
menu.add_cascade(label='Help', menu=help)
help.add_command(label='Exit', command=root.destroy)

prompt1 = Label(text="URL : ")
prompt1.place(relx = 0.1, rely = 0.3)

get_url = Entry(root,width=100)
get_url.place(relx = 0.2, rely = 0.3)


prompt2 = Label(text="QR_Name : ")
prompt2.place(relx = 0.1, rely = 0.4)

get_imgname = Entry(root,width=100)
get_imgname.place(relx = 0.2, rely = 0.4)


prompt3 = Label(text="Directory : ")
prompt3.place(relx = 0.1, rely = 0.5)

get_dirname = Entry(root,width=100)
get_dirname.place(relx = 0.2, rely = 0.5)

def disp(dir):
    os.chdir(dir)
    url = get_url.get()
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img_name = get_imgname.get()
    img_name += ".png"
    img.save(img_name)
    qr.clear()

    new_window = Toplevel(root)
    new_window.title(img_name)


    canvas = Canvas(new_window, width=500, height=500)
    canvas.pack()
    img = PhotoImage(file=img_name)
    canvas.create_image(250, 250, anchor=CENTER, image=img)
    os.chdir(maindir)
    mainloop()

create = Button(root,text="Create QR",command=lambda:disp(get_dirname.get()))
create.place(relx = 0.5, rely = 0.6)
if maindir != os.getcwd():
    os.chdir(maindir)
mainloop()
