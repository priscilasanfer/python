
num = int(input("Digite um numero de 1000 a 9999: "))

while num < 1000 or num > 9999:
    num = int(input("Digite um numero de 1000 a 9999: "))

num = str(num)
for index in range(len(num)):
    print(f"{num[index]}")



