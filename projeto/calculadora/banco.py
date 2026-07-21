# ============================================
# banco.py
# Banco de dados da Calculadora 4.0
# ============================================

import sqlite3
from datetime import datetime



class BancoDados:


    def __init__(self):

        self.conexao = sqlite3.connect(
            "calculadora.db"
        )


        self.criar_tabela()



    # --------------------------------
    # Criar tabela
    # --------------------------------

    def criar_tabela(self):

        cursor = self.conexao.cursor()


        cursor.execute(

            """
            CREATE TABLE IF NOT EXISTS historico(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                expressao TEXT,

                resultado TEXT,

                data TEXT

            )
            """

        )


        self.conexao.commit()



    # --------------------------------
    # Adicionar operação
    # --------------------------------

    def adicionar(
            self,
            expressao,
            resultado
    ):


        cursor = self.conexao.cursor()


        cursor.execute(

            """
            INSERT INTO historico
            (
                expressao,
                resultado,
                data
            )

            VALUES
            (
                ?,
                ?,
                ?
            )

            """,

            (

                expressao,

                resultado,

                datetime.now().strftime(
                    "%d/%m/%Y %H:%M:%S"
                )

            )

        )


        self.conexao.commit()



    # --------------------------------
    # Listar histórico
    # --------------------------------

    def listar(self):

        cursor = self.conexao.cursor()


        cursor.execute(

            """
            SELECT 
            expressao,
            resultado,
            data

            FROM historico

            ORDER BY id DESC

            """

        )


        return cursor.fetchall()



    # --------------------------------
    # Limpar tudo
    # --------------------------------

    def limpar(self):

        cursor = self.conexao.cursor()


        cursor.execute(

            "DELETE FROM historico"

        )


        self.conexao.commit()



    # --------------------------------
    # Excluir item
    # --------------------------------

    def excluir(self,id):

        cursor = self.conexao.cursor()


        cursor.execute(

            """
            DELETE FROM historico
            WHERE id=?

            """,

            (id,)

        )


        self.conexao.commit()



    # --------------------------------
    # Fechar banco
    # --------------------------------

    def fechar(self):

        self.conexao.close()