"""
Escreva um programa que leia o código do produto escolhido no cardápio de uma lanchonete e a quantidade.
O programa deve cálcular o valor a ser pago por aquele lanche. Considere que a cada execução somente sera cálculado
um pedido.

Objeto/Código/Preço

Cachorro quente/100/1.20
Bauru/101/1.30
Bauru com ovo/102/1.50
Hamburguer/103/1.20
Cheseeburguer/104/1.70
Suco/105/2.20
Refrigerante/106/1.00
"""
Resposta = ''
Preco = []
Pedidos = []

while Resposta != 'não':
    print("Insira o código do que deseja comer ou digite Sair para Sair \n")
    Resposta = input()
    if Resposta == 'Sair':
        break
    print("Qual a quantidade do que deseja comer? \n")
    Numero = int(input())
    Pedidos.append(Resposta)
    Pedidos.append(Numero)
    if Resposta == '100':
        Valor = Numero * 1.20
        Preco.append(Valor)
    elif Resposta == '101':
        Valor = Numero * 1.30
        Preco.append(Valor)
    elif Resposta == '102':
        Valor = Numero * 1.50
        Preco.append(Valor)
    elif Resposta == '103':
        Valor = Numero * 1.20
        Preco.append(Valor)
    elif Resposta == '104':
        Valor = Numero * 1.70
        Preco.append(Valor)
    elif Resposta == '105':
        Valor = Numero * 2.20
        Preco.append(Valor)
    elif Resposta == '106':
        Valor = Numero * 1.00
        Preco.append(Valor)

print(Preco)
print(Pedidos)
print(f"O preço total dos seus pedidos foram de R${sum(Preco): .2f}")

