from tkinter import *
import smtplib
#Main Screen
master = Tk()
master.title("Custom Python Email App")
master.geometry("300x350")


#functions
def send():
    try:

        username=temp_username.get()
        password=temp_password.get()
        to=temp_receiver.get()
        subject=temp_subject.get()
        body=temp_body.get()

        if username=="" or password=="" or to=="" or subject=="" or body=="":
            notif.config(text="All fields required!",fg="red")
            return
        else:
            finalMessage='Subject: {}\n\n{}'.format(subject,body)
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(username,password)
            server.sendmail(username,to,finalMessage)
            notif.config(text="Email has been sent",fg='green')
    except:
        notif.config(text="Error sending the message",fg="red")



def reset():
    usernameEntry.delete(0,'end')
    passwordEntry.delete(0,'end')
    receiverEntry.delete(0,'end')
    subjectEntry.delete(0,'end')
    bodyEntry.delete(0,'end')

#Graphics
Label (master, text="Customized Email App", font=('Calibri',15)).place(x=50,y=10)
Label (master, text="Use the form below to send an email", font=('Calibri',11)).place(x=30,y=45)

Label (master, text="Email", font=('Calibri',11)).place (x=40,y=100)
Label (master, text="Password", font=('Calibri',11)).place (x=40,y=140)
Label (master, text="To", font=('Calibri',11)).place (x=40,y=180)
Label (master, text="Subject", font=('Calibri',11)) .place(x=40,y=220)
Label (master, text="Body", font=('Calibri',11)) .place (x=40,y=260)
notif = Label (master, text="", font=("Calibri",11))
notif.grid(row=7,sticky=S,padx=5)


#Storage
temp_username = StringVar()
temp_password = StringVar()
temp_receiver =StringVar ()
temp_subject = StringVar ()
temp_body = StringVar ()



#Entries
usernameEntry =Entry (master, textvariable=temp_username)
usernameEntry.place(x=120,y=100)
passwordEntry=Entry(master,show="*", textvariable=temp_password)
passwordEntry.place(x=120,y=140)
receiverEntry=Entry(master, textvariable=temp_receiver)
receiverEntry.place(x=120,y=180)
subjectEntry=Entry(master,textvariable=temp_subject)
subjectEntry.place(x=120,y=220)
bodyEntry=Entry(master,textvariable=temp_body)
bodyEntry.place(x=120,y=260) 

#buttons
Button(master,text="Send",command=send).place(x=40,y=300)
Button(master,text="Reset",command=reset).place(x=80,y=300)




master.mainloop()
