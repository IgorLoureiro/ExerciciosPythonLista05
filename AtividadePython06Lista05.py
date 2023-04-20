""""
Escreva um programa que dados dois numeros inteiros, mostre na tela o maior deles e a diferença entre um e outro
"""

Numero = int(input("Escreva o primeiro numero \n"))

Numero2 = int(input("Escreva o segundo numero \n"))

Numeros = []

Numeros.append(Numero)
Numeros.append(Numero2)
Numeros.sort()

print(f"O maior número informado é o {Numeros[1]}, sendo a diferença entre eles {Numeros[1] - Numeros[0]}")





