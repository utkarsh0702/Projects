from tkinter import *
import smtplib
import os
import csv
from tkinter import filedialog

from email.mime.multipart import MIMEMultipart from email.mime.base import MIMEBase 
from email.mime.text import MIMEText 
from email import encoders 

count=0
c=0
creds='/tempfile.temp'

def Log():
    global root
    global e1
    global e2
    #creating a window manager
    root=Tk()
    root.title('Login')
    root.iconbitmap(r'C:\Users\Utkarsh\Desktop\images.ico')
    l1= Label(root, text='Please Login\n')
    l1.grid(sticky=E)
    
    # creating entry place
    l2=Label(root, text='Username ')
    l2.grid(row=1, sticky=E)
    e1=Entry(root)
    e1.grid(row=1,column=1)
    l3=Label(root, text='Password ')
    l3.grid(row=2, sticky=E)
    e2=Entry(root,show='*')
    e2.grid(row=2,column=1)
    
    # button to access accounts
    b1=Button(root,text='Login',relief=GROOVE,command=login)
    b1.grid(columnspan=2,sticky=W)
    b2=Button(root,text='Sign In',relief=GROOVE,command= signIn)
    b2.grid(columnspan=2,sticky=W)
    b3=Button(root,text='Delete User',relief=GROOVE, fg='red',command=deluser)
    b3.grid(columnspan=2,sticky=E)
    
    root.mainloop()

def login():
    global root1
    with open(creds) as f:
        data=csv.reader(f)
        for line in data:
            try:
                uname=line[0]
                passwd=line[1]
                if e1.get()==uname && e2.get()==passwd:
                    root.destroy()
                    root1=Tk()
                    root1.title('Login')
                    root1.iconbitmap(r'C:\Users\Utkarsh\Desktop\images.ico')
                    root1.geometry('150x150+120+120')
                    l4=Label(root1,text='\n [+]Logged In')
                    l4.pack()
                    root1.mainloop()
                    #calling send function to end an email
                    send()
                    
            except IndexError:
                pass
            else:
                root.destroy()
                root1=Tk()
                root1.title('Error!!!')
                root1.iconbitmap(r'C:\Users\Utkarsh\Desktop\images.ico')
                root.geometry('150x150+120+120')
                l5=Label(root1,text='\n[!] Invalid Login')
                l5.pack()
                root1.mainloop()
                # calling the log function
                Log()
                
def send():
    global ro
    root1.destroy()
    ro=Tk()
    ro.title('Send Message')
    ro.iconbitmap(r'')
    ro.geometry('200x100+120+120')
    b4=Button(ro,text='New Message',relief=GROOVE,command=mail)
    b4.pack(row=1,column=0, sticky=N)
    b5=Button(ro,text='New Message',relief=GROOVE,command=logout)
    b5.pack(row=1,column=2, sticky=N)
    ro.mainloop()
    
def mail():
    def attach():
        global count
        count+=1
        file= filedialog.askopenfilename(initialdir='/',title='Select File',filetypes=(('jpeg file','*.jpg'),('All Files','*.*')))
        
    def Pass():
        pass
    
    def Sendmail():
        global count
        global c
        msg= MIMEMultipart()
        # sender's email id
        msg['From']='abc1234@gmail.com' 
        msg['To']= Toe.get()
        msg['Subject']= subject.get()
        body = texte.get("1.0","end-1c")
        msg.attach(MIMEText(body,'plain'))
        if count>0:
            attachment=open(file,'rb')
            part=MIMEBase('application','octet-stream') 
            part.set_payload((attachment).read()) 
            encoders.encode_base64(part) 
            part.add_header('Content-Disposition',"attachment; filename="+file)      
            msg.attach(part)
            
        else: 
            pass
        
        text=msg.as_string()
        mail=smtplib.SMTP('smtp.gmail.com',587)     
        mail.ehlo() 
        mail.starttls() 
        mail.login("abc1234@gmail.com","Abc@123")  
        try: 
            mail.sendmail("abc1234@gmail.com",msg['To'],texte) 
            c+=1  #incrementing the counter c             print('email sent') 
        except:             print ('error sending email') 
        mail.quit()   
        if c >= 1: 
            #if mail was sent successfully the new window is opened and following message is displayed 
            r=Tk()          
            r.title(':D') 
            r.iconbitmap(r'C:\Users\Utkarsh\Desktop\images.ico') 
            r.geometry('150x50')
            l7=Label(r,text='\n[+] Email sent') 
            l7.pack() 
            r.mainloop()
        else:
            r=Tk()          
            r.title(':D') 
            r.iconbitmap(r'C:\Users\Utkarsh\Desktop\images.ico') 
            r.geometry('150x50')
            l7=Label(r,text='\n[!]Error Sending Email') 
            l7.pack() 
            r.mainloop()
            
    root=Tk() 
    root.title('New Message')     
    root.iconbitmap(r'C:\Users\Utkarsh\Desktop\images.ico') 
    To=Label(root,text="To:") 
    Subject=Label(root,text="Subject:")
    text=Label(root,text="Message:") 
    To.grid(row=1,column=0,sticky=W) 
    Subject.grid(row=2,column=0,sticky=W) 
    text.grid(row=3,column=0,sticky=NW) 
    
    Toe=Entry(root,width=67) 
    Subjecte=Entry(root,width=67) 
    texte=Text(root,width=50,height=5)
    Toe.grid(row=1,column=1,sticky=W) 
    Subjecte.grid(row=2,column=1,sticky=W) 
    texte.grid(row=3,column=1,sticky=W) 
    
    attach=Button(root,text="Attach",relief=GROOVE, command=attach) 
    attach.grid(row=6,column=1,sticky=W) 
    send=Button(root,text="Send",relief=GROOVE,command=Sendmail) 
    send.grid(row=6,column=0,sticky=W) 
    file=Label(root,text='') 
    file.grid(row=7,column=0,sticky=W) 
    root.geometry('500x170')     
    root.mainloop()
    
def logout():
    ro.destroy()
    r=Tk() 
    r.title(':D')
    r.iconbitmap(r'C:\Users\Utkarsh\Desktop\images.ico') 
    r.geometry('150x150') 
    l8=Label(r,text='\n[+] Logged Out Successfully.')
    l8.pack() 
    r.mainloop() 
    login() 
    
def Signup():   
    global user
    global paswd 
    global roots 
    rootA.destroy()
    roots=Tk() 
    roots.title("Sign Up")     
    roots.iconbitmap(r'C:\Users\Utkarsh\Desktop\images.ico') 
      
    intruction=Label(roots,text='Please Enter new Credidentials\n')  
    intruction.grid(row=0,column=0,sticky=E)     
    l1=Label(roots,text='New Username: ')  
    l2=Label(roots,text='New Password: ')     
    l1.grid(row=1,column=0,sticky=W) 
    l2.grid(row=2,column=0,sticky=W) 
    user=Entry(roots)   
    paswd=Entry(roots,show='*')
    user.grid(row=1,column=1) 
    paswd.grid(row=2,column=1) 
    signupButton=Button(roots,text='Signup', relief=GROOVE, command=FSSignup)    
    signupButton.grid(columnspan=2,sticky=W) 
    roots.mainloop()
    
def FSSignup(): 
    with open(creds,'a') as f:
        f.write(nameE.get())  
        f.write(',') 
        f.write(pwordE.get()) 
        f.close()    
    roots.destroy() 
    login()
    
def DelUser():
    os.remove(creds)  
    rootA.destroy() 
    Signup()
    
    
if os.path.isfile(creds):
    login() 
    
else: 
    Signup() 
