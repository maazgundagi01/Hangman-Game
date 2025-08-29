import random
import words
import diagrams

#Picks a random word from the array of words in the "word" module
def pick_a_string():
    random_int = random.randint(0, len(words.guess_words) - 1)
    word = words.guess_words[random_int]
    return word

random_word = pick_a_string()

# For comparison, we need the string split into set of unique characters
set_of_characters = set(random_word)

#Come back to this function when reading the while loop.
#This block distinguishes guessed and unguessed letters in the word user is guessing and outputs the word as combination of blanks and letters
def print_blanks(current_answer):
    blanks = []
    for letter in set_of_characters:
        if letter in current_answer:
            blanks.append(letter)
        else:
            blanks.append("_")
    word_status = "".join(blanks)
    return word_status

#These variables track score
user_lives = 7
answer = {}
wrong_answers = {}
print(diagrams.hangman_text)
print(f"\nWelcome to Hangman!\nHangman is a simple game, you have to guess all the letters of the word\nyou will be eliminated from the game if you guess more than 6 wrong words!\nLet's Begin!\n")

while answer != set_of_characters:
    print(f'{diagrams.decoration_line} Lives:{user_lives - 1} {diagrams.decoration_line}')
    print(f'{diagrams.diagram[user_lives - 1]}')
    print(f'WORD YOU ARE GUESSING: {print_blanks(answer)}')
    print(f'Your WRONG Guesses: {",".join(wrong_answers)}')
    character = input("Type a letter that you think exists in the word! --> ")
    if character in set_of_characters:
        if character not in answer:
            answer.add(character)
            print('Yes! The letter is in the word!')
        else:
            print('Nice try but you already guessed that character!\nNo lives were deducted, try a different character!')
    else:
        if character not in wrong_answers:
            wrong_answers.add(character)
            user_lives = user_lives - 1
            print('Aw, Snap! The letter is not in the word!')
        else:
            print("Aw, Snap! You already tried that character and it is not in the word!\nNo lives were deducted, try a different character!")

if answer == set_of_characters:
    print(f'{diagrams.decoration_line}{diagrams.decoration_line}\n{diagrams.you_win}\nYOU WIN! You correctly guessed the word {random_word}!\nRetry again to get a different word!\n:)')
    exit(0)
else:
    print(f'{diagrams.decoration_line}{diagrams.decoration_line}\n{diagrams.you_lose}\nDAMN HARD LUCK! You Lose, the word was {random_word}!\nTry again next time...\n:)!')
    exit(0)