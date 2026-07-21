# ============================================
# interface.py
# Calculadora Profissional 4.0
# Parte 1/3
# ============================================


import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv


from operacoes import (
    raiz_quadrada,
    fatorial,
    seno,
    cosseno,
    tangente,
    logaritmo,
    potencia as calcular_potencia
)


from historico import Historico
from memoria import Memoria
from temas import Tema

from calculador_seguro import calcular



class Calculadora:


    def __init__(self):

        self.janela = tk.Tk()


        self.janela.title(
            "Calculadora Profissional 4.0"
        )


        self.janela.geometry(
            "520x850"
        )


        self.janela.resizable(
            False,
            False
        )


        # -----------------------------
        # Módulos
        # -----------------------------

        self.historico = Historico()

        self.memoria = Memoria()

        self.tema = Tema()



        # -----------------------------
        # Estilo
        # -----------------------------

        self.estilo = ttk.Style()

        self.estilo.theme_use(
            "clam"
        )



        # Criar componentes

        self.criar_menu()

        self.criar_interface()


        self.aplicar_tema()



        # -----------------------------
        # Atalhos
        # -----------------------------

        self.janela.bind(

            "<Return>",

            lambda evento:
            self.calcular_resultado()

        )


        self.janela.bind(

            "<BackSpace>",

            lambda evento:
            self.apagar()

        )


        self.janela.bind(

            "<Escape>",

            lambda evento:
            self.limpar()

        )



    # ========================================
    # MENU
    # ========================================


    def criar_menu(self):


        barra = tk.Menu(
            self.janela
        )


        arquivo = tk.Menu(
            barra,
            tearoff=0
        )


        arquivo.add_command(

            label="Exportar Histórico",

            command=self.exportar_csv

        )


        arquivo.add_command(

            label="Limpar Histórico",

            command=self.limpar_historico

        )


        arquivo.add_separator()



        arquivo.add_command(

            label="Sair",

            command=self.janela.destroy

        )



        barra.add_cascade(

            label="Arquivo",

            menu=arquivo

        )



        opcoes = tk.Menu(

            barra,

            tearoff=0

        )


        opcoes.add_command(

            label="Alternar Tema",

            command=self.alternar_tema

        )



        barra.add_cascade(

            label="Opções",

            menu=opcoes

        )



        ajuda = tk.Menu(

            barra,

            tearoff=0

        )


        ajuda.add_command(

            label="Sobre",

            command=self.sobre

        )


        barra.add_cascade(

            label="Ajuda",

            menu=ajuda

        )


        self.janela.config(

            menu=barra

        )



    # ========================================
    # INTERFACE PRINCIPAL
    # ========================================


    def criar_interface(self):


        visor_frame = ttk.Frame(

            self.janela

        )


        visor_frame.pack(

            pady=15

        )



        ttk.Label(

            visor_frame,

            text="Expressão"

        ).pack(

            anchor="w"

        )



        self.expressao = ttk.Entry(

            visor_frame,

            font=(

                "Segoe UI",

                16

            ),

            justify="right",

            width=32

        )


        self.expressao.pack()



        ttk.Label(

            visor_frame,

            text="Resultado"

        ).pack(

            anchor="w",

            pady=(10,0)

        )



        self.visor = ttk.Entry(

            visor_frame,

            font=(

                "Segoe UI",

                26

            ),

            justify="right",

            width=25

        )


        self.visor.pack()



        # Memória

        self.memoria_label = ttk.Label(

            self.janela,

            text="Memória: 0"

        )


        self.memoria_label.pack()



        # Teclado

        teclado = ttk.Frame(

            self.janela

        )


        teclado.pack(

            pady=10

        )



        botoes = [

            ("7","7"),
            ("8","8"),
            ("9","9"),
            ("÷","/"),

            ("4","4"),
            ("5","5"),
            ("6","6"),
            ("×","*"),

            ("1","1"),
            ("2","2"),
            ("3","3"),
            ("−","-"),

            ("0","0"),
            (".","."),
            ("=","="),
            ("+","+")

        ]



        linha = 0

        coluna = 0



        for texto,valor in botoes:


            ttk.Button(

                teclado,

                text=texto,

                width=8,

                command=lambda v=valor:

                self.entrada(v)

            ).grid(

                row=linha,

                column=coluna,

                padx=4,

                pady=4,

                ipadx=5,

                ipady=8

            )



            coluna += 1


            if coluna == 4:

                coluna = 0

                linha += 1



        self.teclado = teclado
            # ========================================
    # Parte 2/3
    # Científica, memória e histórico
    # ========================================



        # -----------------------------
        # Funções científicas
        # -----------------------------


        cientifica = ttk.LabelFrame(

            self.janela,

            text="Funções Científicas"

        )


        cientifica.pack(

            pady=10

        )



        botoes_cientificos = [


            ("√", self.raiz),

            ("x²", self.quadrado),

            ("x³", self.cubo),

            ("xʸ", self.potencia),

            ("%", self.porcentagem),

            ("sin", self.func_seno),

            ("cos", self.func_cosseno),

            ("tan", self.func_tangente),

            ("log", self.func_log),

            ("n!", self.func_fatorial)

        ]



        linha = 0

        coluna = 0



        for texto, comando in botoes_cientificos:


            ttk.Button(

                cientifica,

                text=texto,

                width=7,

                command=comando

            ).grid(

                row=linha,

                column=coluna,

                padx=3,

                pady=3

            )



            coluna += 1



            if coluna == 5:

                coluna = 0

                linha += 1





        # -----------------------------
        # Memória
        # -----------------------------


        memoria_frame = ttk.LabelFrame(

            self.janela,

            text="Memória"

        )


        memoria_frame.pack(

            pady=5

        )



        botoes_memoria = [


            ("MC", self.memoria_limpar),

            ("MR", self.memoria_recuperar),

            ("MS", self.memoria_salvar),

            ("M+", self.memoria_adicionar),

            ("M-", self.memoria_subtrair)

        ]



        for texto, comando in botoes_memoria:


            ttk.Button(

                memoria_frame,

                text=texto,

                width=7,

                command=comando

            ).pack(

                side="left",

                padx=3

            )





        # -----------------------------
        # Controles
        # -----------------------------


        controle = ttk.Frame(

            self.janela

        )


        controle.pack(

            pady=5

        )



        ttk.Button(

            controle,

            text="C",

            width=8,

            command=self.limpar

        ).grid(

            row=0,

            column=0,

            padx=3

        )



        ttk.Button(

            controle,

            text="⌫",

            width=8,

            command=self.apagar

        ).grid(

            row=0,

            column=1,

            padx=3

        )



        ttk.Button(

            controle,

            text="Copiar",

            width=8,

            command=self.copiar_resultado

        ).grid(

            row=0,

            column=2,

            padx=3

        )



        ttk.Button(

            controle,

            text="Tema",

            width=8,

            command=self.alternar_tema

        ).grid(

            row=0,

            column=3,

            padx=3

        )





        # -----------------------------
        # Histórico profissional
        # -----------------------------


        historico_frame = ttk.LabelFrame(

            self.janela,

            text="Histórico"

        )


        historico_frame.pack(

            pady=10

        )



        pesquisa_frame = ttk.Frame(

            historico_frame

        )


        pesquisa_frame.pack(

            pady=5

        )



        self.pesquisa = ttk.Entry(

            pesquisa_frame,

            width=30

        )


        self.pesquisa.pack(

            side="left",

            padx=5

        )



        ttk.Button(

            pesquisa_frame,

            text="Buscar",

            command=self.buscar_historico

        ).pack(

            side="left"

        )



        self.lista_historico = tk.Listbox(

            historico_frame,

            width=65,

            height=10

        )


        self.lista_historico.pack(

            pady=5

        )



        self.lista_historico.bind(

            "<Double-Button-1>",

            self.recuperar_historico

        )



        botoes_hist = ttk.Frame(

            historico_frame

        )


        botoes_hist.pack()



        ttk.Button(

            botoes_hist,

            text="Excluir Selecionado",

            command=self.excluir_historico

        ).grid(

            row=0,

            column=0,

            padx=5

        )



        ttk.Button(

            botoes_hist,

            text="Limpar Tudo",

            command=self.limpar_historico

        ).grid(

            row=0,

            column=1,

            padx=5

        )



        self.atualizar_historico()
        # ========================================
