import pyjokes
import pyttsx3
import random
import sys

from bokeh.core.validation.check import Validator

# Initialize voice engine globally to avoid reinitializing
try:
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    voice_enabled = True
except Exception:
    voice_enabled = False

# Store history of jokes and ratings
joke_history = []
rating_history = []

# Supported categories in pyjokes (manually defined)
CATEGORIES = ["all", "neutral", "chuck"]


def voice_output(text: str):
    """
    Speak text if voice engine is available, otherwise skip.
    """
    if not voice_enabled:
        return
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception:
        pass


def print_commands():
    commands = {
        1: 'Tell me a joke',
        2: 'Exit the program',
        3: f"Choose a joke category from {CATEGORIES}",
        4: 'Show past jokes in this session',
        5: 'Hear the last joke again',
        6: 'Show stats on jokes and ratings',
    }
    print("\nAvailable commands:")
    for cmd, desc in commands.items():
        print(f"  {cmd}: {desc}")


def choose_category():
    print(f"Available categories: {', '.join(CATEGORIES)}")
    selected = input("Choose a category (or press Enter for default): ").strip().lower()
    if selected in CATEGORIES:
        return selected
    elif selected == '':
        return None
    else:
        print("Unknown category, using default.")
        return None


def tell_joke(category=None):
    # Fetch joke
    try:
        joke = pyjokes.get_joke(category=category) if category else pyjokes.get_joke()
    except Exception:
        joke = pyjokes.get_joke()
    joke_history.append(joke)

    # Display and speak
    print("\nHere's your joke:")
    print(joke)
    voice_output(joke)

    # Laugh reaction
    laugh = random.choice(["Ha ha ha!", "He he he!", "Ho ho ho!"])
    print(laugh)
    voice_output(laugh)

    # Ask for rating
    while True:
        rating = input("Rate this joke from 1 (bad) to 5 (great): ").strip()
        if rating.isdigit() and 1 <= int(rating) <= 5:
            rating = int(rating)
            break
        print("Please enter a number between 1 and 5.")

    rating_history.append(rating)
    if rating >= 4:
        response = "Glad you liked it!"
    elif rating >= 2:
        response = "Thanks for your feedback! I'll try to do better."
    else:
        response = "Sorry that one missed the mark. I'll find a funnier one next time!"
    print(response)
    voice_output(response)


def show_history():
    if not joke_history:
        print("No jokes told yet.")
    else:
        print("\nJokes told this session:")
        for idx, j in enumerate(joke_history, 1):
            print(f"  {idx}. {j}")


def repeat_last():
    if not joke_history:
        print("No joke to repeat yet.")
    else:
        last = joke_history[-1]
        print("\nRepeating last joke:")
        print(last)
        voice_output(last)


def show_stats():
    count = len(joke_history)
    if count == 0:
        print("No jokes or ratings yet.")
    else:
        avg = sum(rating_history) / len(rating_history)
        print(f"\nTotal jokes told: {count}")
        print(f"Average rating: {avg:.2f} / 5")


def vjokes():
    print("Welcome to Jokes Program!")
    voice_output("Welcome to Jokes Program!")

    name = input("What's your name?: \n").strip()
    if name:
        greeting = f"Hi, {name}! Ready for some laughs?"
    else:
        greeting = "Hi there! Ready for some laughs?"
    print(greeting)
    voice_output(greeting)

    current_category = None
    print_commands()

    while True:
        try:
            print_commands()
            cmd = int(input("\nEnter command : "))

            match cmd:
                # tell a joke
                case 1:
                    tell_joke(current_category)

                # exit
                case 2:
                    farewell = "See you soon!"
                    print(farewell)
                    voice_output(farewell)
                    break

                # choose category
                case 3:
                    current_category = choose_category()

                # history
                case 4:
                    show_history()

                # repeat last
                case 5:
                    repeat_last()

                # stats
                case 6:
                    show_stats()
        except ValueError:
            print("Enter Valid Option.")
            voice_output("Sorry,Enter Valid Option.")


if __name__ == "__main__":
    try:
        vjokes()
    except KeyboardInterrupt:
        print("\nInterrupted. Goodbye!")
        sys.exit(0)
