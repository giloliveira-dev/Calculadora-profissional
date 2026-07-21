# ============================================
# historico.py
# Histórico profissional 4.0
# ============================================


from banco import BancoDados



class Historico:


    def __init__(self):

        self.banco = BancoDados()



    def adicionar(self,texto):

        partes = texto.split("=")


        if len(partes) >= 2:

            expressao = partes[0].strip()

            resultado = partes[1].strip()


        else:

            expressao = texto

            resultado = ""



        self.banco.adicionar(

            expressao,

            resultado

        )



    def listar(self):

        dados = self.banco.listar()


        lista = []


        for item in dados:


            lista.append(

                f"{item[0]} = {item[1]}  |  {item[2]}"

            )


        return lista



    def buscar(self,texto):

        dados = self.banco.buscar(texto)


        lista = []


        for item in dados:


            lista.append(

                f"{item[0]} = {item[1]}  |  {item[2]}"

            )


        return lista



    def limpar(self):

        self.banco.limpar()



    def excluir(self,id):

        self.banco.excluir(id)