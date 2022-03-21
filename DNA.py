import random, sys, time


PAUSE = 0.1

SEQUENCIA = [
     '       ##', 
     '      #{}-{}#',
     '     #{}---{}#',
     '    #{}-----{}#',
     '   #{}------{}#',
     '   #{}-----{}#',
     '    #{}---{}#',
     '    #{}-{}#',
     '     ##', # 
     '    #{}-{}#',
     '    #{}---{}#',
     '   #{}-----{}#',
     '   #{}------{}#',
     '    #{}------{}#',
     '     #{}-----{}#',
     '      #{}---{}#',
     '       #{}-{}#']

try:
    print('Animaçao de DNA')
    print('Pressione Ctrl-C para sair...')
    time.sleep(2)
    indice_sequencia = 0
    
    while True:
        indice_sequencia = indice_sequencia + 1
        if indice_sequencia== len(SEQUENCIA):
            indice_sequencia = 0
            
        if indice_sequencia == 0 or indice_sequencia == 9:
            print(SEQUENCIA[indice_sequencia])
            continue
        Selecao_aleatoria = random.randint(1, 4)
        if Selecao_aleatoria == 1:
            nucleotideo_esquerdo, nucleotideo_direito = 'A', 'T'
        elif Selecao_aleatoria == 2:
            nucleotideo_esquerdo, nucleotideo_direito = 'T', 'A'
        elif Selecao_aleatoria == 3:
            nucleotideo_esquerdo, nucleotideo_direito = 'C', 'G'
        elif Selecao_aleatoria == 4:
            nucleotideo_esquerdo, nucleotideo_direito = 'G', 'C'
            
        print(SEQUENCIA[indice_sequencia].format(nucleotideo_esquerdo, nucleotideo_direito))
        time.sleep(PAUSE)
        
except KeyboardInterrupt:
    sys.exit()                                                     
