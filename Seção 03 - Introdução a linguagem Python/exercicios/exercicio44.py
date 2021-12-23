import math

degrau = int(input("Digite a altura desejada do degrau: "))
alt = int(input("Digite a altura desejada da escada: "))

altd = math.ceil(alt / degrau)
print(f"A altura desejada é de: {altd}")