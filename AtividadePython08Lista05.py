"""
Faça um programa que leia 2 notas de um aluno e informe se são validas
"""

Nota = float(input("Informe a primeira nota do aluno \n"))
Nota2 = float(input("Informe a segunda nota do aluno \n"))

if 0 < Nota < 10.1 and 0 < Nota2 < 10.1:
    print("Ambas as notas são validas")


elif (Nota > 10 or Nota < 0) and (Nota2 > 10 or Nota2 < 0):
    print("Ambas as notas são invalidas")

else:

        if 0 < Nota < 10.1:
            print("A primeira nota informada é válida")
        else:
            print("A primeira nota informada é inválida")

        if 0 < Nota2 < 10.1:
            print("A segunda nota informada é valida")
        else:
            print("A segunda nota informada é invalida")






