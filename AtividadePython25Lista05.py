"""
Faça um programa que cálcule raizes de equação de segundo grau
"""

A = int(input("Informe os numeros para serem A, B e C respectivamente \n"))
B = int(input())
C = int(input())

if A == 0:
    print("Não é equação de segundo grau")

else:
    X = B**2 - (4*A*C)

    if X < 0:
        print("Não existe raiz")

    elif X == 0:
        print("raiz única")

    elif X >= 0:
        print(f"Raiz positiva {X}")
        print(f"Raiz negativa {-X}")


