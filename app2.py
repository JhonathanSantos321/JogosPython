#python
# Importa o Modulo random para seleçao aleatoria de palavra
import random

# Lista de palavras para o jogo (banco de palavras)
palavra = ['maçã', 'banana', 'laranja', 'uva', 'morango']
           
def jogo_da_forca():
       """
    Funçao principal que gerencia  toda a logica o jogo de forca:
    - seleçao da palavra
    - Controle de tentativas
    - Validaçao das Letras
    - Exibiçao do estado do jogo_da_forca
       """



    # Seleciona aleatoriamente uma palavra da lista
    palavra_secreta = random.choice(palavras)
    
    # Lista para armazenar as letras descobertas (inicialmente todas ocultas)
    letras_corretas = ['_'] * len(palavra_secreta)
    
    # Lista para registrar letras incorretas digitadas
    letras_erradas = []
    
    # Define o número máximo de tentativas permitidas
    tentativas_restantes = 6

    # Mensagem inicial do jogo
    print("\nBem-vindo ao jogo da forca!")
    print(f"Voce tem {tentativas_restantes} tentativas para adivinhar a palavra.\n")

    # Loop principal do jogo: continua enquanto houver tentativas para adivinhar e letras faltando
    while tentativas_restantes > 0 and '_' in letras_corretas:
        # Exibe o progresso atual do jogador
        print(' '.join(letras_corretas))

        # Solicita e processa a tentativa do jogador
        tentativa = input("\nDigite uma letra: ").lower() # Converte para minuscula

        # Verifica se a letra se a letra esta na palavra secreta
        if tentativa in palavra_secreta
            # Atualiza as letra corretas reveladas
            for indice, letra in enumerate(palavra_secreta):
                if letra == tentativa:
                    letras_corretas[indice] = tentativa

        else:
            # trata letra incorreta
            letras_erradas.append(tentativa)  # Registra a tentativa errada
            tentativas_restantes -= 1         # Reduz o numero de tentativas

            # Feedback mediato para o jogador
            print(f"\nLetra incorreta ! tentativa restantes:")

           
            