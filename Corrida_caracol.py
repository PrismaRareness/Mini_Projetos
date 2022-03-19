import time, sys
from random import choice, randint


NUM_MAX_CARACOL = 8
COMPRIMENTO_NOME_MAX = 20
LINHA_CHEGADA = 40


print(''' \n--------------------------------------------------------------------------------
                             Corrida de Caracois!
--------------------------------------------------------------------------------
    @> <-- caracol 

''')

while True:
    response = input('\nQuantos caracóis vao correr? (Máx {}) '.format(NUM_MAX_CARACOL))
    if response.isdecimal():
        num_caracois_corrida = int(response)
        if 1 < num_caracois_corrida <= NUM_MAX_CARACOL:
            break
        print('Digite um número entre 1 e ', NUM_MAX_CARACOL)

nomes_caracois = []
for i in range(1, num_caracois_corrida + 1):
    while True:
        nome = input('Digite o nome do caracol #' + str(i) + ': ')
        if len(nome) == 0:
            print('Por favor, digite um nome.')
        elif nome in nomes_caracois:
            print('Escolha um nome que ainda não tenha sido usado.')            
        else:
            break
    nomes_caracois.append(nome)

print('\n' * 40)
print('Partida' + (' ' * (LINHA_CHEGADA - len('Partida')) + 'Chegada'))            
print('|' + (' ' * (LINHA_CHEGADA - len('|')) + '|'))
caracol_progresso = {}

for nome_caracol in nomes_caracois:
    print(nome_caracol[:COMPRIMENTO_NOME_MAX])
    print('@>')
    caracol_progresso[nome_caracol] = 0

time.sleep(1.5)

while True:
    for i in range(randint(1, num_caracois_corrida // 2)):
        random_nome_caracol = choice(nomes_caracois)
        turn = randint(1, 2)
        caracol_progresso[random_nome_caracol] += turn

        if caracol_progresso[random_nome_caracol] == LINHA_CHEGADA:
            print(random_nome_caracol, 'venceu!')
            sys.exit()

    time.sleep(0.5)

    print('\n' * 40)       

    print('Partida' + (' ' * (LINHA_CHEGADA - len('Partida')) + 'Chegada'))
    print('|' + (' ' * (LINHA_CHEGADA - 1) + '|'))

    for nome_caracol in nomes_caracois:
        spaces = caracol_progresso[nome_caracol]
        print((' ' * spaces) + nome_caracol[:COMPRIMENTO_NOME_MAX])
        print('.' * caracol_progresso[nome_caracol] + '@>')