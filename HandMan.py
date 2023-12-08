import random

class HangmanAI:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word_to_guess = random.choice(self.word_list)
        self.guesses = set()
        self.max_attempts = 6

    def display_word(self):
        return ''.join(letter if letter in self.guesses or letter == ' ' else '_' for letter in self.word_to_guess)

    def make_guess(self):
        # Implementa el algoritmo Minimax simple para elegir la letra que maximiza las posibilidades
        possible_guesses = [letter for letter in 'abcdefghijklmnopqrstuvwxyz' if letter not in self.guesses]
        best_guess = max(possible_guesses, key=lambda letter: self.calculate_score(letter))
        self.guesses.add(best_guess)
        return best_guess

    def calculate_score(self, guess):
        # Calcula un puntaje simple basado en la cantidad de letras reveladas por la elección
        revealed_letters = sum(1 for letter in self.word_to_guess if letter == guess or letter in self.guesses)
        return revealed_letters

def play_hangman_ai(word_list):
    hangman_ai = HangmanAI(word_list)

    while True:
        # Turno del jugador
        player_guess = input("Tu turno. Ingresa una letra: ").lower()
        hangman_ai.guesses.add(player_guess)
        print("Palabra actual: ", hangman_ai.display_word())

        if set(hangman_ai.word_to_guess) <= hangman_ai.guesses:
            print("¡Ganaste! La palabra es:", hangman_ai.word_to_guess)
            break
        elif len(hangman_ai.guesses) >= hangman_ai.max_attempts:
            print("¡Perdiste! La palabra era:", hangman_ai.word_to_guess)
            break

        # Turno de la máquina
        print("\nTurno de la máquina.")
        guess = hangman_ai.make_guess()
        print("La máquina elige la letra:", guess)

        if guess in hangman_ai.word_to_guess:
            print("¡Correcto!")
        else:
            print("Incorrecto. Intentos restantes:", hangman_ai.max_attempts - len(hangman_ai.guesses))

        if set(hangman_ai.word_to_guess) <= hangman_ai.guesses:
            print("¡Ganó la máquina! La palabra es:", hangman_ai.word_to_guess)
            break
        elif len(hangman_ai.guesses) >= hangman_ai.max_attempts:
            print("¡Perdiste! La palabra era:", hangman_ai.word_to_guess)
            break

if __name__ == "__main__":
    word_list = ["camilla", "computador", "programacion", "lenguaje", "artificial", "intelligencia"]
    play_hangman_ai(word_list)
