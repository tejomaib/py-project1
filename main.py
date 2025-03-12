import random

def get_words():
    words = []
    print("Enter words for the game (press Enter twice to finish):")
    while True:
        word = input().strip()
        if word == "":
            if len(words) == 0:
                print("Please enter at least one word.")
                continue
            else:
                break
        words.append(word)
    return words

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    # Ask for the number of body parts (attempts)
    attempts = int(input("Enter the number of body parts (attempts) for the hangman: "))
    if attempts < 1:
        print("Number of attempts must be at least 1.")
        return

    # Get words from the user
    words = get_words()
    chosen_word = random.choice(words).lower()
    guessed_letters = set()
    incorrect_guesses = 0

    print("\nLet's play Hangman!")
    print(f"The word has {len(chosen_word)} letters.")
    print(display_word(chosen_word, guessed_letters))

    while incorrect_guesses < attempts:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in chosen_word:
            print("Correct!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect! {attempts - incorrect_guesses} attempts remaining.")

        # Display the current state of the word
        current_display = display_word(chosen_word, guessed_letters)
        print(current_display)

        # Check if the player has won
        if "_" not in current_display:
            print("Congratulations! You guessed the word!")
            return

    # If the loop ends, the player has run out of attempts
    print(f"Game over! The word was: {chosen_word}")

if __name__ == "__main__":
    hangman()
