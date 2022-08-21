from tkinter import *



def janela_cadastro():

    class Rotas_cadastro():
        def chamar_login():
            root.destroy()
            from login import janela_login
            janela_login()


    root = Tk()
    root.title('')
    root.geometry('150x150')
    label=Label(root,text='Cadastro',font=50)
    label.place(relx=0.2,rely=0)
    bt=Button(root,text='Login',command=Rotas_cadastro.chamar_login)
    bt.place(relx=0.2,rely=0.23)

    root.mainloop()


