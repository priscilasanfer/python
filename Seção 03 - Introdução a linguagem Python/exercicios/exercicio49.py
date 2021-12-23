import datetime

inicio = input("Digite a hora de inicio no formato HH:MM:SS= ")
duracao = int(input("Digite a duração do experimento= "))

data = datetime.datetime.strptime(inicio, '%H:%M:%S')
final = data + datetime.timedelta(0, duracao)
horas = final.strftime("%H:%M:%S")
print(f"A experiência irá terminar as: {horas}")

