import sys


print('''\nA sequência de Fibonacci começa com 0 e 1, e o próximo número é a soma dos dois números anteriores. A sequência continua para sempre: 0, 1, 1, 2, 3, 5, 8, 13, 
21, 34, 55, 89, 144, 233, 377, 610, 987...''')

while True:
    while True:
        response = input('\nEscolha o enésimo número de Fibonacci: ').upper()
        
        if response == 'SAIR':
            print('Obrigado por jogar!')
            sys.exit()
            
        if response.isdecimal() and int(response) != 0:
            nth = int(response)         
            break
    
        print('Insira um número maior que 0')
    print()

    if nth == 1:
        print('0')
        print()
        print('O #1 número de Fibonacci é 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('O #2 número de Fibonnaci é 1.')
        continue

    if nth >= 10000:
        print('AVISO: Isso levará algum tempo para ser exibido na tela')      
        input('Pressione ENTER para começar...')
    
    penultimo_numero = 0
    ultimo_numero = 1
    num_calculado = 2
    print('0, 1, ', end='')
    
    
    while True:
        proximo_numero = penultimo_numero + ultimo_numero
        num_calculado += 1
        
        print(proximo_numero, end='')                
        
        if num_calculado == nth:
            print()
            print()
            print('O #', num_calculado, ' Fibonacci ', 'numero é ', proximo_numero, sep='')
            break
        
        print(', ', end='')
        
        penultimo_numero = ultimo_numero
        ultimo_numero = proximo_numero