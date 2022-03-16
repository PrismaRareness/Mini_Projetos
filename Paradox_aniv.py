import datetime, random



#----------------------------------------- 
# Gerar uma data de aniversário aleatória
#-----------------------------------------
def obter_aniver(num_aniversario):
    """Retorna uma lista de objetos de data aleatória de número para aniversários."""
    aniversarios = []

    for i in range(num_aniversario):
        Inicio_ano = datetime.date(2022, 1, 1)
        Num_aleatorio_dias = datetime.timedelta(random.randint(0, 364))
        aniversario = Inicio_ano + Num_aleatorio_dias
        aniversarios.append(aniversario)
    return aniversarios    

def obter_correspondencia(aniversarios):
    """Retorna o objeto de data de um aniversário 
    que ocorre mais de uma vez na lista de aniversários."""
    
    if len(aniversarios) == len(set(aniversarios)):
        return None
    
    for a_i, aniversario_A in enumerate(aniversarios):
        for b_i, aniversario_B in enumerate(aniversarios[a_i + 1:]): 
            if aniversario_A == aniversario_B:
                return aniversario_A

print("""\n--------------------------------------------------------------------------------                           Paradoxo do Aniversário \n--------------------------------------------------------------------------------\n\nO Paradoxo do Aniversario nos mostra que em um grupo de N pessoas, as chances de que duas delas tenham aniversarios iguais é surpreendentemente grande. Este
programa faz uma simulacao de Monte Carlo (ou seja, simulacoes aleatorias
repetidas) para explorar este conceito.""")            

MESES = ('\nJaneiro', '\nFevereiro', '\nMarco', '\nAbril', '\nMaio', '\nJunho', '\nJulho', '\nAgosto', '\nSetembro', '\nOutubro', '\nNovembro', '\nDezembro')            

while True: 
    print('\nQuantos aniversários voce quer gerar? (Max: 1000)\n')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 1000):
        numDdias = int(response)
        break
print()    


print('Aqui estao', numDdias, 'aniversários:')
aniversarios = obter_aniver(numDdias)
for i, aniversario in enumerate(aniversarios):
    if i != 0:
        print(', ', end='')
    MES_Nome = MESES[aniversario.month - 1]
    dataTexto = '{}, dia {}'.format(MES_Nome, aniversario.day)
    print(dataTexto, end='')
print()
print()

match = obter_correspondencia(aniversarios)


print('Nesta simulacao, ', end='')    
if match != None:
    MES_Nome = MESES[match.month - 1]
    dataTexto = '{} de {}'.format(match.day, MES_Nome)
    print('varias pessoas fazem aniversario em', dataTexto)
else:
     print('nao há aniversarios correspondentes.')
print()

print('Voce quer gerar', numDdias, 'aniversarios aleatorios 100.000 vezes?')
input('Precione Enter para começar ')

print('Vamos fazer mais 100.000 simulacoes.')
simMatch = 0

for i in range(100000):
    if i % 10000 == 0:
        print(i, 'simulacoes')
    aniversarios = obter_aniver(numDdias)
    if obter_correspondencia(aniversarios) != None:
        simMatch = simMatch +1
print('100000 simulacoes...') 
probability = round(simMatch / 100_000 * 100, 2)
print('\nResultado:\n\nDe 100.000 simulacoes de', numDdias, 'pessoas, houve um aniversário correspondente naquele grupo',simMatch, 'vezes.')
print('Isso significa que a correspondencia de aniversários nesse grupo é de ',simMatch, 'vezes.')
print('Isso também mostra que. com', numDdias, 'pessoas, há', probability, '% de chance de existir um aniversário correspondente dentro do grupo. Isso é mais provavel do que você imagina!')
           
            