Numero = int(input("Informe um numero maior que zero para receber a soma de seus digitos \n"))

if Numero <= 0:
    print("O numero informado se encontra fora dos padrões solicitados")

else:
    soma = 0
    while Numero != 0:

        Num = Numero % 10
        Numero = Numero // 10
        soma = soma + Num

    print(f"Resultado {soma}")