"""
File: CodeAplha_Project_Hangman Game.py
Author: veerakoteswararao 
Created: April 13, 2025 
"""

# Importing necessary libraries
import random               # Library to choose random words from our list
import string               # To get all English lowercase letters (a-z)

def hangman():      # Main function that contains all game logic

    # List of 8 challenging words for the game
    word_list = ["python", "hangman", "programming", "computer", 
                "keyboard", "developer", "algorithm", "variable"]

    # Selecting a random word and converting to lowercase for consistency
    secret_word = random.choice(word_list).lower()      # Using .lower() to ensure all letters are small

    # Creating a set of unique letters in the secret word that need to be guessed
    letters_to_guess = set(secret_word)  # Using set() to get only unique letters

    # Creating a set of all English lowercase letters for validation
    alphabet = set(string.ascii_lowercase)  # Contains all letters from a to z

    # Set to store letters the player has already guessed
    guessed_letters = set()  # Starts empty, will fill as player makes guesses

    lives = 6  # Traditional hangman rules - 6 incorrect guesses allowed

    # Displaying welcome message and initial information
    print("Welcome to Hangman!") # Greeting the player to our awesome game

    # Showing how many letters the secret word contains
    print(f"The word has {len(secret_word)} letters.") # Giving player first clue

    # Main game loop - runs until word is guessed or lives run out
    while len(letters_to_guess) > 0 and lives > 0:
        # Displaying current progress - showing guessed letters and blanks
        word_progress = [letter if letter in guessed_letters else '_' for letter in secret_word]
        print("\nCurrent word: " + " ".join(word_progress)) # Showing progress with spaces between letters
        print(f"Lives left: {lives}") # Reminding player how many attempts remain
        print(f"Guessed letters: " + " ".join(sorted(guessed_letters))) # Showing previous guesses

        # Getting player's letter guess and converting to lowercase
        guess = input("Guess a letter: ").lower() # Using .lower() to standardize input

        # Validating the player's input
        if len(guess) != 1: # Checking if input is exactly one character
            print("Please enter a single letter.") # Error message for wrong input length
            continue # Skip to next iteration of loop
        if guess not in alphabet: # Checking if input is a valid letter
            print("Please enter a valid letter (a-z).") # Error for non-alphabet characters
            continue
        if guess in guessed_letters: # Checking if letter was already guessed
            print("You've already guessed that letter. Try another one.") # No penalty for repeat
            continue

        # Adding the valid, new guess to our set of guessed letters
        guessed_letters.add(guess) # Using set's add() method to store the guess

        # Checking if the guessed letter is in the secret word
        if guess in letters_to_guess: # Letter is correct!
            letters_to_guess.remove(guess) # Remove from letters remaining to guess
            print("Good guess!") # Positive feedback for player
        else: # Letter is not in the word
            lives -= 1 # Deduct one life for incorrect guess
            print(f"Wrong guess! The letter '{guess}' is not in the word.") # Inform player

    # Game over - determining if player won or lost
    if lives == 0: # Player ran out of lives
        print(f"\nGame over! You lost. The word was: {secret_word}") # Revealing the word
    else: # Player guessed all letters
        print(f"\nCongratulations! You guessed the word: {secret_word}") # Victory message

# This block ensures the game only runs when executed directly
if _name_ == "_main_":
    hangman() # Starting our awesome Hangman game!
