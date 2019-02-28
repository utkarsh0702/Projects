from tkinter import *
from tkinter.font import Font
import csv
import smtplib
from tkinter import filedialog
from tkinter import simpledialog

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 

def main_page():
    global root
    global e1
    global e2
    root=Tk()
    root.title('Login Panel')
    root.iconbitmap(r'C:\Users\Utkarsh\Desktop\images.ico')
    root.geometry('400x200+120+120')
    root.resizable(0,0)
    f=Font(size=20, family='New Times Roman',weight='bold',slant='italic',underline=1)
    fo= Font(size=13, family='New Times Roman',weight='bold')
    
    l1=Label(root,text='Login Panel',font=f, fg='Purple')
    l1.pack(anchor='center')
    l2=Label(root,text='Username', fg='green',font=fo)
    l2.place(x=25, y=75)
    e1=Entry(root)
    e1.place(x=125, y=75)
    l3=Label(root,text='Password', fg='green',font=fo)
    l3.place(x=25, y=100)
    e2=Entry(root)
    e2.place(x=125, y=100)
    b1=Button(root,text='Log In',relief=GROOVE, command=login)
    b1.place(x=35, y=130)
    b2=Button(root,text='New Account',relief=GROOVE, command= newacc)
    b2.place(x=35, y=160)
    b3=Button(root,text='Delete Account',relief=GROOVE, fg='red', command= dele)
    b3.place(x=300, y=130)
    
    root.mainloop()
    
def dele():
    with open(r'C:\Users\Utkarsh\Desktop\record.txt','r') as file:
        filereader= file.readlines()
        for i in filereader:
            lo= i.split(',')
            if lo[0]==e1.get() and lo[1]==e2.get():
                with open(r'C:\Users\Utkarsh\Desktop\hell.txt','w') as fi:
				    fi.write(lo[0])
					fi.write(',')
					fi.write(lo[1])
					fi.write('\n')

def login():
    global root1
    flag=0
    with open(r'C:\Users\Utkarsh\Desktop\record.txt','r') as file:
        filereader= file.readlines()
        for i in filereader:
            lo= i.split(' ')
            if lo[0]==e1.get() and lo[1]==e2.get():
                flag=1
                
    if flag==1:
        root.destroy()
        root1=Tk()        # creating a new window
        root1.title('Message')
        root1.iconbitmap(r'C:\Users\Utkarsh\Desktop\images.ico')
        root1.geometry('200x200+120+120') 
        root1.resizable(0,0)  # function to stop sizing of the window
        f=Font(size=20, family='New Times Roman',weight='bold',slant='italic',underline=1)
        l1=Label(root1,text='[+]Login Successfull',font=f, fg='Purple')
        l1.pack(anchor='center')
        b1=Button(root1,text='Continue',fg='blue', command= send)
        b1.place(x=80, y=150)
        root1.mainloop()
        
    else:
        l4=Label(root,text='Login Unsuccessfull', fg='red')
        l4.place(x=100, y=130)

# function to send an email
def send():
    global rootA
    global text
    global s1
    global e4
    global e5
    root1.destroy()
    rootA=Tk()
    rootA.title('Email')
    rootA.iconbitmap(r'C:\Users\Utkarsh\Desktop\images.ico')
    rootA.geometry('400x300+120+120') 
    rootA.resizable(0,0)  # function to stop sizing of the window
    f=Font(size=10, family='New Times Roman',weight='bold')
    
    s1=StringVar()
    l1=Label(rootA,text='FROM ', font=f)
    l1.place(x=20, y=25)
    e3=Entry(rootA, width=50, textvariable=s1)
    e3.place(x=70, y=25)
    l1=Label(rootA,text='TO ', font=f)
    l1.place(x=25, y=50)
    e4=Entry(rootA, width=50)
    e4.place(x=70, y=50)
    l1=Label(rootA,text='SUBJECT ', font=f)
    l1.place(x=5, y=75)
    e5=Entry(rootA, width=50)
    e5.place(x=70, y=75)
    text=Text(rootA,width=46, height=10,wrap=WORD)
    text.place(x=15, y=100)
    b1=Button(rootA,text='Send',relief=GROOVE, command= send_email)
    b1.place(x=25, y=270)
    b2=Button(rootA,text='Cancel',relief=GROOVE, command= blew)
    b2.place(x=75, y=270)
    b3=Button(rootA,text=chr(167),relief=GROOVE, command= atta)
    b3.place(x=135, y=270)
    em= simpledialog.askstring('Input String','Please enter your Email Id:')
    pas=simpledialog.askstring('Input String','Please enter your password:',show='*')
    s1.set(em)
    rootA.mainloop() 
    
