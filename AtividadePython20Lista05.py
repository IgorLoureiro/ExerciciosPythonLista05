"""
Dados três valores, A, B e C, verifique se eles podem ser os valores de um triângulo e se forem se é um escaleno
equilatéro ou isoceles
"""

print("Digite três numeros para se tornarem o lado de triângulo e descubra se ele é escaleno, equilatéro ou isoceles")

Numero1 = int(input())
Numero2 = int(input())
Numero3 = int(input())

if Numero1 > Numero2 + Numero3 or Numero2 > Numero1 + Numero3 or Numero3 > Numero1 + Numero2:
    print("Um ou mais numeros informados são inválidos por serem muito maiores que os outros dois")

elif Numero1 == Numero2 and Numero2 == Numero3:
    print("Triângulo Equilatero")

elif Numero1 == Numero2 or Numero1 == Numero3 or Numero2 == Numero3:
    print("Triângulo Isóceles")

else:
    print("Triângulo Escaleno")
