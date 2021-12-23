import math

alt = float(input("Digite a altura do cilindro: "))
rai = float(input("Digite o raio do cilindro: "))
vol = math.pi * math.pow(rai, 2) * alt

print(f"O volume é: {vol:.2f}")