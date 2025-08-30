import streamlit as st
import random

# Word lists from your words module
words = {
    'fruits': [
        "apple", "banana", "orange", "grape", "mango", "pineapple", "peach", "pear", "plum", "cherry",
        "watermelon", "strawberry", "blueberry", "raspberry", "lemon", "lime", "kiwi", "papaya", "coconut",
        "pomegranate"
    ],
    'objects': [
        "chair", "table", "pencil", "notebook", "backpack", "phone", "wallet", "key", "lamp", "mirror",
        "toothbrush", "towel", "cup", "bottle", "scissors", "remote", "blanket", "clock", "comb", "spoon",
        "fork", "plate", "bag", "glasses", "soap", "shampoo", "charger", "fan", "mouse", "keyboard"
    ],
    'animals': [
        "dog", "cat", "cow", "horse", "sheep", "goat", "pig", "chicken", "duck", "rabbit",
        "elephant", "lion", "tiger", "bear", "zebra", "giraffe", "monkey", "panda", "kangaroo", "fox",
        "wolf", "deer", "camel", "donkey", "leopard", "mouse", "rat", "snake", "frog", "turtle"
    ]
}

# Hangman diagrams
diagrams = [
    '''
+---+
  |   |
 0_   |
 /|/  |
 ||   |
]   []|
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
[][][]|
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
[][][]|
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
[][][]|
=========''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
[][][]|
=========''',
    '''
+---+
  |   |
  O   |
  |   |
      |
[][][]|
=========''',
    '''
+---+
  |   |
  O   |
      |
      |
[][][]|
=========''',
    '''
+---+
  |   |
      |
      |
      |
[][][]|
=========''',
    '''
+---+
      |
      |
      |
      |
[][][]|
========='''
]


def initialize_game():
    """Initialize game state"""
    if 'game_started' not in st.session_state:
        st.session_state.game_started = False
    if 'user_lives' not in st.session_state:
        st.session_state.user_lives = 8
    if 'answer' not in st.session_state:
        st.session_state.answer = set()
    if 'wrong_answers' not in st.session_state:
        st.session_state.wrong_answers = set()
    if 'random_word' not in st.session_state:
        st.session_state.random_word = ""
    if 'set_of_characters' not in st.session_state:
        st.session_state.set_of_characters = set()
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    if 'won' not in st.session_state:
        st.session_state.won = False


def pick_random_word(category):
    """Pick a random word from the selected category"""
    category_map = {'Fruits': 'fruits', 'Objects': 'objects', 'Animals': 'animals'}
    word_list = words[category_map[category]]
    return random.choice(word_list)


def print_blanks(current_answer, word):
    """Display word with guessed letters revealed"""
    blanks = []
    for letter in word:
        if letter in current_answer:
            blanks.append(letter)
        else:
            blanks.append("_")
    return "".join(blanks)


def reset_game():
    """Reset all game state"""
    st.session_state.game_started = False
    st.session_state.user_lives = 8
    st.session_state.answer = set()
    st.session_state.wrong_answers = set()
    st.session_state.random_word = ""
    st.session_state.set_of_characters = set()
    st.session_state.game_over = False
    st.session_state.won = False