def atta():
    global msg
    filename= filedialog.askopenfile(initialdir='/',title='Select File',filetypes=(("Text Files",".txt"),("All files",".*")))
    fi= open(filename)
    attachment= MIMEText(fi.read())
    attachment.add_header('Content-Disposition','attachment', filename= filename)
    msg.attach(attachment)
    
def send_email():
    global msg
    content= text.get(1.0, END)
    msg= MIMEMultipart()
    msg['From']=s1.get()
    msg['To']=e4.get()
    msg['Subject']=e5.get()
    msg.attach(MIMEText(content,'plain'))
    
    mail= smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()  
    mail.starttls()  # transport layer security
    mail.login(em, pas)
    tex=msg.as_string()
    try:
        mail.sendmail(s1.get(),e4.get(),tex)
    except: print('Error sending mail.....')
        
    mail.quit()
    

def blew():
    rootA.destroy()
    main_page()
    
# function to create new account
def newacc():
    global root2
    global e8
    global e7
    root.destroy()
    root2=Tk()
    root2.title('New Account')
    root2.iconbitmap(r'C:\Users\Utkarsh\Desktop\images.ico')
    root2.geometry('300x200+120+120') 
    root2.resizable(0,0)  # function to stop sizing of the window
    f=Font(size=20, family='New Times Roman',weight='bold',slant='italic',underline=1)
    fo=Font(size=13, family='New Times Roman',weight='bold')
    
    l1=Label(root2,text='New Account',font=f, fg='Purple')
    l1.pack(anchor='center')
    l2= Label(root2, text='Name', font=fo, fg='green')
    l2.place(x=25, y=60)
    e6= Entry(root2)
    e6.place(x=125, y=60)
    l2= Label(root2, text='Username', font=fo, fg='green')
    l2.place(x=25, y=85)
    e7= Entry(root2)
    e7.place(x=125, y=85)
    l2= Label(root2, text='Password', font=fo, fg='green')
    l2.place(x=25, y=110)
    e8= Entry(root2, show='*')
    e8.place(x=125, y=110)
    b1=Button(root2,text='Sign Up', command=check)
    b1.place(x=80, y=150)
    root2.mainloop()
    
# function to check whether the account exist or not and if it does not exist, add it in csv file
def check():
    global root1
    flag=0
    with open(r'C:\Users\Utkarsh\Desktop\record.txt','r') as file:
        filereader= file.readlines()
        for i in filereader:
            lo= i.split(',')
            if lo[0]==e7.get() and lo[1]==e8.get():
                flag=1
    
    if flag==1:
        with open(r'C:\Users\Utkarsh\Desktop\record.txt','a') as csvfile:
            csvfile.write(e7.get())
            csvfile.write(',')
            csvfile.write(e8.get())
            csvfile.write('\n')
        
        root2.destroy()
        root1=Tk()        # creating a new window
        root1.title('Message')
        root1.iconbitmap(r'C:\Users\Utkarsh\Desktop\images.ico')
        root1.geometry('200x200+120+120') 
        root1.resizable(0,0)  # function to stop sizing of the window
        f=Font(size=10, family='New Times Roman',weight='bold',slant='italic',underline=1)
        l1=Label(root1,text='New Account Successfull',font=f, fg='Purple')
        l1.pack(anchor='center')
        b1=Button(root1,text='Continue',fg='blue', command= send)
        b1.place(x=80, y=150)
        root1.mainloop()
    
    else:
        l4=Label(root2,text='!! Try Different Username !!', fg='red')
        l4.place(x=70, y=180)
        
main_page()