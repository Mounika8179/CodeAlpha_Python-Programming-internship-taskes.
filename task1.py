import random

# List of words for the game
word_list = ['python', 'java', 'javascript', 'hangman', 'developer', 'programming', 'data', 'science']

def get_random_word(word_list):
    """Selects a random word from the provided list."""
    return random.choice(word_list).lower()

def display_word(word, guessed_letters):
    """Displays the word with guessed letters and underscores for unguessed letters."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = get_random_word(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    print("Welcome to Hangman!")

    # Loop until the player has reached the max number of incorrect guesses or has guessed the word
    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        
        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single alphabetical character.")
            continue

        # Check if the guessed letter is in the word
        if guess in word:
            if guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try a different letter.")
            else:
                print(f"Good job! '{guess}' is in the word.")
                guessed_letters.add(guess)
        else:
            if guess in guessed_letters:
                print(f"You already guessed '{guess}' and it's not in the word.")
            else:
                print(f"Oops! '{guess}' is not in the word.")
                incorrect_guesses += 1
                guessed_letters.add(guess)

        # Check if the player has guessed the entire word
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nSorry, you've run out of guesses! The word was: {word}")

if __name__ == '__main__':
    hangman()
