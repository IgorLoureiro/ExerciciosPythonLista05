"""
faça um programa que receba a altura e o sexo de uma pessoa e mostre seu peso ideal
"""

Altura = float(input("Qual a sua altura? \n"))
Sexo = input("Qual seu sexo? \n")

match Sexo:
    case "Masculino":
        Altura = (72.7 * Altura) - 58
        print(f"Seu peso ideal é de {Altura: .2f} KG")
    case "Feminino":
        Altura = (62.1 *Altura) - 44.7
        print(f"Seu peso ideal é {Altura: .2f} KG")
    case _:
        print("Por favor digite se seu sexo é Feminino ou Masculino")