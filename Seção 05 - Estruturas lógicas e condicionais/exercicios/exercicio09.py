sal = float(input("Digite o salário: "))
prest = float(input("Digite o valor da prestação do empréstimo: "))

if prest > (sal * 0.20):
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido")