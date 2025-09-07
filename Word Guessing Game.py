import random

# Word lists based on difficulty
EASY_WORDS = ["cat", "dog", "ball", "book", "tree"]
MEDIUM_WORDS = ["python", "school", "flower", "planet", "garden"]
HARD_WORDS = ["difficult", "mystery", "computer", "programming", "adventure"]

def choose_difficulty():
    print("Choose difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            return EASY_WORDS
        elif choice == "2":
            return MEDIUM_WORDS
        elif choice == "3":
            return HARD_WORDS
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

def play_game():
    print("===== Welcome to the Word Guessing Game =====")
    print("Rules: Try to guess the secret word. After each guess,")
    print("you'll be told how many letters are correct and in the correct place.\n")

#  choose difficulty
    word_list = choose_difficulty()

#  randomly select a word
    secret_word = random.choice(word_list)

#  tell length
    print(f"\nThe secret word has {len(secret_word)} letters.")

# attempt counter
    attempts = 0

#  loop until guessed
    while True:
        guess = input("\nEnter your guess: ").lower()
        attempts += 1

        if guess == secret_word:
            print(f" Congratulations! You guessed the word '{secret_word}' in {attempts} attempts.")
            break
        else:
# feedback
            correct_positions = sum(1 for g, s in zip(guess, secret_word) if g == s)
            print(f"Not correct yet! {correct_positions} letters are in the correct place.")

if __name__ == "__main__":
 play_game()
