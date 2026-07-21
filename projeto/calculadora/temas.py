# ============================================
# temas.py
# Controle de aparência da calculadora
# ============================================


class Tema:


    def __init__(self):

        self.modo = "claro"



    # -----------------------------
    # Alternar tema
    # -----------------------------

    def alternar(self):

        if self.modo == "claro":

            self.modo = "escuro"

        else:

            self.modo = "claro"



    # -----------------------------
    # Retornar tema atual
    # -----------------------------

    def atual(self):

        return self.modo



    # -----------------------------
    # Configurações de cores
    # -----------------------------

    def cores(self):


        if self.modo == "escuro":

            return {

                "fundo": "#202020",

                "painel": "#303030",

                "botao": "#505050",

                "botao_operacao": "#0078D7",

                "texto": "#FFFFFF",

                "visor": "#111111",

                "visor_texto": "#00FF00"

            }


        else:

            return {

                "fundo": "#ECECEC",

                "painel": "#FFFFFF",

                "botao": "#DDDDDD",

                "botao_operacao": "#4CAF50",

                "texto": "#000000",

                "visor": "#FFFFFF",

                "visor_texto": "#000000"

            }