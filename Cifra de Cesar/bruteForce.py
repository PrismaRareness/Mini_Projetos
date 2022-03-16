print('\nDigite a mensagem da cifra de César:')
mensagem = input(' ')


SIMBOLOS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for chave in range(len(SIMBOLOS)):
    traducao = ''
    
    for simbolo in mensagem:
        if simbolo in SIMBOLOS:
            num = SIMBOLOS.find(simbolo)
            num = num - chave
            if num < 0:
                num = num + len(SIMBOLOS)
            traducao = traducao + SIMBOLOS[num]
    else:
        traducao = traducao + simbolo
 
while True:        
    print('Chave {}: {}'.format(chave, traducao))                        
                
                
