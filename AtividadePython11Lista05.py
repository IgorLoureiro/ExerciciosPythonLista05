"""
Escreva um programa que receba um numero maior que zero e devolva a soma de seus algarismos, caso seja zero, informe que
o numero informado é invalido
"""

Numero = int(input("Informe um numero maior que zero para receber a soma de seus algarismos \n"))


if Numero < 0:
    print("O numero informado não corresponde aos padrões solicitados")

elif Numero > 0:

    Numero = str(Numero)

    Numero = list(Numero)

    ListaNumero = [int(n) for n in Numero]

    print(f"A soma dos algarismos do número informado é igual a {sum(ListaNumero)}")