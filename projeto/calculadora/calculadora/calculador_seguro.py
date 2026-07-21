# ============================================
# calculador_seguro.py
# Interpretador matemático seguro
# ============================================

import ast
import operator


# Operações permitidas

operacoes = {

    ast.Add: operator.add,

    ast.Sub: operator.sub,

    ast.Mult: operator.mul,

    ast.Div: operator.truediv,

    ast.Pow: operator.pow,

    ast.USub: operator.neg

}



def calcular(expressao):

    try:

        arvore = ast.parse(
            expressao,
            mode="eval"
        )


        resultado = avaliar(
            arvore.body
        )


        return resultado



    except ZeroDivisionError:

        raise Exception(
            "Não é possível dividir por zero."
        )



    except Exception:

        raise Exception(
            "Expressão inválida."
        )



def avaliar(no):


    # Números

    if isinstance(
        no,
        ast.Constant
    ):


        if isinstance(
            no.value,
            (int, float)
        ):

            return no.value



    # Operações matemáticas

    elif isinstance(
        no,
        ast.BinOp
    ):


        operador = operacoes.get(
            type(no.op)
        )


        if operador:


            return operador(

                avaliar(no.left),

                avaliar(no.right)

            )



    # Números negativos

    elif isinstance(
        no,
        ast.UnaryOp
    ):


        operador = operacoes.get(
            type(no.op)
        )


        if operador:


            return operador(

                avaliar(no.operand)

            )



    raise Exception(
        "Operação não permitida."
    )