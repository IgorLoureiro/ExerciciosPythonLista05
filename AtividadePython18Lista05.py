"""
Faça um programa que pergunte ao usuario 4 opções de matematica e realize a operação
"""

Operacao = (input("Você deseja realizar qual das operações matématicas? (Escolha entre multiplicação, divisão, "
                     "soma e subtração? \n"))

match Operacao:
    case "multiplicação":
        Num1 = int(input("Informe dois Numeros para serem multiplicados \n"))
        Num2 = int(input(""))
        Num3 = Num1*Num2
        print(Num3)
    case "divisão":
        Num1 = int(input("Informe dois Numeros para serem dividos \n"))
        Num2 = int(input(""))
        Num3 = Num1/Num2
        print(Num3)
    case "soma":
        Num1 = int(input("Informe dois Numeros para serem somados \n"))
        Num2 = int(input(""))
        Num3 = Num1 + Num2
        print(Num3)
    case "subtração":
        Num1 = int(input("Informe dois Numeros para serem subtraidos \n"))
        Num2 = int(input(""))
        Num3 = Num1 - Num2
        print(Num3)
    case _:
        print("Por favor, escolha entre: multiplicação, divisão, soma ou subtração")