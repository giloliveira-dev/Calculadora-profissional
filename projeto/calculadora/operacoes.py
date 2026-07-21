# ============================================
# operacoes.py
# Funções matemáticas da calculadora
# ============================================

import math


# -----------------------------
# Operações básicas
# -----------------------------

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError(
            "Não é possível dividir por zero."
        )

    return a / b


# -----------------------------
# Operações extras
# -----------------------------

def porcentagem(valor, porcentagem):
    """
    Calcula uma porcentagem.
    Exemplo:
    10% de 200 = 20
    """
    return (valor * porcentagem) / 100



def potencia(base, expoente):

    # Proteção contra números gigantes
    if abs(expoente) > 100:
        raise OverflowError(
            "Expoente muito grande."
        )

    resultado = base ** expoente

    if math.isinf(resultado):
        raise OverflowError(
            "Resultado muito grande."
        )

    return resultado



def raiz_quadrada(numero):

    if numero < 0:
        raise ValueError(
            "Não existe raiz real de número negativo."
        )

    return math.sqrt(numero)



def fatorial(numero):

    if numero < 0:
        raise ValueError(
            "O número deve ser positivo."
        )

    if numero != int(numero):
        raise ValueError(
            "O fatorial aceita apenas números inteiros."
        )

    return math.factorial(int(numero))


# -----------------------------
# Funções científicas
# -----------------------------

def seno(graus):

    return math.sin(
        math.radians(graus)
    )



def cosseno(graus):

    return math.cos(
        math.radians(graus)
    )



def tangente(graus):

    return math.tan(
        math.radians(graus)
    )



def logaritmo(numero):

    if numero <= 0:
        raise ValueError(
            "O logaritmo precisa de um número maior que zero."
        )

    return math.log10(numero)



def log_natural(numero):

    if numero <= 0:
        raise ValueError(
            "Número inválido para log natural."
        )

    return math.log(numero)



def valor_absoluto(numero):

    return abs(numero)