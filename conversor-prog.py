from tkinter import *

class Tela:
    cor_fundo = "#ECA400"
    def __init__(self):
        self.root = root
        self.configura_tela()
        self.widgets()
        root.mainloop()

    def configura_tela(self):
        self.root.title("Conversor")
        self.root.iconbitmap('conversor.ico')
        self.root.state("zoomed")
        self.root.configure(bg=self.cor_fundo)

    def widgets(self):
        Label(self.root, text="CONVERSOR", font=("Arial 40 bold"), bg=self.cor_fundo).place(relx=0.42, rely=0.05)

        self.tb_entrada = Entry(self.root, text=float(),font=("Arial 20 bold"), justify=CENTER)
        self.tb_entrada.place(relx=0.05, rely=0.15, relwidth=0.3, relheight=0.17)

        self.tb_saida = Label(self.root, text=None, font=("Arial 20 bold"), bg="white")
        self.tb_saida.place(relx=0.66, rely=0.15, relwidth=0.3, relheight=0.17)

        Label(self.root, text="=", font=("Arial 80 bold"), bg=self.cor_fundo).place(relx=0.49, rely=0.156)

        Label(self.root, text="Escolha o tipo de conversão:", font=("Arial 20 bold"), bg=self.cor_fundo).place(relx=0.05, rely=0.35)

        Label(self.root, text="→", font=("Arial 70 bold"), bg=self.cor_fundo).place(relx=0.48, rely=0.365)


        listaMedidas = ["Milímetro", "Centímetro", "Metro", "Polegada"]

        self.escolhaEsq = StringVar()
        self.escolhaEsq.set(listaMedidas[0])
        op_escolhaEsq = OptionMenu(self.root, self.escolhaEsq, *listaMedidas)
        op_escolhaEsq.place(relx=0.05, rely=0.4, relwidth=0.38, relheight=0.06)

        self.escolhaDir = StringVar()
        self.escolhaDir.set(listaMedidas[1])
        op_escolhaDir = OptionMenu(self.root, self.escolhaDir, *listaMedidas)
        op_escolhaDir.place(relx=0.58, rely=0.4, relwidth=0.38, relheight=0.06)


        self.btn_converte = Button(self.root, text="Converter",font=("Arial 15 bold"), bg="#1B4332", fg="#fff", activebackground="#52B788", activeforeground="#000", command=self.converter)
        self.btn_converte.place(relx=0.58, rely=0.5, relwidth=0.38, relheight=0.09)

        self.btn_limpa = Button(self.root, text="Limpar",font=("Arial 15 bold"), bg="#9D0208", fg="#fff", activebackground="#DC2F02", activeforeground="#000", command=self.limpar)
        self.btn_limpa.place(relx=0.05, rely=0.5, relwidth=0.38, relheight=0.09)

    def converter(self):
        tipoEsq = self.escolhaEsq.get()
        tipoDir = self.escolhaDir.get()
        if self.tb_entrada.get() != "":
            numero = float(self.tb_entrada.get())
            if tipoEsq == "Milímetro":
                if tipoDir == "Milímetro":
                    resultado = numero
                elif tipoDir == "Centímetro":
                    resultado = numero / 10
                elif tipoDir == "Metro":
                    resultado = numero / 1000
                elif tipoDir == "Polegada":
                    resultado = numero / 25.4
                Label(self.root, text=resultado, font=("Arial 20 bold"), bg="white").place(relx=0.66, rely=0.15, relwidth=0.3, relheight=0.17)

            elif tipoEsq == "Centímetro":
                if tipoDir == "Milímetro":
                    resultado = numero * 10
                elif tipoDir == "Centímetro":
                    resultado = numero
                elif tipoDir == "Metro":
                    resultado = numero / 100
                elif tipoDir == "Polegada":
                    resultado = numero / 2.54 
                Label(self.root, text=resultado, font=("Arial 20 bold"), bg="white").place(relx=0.66, rely=0.15, relwidth=0.3, relheight=0.17)

            elif tipoEsq == "Metro":
                if tipoDir == "Milímetro":
                    resultado = numero * 1000
                elif tipoDir == "Centímetro":
                    resultado = numero * 100
                elif tipoDir == "Metro":
                    resultado = numero
                elif tipoDir == "Polegada":
                    resultado = numero * 39.37
                Label(self.root, text=resultado, font=("Arial 20 bold"), bg="white").place(relx=0.66, rely=0.15, relwidth=0.3, relheight=0.17)
            
            elif tipoEsq == "Polegada":
                if tipoDir == "Milímetro":
                    resultado = numero * 25.4
                elif tipoDir == "Centímetro":
                    resultado = numero * 2.54
                elif tipoDir == "Metro":
                    resultado = numero / 39.37
                elif tipoDir == "Polegada":
                    resultado = numero
                Label(self.root, text=resultado, font=("Arial 20 bold"), bg="white").place(relx=0.66, rely=0.15, relwidth=0.3, relheight=0.17)

    def limpar(self, *args):
        self.tb_entrada.delete(0, END)
        Label(self.root, text=None, font=("Arial 20 bold"), bg="white").place(relx=0.66, rely=0.15, relwidth=0.3, relheight=0.17)

root = Tk()
Tela()