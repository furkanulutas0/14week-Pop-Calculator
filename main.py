from tkinter import *
from tkinter import messagebox


def info():
    quiz = float(quizEntry.get())
    wt1= float(wt1Entry.get())
    mid= float(midEntry.get())
    wt2= float(wt2Entry.get())
    spk= float(spkEntry.get())
    cp= float(cpEntry.get())
    op= float(opEntry.get())
    pop= float(popEntry.get())

    if quiz > 100 or quiz <0:
        messagebox.showerror("QUIZ NOTU HATALI!", "Program bir hatayla karşılaştı. Quiz Notunuzu kontrol edin.")
        clear()
        return
    if wt1 > 100 or wt1 <0:
        messagebox.showerror("WT-1 NOTU HATALI!", "Program bir hatayla karşılaştı. WT-1 Notunuzu kontrol edin.")
        clear()
        return
    if mid > 100 or mid <0:
        messagebox.showerror("MIDTERM NOTU HATALI!", "Program bir hatayla karşılaştı. MIDTERM Notunuzu kontrol edin.")
        clear()
        return
    if wt2 > 100 or wt2 <0:
        messagebox.showerror("WT-2 NOTU HATALI!", "Program bir hatayla karşılaştı. WT-2 Notunuzu kontrol edin.")
        clear()
        return
    if spk > 100 or spk <0:
        messagebox.showerror("SPEAKING NOTU HATALI!", "Program bir hatayla karşılaştı. SPEAKING Notunuzu kontrol edin.")
        clear()
        return
    if cp > 100 or cp <0:
        messagebox.showerror("CLASS PARTICIPATION NOTU HATALI!", "Program bir hatayla karşılaştı. CLASS PARTICIPATION Notunuzu kontrol edin.")
        clear()
        return
    if op > 100 or op <0:
        messagebox.showerror("ONLINE PRACTISE NOTU HATALI!", "Program bir hatayla karşılaştı. ONLINE PRACTISE Notunuzu kontrol edin.")
        clear()
        return
    if pop > 100 or pop <0:
        messagebox.showerror("POP NOTU HATALI!", "Program bir hatayla karşılaştı. POP Notunuzu kontrol edin.")
        clear()
        return



    islem = (wt1*0.025) + (mid*0.15) + (wt2*0.025) + (quiz*0.05) + (spk*0.05) + (op*0.05) + (cp*0.05) + (pop*0.6)

    if islem > 100 or islem <0:
        messagebox.showwarning("HATA", "Program bir hatayla karşılaştı. Notlarınızı kontrol edin.")
        clear()
        return

    if islem >= 60 and islem <= 100:
        messagebox.showinfo("Tebrikler", f"Pop'u {islem} puanla geçmeye hak kazandınız.")
        clear()
    else:
        messagebox.showerror("Aga b", f"Pop'u geçmek için {60-islem} puana ihtiyacın var.")
        clear()

def clear():
    check = CheckVar1.get()
    if check == True:
        popEntry.delete(0, END)
        popEntry.insert(0, 0)
        return
    else:
        quizEntry.delete(0, END)
        quizEntry.insert(0, 0)

        wt1Entry.delete(0, END)
        wt1Entry.insert(0, 0)

        midEntry.delete(0, END)
        midEntry.insert(0, 0)

        wt2Entry.delete(0, END)
        wt2Entry.insert(0, 0)

        spkEntry.delete(0, END)
        spkEntry.insert(0, 0)

        opEntry.delete(0, END)
        opEntry.insert(0, 0)

        cpEntry.delete(0, END)
        cpEntry.insert(0, 0)

        popEntry.delete(0, END)
        popEntry.insert(0, 0)