# Parte 3/3
# Funções, banco, controle e execução
# ========================================


    # -----------------------------
    # Entrada
    # -----------------------------

    def entrada(self, valor):

        if valor == "=":

            self.calcular_resultado()

        else:

            self.expressao.insert(

                tk.END,

                valor

            )



    # -----------------------------
    # Cálculo seguro
    # -----------------------------

    def calcular_resultado(self):

        try:

            texto = self.expressao.get()


            resultado = calcular(

                texto

            )


            self.visor.delete(

                0,

                tk.END

            )


            self.visor.insert(

                tk.END,

                resultado

            )


            self.historico.adicionar(

                f"{texto} = {resultado}"

            )


            self.atualizar_historico()



        except Exception as erro:

            messagebox.showerror(

                "Erro",

                str(erro)

            )



    # -----------------------------
    # Funções auxiliares
    # -----------------------------

    def obter_numero(self):

        return float(

            self.visor.get()

        )



    def mostrar(self, valor):

        self.visor.delete(

            0,

            tk.END

        )


        self.visor.insert(

            tk.END,

            valor

        )



    def aplicar_funcao(self, funcao):

        try:

            numero = self.obter_numero()


            resultado = funcao(

                numero

            )


            self.mostrar(

                resultado

            )


            self.historico.adicionar(

                f"{funcao.__name__}({numero}) = {resultado}"

            )


            self.atualizar_historico()



        except Exception as erro:

            messagebox.showerror(

                "Erro",

                str(erro)

            )



    # -----------------------------
    # Científica
    # -----------------------------

    def raiz(self):

        self.aplicar_funcao(

            raiz_quadrada

        )



    def quadrado(self):

        self.aplicar_funcao(

            lambda x:

            calcular_potencia(x,2)

        )



    def cubo(self):

        self.aplicar_funcao(

            lambda x:

            calcular_potencia(x,3)

        )



    def potencia(self):

        try:

            base = self.obter_numero()


            janela = tk.Toplevel(

                self.janela

            )


            janela.title(

                "Potenciação"

            )


            janela.geometry(

                "250x150"

            )


            ttk.Label(

                janela,

                text="Expoente:"

            ).pack(

                pady=10

            )


            campo = ttk.Entry(

                janela

            )


            campo.pack()



            def executar():

                try:

                    expoente = float(

                        campo.get()

                    )


                    resultado = calcular_potencia(

                        base,

                        expoente

                    )


                    self.mostrar(

                        resultado

                    )


                    self.historico.adicionar(

                        f"{base}^{expoente} = {resultado}"

                    )


                    self.atualizar_historico()


                    janela.destroy()



                except Exception as erro:

                    messagebox.showerror(

                        "Erro",

                        str(erro)

                    )



            ttk.Button(

                janela,

                text="Calcular",

                command=executar

            ).pack(

                pady=10

            )


        except Exception as erro:

            messagebox.showerror(

                "Erro",

                str(erro)

            )



    def porcentagem(self):

        self.aplicar_funcao(

            lambda x: x / 100

        )



    def func_seno(self):

        self.aplicar_funcao(seno)



    def func_cosseno(self):

        self.aplicar_funcao(cosseno)



    def func_tangente(self):

        self.aplicar_funcao(tangente)



    def func_log(self):

        self.aplicar_funcao(logaritmo)



    def func_fatorial(self):

        self.aplicar_funcao(fatorial)



    # -----------------------------
    # Memória
    # -----------------------------

    def memoria_limpar(self):

        self.memoria.limpar()

        self.atualizar_memoria()



    def memoria_salvar(self):

        try:

            self.memoria.salvar(

                self.obter_numero()

            )

            self.atualizar_memoria()

        except:

            pass



    def memoria_recuperar(self):

        self.mostrar(

            self.memoria.recuperar()

        )



    def memoria_adicionar(self):

        try:

            self.memoria.adicionar(

                self.obter_numero()

            )

            self.atualizar_memoria()

        except:

            pass



    def memoria_subtrair(self):

        try:

            self.memoria.subtrair(

                self.obter_numero()

            )

            self.atualizar_memoria()

        except:

            pass



    def atualizar_memoria(self):

        self.memoria_label.config(

            text=f"Memória: {self.memoria.mostrar()}"

        )



    # -----------------------------
    # Histórico
    # -----------------------------

    def atualizar_historico(self):

        self.lista_historico.delete(

            0,

            tk.END

        )


        for item in self.historico.listar():

            self.lista_historico.insert(

                tk.END,

                item

            )



    def buscar_historico(self):

        texto = self.pesquisa.get()


        self.lista_historico.delete(

            0,

            tk.END

        )


        for item in self.historico.buscar(texto):

            self.lista_historico.insert(

                tk.END,

                item

            )



    def recuperar_historico(self,event):

        selecionado = self.lista_historico.curselection()


        if selecionado:

            texto = self.lista_historico.get(

                selecionado[0]

            )


            expressao = texto.split("=")[0]


            self.expressao.delete(

                0,

                tk.END

            )


            self.expressao.insert(

                tk.END,

                expressao.strip()

            )



    def excluir_historico(self):

        selecionado = self.lista_historico.curselection()


        if selecionado:

            self.lista_historico.delete(

                selecionado[0]

            )



    def limpar_historico(self):

        self.historico.limpar()

        self.atualizar_historico()



    # -----------------------------
    # Controle
    # -----------------------------

    def limpar(self):

        self.expressao.delete(

            0,

            tk.END

        )


        self.visor.delete(

            0,

            tk.END

        )



    def apagar(self):

        texto = self.expressao.get()


        self.expressao.delete(

            0,

            tk.END

        )


        self.expressao.insert(

            tk.END,

            texto[:-1]

        )



    def copiar_resultado(self):

        self.janela.clipboard_clear()

        self.janela.clipboard_append(

            self.visor.get()

        )



    # -----------------------------
    # Exportação
    # -----------------------------

    def exportar_csv(self):

        arquivo = filedialog.asksaveasfilename(

            defaultextension=".csv",

            filetypes=[

                ("CSV","*.csv")

            ]

        )


        if arquivo:

            with open(

                arquivo,

                "w",

                newline="",

                encoding="utf-8"

            ) as f:


                escritor = csv.writer(f)


                escritor.writerow(

                    ["Histórico"]

                )


                for item in self.historico.listar():

                    escritor.writerow(

                        [item]

                    )



            messagebox.showinfo(

                "Sucesso",

                "Arquivo exportado."

            )



    # -----------------------------
    # Tema
    # -----------------------------

    def alternar_tema(self):

        self.tema.alternar()

        self.aplicar_tema()



    def aplicar_tema(self):

        cores = self.tema.cores()


        self.janela.configure(

            bg=cores["fundo"]

        )



    def sobre(self):

        messagebox.showinfo(

            "Sobre",

            "Calculadora Profissional 4.0\nPython + Tkinter + SQLite"

        )



    # -----------------------------
    # Executar
    # -----------------------------

    def executar(self):

        self.janela.mainloop()