# Calculadora Profissional 4.0

## Descrição

Projeto de uma calculadora desktop desenvolvida em Python utilizando a biblioteca Tkinter.

O objetivo do projeto é criar uma aplicação gráfica completa, organizada e segura, com funcionalidades semelhantes às encontradas em calculadoras científicas modernas.

---

# Tecnologias utilizadas

* Python 3.13
* Tkinter (interface gráfica)
* Programação orientada a objetos
* Abstract Syntax Tree (AST) para cálculo seguro
* Arquitetura modular

---

# Funcionalidades

## Operações básicas

A calculadora possui suporte para:

* Soma (+)
* Subtração (-)
* Multiplicação (×)
* Divisão (÷)

Com tratamento de:

* Valores inválidos
* Expressões incorretas
* Divisão por zero

---

# Sistema de cálculo seguro

Foi removido o uso direto do `eval()`.

A versão profissional utiliza um interpretador próprio baseado em:

```
ast (Abstract Syntax Tree)
```

permitindo somente operações matemáticas autorizadas.

Operações aceitas:

* Adição
* Subtração
* Multiplicação
* Divisão
* Potenciação
* Números negativos

Benefícios:

* Maior segurança
* Controle das operações permitidas
* Redução de riscos de execução de comandos externos

---

# Funções científicas

A calculadora possui recursos avançados:

## Potenciação

Exemplo:

```
2² = 4
```

Permite informar diferentes expoentes.

---

## Raiz quadrada

Exemplo:

```
√25 = 5
```

---

## Cubo

Exemplo:

```
3³ = 27
```

---

## Porcentagem

Exemplo:

```
50%
= 0.5
```

---

## Funções trigonométricas

Disponível:

* seno
* cosseno
* tangente

---

## Logaritmo

Suporte para cálculos logarítmicos.

---

## Fatorial

Exemplo:

```
5!
= 120
```

---

# Sistema de memória

A calculadora possui memória semelhante às calculadoras físicas.

Funções:

## MC

Limpar memória.

## MR

Recuperar valor armazenado.

## MS

Salvar valor atual.

## M+

Adicionar valor à memória.

## M-

Subtrair valor da memória.

---

# Sistema de histórico

A aplicação mantém registro das operações realizadas.

Recursos:

* Visualização das operações
* Pesquisa no histórico
* Recuperação de expressões antigas
* Limpeza do histórico
* Exportação para CSV

Exemplo:

```
10+5 = 15
25*4 = 100
```

---

# Exportação de dados

O histórico pode ser exportado para arquivo:

```
historico.csv
```

Formato compatível com:

* Microsoft Excel
* Google Planilhas
* Editores de texto

---

# Interface gráfica

A interface possui:

* Janela personalizada
* Dois visores:

  * Expressão digitada
  * Resultado
* Teclado numérico
* Botões científicos
* Área de memória
* Área de histórico

---

# Atalhos de teclado

## ENTER

Executa o cálculo.

## BACKSPACE

Apaga o último caractere.

## ESC

Limpa os campos.

---

# Sistema de temas

Possui suporte para alteração visual da aplicação.

Recursos:

* Alternância de tema
* Estrutura preparada para novos estilos

---

# Estrutura do projeto

```
calculadora/

│
├── main.py
│   Arquivo responsável por iniciar o programa
│
├── interface.py
│   Interface gráfica e controle da aplicação
│
├── calculador_seguro.py
│   Interpretador matemático seguro
│
├── operacoes.py
│   Funções matemáticas
│
├── historico.py
│   Gerenciamento do histórico
│
├── memoria.py
│   Sistema de memória
│
├── temas.py
│   Controle visual dos temas
│
└── README.md
    Documentação do projeto
```

---

# Como executar

Instale o Python 3.13.

Abra o terminal na pasta do projeto:

```bash
cd caminho/da/calculadora
```

Execute:

```bash
python main.py
```

---

# Tratamento de erros

O sistema possui tratamento para:

* Divisão por zero
* Entrada inválida
* Operações não permitidas
* Resultados matemáticos inválidos
* Erros de conversão

---

# Conceitos aplicados

Durante o desenvolvimento foram utilizados:

* Classes e objetos
* Modularização
* Separação de responsabilidades
* Interfaces gráficas
* Tratamento de exceções
* Manipulação de arquivos
* Estruturas de dados

---

# Histórico de versões

## Versão 1.0

Calculadora básica:

* Operações fundamentais
* Interface Tkinter simples

---

## Versão 2.0

Adicionado:

* Funções científicas
* Memória
* Histórico
* Temas

---

## Versão 3.0

Melhorias:

* Remoção do eval()
* Cálculo seguro
* Visor duplo
* Copiar resultado

---

## Versão 4.0

Atual:

* Menu superior
* Exportação CSV
* Pesquisa de histórico
* Recuperação de cálculos
* Interface profissional

---

# Possíveis melhorias futuras

Versões futuras podem incluir:

* Banco de dados SQLite
* Gráficos matemáticos
* Conversor de unidades
* Conversor de moedas
* Histórico permanente
* Instalador Windows (.exe)
* Ícone personalizado
* Atualização automática

---

# Autor

Projeto desenvolvido para estudo e prática de:

* Python
* Tkinter
* Desenvolvimento de aplicações desktop
