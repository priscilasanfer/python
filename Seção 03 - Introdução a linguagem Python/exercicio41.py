ht = float(input("Digite o valor da hora de trabalho em reais, incluindo os centavos: "))
hm = int(input("Digite o numero de horas trabalhadas no mês: "))
sal = (ht * hm) * 1.10
print(f"O valor é de {sal:.2f}")