def main():
    st.set_page_config(page_title="Hangman Game", page_icon="🎯", layout="centered")

    # Custom CSS for better styling
    st.markdown("""
    <style>
    .hangman-ascii {
        font-family: 'Courier New', monospace;
        font-size: 14px;
        white-space: pre;
        background-color: #f0f0f0;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    .word-display {
        font-family: 'Courier New', monospace;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        background-color: #e6f3ff;
        border-radius: 10px;
        margin: 20px 0;
    }
    .game-info {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    initialize_game()

    st.title("🎯 Hangman Game")
    st.markdown("---")

    # Game introduction
    if not st.session_state.game_started:
        st.markdown("""
        ## Welcome to Hangman! 

        **How to play:**
        - **Win:** Guess all letters with 8 or fewer mistakes!
        - **Lose:** Make more than 8 wrong guesses and you're out!

        Choose a category and start guessing!
        """)

        # Category selection
        category = st.selectbox(
            "What kind of word would you like to guess?",
            ["Select a category...", "Fruits", "Objects", "Animals"]
        )

        if category != "Select a category...":
            if st.button("🎮 Start Game", type="primary"):
                st.session_state.random_word = pick_random_word(category)
                st.session_state.set_of_characters = set(st.session_state.random_word)
                st.session_state.game_started = True
                st.success(f"You selected to guess a {category.lower()[:-1]}! Good luck!")
                st.rerun()

    # Main game
    elif st.session_state.game_started and not st.session_state.game_over:
        # Game status
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"<div class='game-info'><strong>Lives Remaining:</strong> {st.session_state.user_lives}</div>",
                        unsafe_allow_html=True)
        with col2:
            st.markdown(
                f"<div class='game-info'><strong>Word Length:</strong> {len(st.session_state.random_word)} letters</div>",
                unsafe_allow_html=True)
        with col3:
            st.markdown(
                f"<div class='game-info'><strong>Letters Guessed:</strong> {len(st.session_state.answer) + len(st.session_state.wrong_answers)}</div>",
                unsafe_allow_html=True)

        # Hangman diagram
        st.markdown(f"<div class='hangman-ascii'>{diagrams[st.session_state.user_lives]}</div>", unsafe_allow_html=True)

        # Word display
        word_display = print_blanks(st.session_state.answer, st.session_state.random_word)
        st.markdown(f"<div class='word-display'>{word_display}</div>", unsafe_allow_html=True)

        # Wrong guesses
        if st.session_state.wrong_answers:
            wrong_list = sorted(list(st.session_state.wrong_answers))
            st.markdown(f"**Wrong Guesses:** {', '.join(wrong_list)}")

        # Input for letter guess
        col1, col2 = st.columns([3, 1])
        with col1:
            letter_guess = st.text_input(
                "Type a letter that you think exists in the word:",
                max_chars=1,
                key="letter_input"
            ).lower()

        with col2:
            guess_button = st.button("🎯 Guess!", type="primary")

        # Process guess
        if guess_button and letter_guess:
            if len(letter_guess) == 1 and letter_guess.isalpha():
                if letter_guess in st.session_state.set_of_characters:
                    if letter_guess not in st.session_state.answer:
                        st.session_state.answer.add(letter_guess)
                        st.success("🎉 Yes! The letter is in the word!")
                    else:
                        st.warning("🤔 You already guessed that letter! No lives deducted.")
                else:
                    if letter_guess not in st.session_state.wrong_answers:
                        st.session_state.wrong_answers.add(letter_guess)
                        st.session_state.user_lives -= 1
                        st.error("❌ Oops! The letter is not in the word!")
                    else:
                        st.warning("🤔 You already tried that letter! No lives deducted.")

                # Check win/lose conditions
                if st.session_state.answer == st.session_state.set_of_characters:
                    st.session_state.game_over = True
                    st.session_state.won = True
                elif st.session_state.user_lives < 0:
                    st.session_state.game_over = True
                    st.session_state.won = False

                # Clear input and rerun
                st.rerun()
            else:
                st.error("⚠️ Please enter exactly one letter!")

    # Game over screen
    elif st.session_state.game_over:
        if st.session_state.won:
            st.balloons()
            st.success("🎉🎉🎉 CONGRATULATIONS! YOU WIN! 🎉🎉🎉")
            st.markdown(f"### You correctly guessed the word: **{st.session_state.random_word.upper()}**")
            st.markdown("🌟 Great job! You saved the hangman!")
        else:
            st.markdown(f"<div class='hangman-ascii'>{diagrams[0]}</div>", unsafe_allow_html=True)
            st.error("💀 GAME OVER! You lost this time...")
            st.markdown(f"### The word was: **{st.session_state.random_word.upper()}**")
            st.markdown("😔 Better luck next time!")

        # Play again button
        if st.button("🔄 Play Again", type="primary"):
            reset_game()
            st.rerun()


if __name__ == "__main__":
    main()