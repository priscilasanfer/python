num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 > num2:
    print(f"O {num1} é maior que o {num2}")
elif num1 < num2:
    print(f"O {num2} é maior que o {num1}")
else:
    print(f"O {num2} é igual ao {num1}")

print(f"e a diferença entre eles é {abs(num1 - num2)}")
