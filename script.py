import customtkinter as ctk

class Calculadora(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.valor = ""

        self.geometry("400x600")
        self.resizable(False, False)


        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)

        self.display = ctk.CTkLabel(self, text=self.valor, font=("Arial", 24), width=380, height=50, fg_color="gray20")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        botoes = [
            ("7", self.N7), ("8", self.N8), ("9", self.N9), ("/", self.Divisao),
            ("4", self.N4), ("5", self.N5), ("6", self.N6), ("*", self.Multiplica),
            ("1", self.N1), ("2", self.N2), ("3", self.N3), ("-", self.Subtracao),
            ("0", self.N0), ("=", self.Igual), ("+", self.Soma)
        ]

        # Posicionando botões na grade
        row, col = 1, 0
        for text, command in botoes:
            botao = ctk.CTkButton(self, text=text, width=80, height=60, command=command)
            botao.grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col > 3:
                col = 0
                row += 1

    def N7(self):
        self.atualizar_display("7")
    def N8(self):
        self.atualizar_display("8")
    def N9(self):
        self.atualizar_display("9")
    def N4(self):
        self.atualizar_display("4")
    def N5(self):
        self.atualizar_display("5")
    def N6(self):
        self.atualizar_display("6")
    def N1(self):
        self.atualizar_display("1")
    def N2(self):
        self.atualizar_display("2")
    def N3(self):
        self.atualizar_display("3")
    def N0(self):
        self.atualizar_display("0")

    def atualizar_display(self, num):
        self.valor += num
        self.display.configure(text=self.valor)

    def Divisao(self): self.atualizar_display("/")
    def Multiplica(self): self.atualizar_display("*")
    def Subtracao(self): self.atualizar_display("-")
    def Soma(self): self.atualizar_display("+")

    def Igual(self):
        try:
            resultado = eval(self.valor)
            self.display.configure(text=str(resultado))
            self.valor = str(resultado)
        except:
            self.display.configure(text="Erro")
            self.valor = ""

app = Calculadora()
app.mainloop()
