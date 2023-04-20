print("Escreva três numeros para recebelos em ordem crescente")

Numero1 = int(input())
Numero2 = int(input())
Numero3 = int(input())

Lista = []

Lista.append(Numero1)
Lista.append(Numero2)
Lista.append(Numero3)

Lista.sort()

print(Lista[::-1])

