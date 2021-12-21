num = int(input("Digite um numero \n"))
num1 = str(num)
soma = 0
if num > 0:
    for index in range(len(num1)):
        soma += int(num1[index])
    print(soma)
else:
    print("Numero invalido")
