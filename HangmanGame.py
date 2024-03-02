import random

def choose_word():
    words = ["hangman", "python", "programming", "developer", "openai", "challenge", "hi", "war", "lion", "laptop", "lifeh",]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    MAX_INCORRECT_GUESSES = 6
    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    
    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            incorrect_guesses += 1
            print("Incorrect guess. Attempts left:", MAX_INCORRECT_GUESSES - incorrect_guesses)
        else:
            print("Good guess!")

        if set(guessed_letters) == set(word_to_guess):
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break

    if incorrect_guesses == MAX_INCORRECT_GUESSES:
        print("\nSorry, you ran out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
