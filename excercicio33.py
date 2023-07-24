from tkinter import *
import re

class Application:
    def __init__(self, master=None):

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
        self.primeiroContainer.configure(bg="blue")

        self.titulo = Label(self.primeiroContainer, foreground="white", bg="blue", text="")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        self.primeiroContainer.configure(bg="blue")

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 25
        self.segundoContainer.pack()
        self.segundoContainer.configure(bg="blue")

        self.nomeLabel = Label(self.segundoContainer, bg="blue",text="Nome             ",foreground="white", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        self.segundoContainer.configure(bg="blue")

        self.nome = Entry(self.segundoContainer, foreground="blue")
        self.nome.focus()
        self.nome["width"] = 35
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
        self.terceiroContainer.configure(bg="blue")

        self.idadelabel = Label(self.terceiroContainer, bg="blue", foreground="white", text="Idade em anos", font=self.fontePadrao)
        self.idadelabel.pack(side=LEFT)
        self.terceiroContainer.configure(bg="blue")

        self.idade = Entry(self.terceiroContainer, foreground="blue")
        self.idade.tk_focusFollowsMouse()
        self.idade["width"] = 35
        self.idade["font"] = self.fontePadrao
        self.idade.pack(side=LEFT)
        self.terceiroContainer.configure(bg="blue")

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
        self.quartoContainer.configure(bg="blue")

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Eviar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.exibir
        self.autenticar.pack()
        self.quartoContainer.configure(bg="blue")

        self.rquartoContainer = Frame(master)
        self.rquartoContainer["pady"] = 0
        self.rquartoContainer.pack()
        self.rquartoContainer.configure(bg="blue")
        
        self.mensagem = Label(self.rquartoContainer, bg="blue", foreground="white", font=self.fontePadrao)
        self.mensagem.pack()
        self.rquartoContainer.configure(bg="blue")
        
    def exibir(self):
        nome = self.nome.get()
        anos = self.idade.get()
        if nome == "" or int(anos) == "" or int(anos) == 0:
            self.mensagem["text"] = "Nome e Idade não podem ficar em branco!!"

            if int(anos) == 0:
                self.mensagem["text"] = "Idade não ser 0!!"
        else:

            resultado = ""

            if int(anos)%2==0:
                self.mensagem["text"] = "\nIdade é Par"
                resultado += "Idade é Par"
            else: 
                resultado += "Idade é Impar"

            resultado +="\nSua Idade em dias é:" + str(int(anos)* 365)
            resultado += "\nSua Idade em meses é:" + str(int(anos)* 12)
            
            res = bool(re.search(r"\s", nome)) 
            if res == True:
                resultado += "\nSeu nome  contem espaco"
            else:
                resultado += "\nSeu nome nao contem espaco"

            resultado += "\nA primeira letra é:" + str(nome).split()[0][0]
            maximo = len(nome)
            resultado += "\nA ultima letra é:" + str(nome).split()[0][maximo-1]
            self.mensagem["text"] = resultado
            

interface = Tk()
interface.title("Exercicio 3")
Application()
interface.configure(bg="blue")
interface.mainloop()