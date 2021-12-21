import math

numR = float(input("Digite um numero real: "))

if numR >= 0:
    rqd = math.sqrt(numR)
    print(f"A raiz quadrada é {rqd}")
else:
    nqd = math.pow(numR, 2)
    print(f"O numero digitado ao quadrado é: {nqd}")