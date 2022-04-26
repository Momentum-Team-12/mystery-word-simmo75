import random


def play_game():
    # computer reads file
    with open('words.txt') as file_contents:
        # reads the contents
        contents_string = file_contents.read()
        contents_list = contents_string.split()
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
                    print("_")
                    # print(letter, end=" ")
                    failed += 1

            if failed == 0:
                print("The word is: ", random_word)
                print("You Win")
                break

            print()
            guess = input("Guess a letter:")
            guesses += guess

            if guess not in random_word:
                turns -= 1
                print("Wrong")
                print("You have", + turns, 'more guesses')

                if turns == 0:
                    print("You Lose, the word is: ", random_word)


if __name__ == "__main__":
    play_game()