def mainScreen():
    global quizEntry
    global wt1Entry
    global midEntry
    global wt2Entry
    global spkEntry
    global cpEntry
    global opEntry
    global popEntry
    global CheckVar1
    main = Tk()
    main.title("14 Week Calculator")
    main.geometry("512x512")


    mainCanvas = Canvas(main, height=512, width=512)
    mainCanvas.pack()

    frameBG= Frame(main)
    frameBG.place(relx=0,rely=0,relheight=1,relwidth=1)

    CheckVar1 = BooleanVar()

    c1 = Checkbutton(frameBG, text="Only Pop", variable=CheckVar1)
    c1.place(relx=0.01,rely=0.2, relwidth=0.2, relheight=0.2)

    quizLabel = Label(frameBG, text='Quiz', bg='grey')
    quizLabel.place(relx=0.2,rely=0.05,relheight=0.05,relwidth=0.3)

    quizEntry = Entry(frameBG, bd=2, font='Calbri 10')
    quizEntry.insert(END, '0')
    quizEntry.place(relx=0.501, rely=0.05, relwidth=0.3, relheight=0.05)

    wt1Label = Label(frameBG, text='WT 1', bg='grey')
    wt1Label.place(relx=0.2,rely=0.15,relheight=0.07,relwidth=0.3)

    wt1Entry = Entry(frameBG, bd=2, font='Calbri 10', )
    wt1Entry.insert(END, '0')
    wt1Entry.place(relx=0.501, rely=0.15, relwidth=0.3, relheight=0.07)

    midLabel = Label(frameBG, text='Midterm', bg='grey')
    midLabel.place(relx=0.2,rely=0.25,relheight=0.07,relwidth=0.3)

    midEntry = Entry(frameBG, bd=2, font='Calbri 10')
    midEntry.insert(END, '0')
    midEntry.place(relx=0.501, rely=0.25, relwidth=0.3, relheight=0.07)

    wt2Label = Label(frameBG, text='WT 2', bg='grey')
    wt2Label.place(relx=0.2,rely=0.35,relheight=0.07,relwidth=0.3)

    wt2Entry = Entry(frameBG, bd=2, font='Calbri 10')
    wt2Entry.insert(END, '0')
    wt2Entry.place(relx=0.501, rely=0.35, relwidth=0.3, relheight=0.07)

    spkLabel = Label(frameBG, text='Speaking', bg='grey')
    spkLabel.place(relx=0.2,rely=0.45,relheight=0.07,relwidth=0.3)

    spkEntry = Entry(frameBG, bd=2, font='Calbri 10')
    spkEntry.insert(END, '0')
    spkEntry.place(relx=0.501, rely=0.45, relwidth=0.3, relheight=0.07)

    cpLabel = Label(frameBG, text='Class Partication', bg='grey')
    cpLabel.place(relx=0.2,rely=0.55,relheight=0.07,relwidth=0.3)

    cpEntry = Entry(frameBG, bd=2, font='Calbri 10')
    cpEntry.insert(END, '0')
    cpEntry.place(relx=0.501, rely=0.55, relwidth=0.3, relheight=0.07)

    opLabel = Label(frameBG, text='Online Practise', bg='grey')
    opLabel.place(relx=0.2,rely=0.65,relheight=0.07,relwidth=0.3)

    opEntry = Entry(frameBG, bd=2, font='Calbri 10')
    opEntry.insert(END, '0')
    opEntry.place(relx=0.501, rely=0.65, relwidth=0.3, relheight=0.07)

    popLabel = Label(frameBG, text='Pop Exam', bg='grey')
    popLabel.place(relx=0.2,rely=0.75,relheight=0.07,relwidth=0.3)

    popEntry = Entry(frameBG, bd=2, font='Calbri 10')
    popEntry.insert(END, '0')
    popEntry.place(relx=0.501, rely=0.75, relwidth=0.3, relheight=0.07)

    gonderBtn = Button(frameBG, text='Gönder', command = info)
    gonderBtn.place(relx=0.301, rely=0.9, relwidth=0.3, relheight=0.07)

    msgLabel = Label(frameBG, text='copyright © Furkan Ulutas', font='trebuchetms 8 bold')
    msgLabel.place(relx=0.7,rely=0.9, relwidth=0.3, relheight=0.1)

    main.mainloop()
mainScreen()
