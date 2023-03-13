from tkinter import *
from PIL import *
from PIL import Image, ImageTk
from pymysql import *
from tkinter import messagebox
from tkcalendar import *

root = Tk()
root.geometry("1000x1000")

root.configure(bg = "light gray")
root.wm_iconbitmap(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\chrome.ico")
root.title("Google Interface")

bg = PhotoImage(file = r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\backg.png")

canvas = Canvas(root, width = 1000, height = 1000, highlightthickness = 0)
canvas.pack(fill = "both", expand = True)
canvas.create_image(0,0, image = bg, anchor = "nw")
art = (Image.open(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\artt.png"))
resized_art = art.resize((430,190), Image.ANTIALIAS)
new_art = ImageTk.PhotoImage(resized_art)
canvas.create_image(590,50,anchor = NW,image = new_art)

def chat():
    t = Toplevel(root)
    t.title("Chat Bot")
    t.geometry("500x500")
    t.resizable(0,0)
    t.wm_iconbitmap(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\chatbot.ico")
    t.config(bg="light gray")
    chat = Label(t,text="CHAT BOT", fg= "Black", font=("Times New Roman",20))
    chat.pack()
    window = Text(t,bg = "black",height = 15, width = 100,fg='white',font=("Arial",15),wrap='word')
    window.place(x=1,y=40,height=400, width = 499)
    mwindow = Entry(t,bg = "white",font=("Arial",20),fg="black")
    mwindow.place(x=110,y=441,height=55, width = 398)
    
    def reply():
        ques = mwindow.get()
        window.insert(END,"\nYou: " + ques)
        mwindow.delete(0,END)
        if ques=="hello":
            window.insert(END,"\n" + "Bot: Hi, How can I help you?")
        elif ques=="who are you?":
            window.insert(END,"\n" + "Bot: I'm a chatbot and I'm here to serve you :)")
        elif ques=="tell me about this project":
            window.insert(END,"\n" + "Bot: This project represents a google interface. \nAfter logging in it will direct you to some of the google apps. \nThese apps are quite interesting and you definitely need to try them! \nIf you dont have an account you can also create a new account by registering.")
        elif ques=="bye":
            window.insert(END,"\n" + "Bot: Goodbye! Make sure to visit again!")
        else:
            window.insert(END,"\n" + "Bot: Sorry, I didn't quite get that?")
    
    but = Button(t,text="SEND",command=reply,font=("Times new roman",15),bg="light blue", activebackground = "red", width=10, height = 5)
    but.place(x=5,y=441,height = 57, width=100)

def login():
    log = Toplevel(root)
    log.title("Login Page")
    log.geometry("700x600")
    log.resizable(0,0)
    log.wm_iconbitmap(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\login.ico")
    log.config(bg="light blue")
    l = Label(log,text="LOGIN TO YOUR ACCOUNT HERE!",fg="Dark Blue", bg = "light Blue",font=("8514oem",30))
    l.place(x=70,y=30)
    l1 = Label(log,text="Username:-",fg = "black", bg = "white", font = ("Times New Roman",20,"bold"))
    l1.place(x = 80, y = 150)
    l2 = Label(log,text="Password:-",fg = "black", bg = "white", font = ("Times New Roman",20,"bold"))
    l2.place(x = 80, y = 260)
    l3 = Label(log,text="Captcha:-",fg = "black", bg = "white", font = ("Times New Roman",20,"bold"))
    l3.place(x = 80, y = 370)
    
    e1 = Entry(log, font=("Times New Roman",20),bg = "light gray")
    e1.place(x = 280, y = 150)
    e2 = Entry(log, font=("Times New Roman",20),bg = "light gray")
    e2.place(x = 280, y = 260)
    e3 = Entry(log, font=("Times New Roman",20),bg = "light gray")
    e3.place(x = 280, y = 410)
    
    import random
    cap = random.randint(1000,9999)
    l_cap = Label(log,text=cap,font=("Comic Sans MS",25,"bold"),bg="light blue",fg="Dark Blue")
    l_cap.place(x=370,y=358)

    def submit_log():
        if e1.get()=="shrutisakpal" and e2.get()=="abc@123" and int(e3.get())==cap:
            connection = connect(host = "localhost",user="root",password="Shruti@24",database="login")                       
            c = connection.cursor()                                                                                         
            c.execute("insert into login_db values ('{}','{}');".format(e1.get(),e2.get()))                                    
            c.execute("select * from login_db")
##            for data in c:                                                                                                  
##                print(data)
            connection.commit()
            connection.close()
            print("Database connected!")
            messagebox.showinfo("LOG IN","Logged In Successfully!")

            home = Toplevel(root)
            home.title("Application Page")
            home.geometry("1000x1000")
            home.config(bg = "light gray")
            home.wm_iconbitmap(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\apps.ico")
            label = Label(home,text="Google Apps",font = ("Segoe UI Black",95),fg="Dark Blue",bg="light gray")
            label.place(x=350,y=25)
                        
            def translate():
                from tkinter import ttk, messagebox
                import googletrans
                from googletrans import Translator

                trans = Toplevel(home)
                trans.title("Google Translator")
                trans.geometry("1080x400")
                trans.resizable(0,0)
                trans.configure(bg="white")
                trans.wm_iconbitmap(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\translate.ico")

                arrow = (Image.open(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\arrow.png"))
                resized_arrow = arrow.resize((100,100), Image.ANTIALIAS)
                new_arrow = ImageTk.PhotoImage(resized_arrow)
                arrow_l = Label(trans, image = new_arrow)
                arrow_l.photo = new_arrow
                arrow_l.place(x=485,y=50)
                
                def label_change():
                    c1 = combo1.get()
                    c2 = combo2.get()

                    c1_l.configure(text=c1)
                    c2_l.configure(text=c2)
                    trans.after(1000, label_change)

                def translate_now():
                    text = text1.get(1.0,END)
                    t1 = Translator()
                    trans_text = t1.translate(text, src = combo1.get(), dest = combo2.get())
                    trans_text = trans_text.text
                    text2.delete(1.0, END)
                    text2.insert(END, trans_text)

                languages = googletrans.LANGUAGES
                languageV = list(languages.values())

                combo1 = ttk.Combobox(trans, values=languageV, font=("Arial",15), state = 'r')
                combo1.place(x=100,y=20)
                combo1.set('ENGLISH')

                c1_l = Label(trans,text="ENGLISH",font=("Arial",30,"bold"),bg="white",width=18,bd=5,relief = GROOVE)
                c1_l.place(x=10,y=50)

                f1 = Frame(trans,bg="Black",bd=5)
                f1.place(x=10,y=118,width=440,height=210)

                text1 = Text(f1, font=("Arial",20), bg="white", relief=GROOVE, wrap=WORD)
                text1.place(x=0,y=0,width=430,height=200)

                combo2 = ttk.Combobox(trans, values=languageV, font=("Arial",15), state = 'r')
                combo2.place(x=730,y=20)
                combo2.set('SELECT LANGUAGE')

                c2_l = Label(trans,text="ENGLISH",font=("Arial",30,"bold"),bg="white",width=18,bd=5,relief = GROOVE)
                c2_l.place(x=620,y=50)

                f2 = Frame(trans,bg="Black",bd=5)
                f2.place(x=620,y=118,width=440,height=210)

                text2 = Text(f2, font=("Arial",20), bg="white", relief=GROOVE, wrap=WORD)
                text2.place(x=0,y=0,width=430,height=200)

                trans_button = Button(trans,text="TRANSLATE", font=("Arial",15,"bold","italic"),cursor = "hand2", bg="red",fg="white",command=translate_now)
                trans_button.place(x=465,y=250)

                label_change()
                        
            def gmaiil():
                import smtplib
                gmail = Toplevel(home)
                gmail.title("Gmail")
                gmail.geometry("600x600")
                gmail.resizable(0,0)
                gmail.configure(bg="white")
                gmail.wm_iconbitmap(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\gmail.ico")

                main_l = Label(gmail,text="GMAIL",font=("Times New Roman",40,"bold","underline"),fg="dark red",bg="white")
                main_l.place(x=220,y=20)
                eid = Label(gmail,text="Email ID",font=("Times New Roman",20),fg="black",bg="white")
                eid.place(x=60,y=130)
                password = Label(gmail,text="Password",font=("Times New Roman",20),fg="black",bg="white")
                password.place(x=60,y=190)                
                to = Label(gmail,text="To",font=("Times New Roman",20),fg="black",bg="white")
                to.place(x=60,y=260)
                subject = Label(gmail,text="Subject",font=("Times New Roman",20),fg="black",bg="white")
                subject.place(x=60,y=330)               
                body = Label(gmail,text="Body",font=("Times New Roman",20),fg="black",bg="white")
                body.place(x=60,y=390)
                errormsg = Label(gmail,text="",font=("Times New Roman",15,"bold"),bg="white")
                errormsg.place(x=80,y=460)

                store_eid = StringVar()
                store_password = StringVar()
                store_to = StringVar()
                store_sub = StringVar()
                store_body = StringVar()

                en1 = Entry(gmail, textvariable = store_eid, font=("Times New Roman",20),bg = "light gray")
                en1.place(x = 210, y = 130)
                en2 = Entry(gmail, textvariable = store_password, show="*", font=("Times New Roman",20),bg = "light gray")
                en2.place(x = 210, y = 190)
                en3 = Entry(gmail, textvariable = store_to, font=("Times New Roman",20),bg = "light gray")
                en3.place(x = 210, y = 260)
                en4 = Entry(gmail, textvariable = store_sub, font=("Times New Roman",20),bg = "light gray")
                en4.place(x = 210, y = 330)
                en5 = Entry(gmail, textvariable = store_body, font=("Times New Roman",20),bg = "light gray")
                en5.place(x = 210, y = 390)

                def sendd():
                    try:
                        us = store_eid.get()
                        pw = store_password.get()
                        too = store_to.get()
                        sub = store_sub.get()
                        bodyy = store_body.get()
                        if en1.get()=="" or en2.get()=="" or en3.get()=="" or en4.get()=="" or en5.get()=="":
                            errormsg.config(text="All Fields required!", fg="red")
                            return
                        else:
                            final_mail = "Subject: {}\n{}".format(sub,bodyy)
                            server = smtplib.SMTP("smtp.gmail.com",587)
                            server.starttls()
                            server.login(us,pw)
                            server.sendmail(us,too,final_mail)
                            errormsg.config(text="Email Sent Successfully!", fg="green")
                    except:
                        errormsg.config(text="Couldn't Send Email due to some error...",fg ="red")
       
                def resett():
                    en1.delete(0,END)
                    en2.delete(0,END)
                    en3.delete(0,END)
                    en4.delete(0,END)
                    en5.delete(0,END)

                send = Button(gmail,text="Send Mail",font=("Times new roman",15,"bold","italic"),bg="dark gray", activebackground = "white", width=20, height = 10,relief=SUNKEN,command=sendd)
                send.place(x=150,y=500,height = 60, width=130)
                reset = Button(gmail,text="Reset",font=("Times new roman",15,"bold","italic"),bg="dark gray", activebackground = "white", width=20, height = 10,relief=SUNKEN,command=resett)
                reset.place(x=350,y=500,height = 60, width=130)
                
            def notes():
                from tkinter import filedialog
                note = Toplevel(home)
                note.geometry("600x600")
                note.title("Google Notes")
                note.config(bg="light gray")
                note.resizable(0,0)
                note.wm_iconbitmap(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\notes.ico")

                def save():
                    open_file = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
                    if open_file is None:
                        return
                    text = str(entry.get(1.0,END))
                    open_file.write(text)
                    open_file.close()

                def open_file():
                    file = filedialog.askopenfile(mode='r', filetype=[('text file','*.txt')])
                    if file is not None:
                        content = file.read()
                    entry.insert(INSERT,content)

                def exit():
                    note.destroy()

                save = Button(note,activebackground='dark gray',width='5',height='1',bg='light gray',text='Save',command=save)
                save.place(x=1,y=3)
                open = Button(note,activebackground='dark gray',width='5',height='1',bg='light gray',text='Open',command=open_file)
                open.place(x=50,y=3)
                exit = Button(note,activebackground='dark gray',width='5',height='1',bg='light gray',text='Exit',command=exit)
                exit.place(x=100,y=3)
                entry=Text(note,height=33,width=72,wrap=WORD,bg="black",fg="white",font=("Arial",15))
                entry.place(x=1,y=60)
                note.mainloop()

            def calendar():
                cal = Toplevel(home)
                cal.geometry("600x600")
                cal.title("Google Calendar")
                cal.config(bg="light salmon")
                cal.resizable(0,0)
                cal.wm_iconbitmap(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\calendar.ico")

                g_cal = Calendar(cal,selectmode="day",year=2023,month=2,day=6)
                g_cal.pack(fill='both',expand=True)

##                def get_date():
##                    my_label.config(text="Today,s date is "+cal.get_date())
##                c_button = Button(cal,text="Get Date",command=get_date)
##                cal_button.place(x=300,y=400)
##                my_label = Label(cal,text='')
##                my_label.place(x=300,y=450)

            from PIL import Image, ImageTk
            icon1 = (Image.open(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\translate.png"))
            resized_1 = icon1.resize((250,250), Image.ANTIALIAS)
            new_1 = ImageTk.PhotoImage(resized_1)
            icon1_l = Label(home, image = new_1)
            icon1_l.photo = new_1
            icon1_b = Button(home, height = 250, width = 250, image=new_1,command=translate, borderwidth=0)
            icon1_b.place(x=105, y=290)
            l1 = Label(home,text="Google Translate",font=("Verdana",15, "underline", "bold"))
            l1.place(x=135,y=640)
           
            icon2 = (Image.open(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\notes.png"))
            resized_2 = icon2.resize((250,250), Image.ANTIALIAS)
            new_2 = ImageTk.PhotoImage(resized_2)
            icon2_l = Label(home, image = new_2)
            icon2_l.photo = new_2
            icon2_b = Button(home, height = 250, width = 250, image=new_2,command=notes,borderwidth=0)
            icon2_b.place(x=455,y=290)
            l2 = Label(home,text="Google Notes",font=("Verdana",15, "underline", "bold"))
            l2.place(x=505,y=640)

            icon3 = (Image.open(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\gmail.jpg"))
            resized_3 = icon3.resize((250,250), Image.ANTIALIAS)
            new_3 = ImageTk.PhotoImage(resized_3)
            icon3_l = Label(home, image = new_3)
            icon3_l.photo = new_3
            icon3_b = Button(home, height = 250, width = 250, image=new_3,command=gmaiil,borderwidth=0)
            icon3_b.place(x=805,y=290)
            l3 = Label(home,text="Gmail",font=("Verdana",15, "underline", "bold"))
            l3.place(x=900,y=640)

            icon4 = (Image.open(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\calendar.png"))
            resized_4 = icon4.resize((250,250), Image.ANTIALIAS)
            new_4 = ImageTk.PhotoImage(resized_4)
            icon4_l = Label(home, image = new_4)
            icon4_l.photo = new_4
            icon4_b = Button(home, height = 250, width = 250, image=new_4,command=calendar,borderwidth=0)
            icon4_b.place(x=1155,y=290)
            l4 = Label(home,text="Google Calendar",font=("Verdana",15, "underline", "bold"))
            l4.place(x=1190,y=640)
            
        elif e1.get()=="shrutisakpal" and e2.get()=="abc@123" and int(e3.get())!=cap:
            messagebox.showwarning("ERROR","Invalid captcha")
        else:
            messagebox.showerror("ERROR","Incorrect Credentials! \nDont have an account? Create a new one now")
            
    button = Button(log,text="LOG IN",fg = "Black", bg = "light gray",font = ("Times New Roman",15,"bold"), height = 2,width = 10,activebackground = "dark gray",command = submit_log)
    button.place(x=300,y=500)   

def new_acc():
    na = Toplevel(root)
    na.title("Registration Page")
    na.geometry("800x700")
    na.resizable(0,0)
    na.wm_iconbitmap(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\reg.ico")
    na.config(bg="light pink")
    l = Label(na,text="CREATE YOUR NEW ACCOUNT",fg="dark red", bg = "light Pink",font=("8514oem",37))
    l.place(x=150,y=30)
    l1 = Label(na,text="UserName:-",fg = "black", bg = "white", font = ("Times New Roman",20,"bold"))
    l1.place(x = 100, y = 150)
    l2 = Label(na,text="Email:-",fg = "black", bg = "white", font = ("Times New Roman",20,"bold"))
    l2.place(x = 100, y = 260)
    l3 = Label(na,text="Password:-",fg = "black", bg = "white", font = ("Times New Roman",20,"bold"))
    l3.place(x = 100, y = 370)
    l3 = Label(na,text="Confirm Password:-",fg = "black", bg = "white", font = ("Times New Roman",20,"bold"))
    l3.place(x = 100, y = 480)

    e1 = Entry(na, font=("Times New Roman",20),bg = "light gray")
    e1.place(x = 350, y = 150)
    e2 = Entry(na, font=("Times New Roman",20),bg = "light gray")
    e2.place(x = 350, y = 260)
    e3 = Entry(na, font=("Times New Roman",20),bg = "light gray")
    e3.place(x = 350, y = 370)
    e4 = Entry(na, font=("Times New Roman",20),bg = "light gray")
    e4.place(x = 350, y = 480) 

    def clear():
        e1.delete(first=0,last=1000)
        e2.delete(first=0,last=1000)
        e3.delete(first=0,last=1000)
        e4.delete(first=0,last=1000)
    def error():
        messagebox.showerror("Error","Passwords not same")
        
    def submit_reg():
        connection = connect(host = "localhost",user="root",password="Shruti@24",database="login")                       
        c = connection.cursor()                                                                                         
        c.execute("insert into reg_acc values ('{}','{}','{}','{}');".format(e1.get(),e2.get(),e3.get(),e4.get()))                                    
        c.execute("select * from reg_acc")
        for data in c:                                                                                                  
            print(data)
        if e3.get() == e4.get():
            connection.commit()
            clear()
            from tkinter import messagebox
            messagebox.showinfo("REGISTERED","New Account created Successfully!")

            home = Toplevel(root)
            home.title("Application Page")
            home.geometry("1000x1000")
            home.config(bg = "light gray")
            home.wm_iconbitmap(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\apps.ico")
            label = Label(home,text="Google Apps",font = ("Segoe UI Black",95),fg="Dark Blue",bg="light gray")
            label.place(x=350,y=25)
                                    
            def translate():
                from tkinter import ttk, messagebox
                import googletrans
                from googletrans import Translator

                trans = Toplevel(home)
                trans.title("Google Translator")
                trans.geometry("1080x400")
                trans.resizable(0,0)
                trans.configure(bg="white")
                trans.wm_iconbitmap(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\translate.ico")

                arrow = (Image.open(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\arrow.png"))
                resized_arrow = arrow.resize((100,100), Image.ANTIALIAS)
                new_arrow = ImageTk.PhotoImage(resized_arrow)
                arrow_l = Label(trans, image = new_arrow)
                arrow_l.photo = new_arrow
                arrow_l.place(x=485,y=50)
                
                def label_change():
                    c1 = combo1.get()
                    c2 = combo2.get()

                    c1_l.configure(text=c1)
                    c2_l.configure(text=c2)
                    trans.after(1000, label_change)

                def translate_now():
                    text = text1.get(1.0,END)
                    t1 = Translator()
                    trans_text = t1.translate(text, src = combo1.get(), dest = combo2.get())
                    trans_text = trans_text.text
                    text2.delete(1.0, END)
                    text2.insert(END, trans_text)

                languages = googletrans.LANGUAGES
                languageV = list(languages.values())

                combo1 = ttk.Combobox(trans, values=languageV, font=("Arial",15), state = 'r')
                combo1.place(x=100,y=20)
                combo1.set('ENGLISH')

                c1_l = Label(trans,text="ENGLISH",font=("Arial",30,"bold"),bg="white",width=18,bd=5,relief = GROOVE)
                c1_l.place(x=10,y=50)

                f1 = Frame(trans,bg="Black",bd=5)
                f1.place(x=10,y=118,width=440,height=210)

                text1 = Text(f1, font=("Arial",20), bg="white", relief=GROOVE, wrap=WORD)
                text1.place(x=0,y=0,width=430,height=200)

                combo2 = ttk.Combobox(trans, values=languageV, font=("Arial",15), state = 'r')
                combo2.place(x=730,y=20)
                combo2.set('SELECT LANGUAGE')

                c2_l = Label(trans,text="ENGLISH",font=("Arial",30,"bold"),bg="white",width=18,bd=5,relief = GROOVE)
                c2_l.place(x=620,y=50)

                f2 = Frame(trans,bg="Black",bd=5)
                f2.place(x=620,y=118,width=440,height=210)

                text2 = Text(f2, font=("Arial",20), bg="white", relief=GROOVE, wrap=WORD)
                text2.place(x=0,y=0,width=430,height=200)

                trans_button = Button(trans,text="TRANSLATE", font=("Arial",15,"bold","italic"),cursor = "hand2", bg="red",fg="white",command=translate_now)
                trans_button.place(x=465,y=250)

                label_change()
                        
            def gmaiil():
                import smtplib
                gmail = Toplevel(home)
                gmail.title("Gmail")
                gmail.geometry("600x600")
                gmail.resizable(0,0)
                gmail.configure(bg="white")
                gmail.wm_iconbitmap(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\gmail.ico")

                main_l = Label(gmail,text="GMAIL",font=("Times New Roman",40,"bold","underline"),fg="dark red",bg="white")
                main_l.place(x=220,y=20)
                eid = Label(gmail,text="Email ID",font=("Times New Roman",20),fg="black",bg="white")
                eid.place(x=60,y=130)
                password = Label(gmail,text="Password",font=("Times New Roman",20),fg="black",bg="white")
                password.place(x=60,y=190)                
                to = Label(gmail,text="To",font=("Times New Roman",20),fg="black",bg="white")
                to.place(x=60,y=260)
                subject = Label(gmail,text="Subject",font=("Times New Roman",20),fg="black",bg="white")
                subject.place(x=60,y=330)               
                body = Label(gmail,text="Body",font=("Times New Roman",20),fg="black",bg="white")
                body.place(x=60,y=390)
                errormsg = Label(gmail,text="",font=("Times New Roman",15,"bold"),bg="white")
                errormsg.place(x=80,y=460)

                store_eid = StringVar()
                store_password = StringVar()
                store_to = StringVar()
                store_sub = StringVar()
                store_body = StringVar()

                en1 = Entry(gmail, textvariable = store_eid, font=("Times New Roman",20),bg = "light gray")
                en1.place(x = 210, y = 130)
                en2 = Entry(gmail, textvariable = store_password, show="*", font=("Times New Roman",20),bg = "light gray")
                en2.place(x = 210, y = 190)
                en3 = Entry(gmail, textvariable = store_to, font=("Times New Roman",20),bg = "light gray")
                en3.place(x = 210, y = 260)
                en4 = Entry(gmail, textvariable = store_sub, font=("Times New Roman",20),bg = "light gray")
                en4.place(x = 210, y = 330)
                en5 = Entry(gmail, textvariable = store_body, font=("Times New Roman",20),bg = "light gray")
                en5.place(x = 210, y = 390)

                def sendd():
                    try:
                        us = store_eid.get()
                        pw = store_password.get()
                        too = store_to.get()
                        sub = store_sub.get()
                        bodyy = store_body.get()
                        if en1.get()=="" or en2.get()=="" or en3.get()=="" or en4.get()=="" or en5.get()=="":
                            errormsg.config(text="All Fields required!", fg="red")
                            return
                        else:
                            final_mail = "Subject: {}\n{}".format(sub,bodyy)
                            server = smtplib.SMTP("smtp.gmail.com",587)
                            server.starttls()
                            server.login(us,pw)
                            server.sendmail(us,too,final_mail)
                            errormsg.config(text="Email Sent Successfully!", fg="green")
                    except:
                        errormsg.config(text="Couldn't Send Email due to some error...",fg ="red")

                def resett():
                    en1.delete(0,END)
                    en2.delete(0,END)
                    en3.delete(0,END)
                    en4.delete(0,END)
                    en5.delete(0,END)

                send = Button(gmail,text="Send Mail",font=("Times new roman",15,"bold","italic"),bg="dark gray", activebackground = "white", width=20, height = 10,relief=SUNKEN,command=sendd)
                send.place(x=150,y=500,height = 60, width=130)
                reset = Button(gmail,text="Reset",font=("Times new roman",15,"bold","italic"),bg="dark gray", activebackground = "white", width=20, height = 10,relief=SUNKEN,command=resett)
                reset.place(x=350,y=500,height = 60, width=130)
                
            def notes():
                from tkinter import filedialog
                note = Toplevel(home)
                note.geometry("600x600")
                note.title("Google Notes")
                note.config(bg="light gray")
                note.resizable(0,0)
                note.wm_iconbitmap(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\notes.ico")

                def save():
                    open_file = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
                    if open_file is None:
                        return
                    text = str(entry.get(1.0,END))
                    open_file.write(text)
                    open_file.close()

                def open_file():
                    file = filedialog.askopenfile(mode='r', filetype=[('text file','*.txt')])
                    if file is not None:
                        content = file.read()
                    entry.insert(INSERT,content)

                def exit():
                    note.destroy()

                save = Button(note,activebackground='dark gray',width='5',height='1',bg='light gray',text='Save',command=save)
                save.place(x=1,y=3)
                open = Button(note,activebackground='dark gray',width='5',height='1',bg='light gray',text='Open',command=open_file)
                open.place(x=50,y=3)
                exit = Button(note,activebackground='dark gray',width='5',height='1',bg='light gray',text='Exit',command=exit)
                exit.place(x=100,y=3)
                entry=Text(note,height=33,width=72,wrap=WORD,bg="black",fg="white",font=("Arial",15))
                entry.place(x=10,y=60)
                note.mainloop()

            def calendar():
                cal = Toplevel(home)
                cal.geometry("600x600")
                cal.title("Google Calendar")
                cal.config(bg="light salmon")
                cal.resizable(0,0)
                cal.wm_iconbitmap(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\calendar.ico")

                g_cal = Calendar(cal,selectmode="day",year=2023,month=2,day=6)
                g_cal.pack(fill='both',expand=True)

##                def get_date():
##                    my_label.config(text="Today,s date is "+cal.get_date())
##                c_button = Button(cal,text="Get Date",command=get_date)
##                cal_button.place(x=300,y=400)
##                my_label = Label(cal,text='')
##                my_label.place(x=300,y=450)
                
            from PIL import Image, ImageTk
            icon1 = (Image.open(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\translate.png"))
            resized_1 = icon1.resize((250,250), Image.ANTIALIAS)
            new_1 = ImageTk.PhotoImage(resized_1)
            icon1_l = Label(home, image = new_1)
            icon1_l.photo = new_1
            icon1_b = Button(home, height = 250, width = 250, image=new_1,command=translate, borderwidth=0)
            icon1_b.place(x=105, y=290)
            l1 = Label(home,text="Google Translate",font=("Verdana",15, "underline", "bold"))
            l1.place(x=135,y=640)
           
            icon2 = (Image.open(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\notes.png"))
            resized_2 = icon2.resize((250,250), Image.ANTIALIAS)
            new_2 = ImageTk.PhotoImage(resized_2)
            icon2_l = Label(home, image = new_2)
            icon2_l.photo = new_2
            icon2_b = Button(home, height = 250, width = 250, image=new_2,command=notes,borderwidth=0)
            icon2_b.place(x=455,y=290)
            l2 = Label(home,text="Google Notes",font=("Verdana",15, "underline", "bold"))
            l2.place(x=505,y=640)

            icon3 = (Image.open(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\gmail.jpg"))
            resized_3 = icon3.resize((250,250), Image.ANTIALIAS)
            new_3 = ImageTk.PhotoImage(resized_3)
            icon3_l = Label(home, image = new_3)
            icon3_l.photo = new_3
            icon3_b = Button(home, height = 250, width = 250, image=new_3,command=gmaiil,borderwidth=0)
            icon3_b.place(x=805,y=290)
            l3 = Label(home,text="Gmail",font=("Verdana",15, "underline", "bold"))
            l3.place(x=900,y=640)

            icon4 = (Image.open(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\calendar.png"))
            resized_4 = icon4.resize((250,250), Image.ANTIALIAS)
            new_4 = ImageTk.PhotoImage(resized_4)
            icon4_l = Label(home, image = new_4)
            icon4_l.photo = new_4
            icon4_b = Button(home, height = 250, width = 250, image=new_4,command=calendar,borderwidth=0)
            icon4_b.place(x=1155,y=290)
            l4 = Label(home,text="Google Calendar",font=("Verdana",15, "underline", "bold"))
            l4.place(x=1190,y=640)

        else:
            error()
        connection.close()
        print("Database connected!")
    
    button = Button(na,text="REGISTER",fg = "dark blue", bg = "light gray",font = ("Times New Roman",17,"bold"), height = 2,width = 10,activebackground = "dark gray",command= submit_reg)
    button.place(x=330,y=580)   

canvas.create_text(800,350,text="Google", font = ("Segoe UI Black",95), fill = "white")

b_login = Button(root, text = "LOG IN ", font = ("Times New Roman",15,"bold"),width = 25, height = 3, bd = '10', command = login)
b_acc = Button(root, text = "CREATE NEW ACCOUNT", font = ("Times New Roman",15,"bold"), width = 25, height = 3, bd = '10', command = new_acc)

import tkinter as tk
chatbot = (Image.open(r"C:\Users\Shruti Sakpal\OneDrive\Desktop\png\chatbot.png"))
resized_chatbot = chatbot.resize((100,100), Image.ANTIALIAS)
new_chatbot = ImageTk.PhotoImage(resized_chatbot)
chatbot_l = Label(root, image = new_chatbot)
chatbot_l.photo = new_chatbot
chatbot_b = tk.Button(root, height = 100, width = 100, image=new_chatbot,command=chat, borderwidth=0)
chatbot_b.place(x=80, y=650)

b_login_window = canvas.create_window(430,500, anchor = "nw", window = b_login)
b_acc_window = canvas.create_window(920,500, anchor = "nw", window = b_acc)
root.mainloop()
