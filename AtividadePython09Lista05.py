"""
Leia o salário e o valor de um empréstimo, se o valor do impréstimo for maior que 20% do salário, negue-o
"""
Salario = int(input("Qual o seu salário? \n"))
Emprestimo = int(input("Qual o valor do empréstimo? \n"))

if Emprestimo > (Salario/5):
    print("Empréstimo negado")
else:
    print("Empréstimo concedido")