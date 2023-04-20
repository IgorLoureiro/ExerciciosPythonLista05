"""
Usando switch, escreva um programa que leia um numero inteiro entre 1 e 7 e imprima o dia da semana correspondente
ao numero indicado
"""

Numero = int(input("Digite um numero de 1 a 7 para que seja impresso o dia da semana referente a este dia \n"))

match Numero:
    case 1: print("Domingo")
    case 2: print("Segunda")
    case 3: print("Terça")
    case 4: print("Quarta")
    case 5: print("Quinta")
    case 6: print("Sexta")
    case 7: print("Sabado")
    case _: print("Numero invalido")