import math

num = int(input("Digite um numero inteiro: "))

if num < 0:
    print("Numero invalido")
else:
    print(f"{math.log(num)}")