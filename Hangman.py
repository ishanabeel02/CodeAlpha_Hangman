import random as r
import os

# Color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

MAX_TRIES_BY_DIFFICULTY = {
    '1': 6,  # Easy
    '2': 5,  # Medium
    '3': 4   # Hard
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_hangman(wrong, total_tries, message="Make a Guess!"):
    stages = [
        [" ", " ", " ", " "],
        ["O", " ", " ", " "],
        ["O", "/", " ", " "],
        ["O", "/", "\\", " "],
        ["O", "/", "\\", "|"],
        ["O", "/", "\\", "|", "/"],
        ["O", "/", "\\", "|", "/", "\\"]
    ]
    hang = stages[wrong] if wrong < len(stages) else stages[-1]

    print("___________________________")
    print(" |            |")
    print(f" |            {hang[0] if len(hang) > 0 else ''}")
    print(f" |           {hang[1] if len(hang) > 1 else ''}{hang[2] if len(hang) > 2 else ''}")
    print(f" |            {hang[3] if len(hang) > 3 else ''}")
    print(f" |           {hang[4] if len(hang) > 4 else ''}{hang[5] if len(hang) > 5 else ''}")
    print(" |                                                       " + message)
    print(" |                                                     /")
    print(" |      ==================                            O")
    print(" |      ||               ||                          / \\")
    print(" |      ||               ||                    |      |")
    print(" |      ||               ||                  =====   / \\")
    print("---------------------------------------------|---|--------------------------------")
    print("\n\n==============================================")
    print(f"                 LIFE: {total_tries - wrong}")
    print("==============================================")

def get_word():
    words_with_hints = {
        'python': 'Programming language 🐍',
        'hangman': 'A classic word guessing game',
        'developer': 'One who writes code',
        'monitor': 'Part of a computer setup',
        'keyboard': 'Input device with keys',
        'internet': 'A global network',
        'syntax': 'Rules of a programming language',
        'function': 'Reusable block of code',
        'variable': 'A placeholder for data',
        'object': 'An instance of a class',
        'laptop': 'Portable computer',
        'compile': 'Convert code to machine language',
        'debugger': 'Tool for fixing bugs',
        'challenge': 'Something that tests your skill',
        'program': 'Set of instructions for the computer'
    }
    word = r.choice(list(words_with_hints.keys()))
    hint = words_with_hints[word]
    return word, hint

def choose_difficulty():
    while True:
        print("\nChoose difficulty:")
        print(" 1. Easy (6 tries)")
        print(" 2. Medium (5 tries)")
        print(" 3. Hard (4 tries)")
        choice = input(">>> ").strip()
        if choice in MAX_TRIES_BY_DIFFICULTY:
            return MAX_TRIES_BY_DIFFICULTY[choice]
        print(f"{YELLOW}Invalid choice. Please enter 1, 2, or 3.{RESET}")

def play():
    clear_screen()
    word, hint = get_word()
    guessed_word = ['_'] * len(word)
    guessed_letters = []
    wrong_guesses = 0
    total_tries = choose_difficulty()

    print("\nLet's play Hangman!")
    print(f"The word has {len(word)} letters.")

    want_hint = input(f"{CYAN}Do you want a hint? (yes/no): {RESET}").strip().lower()
    if want_hint in ['yes', 'y']:
        print(f"{CYAN}Hint: {hint}{RESET}")

    first_try = True

    while wrong_guesses < total_tries and '_' in guessed_word:
        if first_try:
            print_hangman(wrong_guesses, total_tries, message="Make a Guess!")
            first_try = False
        else:
            print('Word:', ' '.join(guessed_word))
            print("Guessed letters:", ' '.join(sorted(guessed_letters)))

        guess = input("\nGuess a letter: ").lower().strip()

        if not guess.isalpha() or len(guess) != 1:
            print(f"{YELLOW}Please enter a valid single letter.{RESET}")
            continue

        if guess in guessed_letters:
            print(f"{YELLOW}You already guessed that letter.{RESET}")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print(f"{GREEN}Correct!{RESET}")
            print_hangman(wrong_guesses, total_tries, message="Nice Guess!")
        else:
            wrong_guesses += 1
            print(f"{RED}Wrong! You lost a life.{RESET}")
            print_hangman(wrong_guesses, total_tries, message="Incorrect Guess!")

    if '_' not in guessed_word:
        print(f"\n🎉 {GREEN}Congratulations! You guessed the word: {YELLOW}{word.upper()}{RESET}")

    else:
        print(f"\n💀 {RED}Game Over! The word was: {YELLOW}{word}{RESET}")

def replay():
    while True:
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again in ['yes', 'y']:
            play()
        elif again in ['no', 'n']:
            print(
                f"{CYAN}\t\t\t\tTTTTT  H   H  AAAAA  N   N  K   K    U   U \n"
                f"\t\t\t\t  T    H   H  A   A  NN  N  K  K     U   U \n"
                f"\t\t\t\t  T    HHHHH  AAAAA  N N N  K K      U   U \n"
                f"\t\t\t\t  T    H   H  A   A  N  NN  KK       U   U \n"
                f"\t\t\t\t  T    H   H  A   A  N   N  K  K     U   U \n"
                f"\t\t\t\t  T    H   H  A   A  N   N  K   K    UUUUU \n"
            )
            break
        else:
            print(f"{YELLOW}Invalid input. Please enter 'yes' or 'no'.{RESET}")

# Start the game
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('                         W E L C O M E   T O   H A N G M A N                ')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
play()
replay()
