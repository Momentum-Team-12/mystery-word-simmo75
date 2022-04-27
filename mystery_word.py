import random


def get_list():
    EASY_WORDS = []
    MEDIUM_WORDS = []
    DIFFICULT_WORDS = []

    with open('words.txt') as file_contents:
        # reads the contents
        contents_string = file_contents.read()
        contents_list = contents_string.split()

    for word in contents_list:
        if 4 <= len(word) <= 6:
            EASY_WORDS.append(word)
        elif 7 <= len(word) <= 8:
            MEDIUM_WORDS.append(word)
        elif 9 <= len(word):
            DIFFICULT_WORDS.append(word)
    level = input("Choose your difficuly level: E, M, D : ").upper()
    if level == "E":
        return EASY_WORDS
    elif level == "M":
        return MEDIUM_WORDS
    elif level == "D":
        return DIFFICULT_WORDS


def play_again():
    print("Game over. Would you like to play again? y/n")
    play_response = input()
    yes_input = ['y', 'Y']
    no_input = ['n', 'N']
    if play_response in yes_input:
        play_game()
    elif play_response in no_input:
        exit()
    else:
        print("Invalid response. Enter y for new game, n to exit.")
        play_again()
    exit()


def play_game():
    # computer reads file
    contents_list = get_list()
    random_word = random.choice(contents_list)
    # print(random_word)
    print(f'I am thinking of a word. It has {len(random_word)} letters...')

    guesses = ' '
    turns = 8

    while turns > 0:
        failed = 0

        for letter in random_word:
            if letter in guesses:
                print(letter, end=" ")

            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            print("The word is: ", random_word)
            print("You Win")
            play_again()

        print()
        guess = input("Guess a letter:")
        guesses += guess

        if guess not in random_word:
            turns -= 1
            print("Wrong")
            print("You have", + turns, 'more guesses')

            if turns == 0:
                print("You Lose, the word is: ", random_word)
                play_again()


if __name__ == "__main__":
    play_game()
