import sys
import time



print('''
A sequência Collatz é uma sequência de números produzida a partir de um número 
inicial n, seguindo três regras:
1) Se n for par, o próximo número n será n/2;
2) Se n é ímpar, o próximo número n é n * 3 + 1;
3) Se n for 1, pare. Caso contrário, repita.

Pensa-se geralmente, mas até agora nao provado matematicamente, quando aplicado a esta regra, eventualmente sempre chegará a 4, que se converte em 2 e termina em 1.
''')

response = input('Digite um número inicial (maior que 0): ')

if not response.isdecimal() or response == '0':
    print("Você deve inserir um número inteiro maior que 0.")
    sys.exit()

n = int(response)
print(n, end='', flush=True)
while n != 1:
    if n % 2 == 0: 
        n = n // 2
    else: 
        n = 3 * n + 1

    print(', ' + str(n), end='', flush=True)
    time.sleep(0.1)
print()    
