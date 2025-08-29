import random
import words
import diagrams

# Adds a pause in the game and prompts user to press enter key. Used to prevent a lot of information appearing on the screen at once
def press_enter():
    input('PRESS ENTER TO CONTINUE')

print(diagrams.hangman_text)
print(f"\nWelcome to Hangman!")
press_enter()

print(f"\nHangman is a simple game, you have to guess all the letters of the word.\nWin: You will be eliminated from the game if you guess all the letters with less than six mistakes!\nLose: You will be eliminated from the game if you guess more than 6 wrong letters!\nLet's Begin!\n")
press_enter()

# Picks a random word from the specified topic array of words in the "word" module

category = ''
def pick_a_string(topic):
    if topic == 'a':
        random_int = random.randint(0, len(words.fruits) - 1)
        word = words.fruits[random_int]
        print('You selected to guess a fruit!')
        press_enter()
    elif topic == 'b':
        random_int = random.randint(0, len(words.objects) - 1)
        word = words.objects[random_int]
        print('You selected to guess an object!')
        press_enter()
    elif topic == 'c':
        random_int = random.randint(0, len(words.animals) - 1)
        word = words.animals[random_int]
        print('You selected to guess an animal!')
        press_enter()
    else:
        print('Wrong input please try again')
        word = ''
    return word

while (category != 'a' and category != 'b' and category != 'c') or (category == ''):
    category = input(f"What kind of word would you like to guess?\nType 'a' - to guess a fruit\nType 'b' - to guess an object\nType 'c' - to guess an animal\n--> ").lower()

random_word = pick_a_string(category)



# For comparison, we need the string split into set of unique characters
set_of_characters = set(random_word)

# Come back to this function when reading the while loop.
# This block distinguishes guessed and unguessed letters in the word user is guessing and outputs the word as combination of blanks and letters
def print_blanks(current_answer):
    blanks = []
    for letter in random_word:
        if letter in current_answer:
            blanks.append(letter)
        else:
            blanks.append("_")
    word_status = "".join(blanks)
    return word_status


# These variables track score
user_lives = 8
answer = set()
wrong_answers = set()

# Main Game Loop
while answer != set_of_characters:
    # Display Module
    print(f'{diagrams.decoration_line} Lives:{user_lives - 1} {diagrams.decoration_line}')
    print(f'{diagrams.diagram[user_lives]}\n')
    print(f'WORD YOU ARE GUESSING: {print_blanks(answer)}')
    print(f'Your WRONG Guesses: {",".join(wrong_answers)}')

    # Check user input
    character = input("Type a letter that you think exists in the word! --> ").lower()
    while len(character) > 1:
        character = input("Please only type one single letter at a time -->").lower()
    while len(character) < 1:
        character = input("Please type your answer -->").lower()
    if character in set_of_characters:
        if character not in answer:
            answer.add(character)
            print('\nYes! The letter is in the word!')
            press_enter()
        else:
            print('\nNice try but you already guessed that character!\nNo lives were deducted, try a different character!')
            press_enter()
    else:
        if character not in wrong_answers:
            wrong_answers.add(character)
            user_lives = user_lives - 1
            print('\nAw, Snap! The letter is not in the word!')
            press_enter()
        else:
            print("\nAw, Snap! You already tried that character and it is not in the word!\nNo lives were deducted, try a different character!")
            press_enter()


if answer == set_of_characters:
    print(f'{diagrams.decoration_line}{diagrams.decoration_line}\n{diagrams.you_win}\nYOU WIN! You correctly guessed the word {random_word}!\nRetry again to get a different word!\n:)')
    exit(0)
else:
    print(f'{diagrams.diagram[0]}\n{diagrams.decoration_line}{diagrams.decoration_line}\n{diagrams.you_lose}\nDAMN HARD LUCK! You Lose, the word was {random_word}!\nTry again next time...\n:)!')
    exit(0)