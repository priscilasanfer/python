import math

val1, val2, val3 = input("Digite tres valores reais= ").split()
qv1 = math.pow(float(val1), 2)
qv2 = math.pow(float(val2), 2)
qv3 = math.pow(float(val3), 2)
soma = qv1 + qv2 + qv3
print(f"A soma do quadrado dos 3 valores é: {soma}")