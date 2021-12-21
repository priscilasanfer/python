print("*** Imprimir a soma com antecessor do seu dobro com sucessor do seu triplo ***")
numero = int((input("Digite um numero: ")))
triplo = numero * 3
dobro = numero * 2
resultado = (triplo + 1) + (dobro - 1)
print(f'Valor final: {resultado}')
