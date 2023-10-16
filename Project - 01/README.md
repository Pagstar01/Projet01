Problem Context:
The project is a text-based game called "Wordle" where the player attempts to guess a randomly chosen word from a dictionary. 
The game provides multiple difficulty levels, and the player has a limited number of attempts to guess the word correctly. 
The game tracks the number of correct letters in the correct positions and the number of correct letters in misplaced positions.


Wordle, offers both entertainment and educational value. It expands players vocabulary, challenges logic and deduction, and provides a variable and engaging experience. Building such a game also serves as a valuable practice ground for coding skills, including file I/O, randomization, and input handling.

ALGORITHM
**Input:**
-Load the dictionary of common English words from a file.
-Get the player's chosen level (1 to 6) to determine the number of attempts.
-Within each game, prompt the player to enter a word as their guess.
-Validate that the length of their guess matches the length of the target word.
-Prompt the player if they want to play another game.

**Process:**
1. Initialize the game:
   - Load the dictionary.
   - Set up a game loop to allow the player to play multiple games.
   - Randomly select a word from the dictionary for the player to guess.
   - Track the number of attempts remaining within each game.

2. Within each game loop:
   - Compare the player's guess to the target word.
   - Calculate and display the number of correct letters in the correct positions.
   - Calculate and display the number of correct letters in misplaced positions.
   - Determine the game outcome (win or lose).
   - Continue the game loop or exit if the player decides not to play again.

**Output:**
-Display a congratulations message if the player guesses the word correctly.
-Display a message indicating the game is over if the player runs out of attempts.
-Reveal the target word if the game is over.
-Prompt the player if they want to play another game.
