import random
import words
import diagrams

def pick_a_string():
    random_int = random.randint(0, len(words.guess_words) - 1)
    word = words.guess_words[random_int]
    return word

random_word = pick_a_string()





