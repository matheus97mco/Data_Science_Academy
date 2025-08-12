#import

import random
from os import system,name

#Função para limpar tela em cada execução
def limpa_tela():
    #windows
    if name == 'nt':
        _=system ('cls')
    #mac ou linux
    else:
        _= system('clear')

#função 
def game():
    
    limpa_tela()
    print('\nBem vindo(a) ao jogo da forca!')
    print('Advinha a palavra abaixo:\n')
          
    # Lista de palavras para o jogo 
    palavras = ["abacaxi", "computador", "girassol", "elefante", "montanha", "bicicleta", "astronauta", "biblioteca", "chocolate", "oceano",
 "violino", "cachoeira", "tartaruga", "internet", "pinguim", "pirata", "lanterna", "dinossauro", "espaguete", "martelo", "esquilo", "foguete", "palavra", "mochila", "sapato", "planeta", "travesseiro", "telefone", "camiseta", "abajur", "bola", "teclado", "janela", "carro", "ponte", "floresta", "prancha", "guitarra", "pizza", "relogio", "abelha", "escada", "pintor", "navio", "serrote", "tapete", "trem", "biscoito", "anel", "espelho", "copo", "cadeira", "microfone", "chuva", "ponteiro", "macaco", "raquete", "lousa", "parafuso", "corda", "arvore", "piscina", "cavalo", "escola", "lapis", "borracha", "caneta", "quadro", "livro", "mala", "chave", "porta", "fogao", "geladeira", "televisao", "controle", "prato", "faca", "colher", "garfo", "tapete", "rede", "cinto", "sacola", "banana", "buzina", "moto", "brinquedo", "caminhao", "helicoptero", "tinta", "martelo", "serra", "morango", "cofre", "lampada", "computador", "telefone", "camera", "bateria", "capacete", "relatorio", "moeda", "bussola", "trator"]
    
    #escolhe randomicamente uma palavra
    palavra = random.choice(palavras)
    
    #list comprehension
    letras_descobertas = ['_' for letra in palavra]

    #numero de chances 
    chances = 6
    
    #lista de letras erradas
    letras_erradas = []

    #loop enquanto numero de chances for maior que zero
    while chances > 0:
        #print
        print(' '.join(letras_descobertas))
        print('\nChances restantes: ',chances)
        print('Letras erradas:', ' '.join(letras_erradas))

        #tentativa
        tentativa = input('\nDigite uma letra: ').lower()

        #condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
            
        #condicional
        if '_' not in letras_descobertas:
            print('\nParabens! Você adivinhou a palavra:', palavra)
            break
    
    #condicional
    if '_' in letras_descobertas:
        print('\nVocê perdeu! A palavra era:', palavra)

#bloco main
if __name__== '__main__':
    game()
    print('Obrigado por jogar! Até a próxima!')