nota1 = float(input("Digita a nota da primeira avaliação: "))
nota2 = float(input("Digita a nota da segunda avaliação: "))
if (nota1 <= 0 or nota1 > 10) or (nota2 <= 0 or nota2 > 10):
    print("Nota invalida")
    exit()
else:
    media = (nota1 + nota2) / 2
    print(f"A média é {media}")
