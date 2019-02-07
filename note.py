from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
from tkinter import colorchooser
from tkinter import messagebox

#creating a root window
root=Tk()
root.title('Notepad')
root.geometry('900x500+60+60')


# adding a scroll bar
scroll= Scrollbar(root)
bar=Scrollbar(root, orient= HORIZONTAL)

# font style
fo= Font(size=10,family='Times New Roman')

# text plane
tex=Text(root,wrap= NONE, yscrollcommand= scroll.set, xscrollcommand= bar.set, undo=True, font= fo)
scroll.config(command= tex.yview)
scroll.pack(side=RIGHT, fill=Y)
bar.config(command= tex.xview)
tex.pack(fill=BOTH, expand=1)
bar.pack(side=BOTTOM, fill=X)
# creating a main menu
main_=Menu(root, tearoff=FALSE)
root.config(menu= main_)
# creating sub menues
file= Menu(main_,tearoff=FALSE)
edit= Menu(main_,tearoff=FALSE)
form= Menu(main_,tearoff=FALSE)
helps= Menu(main_,tearoff=FALSE)

main_.add_cascade(label='File',menu= file)
main_.add_cascade(label='Edit',menu= edit)
main_.add_cascade(label='Format',menu= form)
main_.add_cascade(label='Help',menu= helps)



# functions for sub menus
        
def opens(event=''):
    result= filedialog.askopenfile(initialdir='/',title='Open', filetypes=(('Text Files','.txt'),('All Files','.*')))
    if (result !=None):
        tex.delete(1.0,END)
        for i in result:
            tex.insert(END,i)
        
def save(event=''):
    f=filedialog.asksaveasfile(mode=W, defaultextension='.txt')
    if f is None:
        return
    
def new(event=""):
    ans=messagebox.askyesnocancel('Exit','Do you want to save the content?')
    if(ans=='False'):
        tex.delete(1.0, END)
    
    else:
        filedialog.asksaveasfile(mode=W, defaultextension='.txt')
        tex.delete(1.0, END)

def copy(event=''):
    tex.clipboard_clear()
    tex.clipboard_append(tex.selection_get())
    
def cut(event=''):
    copy()
    tex.delete('sel.first','sel.last')
    
def paste(event=''):
    tex.insert(INSERT, tex.clipboard_get())
    
def color_ch():
    clr= colorchooser.askcolor(title='Colour')
    tex.configure(background= clr[1])
    
def save_as():
    save()
    
def intro():
    top= Toplevel()
    top.title('About Notepad')
    top.geometry('400x300+200+200')
    l1= Label(top,text='About Notepad')
    l1.place(x=150,y=50)
    l2=Label(top,text='This Notepad is made by Utkarsh Mishra.....')
    l2.place(x=80,y=100)
    b1= Button(top,text='Close', command= top.destroy)
    b1.place(x=180,y=150)
    
    
# binding the shortcut keys with the root window
root.bind('<Control-n>',new)
root.bind('<Control-o>',opens)
root.bind('<Control-s>',save)
root.bind('<Control-x>',cut)
root.bind('<Control-c>',copy)
root.bind('<Control-v>',paste)

#creating menus of file 
file.add_cascade(label='New      Ctrl+N', command=new)
file.add_cascade(label='Open     Ctrl+O',command=opens)
file.add_separator()
file.add_cascade(label='Save     Ctrl+S',command=save)
file.add_cascade(label='Save as...',command= save_as)
file.add_separator()
file.add_cascade(label='Exit',command= root.quit)

# creating menus of edit
edit.add_cascade(label='Undo',command=tex.edit_undo)
edit.add_cascade(label='Redo',command=tex.edit_redo)
edit.add_separator()
edit.add_cascade(label='Cut       Ctrl+X',command=cut)
edit.add_cascade(label='Copy      Ctrl+C',command=copy)
edit.add_cascade(label='Paste     Ctrl+V',command=paste)

#creating menus of form
form.add_cascade(label='Colour Chooser',command= color_ch)

# creating menu of help
helps.add_cascade(label='About Notepad', command= intro)


root.mainloop()