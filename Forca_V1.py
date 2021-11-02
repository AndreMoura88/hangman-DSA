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

dict_palavra_certa = {} #dict to build to store the right word // dicionário para construir a palavra certa
lista_da_palavra_certa = ['_'] * 20 #list with the characters of the chosen word // lista com os caracteres da palavra sorteada
quant_de_erros = [] #count the wrong attempts //faz a contabilidade das tentativas erradas
lista_de_letras_erradas = [] #to store the correct letters // armazena as letras erradas


# Class//Classe

class Hangman:

    # constructor method// metodo construtor
    def __init__(self, word):
        self.word = word
        print("START")

    # method to guess the letter// método para advinhar a letra
    def guess(self, letter):
        self.letter = letter
        self.cont = 0

        for index, i in enumerate(self.word):
            if i == self.letter:
                dict_palavra_certa[index] = self.letter
                self.cont = self.cont + 1

        for c, v in dict_palavra_certa.items():
            lista_da_palavra_certa[c] = v

    # method to check if the game is over// método para verificar se o jogo terminou
    def hangman_over(self):
        if len(quant_de_erros) == 7:
            return 0
        else:
            return True

    # Method to check if the player has won// Método para verificar se o jogador venceu
    def hangman_won(self, palavra_correta):
        self.teste = palavra_correta
        if self.teste == self.word:
            return True
        else:
            return 0

    # Method for not showing the letter on the board// Método para não mostrar a letra no board
    def hide_word(self):
        letras_certas_em_ordem = ''.join(lista_da_palavra_certa)
        print(f"A palavra é: {letras_certas_em_ordem}")

    # Method for checking game status and printing board on screen// Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        if self.cont == 0:
            print(board[len(quant_de_erros)])
            quant_de_erros.append(1)
            lista_de_letras_erradas.append(self.letter)


# Function to read a word randomly from the word bank// Função para ler uma palavra de forma aleatória no banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do programa
def main():
    # Object// Objeto
    game = Hangman(rand_word())
    del (lista_da_palavra_certa[len(game.word):])
    letras_certas_em_ordem = ' '.join(lista_da_palavra_certa)
    print(f"A palavra é: {letras_certas_em_ordem}, {len(game.word)}")

    # While the game is not finished, print the status, request a letter and read the character
    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do carcter
    while game.hangman_over():
        game.guess(input("digite uma letra:"))
        game.print_game_status()
        del (lista_da_palavra_certa[len(game.word):])
        game.hide_word()
        letras_certas_em_ordem = ''.join(lista_da_palavra_certa)
        print(f"Letras erradas: {', '.join(lista_de_letras_erradas)}")

        # Check game status// Verifica o status do jogo
        if game.hangman_won(letras_certas_em_ordem):
            break

    # According to the status, prints the message on the screen to the user
    # De acordo com o status, imprime a mensagem na tela para o usuário
    if game.hangman_won(letras_certas_em_ordem):
        print("\nCongratulations!! You Win!! -- Parabéns! Você venceu!!")
    else:
        print("\nGame over! Você perdeu!!")
        print(f"\nThe correct word was: A palavra certa era: {game.word}")
    print("\nWas a pleasure -- Come Back to studies --- Foi bom jogar com você! Agora volte aos estudos.")

# Run the program
# Executa o programa
if __name__ == "__main__":
    main()
