import pyjokes
import pyttsx3
import random  # For random laughing styles


def voice_output(text: str):
    """
    Function to output text as speech using pyttsx3.
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speech rate
    engine.setProperty('volume', 1.0)  # Set volume to maximum
    engine.say(text)
    engine.runAndWait()


def vjokes():
    """
    Function to tell jokes and engage in a human-like conversation.
    """
    print("Hi there! Ready for some laughs?")
    voice_output("Hi there! Ready for some laughs?")

    while True:
        # Generate and tell a joke
        print("\nHere's a joke for you:")
        voice_output("Here's a joke for you:")

        joke = pyjokes.get_joke()
        print(joke)
        voice_output(joke)

        # Laugh after the joke
        laughs = ["Ha ha ha!", "He he he!", "Ho ho ho!"]
        laugh = random.choice(laughs)
        print(laugh)
        voice_output(laugh)


        # Ask the user if they want another joke
        voice_output("Do you want to Continue? yes or no: ")
        if input("\n Continue? (y/n):").lower() not in ['y', 'yes']:
            print("See You Soon...")
            voice_output("See You Soon..")
            break # End the loop


# Main execution block
if __name__ == "__main__":
    vjokes()
