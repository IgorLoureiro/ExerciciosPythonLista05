Numero = int(input('Informe um numero, caso ele seja positivo, sera retornado sua raiz quadrada: \n'))

if Numero > 0:
    print(f"A raiz quadrada do numero informado é {Numero**(1/2): .2f}")
elif Numero < 0:
    print(f"O numero informado é invalido")

