import random

# --- 1. Word List ---
# You can expand this list with more words!
WORDS = [
    "python", "programming", "computer", "science", "algorithm",
    "developer", "keyboard", "monitor", "application", "website",
    "challenge", "success", "learning", "project", "bachelor"
]

# --- 2. Hangman ASCII Art (for visual feedback) ---
# Each element in this list represents a stage of the hangman.
# The index corresponds to the number of incorrect guesses.
HANGMAN_PICS = [
    """
       -----
       |   |
           |
           |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ---------
    """
]

# --- 3. Game Functions ---

def get_random_word(word_list):
    """Selects a random word from the provided list."""
    return random.choice(word_list).upper() # Convert to uppercase for case-insensitive matching

def display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word):
    """
    Displays the current state of the game:
    - Hangman ASCII art based on missed guesses.
    - Missed letters.
    - The word with guessed letters revealed and blanks for unguessed ones.
    """
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    print("Missed letters:", end=" ")
    for letter in missed_letters:
        print(letter, end=" ")
    print() # Newline

    blanks = "_" * len(secret_word)

    # Replace blanks with correctly guessed letters
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    # Display the word with spaces between letters
    for letter in blanks:
        print(letter, end=" ")
    print() # Newline

def get_guess(already_guessed):
    """
    Prompts the player for a letter guess and validates it.
    Ensures it's a single letter and hasn't been guessed before.
    """
    while True:
        print("Guess a letter.")
        guess = input().upper() # Convert to uppercase for consistency

        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Choose again.")
        elif not "A" <= guess <= "Z": # Check if it's an alphabet character
            print("Please enter a LETTER.")
        else:
            return guess

def play_again():
    """Asks the player if they want to play another round."""
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")

# --- 4. Game Logic ---

def main():
    print("H A N G M A N")
    missed_letters = []
    correct_letters = []
    secret_word = get_random_word(WORDS)
    game_is_done = False

    while True:
        display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word)

        # Get player's guess
        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters.append(guess)

            # Check if player has won
            found_all_letters = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break
            if found_all_letters:
                print(f"Yes! The secret word is '{secret_word}'! You have won!")
                game_is_done = True
        else:
            missed_letters.append(guess)

            # Check if player has run out of guesses
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word) # Show final state
                print(f"You have run out of guesses!\nThe word was '{secret_word}'. You lose!")
                game_is_done = True

        # Ask to play again if the game is done
        if game_is_done:
            if play_again():
                # Reset game variables
                missed_letters = []
                correct_letters = []
                secret_word = get_random_word(WORDS)
                game_is_done = False
            else:
                break # Exit the game loop

if __name__ == "__main__":
    main()