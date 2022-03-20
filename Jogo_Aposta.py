import random, sys
import time


Numero_dados = {1: '1', 2: '2', 3: '3', 
                   4: '4', 5: '5', 6: '6' }

print('''\nNeste jogo de apostas inspirado e adaptado de Cho-Chan, um jogo de dados 
japonês, dois dados sao rolados em um copo de bambu pelo negociante sentado no 
chao. O jogador deve adivinhar se os dados totalizam um número par ou ímpar.''')

purse = random.randint(50, 1000)

while True:
    print(f'\n- Você tem R$ {purse}. Quanto você aposta?')
    while True:
        pot = input('>> ')
        if pot.upper() == 'SAIR':
            print('Obrigado por jogar!')
            sys.exit()
        elif not pot.isdecimal():
            print('Valor inválido.')
        elif int(pot) > purse:
            print('Você nao tem o suficiente para fazer essa aposta.')                
        else:
            pot = int(pot)
            break
        
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
     
    time.sleep(random.randint(0, 2))
    print('\nO negociante gira o copo e você ouve o barulho dos dados...')
    time.sleep(random.randint(1, 2))
    print('O negociante bate o copo no chao, ainda cobrindo-o...')
    print()
    time.sleep(random.randint(1, 2))
    print('     Par ou Impar?')             
    
    while True:
        aposta = input('\nVocê: ').upper()                             
        if aposta != 'PAR' and aposta != 'IMPAR':
            print('Insira "PAR" ou "IMPAR".')
            continue
        else:
            break
        
    print('\nO negociante levanta o copo para revelar:\n')
    print(f'    Dado 1: {dado_1}, Dado 2: {dado_2}')
    print()
    
    lance_par = (dado_1 + dado_2) % 2 == 0
    if lance_par:
        aposta_correta = 'PAR'
    else:
        aposta_correta = 'IMPAR'
        
    jogador_ganhou = aposta == aposta_correta
    taxa_extra = random.randint(1, 100)
    if jogador_ganhou:
        print(f'Você venceu! Você recebeu + R$ {pot}.')   
        purse = purse + pot 
        print('Você recebe um extra de + R$', pot // taxa_extra)    
        purse = purse - (pot // taxa_extra)
    else:
        purse = purse - pot 
        print('Você perdeu!')     
        
    if purse == 0:
        print('Você ficou sem dinheiro!')       
        time.sleep(0.5)
        print('Obrigado por jogar!')
        sys.exit()