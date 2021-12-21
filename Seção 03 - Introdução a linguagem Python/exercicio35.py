import math
print("Considerando 'a' e 'b' os catetos de um triangulo")
a, b = input("Digite o cateto 'A' e o cateto 'B': ").split()
hip = math.sqrt(math.pow(float(a), 2) + math.pow(float(b), 2))
print(f"a hipotenusa é: {hip:.2f}")