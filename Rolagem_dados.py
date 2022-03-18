from random import randint
import time

faces = int(input('''\n- Digite o número de faces do dado: '''))
numero_dados = int(input('''- Digite quantos dados de {} faces você quer jogar: '''.format(faces)))

resultados = {}
for i in range(numero_dados, (numero_dados * faces) + 1):
    resultados[i] = 0

print('>> Simulando 1.000.000 jogadas de {} dados... \n'.format(numero_dados)) 
LastPrintTime = time.time()
for i in range(1000000):
    if time.time()  > LastPrintTime + 1:
        print('{}%...'.format(round(i / 10000, 1)))
        LastPrintTime = time.time()

    total = 0
    for j in range(numero_dados):
        total = total + randint(1, faces)
    resultados[total] = resultados[total] + 1        

print('\n  Face/Total - Roladas - Porcentagem\n')
for i in range(numero_dados, (numero_dados * faces) + 1):
    roll = resultados[i] 
    percentagem = round(resultados[i] / 10000, 1)
    print('  {} - {} roladas - {}%'.format(i, roll, percentagem))   