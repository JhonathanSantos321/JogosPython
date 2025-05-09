#python
# Importa o Modulo random para seleçao aleatoria de palavra
import random

# Lista de palavras para o jogo (banco de palavras)
palavra = ['maçã', 'banana', 'laranja', 'uva', 'morango']
           
def jogo_da_forca():

    Funçao principal que gerencia  toda a logica o jogo de forca:
    - seleçao da palavra
    - Controle de tentativas
    - Validaçao das Letras
    - Exibiçao do estado do jogo_da_forca


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
    print(f"Voce tem {tentativas_Restantes} tentativas para adivinhar a palavra.\n")

           
            