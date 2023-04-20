import math

print("Informe o horario de chegada ao parque (Primeiro as horas e após os minutos) \n")
CheHor = int(input())
CheMin = int(input())

print("Informe o horario de saida do parque (Primeiro as horas e após os minutos) \n")
SaiHor = int(input())
SaiMin = int(input())

TempoChe = ((CheHor * 60) + CheMin)/60
TempoSai = ((SaiHor * 60) + CheMin)/60
TempoCar = math.ceil(TempoSai - TempoChe)
print(TempoCar)


if TempoCar <= 2:
    Valor = TempoCar * 1
    print(f"O valor a ser pago por estacionar por {TempoCar} horas é de R${Valor: .2f}")

elif 5 > TempoCar > 2:
    Valor = TempoCar * 1.40
    print(f"O valor a ser pago por estacionar por {TempoCar} horas é de R${Valor: .2f}")

elif TempoCar > 5:
    Valor = TempoCar * 2
    print(f"O valor a ser pago por estacionar por {TempoCar} horas é de R${Valor: .2f}")