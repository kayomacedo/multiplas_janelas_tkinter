from tkinter import *




def janela_login():

    class Rotas_login():

        def chamar_cadastro():
            root.destroy()
            from cadastro import janela_cadastro
            janela_cadastro()

    root = Tk()
    root.title('')
    root.geometry('150x150')
    label=Label(root,text='Login',font=50)
    label.place(relx=0.29,rely=0)
    bt=Button(root,text='Cadastro',command=Rotas_login.chamar_cadastro)
    bt.place(relx=0.2,rely=0.23)

    root.mainloop()

janela_login()