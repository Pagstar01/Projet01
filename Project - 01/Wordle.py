import os
from random import choice

# Function to read the dictionary file and return its content
def get_dictionary(file_path):
    # Input: file_path - the path to the dictionary file
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        print("The file does not exist on the desktop.")
        return None
    
# Function to determine the number of attempts based on the selected level
def determine_attempts():
    # Input: user input required
    print("Hello, welcome to Wordle! Here are the levels:")
    print(" - Level 1 (9 attempts)")
    print(" - Level 2 (8 attempts)")
    print(" - Level 3 (7 attempts)")
    print(" - Level 4 (6 attempts)")
    print(" - Level 5 (5 attempts)")
    print(" - Level 6 (4 attempts)")
    
    level = int(input("Level: "))
    
    n = 0
    if level == 1:
        n = 9
    elif level == 2:
        n = 8
    elif level == 3:
        n = 7
    elif level == 4:
        n = 6
    elif level == 5:
        n = 5
    else:
        n = 4
    # Output: n - the number of attempts determined by the selected level
    print("Number of attempts: ", n)
    return n

# Function to choose a word from the list based on length
def choose_word(word_list):
    # Input: word_list - a list of words
    filtered_list = [word for word in word_list if 4 <= len(word) <= 9]
    
    # Output: selected_word - a randomly selected word from the filtered list
    return choice(filtered_list)


# Function to calculate the length of a word
def calculate_word_length(word):
    # Input: word - a word for which to calculate the length
    # Output: length - the number of letters in the word
    return len(word)

# Function to check the user's guess and calculate correct and misplaced letters
def check_guess(target_word, guess):
    # Input: target_word - the word to guess, guess - the user's guessed word
    # Output: correct_letters - the number of correct letters in the correct positions
    # misplaced_letters - the number of correct letters in misplaced positions

    correct_letters = 0
    misplaced_letters = 0
    
    for i in range(len(target_word)):
        if guess[i] == target_word[i]:
            correct_letters += 1
        elif guess[i] in target_word:
            misplaced_letters += 1
    
    return correct_letters, misplaced_letters


# Main function that orchestrates the game
def main():
    while True:
        # Input: None (uses predefined file path and user input for level)
        file_name = "common_words_in_english.txt"
        folder01 = os.path.join(os.path.expanduser("~/Desktop"), "Project - 01")
        file_path = os.path.join(folder01, file_name)

        dictionary = get_dictionary(file_path)

        if dictionary is None:
            return

        attempts = determine_attempts()

        l1 = dictionary.splitlines()

        The_word = choose_word(l1)

        # Output: The_word - the word chosen for the game

        print('\n')
        print(The_word)
        print('\n')

        print("There are:", calculate_word_length(The_word), "letters in the word, and the first letter is:", The_word[0])

        print("Let's play Wordle!")

        while attempts > 0:
            user_guess = input("Attempt: ").strip().lower()

            if len(user_guess) != len(The_word):
                print("The length of the word is", len(The_word), "not", len(user_guess))
                continue

            correct, misplaced = check_guess(The_word, user_guess)

            if correct == len(The_word) and len(user_guess) == len(The_word):
                print("Congratulations! You've guessed the word", The_word, "correctly.")
                break
            else:
                print("Correct letters in correct positions: ", correct)
                print("Correct letters in misplaced positions: ", misplaced)
                print("Attempts remaining: ", attempts - 1)

            attempts -= 1

        if attempts == 0:
            print("Out of attempts! The word was", The_word, ". Better luck next time!")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break


main()
