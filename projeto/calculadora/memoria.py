# ============================================
# memoria.py
# Sistema de memória da calculadora
# ============================================


class Memoria:


    def __init__(self):

        self.valor = 0



    # -----------------------------
    # MC - Memory Clear
    # Limpa a memória
    # -----------------------------

    def limpar(self):

        self.valor = 0



    # -----------------------------
    # MS - Memory Store
    # Salva um valor
    # -----------------------------

    def salvar(self, numero):

        self.valor = numero



    # -----------------------------
    # MR - Memory Recall
    # Recupera valor salvo
    # -----------------------------

    def recuperar(self):

        return self.valor



    # -----------------------------
    # M+
    # Soma valor à memória
    # -----------------------------

    def adicionar(self, numero):

        self.valor += numero



    # -----------------------------
    # M-
    # Subtrai valor da memória
    # -----------------------------

    def subtrair(self, numero):

        self.valor -= numero



    # -----------------------------
    # Verificar memória
    # -----------------------------

    def existe_valor(self):

        return self.valor != 0



    # -----------------------------
    # Exibir memória
    # -----------------------------

    def mostrar(self):

        return self.valor