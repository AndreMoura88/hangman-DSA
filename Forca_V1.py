import random

# board (Tabuleiro)

board = ['''
==========Hangman==========

+---+
|   |
    |
    |
    |
    |
==========''', '''
   +------+
   |      |
 (^_^)    |
          |
          |
          |
==========''', '''
  +-------+
  |       |
 (^_^)    |
  ||      |
          |
          |
==========''', '''
   +------+
   |      |
 (^_^)    |
  /||     |
          |
          |
==========''', '''
   +------+
   |      |
 (0_0)    |
 /||\     |
          |
          |
==========''', '''
   +------+
   |      |
 (0_0)    |
  /||\    |
  /       |
          |
==========''', '''
   +------+
   |      |
 (*_*)    |
========  |
 /||\     |
 /  \     |
          |
==========''']

dict_palavra_certa = {}
lista_da_palavra_certa = ['_'] * 20
quant_de_erros = []
lista_de_letras_erradas = []


# Classe

class Hangman:

    # metodo construtor
    def __init__(self, word):
        self.word = word
        # self.numero_de_erros = 0
        # self.teste = 'a'
        print("START")

    # método para advinhar a letra
    def guess(self, letter):
        self.letter = letter
        # n_de_erros = 0
        self.cont = 0


        for index, i in enumerate(self.word):
            if i == self.letter:
                dict_palavra_certa[index] = self.letter
                self.cont = self.cont + 1

        for c, v in dict_palavra_certa.items():
            lista_da_palavra_certa[c] = v


    # método para verificar se o jogo terminou
    def hangman_over(self):
        if len(quant_de_erros) == 7:
            return 0
        else:
            return True

    # Método para verificar se o jogador venceu
    def hangman_won(self, palavra_correta):
        self.teste = palavra_correta
        if self.teste == self.word:
            return True
        else:
            return 0

    # Método para não mostrar a letra no board
    def hide_word(self):
        letras_certas_em_ordem = ''.join(lista_da_palavra_certa)
        print(f"A palavra é: {letras_certas_em_ordem}")

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        # self.numero_de_erros = 0
        if self.cont == 0:
            print(board[len(quant_de_erros)])
            quant_de_erros.append(1)
            lista_de_letras_erradas.append(self.letter)
            # self.numero_de_erros = self.numero_de_erros + 1
            # numero_de_erros = numero_de_erros + 1
            # print(len(list10))


# Função para ler uma palavra de forma aleatória no banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do programa
def main():
    # Objeto
    game = Hangman(rand_word())
    del (lista_da_palavra_certa[len(game.word):])
    letras_certas_em_ordem = ' '.join(lista_da_palavra_certa)
    print(f"A palavra é: {letras_certas_em_ordem}, {len(game.word)}")

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do carcter

    while game.hangman_over():
        l = game.guess(input("digite uma letra:"))
        game.print_game_status()
        del (lista_da_palavra_certa[len(game.word):])
        game.hide_word()
        letras_certas_em_ordem = ''.join(lista_da_palavra_certa)
        print(f"Letras erradas: {', '.join(lista_de_letras_erradas)}")
        # Verifica o status do jogo

        if game.hangman_won(letras_certas_em_ordem):
            break
        # if game.hangman_over():
        #    break

    # De acordo com o status, imprime a mensagem na tela para o usuário
    if game.hangman_won(letras_certas_em_ordem):
        print("\nParabéns! Você venceu!!")
    else:
        print("\nGame over! Você perdeu!!")
        print(f"\nA palavra certa era: {game.word}")
    print("\nFoi bom jogar com você! Agora volte aos estudos.")


# Executa o programa
if __name__ == "__main__":
    main()
