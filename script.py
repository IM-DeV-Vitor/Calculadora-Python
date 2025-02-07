import customtkinter as ctk

class Calculadora(ctk.CTk): #Classe principal
    def __init__(self): #Função de inicialização
        super().__init__()

        self.valor = ""

        self.geometry("400x600")
        self.resizable(False, False)


        for i in range(4): #Este looping centraliza as linhas e colunas
            self.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)

        self.display = ctk.CTkLabel(self, text=self.valor, font=("Arial", 24), width=380, height=50, fg_color="gray20")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        botoes = [ #Lista dos botões clicáveis
            ("7", self.N7), ("8", self.N8), ("9", self.N9), ("/", self.Divisao),
            ("4", self.N4), ("5", self.N5), ("6", self.N6), ("*", self.Multiplica),
            ("1", self.N1), ("2", self.N2), ("3", self.N3), ("-", self.Subtracao),
            ("0", self.N0), ("=", self.Igual), ("+", self.Soma)
        ]

        row, col = 1, 0
        for text, command in botoes:
            botao = ctk.CTkButton(self, text=text, width=80, height=60, command=command)
            botao.grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col > 3:
                col = 0
                row += 1

    def N7(self): #Função que representa o Número 7
        self.atualizar_display("7")
    def N8(self): #Função que representa o Número 8
        self.atualizar_display("8")
    def N9(self): #Função que representa o Número 9
        self.atualizar_display("9")
    def N4(self): #Função que representa o Número 4
        self.atualizar_display("4")
    def N5(self): #Função que representa o Número 5
        self.atualizar_display("5")
    def N6(self): #Função que representa o Número 6
        self.atualizar_display("6")
    def N1(self): #Função que representa o Número 1
        self.atualizar_display("1")
    def N2(self): #Função que representa o Número 2
        self.atualizar_display("2")
    def N3(self): #Função que representa o Número 3
        self.atualizar_display("3")
    def N0(self): #Função que representa o Número 0
        self.atualizar_display("0")

    def atualizar_display(self, num): #Função responsável pelos aparecimentos dos numeros no display
        self.valor += num
        self.display.configure(text=self.valor)

    def Divisao(self): self.atualizar_display("/")  #Função que torna possível a escolha da operação Divisão
    def Multiplica(self): self.atualizar_display("*") #Função que torna possível a escolha da operação Multiplicação
    def Subtracao(self): self.atualizar_display("-") #Função que torna possível a escolha da operação Subtração
    def Soma(self): self.atualizar_display("+") #Função que torna possível a escolha da operação Soma

    def Igual(self): #Função que verifica se há erros
        try: #Verifica se a operação é possível
            resultado = eval(self.valor)
            self.display.configure(text=str(resultado))
            self.valor = str(resultado)
        except:
            self.display.configure(text="Erro")
            self.valor = ""

app = Calculadora()
app.mainloop()
