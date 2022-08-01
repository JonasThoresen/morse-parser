# Imports
import os

# Constants
NAME = "Python Morse Parser"
VERSION = "1.0.0"
CHAR_LIST = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
             'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', '1', '2',
             '3', '4', '5', '6', '7', '8', '9',
             '0', '.', ',', '?', ''', '!', '/',
             '(', ')', '&', ':', ';', '=', '+',
             '-', '_', ''', 'Æ', 'Ø', 'Å']

MORSE_LIST = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
              "....", "..", ".---", "-.-", ".-..", "--", "-.",
              "---", ".--.", "--.-", ".-.", "...", "-", "..-",
              "...-", ".--", "-..-", "-.--", "--..", ".----", "..---",
              "...--", "....-", ".....", "-....", "--...", "---..", "----.",
              "-----", ".-.-.-", "--..--", "..--..", ".----.", "-.-.--", "-..-.",
              "-.--.", "-.--.-", ".-...", "---...", "-.-.-.", "-...-", ".-.-.-",
              "-....-", "..--.-", ".-..-.", ".-.-", "---.", ".--.-"]

MORSE_OPERATORS = ['-', '.', ' ']


# Functions
def response(response_type="init"):
    """ Print a pre-programmed text response """
    response_type = response_type.lower()

    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    if response_type == "init":
        clear()
        print(f"{NAME} V{VERSION}")
        print("The program reads your input and translates it to text or ")
        print("There is an automatic check to determine if the input is either")
        print("text or morse, and then the output is set to the opposite.")

    elif response_type == "reminder":
        print("Quit with :q")

    elif response_type == "clear":
        clear()

    elif response_type == "quit":
        print("Done parsing, quitting...")


def morse_to_text(morse):
    """ Convert morse data to characters"""
    text = ""
    split_morse = morse.split(' ')
    for morse_str in split_morse:
        try:
            tmp_pos = MORSE_LIST.index(morse_str)
            text += CHAR_LIST[tmp_pos]
        except ValueError:
            if morse_str == "":
                text += ' '
            else:
                print(f"Unknown morse pattern: {morse_str}")
                text += '?'
    return text


def text_to_morse(text):
    """ Convert text to morse"""
    morse = ""
    text = text.upper()
    for i, char in enumerate(text):
        if char == ' ':
            morse += ' '
        else:
            try:
                tmp_pos = CHAR_LIST.index(char)
                morse += MORSE_LIST[tmp_pos]
            except ValueError:
                print(f"Unknown character: {char}")
                morse += '?'

            if i < len(text)-1:
                morse += ' '
    return morse


# Startup
response("init")
parse_morse = True

# Main loop
while parse_morse:
    response("reminder")
    user_str = input("Parse: ")

    if (user_str.strip()).upper() == ":Q":
        parse_morse = False

    else:
        is_morse = True  # Default is txt -> morse
        if len(user_str) > 1:
            for char in user_str:
                if char not in MORSE_OPERATORS:
                    is_morse = False
        else:
            is_morse = False

        if is_morse:
            response("clear")
            print("Starting morse parsing")
            output = f"Text: {user_str}\nMorse: {morse_to_text(user_str)}"
            print(output)

        else:  # Assume characters -> morse
            response("clear")
            print("Starting character parsing")
            output = f"Morse: {user_str}\nText: {text_to_morse(user_str)}"
            print(output)

response("quit")  # When out of loop, display quit message
