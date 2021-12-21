# print("*** Converter para minusculo ***")
# letra = input("Digite uma letra: ")
# print(f'Valor final: {letra.lower()}')


print("*** Converter para minusculo usando tabela asc ***")
print("Digite uma letra em maisculo:")
letMai = input()
ordAsciiMa = ord(letMai)

ordAsciiMi = ord(letMai) + 32
LetMi = chr(ordAsciiMi)

print(f"A letra em misculo é: {LetMi}")
