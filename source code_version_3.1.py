__author__ = 'Mystic Dav'
__version__ = "3.1"
#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class wordlist:
    def __init__(self,master):
        
        master.title('MYSTIC DAV WORDLIST GENERATOR version 2.1')
        master.resizable(False, False)
        master.geometry('537x310+350+200')
        master.configure(background = 'grey')
        label=ttk.Label(master,text="\t\tWORDLIST GENERATOR by C.A.N. ",background='grey')
        label.config(justify=LEFT)
        label.config(font = ('Courier', 11, 'bold'))
        label.place(x=0,y=0,width=537,height=21)
        #logo frame
        logo_frame=ttk.Frame(master)
        logo_frame.config(height=250,width=250)
        logo_frame.config(relief=RIDGE)
        logo_frame.place(x=15,y=20)
         #input frame
        f1=ttk.Frame(master)
        f1.config(height=250,width=260)
        f1.config(relief=RIDGE)
        f1.place(x=260,y=20)
        #label for text box
        ttk.Label(master,text="Enter the Characters").place(x=270,y=23)
        ttk.Label(master,text="Enter the Digits").place(x=270,y=63)
        ttk.Label(master,text="Enter the Punctuations or Symbols").place(x=270,y=103)
        ttk.Label(master,text="Enter the name of file(Don`t add Extension)").place(x=270,y=143)
        ttk.Label(master,text="Select wordlist Max Character").place(x=270,y=183)
        #text box
        self.te1= StringVar()
        ttk.Entry(master,textvariable=self.te1, width = 37).place(x=270,y=40)
        self.te2= StringVar()
        ttk.Entry(master,textvariable=self.te2, width = 37).place(x=270,y=80)
        self.te3= StringVar()
        ttk.Entry(master,textvariable=self.te3, width = 37).place(x=270,y=120)
        self.te4=StringVar()
        ttk.Entry(master,textvariable=self.te4, width = 37).place(x=270,y=160)
        #spinbox
        self.wordlist_len= StringVar()
        Spinbox(master, from_=1,to = 15,textvariable=self.wordlist_len).place(x=270,y=200,width=227,height=25)
        #buttons
        b1 = ttk.Button(master, text = 'Submit',command=self.submit_button)
        b1.place(x=420,y=235)
        b2=ttk.Button(master,text = 'About Us',command=self.about_us_button) #done
        b2.place(x=270,y=235)
        b3=ttk.Button(master,text='close', command=master.destroy) #done
        b3.place(x=444,y=275)
        b4=ttk.Button(master,text='Reset', command=self.clear) #done
        b4.place(x=345,y=235)
        #progress bar
        self.bar=ttk.Progressbar(master,orient = HORIZONTAL, length=415)
        self.bar.config(mode = 'determinate',maximum=100.0)
        self.bar.place(x=15,y=275,height=25)
        self.bar.config(value=5.0)
    
    def clear(self):
        self.te1.set('')
        self.te2.set('')
        self.te3.set('')
        self.te4.set('')
        self.bar.config(value=0.0)
        
    def submit_button(self):
        self.bar.config(value=20.0)
        a=self.te1.get() + self.te2.get() + self.te3.get()
        file_name=self.te4.get()
        length_wordlist=self.wordlist_len.get()
        if file_name == '' :
            messagebox.showinfo(title = 'ERROR', message = 'Please Enter the Name of file ')
        else:
            if length_wordlist == '1':
                self.bar.config(value=50.0)
                FILE = open(file_name + '.txt', "w")
                for x1 in range(0, len(a)):
                    s = ''
                    s = s + a[x1]
                    FILE.write(s + '\n')
                FILE.close()
                self.bar.config(value=100.0)
                messagebox.showinfo(title = 'Complete', message = 'wordlist is Now Generated!')
            elif length_wordlist == '2':
                self.bar.config(value=50.0)
                FILE = open(file_name + '.txt', "w")
                for x1 in range(0, len(a)):
                    s = ''
                    s = s + a[x1]
                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        s = ''
                        s = s + a[x1] + a[x2]
                        FILE.write(s + '\n')
                        self.bar.config(value=100.0)
                        messagebox.showinfo(title = 'Complete', message = 'wordlist is Now Generated!')
            elif length_wordlist == '3':
                self.bar.config(value=50.0)
                FILE = open(file_name + '.txt', "w")
                for x1 in range(0, len(a)):
                    s = ''
                    s = s + a[x1]
                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        s = ''
                        s = s + a[x1] + a[x2]
                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            s = ''
                            s = s + a[x1] + a[x2] + a[x3]
                    FILE.write(s + '\n')
                    self.bar.config(value=100.0)
                    messagebox.showinfo(title = 'Complete', message = 'wordlist is Now Generated!')
            elif length_wordlist == '4':
                self.bar.config(value=50.0)
                FILE = open(file_name + '.txt', "w")
                for x1 in range(0, len(a)):
                    s = ''
                    s = s + a[x1]
                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        s = ''
                        s = s + a[x1] + a[x2]
                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            s = ''
                            s = s + a[x1] + a[x2] + a[x3]
                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                s = ''
                                s = s + a[x1] + a[x2] + a[x3] + a[x4]
                                FILE.write(s + '\n')
                                self.bar.config(value=100.0)
                                messagebox.showinfo(title = 'Complete', message = 'wordlist is Now Generated!')
            elif length_wordlist == '5':
                self.bar.config(value=50.0)
                FILE = open(file_name + '.txt', "w")
                for x1 in range(0, len(a)):
                    s = ''
                    s = s + a[x1]
                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        s = ''
                        s = s + a[x1] + a[x2]
                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            s = ''
                            s = s + a[x1] + a[x2] + a[x3]
                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                s = ''
                                s = s + a[x1] + a[x2] + a[x3] + a[x4]
                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    s = ''
                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5]
                                    FILE.write(s + '\n')
                                    self.bar.config(value=100.0)
                                    messagebox.showinfo(title = 'Complete', message = 'wordlist is Now Generated!')
            elif length_wordlist == '6':
                self.bar.config(value=50.0)
                FILE = open(file_name + '.txt', "w")
                for x1 in range(0, len(a)):
                    s = ''
                    s = s + a[x1]
                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        s = ''
                        s = s + a[x1] + a[x2]
                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            s = ''
                            s = s + a[x1] + a[x2] + a[x3]
                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                s = ''
                                s = s + a[x1] + a[x2] + a[x3] + a[x4]
                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    s = ''
                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5]
                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        s = ''
                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6]
                                        FILE.write(s + '\n')
                                        self.bar.config(value=100.0)
                                        messagebox.showinfo(title = 'Complete', message = 'wordlist is Now Generated!')
            elif length_wordlist == '7':
                self.bar.config(value=50.0)
                FILE = open(file_name + '.txt', "w")
                for x1 in range(0, len(a)):
                    s = ''
                    s = s + a[x1]
                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        s = ''
                        s = s + a[x1] + a[x2]
                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            s = ''
                            s = s + a[x1] + a[x2] + a[x3]
                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                s = ''
                                s = s + a[x1] + a[x2] + a[x3] + a[x4]
                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    s = ''
                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5]
                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        s = ''
                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6]
                                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            s = ''
                                            s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7]
                                            FILE.write(s + '\n')
                                            self.bar.config(value=100.0)
                                            messagebox.showinfo(title = 'Complete', message = 'wordlist is Now Generated!')
            elif length_wordlist == '8':
                self.bar.config(value=50.0)
                FILE = open(file_name + '.txt', "w")
                for x1 in range(0, len(a)):
                    s = ''
                    s = s + a[x1]
                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        s = ''
                        s = s + a[x1] + a[x2]
                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            s = ''
                            s = s + a[x1] + a[x2] + a[x3]
                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                s = ''
                                s = s + a[x1] + a[x2] + a[x3] + a[x4]
                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    s = ''
                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5]
                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        s = ''
                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6]
                                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            s = ''
                                            s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7]
                                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                s = ''
                                                s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8]
                                                FILE.write(s + '\n')
                                                self.bar.config(value=100.0)
                                                messagebox.showinfo(title = 'Complete', message = 'wordlist is Now Generated!')
            elif length_wordlist == '9':
                self.bar.config(value=50.0)
                FILE = open(file_name + '.txt', "w")
                for x1 in range(0, len(a)):
                    s = ''
                    s = s + a[x1]
                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        s = ''
                        s = s + a[x1] + a[x2]
                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            s = ''
                            s = s + a[x1] + a[x2] + a[x3]
                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                s = ''
                                s = s + a[x1] + a[x2] + a[x3] + a[x4]
                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    s = ''
                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5]
                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        s = ''
                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6]
                                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            s = ''
                                            s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7]
                                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                s = ''
                                                s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8]
                                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    s = ''
                                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9]
                                                    FILE.write(s + '\n')
                                                    self.bar.config(value=100.0)
                                                    messagebox.showinfo(title = 'Complete', message = 'wordlist is Now Generated!')
            elif length_wordlist == '10':
                self.bar.config(value=50.0)
                FILE = open(file_name + '.txt', "w")
                for x1 in range(0, len(a)):
                    s = ''
                    s = s + a[x1]
                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        s = ''
                        s = s + a[x1] + a[x2]
                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            s = ''
                            s = s + a[x1] + a[x2] + a[x3]
                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                s = ''
                                s = s + a[x1] + a[x2] + a[x3] + a[x4]
                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    s = ''
                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5]
                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        s = ''
                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6]
                                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            s = ''
                                            s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7]
                                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                s = ''
                                                s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8]
                                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    s = ''
                                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9]
                                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        s = ''
                                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10]  
                                                        FILE.write(s + '\n')
                                                        self.bar.config(value=100.0)
                                                        messagebox.showinfo(title = 'Complete', message = 'wordlist is Now Generated!')
            elif length_wordlist == '11':
                self.bar.config(value=50.0)
                FILE = open(file_name + '.txt', "w")
                for x1 in range(0, len(a)):
                    s = ''
                    s = s + a[x1]
                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        s = ''
                        s = s + a[x1] + a[x2]
                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            s = ''
                            s = s + a[x1] + a[x2] + a[x3]
                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                s = ''
                                s = s + a[x1] + a[x2] + a[x3] + a[x4]
                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    s = ''
                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5]
                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        s = ''
                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6]
                                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            s = ''
                                            s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7]
                                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                s = ''
                                                s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8]
                                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    s = ''
                                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9]
                                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        s = ''
                                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10] 
                                                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        for x11 in range(0, len(a)):
                                                            s = ''
                                                            s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10] + a[x11]
                                                            FILE.write(s + '\n')
                                                            self.bar.config(value=100.0)
                                                            messagebox.showinfo(title = 'Complete', message = 'wordlist is Now Generated!')
            elif length_wordlist == '12':
                self.bar.config(value=50.0)
                FILE = open(file_name + '.txt', "w")
                for x1 in range(0, len(a)):
                    s = ''
                    s = s + a[x1]
                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        s = ''
                        s = s + a[x1] + a[x2]
                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            s = ''
                            s = s + a[x1] + a[x2] + a[x3]
                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                s = ''
                                s = s + a[x1] + a[x2] + a[x3] + a[x4]
                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    s = ''
                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5]
                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        s = ''
                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6]
                                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            s = ''
                                            s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7]
                                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                s = ''
                                                s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8]
                                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    s = ''
                                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9]
                                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        s = ''
                                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10]
                                                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        for x11 in range(0, len(a)):
                                                            s = ''
                                                            s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10] + a[x11]    
                                                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        for x11 in range(0, len(a)):
                                                            for x12 in range(0, len(a)):
                                                                s = ''
                                                                s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10] + a[x11] + a[x12]  
                                                                FILE.write(s + '\n')
                                                                self.bar.config(value=100.0)
                                                                messagebox.showinfo(title = 'Complete', message = 'wordlist is Now Generated!')
            elif length_wordlist == '13':
                self.bar.config(value=50.0)
                FILE = open(file_name + '.txt', "w")
                for x1 in range(0, len(a)):
                    s = ''
                    s = s + a[x1]
                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        s = ''
                        s = s + a[x1] + a[x2]
                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            s = ''
                            s = s + a[x1] + a[x2] + a[x3]
                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                s = ''
                                s = s + a[x1] + a[x2] + a[x3] + a[x4]
                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    s = ''
                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5]
                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        s = ''
                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6]
                                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            s = ''
                                            s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7]
                                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                s = ''
                                                s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8]
                                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    s = ''
                                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9]
                                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        s = ''
                                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10]
                                                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        for x11 in range(0, len(a)):
                                                            s = ''
                                                            s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10] + a[x11]
                                                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        for x11 in range(0, len(a)):
                                                            for x12 in range(0, len(a)):
                                                                s = ''
                                                                s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10] + a[x11] + a[x12]
                                                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        for x11 in range(0, len(a)):
                                                            for x12 in range(0, len(a)):
                                                                for x13 in range(0, len(a)):
                                                                    s = ''
                                                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10] + a[x11] + a[x12] + a[x13]
                                                                    FILE.write(s + '\n')
                                                                    self.bar.config(value=100.0)
                                                                    messagebox.showinfo(title = 'Complete', message = 'wordlist is Now Generated!')
            elif length_wordlist == '14':
                self.bar.config(value=50.0)
                FILE = open(file_name + '.txt', "w")
                for x1 in range(0, len(a)):
                    s = ''
                    s = s + a[x1]
                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        s = ''
                        s = s + a[x1] + a[x2]
                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            s = ''
                            s = s + a[x1] + a[x2] + a[x3]
                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                s = ''
                                s = s + a[x1] + a[x2] + a[x3] + a[x4]
                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    s = ''
                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5]
                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        s = ''
                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6]
                                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            s = ''
                                            s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7]
                                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                s = ''
                                                s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8]
                                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    s = ''
                                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9]
                                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        s = ''
                                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10]
                                                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        for x11 in range(0, len(a)):
                                                            s = ''
                                                            s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10] + a[x11]
                                                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        for x11 in range(0, len(a)):
                                                            for x12 in range(0, len(a)):
                                                                s = ''
                                                                s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10] + a[x11] + a[x12]
                                                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        for x11 in range(0, len(a)):
                                                            for x12 in range(0, len(a)):
                                                                for x13 in range(0, len(a)):
                                                                    s = ''
                                                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10] + a[x11] + a[x12] + a[x13]
                                                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        for x11 in range(0, len(a)):
                                                            for x12 in range(0, len(a)):
                                                                for x13 in range(0, len(a)):
                                                                    for x14 in range(0, len(a)):
                                                                        s = ''
                                                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10] + a[x11] + a[x12] + a[x13] + a[x14]
                                                                        FILE.write(s + '\n')
                                                                        self.bar.config(value=100.0)
                                                                        messagebox.showinfo(title = 'Complete', message = 'wordlist is Now Generated!')
            elif length_wordlist == '15':
                self.bar.config(value=50.0)
                FILE = open(file_name + '.txt', "w")
                for x1 in range(0, len(a)):
                    s = ''
                    s = s + a[x1]
                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        s = ''
                        s = s + a[x1] + a[x2]
                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            s = ''
                            s = s + a[x1] + a[x2] + a[x3]
                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                s = ''
                                s = s + a[x1] + a[x2] + a[x3] + a[x4]
                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    s = ''
                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5]
                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        s = ''
                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6]
                                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            s = ''
                                            s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7]
                                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                s = ''
                                                s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8]
                                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    s = ''
                                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9]
                                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        s = ''
                                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10]
                                                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        for x11 in range(0, len(a)):
                                                            s = ''
                                                            s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10] + a[x11]
                                                            FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        for x11 in range(0, len(a)):
                                                            for x12 in range(0, len(a)):
                                                                s = ''
                                                                s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10] + a[x11] + a[x12]
                                                                FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        for x11 in range(0, len(a)):
                                                            for x12 in range(0, len(a)):
                                                                for x13 in range(0, len(a)):
                                                                    s = ''
                                                                    s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10] + a[x11] + a[x12] + a[x13]
                                                                    FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        for x11 in range(0, len(a)):
                                                            for x12 in range(0, len(a)):
                                                                for x13 in range(0, len(a)):
                                                                    for x14 in range(0, len(a)):
                                                                        s = ''
                                                                        s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10] + a[x11] + a[x12] + a[x13] + a[x14]
                                                                        FILE.write(s + '\n')
                for x1 in range(0, len(a)):
                    for x2 in range(0, len(a)):
                        for x3 in range(0, len(a)):
                            for x4 in range(0, len(a)):
                                for x5 in range(0, len(a)):
                                    for x6 in range(0, len(a)):
                                        for x7 in range(0, len(a)):
                                            for x8 in range(0, len(a)):
                                                for x9 in range(0, len(a)):
                                                    for x10 in range(0, len(a)):
                                                        for x11 in range(0, len(a)):
                                                            for x12 in range(0, len(a)):
                                                                for x13 in range(0, len(a)):
                                                                    for x14 in range(0, len(a)):
                                                                        for x15 in range(0, len(a)):
                                                                            s = ''
                                                                            s = s + a[x1] + a[x2] + a[x3] + a[x4] + a[x5] + a[x6] + a[x7] + a[x8] + a[x9] + a[x10] + a[x11] + a[x12] + a[x13] + a[x14] + a[x15]
                                                                            FILE.write(s + '\n')
                                                                            self.bar.config(value=100.0)
                                                                            messagebox.showinfo(title = 'Complete', message = 'wordlist is Now Generated!')
        
        
    def about_us_button(self):
        window=Toplevel()
        window.resizable(False,False)
        window.geometry('300x50+550+300')
        window.title('About Us')
        Label(window,text='Coding By      :DAVINDER PAL',font = ('Courier', 12, 'bold')).grid(row = 0, column = 0)
        Label(window,text='Logo Desgin By :ASHISH YADAV',font = ('Courier', 12, 'bold')).grid(row = 1, column = 0)

def main():            
    
    root = Tk()
    wordlist1 = wordlist(root)
    root.mainloop()
    
if __name__ == "__main__": main()    
  

