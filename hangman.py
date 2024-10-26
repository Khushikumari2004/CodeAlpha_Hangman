import random

# List of tech company names
companies_list = ['Microsoft', 'Google', 'Amazon', 'Facebook', 'Apple', 'Tesla', 'Netflix', 'Adobe', 'Intel', 'IBM']


def choose_word():
    return random.choice(companies_list).upper()


def hangman_game():
    word = choose_word()
    word_letters = set(word)  # Letters in the word
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    guessed_letters = set()

    tries = 6  # Number of tries before game over

    print("\nWelcome to Hangman: Tech Company Challenge!")

    while tries > 0 and len(word_letters) > 0:
        print(f"\nRemaining attempts: {tries}")
        print(f"Guessed letters: {' '.join(guessed_letters)}")
        current_word = [letter if letter in guessed_letters else '_' for letter in word]
        print("Word to guess: ", ' '.join(current_word))

        guess = input("\nGuess a letter: ").upper()

        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print(f"\nCorrect! {guess} is in the word.")
            else:
                tries -= 1
                print(f"\nWrong guess! {guess} is not in the word.")
        elif guess in guessed_letters:
            print("\nYou already guessed that letter.")
        else:
            print("\nInvalid input.")

    if tries == 0:
        print(f"\nGame over! The company name was {word}.")
    else:
        print(f"\nCongratulations! You've guessed the company name: {word}!")


hangman_game()