import pyperclip



SIMBOLOS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    print('Você deseja (c)riptografar ou (d)escriptografar?')
    response = input(' ').lower()
    if response.startswith('c'):
        mode = 'criptografar'
        break
    elif response.startswith('d'):
        mode = 'descriptografar'
        break
    print('Digite a letra c ou d.')
    
while True:
    Chave_max = len(SIMBOLOS) - 1
    print('Digite a chave (0 a {}) a ser usada'.format(Chave_max))
    response = input(' ').upper()
    if not response.isdecimal():
        continue
    
    elif 0 <= int(response) < len(SIMBOLOS):
        chave = int(response)
        break

print('Digite a mensagem para {}'.format(mode))    
mensagem = input(' ')

#-------------------------------------------------
#A cifra de Cesar só funciona em letras maiúsculas
#-------------------------------------------------

mensagem = mensagem.upper()

traducao = ''

for simbolo in mensagem:
    if simbolo in SIMBOLOS:
        num = SIMBOLOS.find(simbolo)
        if mode == 'criptografar':
            num = num + chave
        elif mode == 'descriptografar':
            num = num - chave
        if num >= len(SIMBOLOS):
            num = num - len(SIMBOLOS)
        elif num < 0:
            num = num + len(SIMBOLOS)
            
        traducao = traducao + SIMBOLOS[num]
    else: 
        traducao = traducao + simbolo    
                                         
print(traducao)
    
try: 
    pyperclip.copy(traducao)
    print('Texto {} completo copiado para a área de transferência.'.format(mode))
except:
    pass    
                                                     