"""
Solicite um numero inteiro, caso positivo, calcule seu logaritmo
"""
import math

Numero = int(input("Informe um numero positivo para receber seu logaritmo \n"))

if Numero < 0:
    print("O número informado é invalido")
else:
    print(f"O logaritmo do numero informado é {math.log1p(Numero): .2f}")
