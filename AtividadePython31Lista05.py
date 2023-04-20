print("Informe seu peso e sua altura para receber sua letra na lista")

Peso = int(input())
Altura = float(input())

if Altura < 1.20 and Peso < 60:
    print("A")

elif 1.70 >= Altura >= 1.20 and Peso < 60:
    print("B")

elif Altura > 1.70 and Peso < 60:
    print("C")

elif Altura < 1.20 and 90 >= Peso >= 60:
    print("D")

elif 1.70 >= Altura >= 1.20 and 90 >= Peso >= 60:
    print("E")

elif Altura > 1.70 and 90 >= Peso >= 60:
    print("F")

elif Altura < 1.20 and Peso > 90:
    print("G")

elif 1.70 >= Altura >= 1.20 and Peso > 90:
    print("H")

elif Altura > 1.70 and Peso > 90:
    print("I")


