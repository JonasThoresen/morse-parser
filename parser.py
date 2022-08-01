# Imports
import os
import sys
import pyperclip

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
ACCEPTED_ARGS = ["-c", "-clipboard", "-h", "-help", "-r", "-retain"]
AUTO_CLIPBOARD = False
RETAIN = False

# Vars
performed_run = False

# Check sysargs
arguments = sys.argv

if len(arguments) > 1:
    # First entry is file name, so we remove it
    arguments.pop(0)
    # Iterate through the args
    for arg in arguments:
        low_arg = arg.lower()
        # If we find an accepted arg, act on it
        if low_arg in ACCEPTED_ARGS:
            if low_arg == "-c" or low_arg == "-clipboard":
                AUTO_CLIPBOARD = True
            elif low_arg == "-r" or low_arg == "-retain":
                RETAIN = True
            elif low_arg == "-h" or low_arg == "-help":
                print("This application can be run in several ways:"
                      "\n\n1. No system arguments, which means you "
                      "\nneed to copy the result manually "
                      "\n\n2. With the '-C' system argument, which "
                      "\nmakes the application automatically copy "
                      "\nthe result to the clipboard (like CTRL + C)."
                      "\n\n3. With the '-R' system argument, which "
                      "\ncauses the application to retain data once "
                      "\nit quits. If -R is not used, data is purged "
                      "\nonce quit."
                      "\n\nNote that system arguments can be chained."
                      "\n")
                input("Press enter to exit")
                quit()


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
        # Clean up clipboard if we used it
        if (AUTO_CLIPBOARD and performed_run and not RETAIN):
            pyperclip.copy("")

        # Then quit
        print("Done parsing, quitting...")
        quit()


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

    if AUTO_CLIPBOARD:
        pyperclip.copy(text)

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

    if AUTO_CLIPBOARD:
        pyperclip.copy(morse)

    return morse


# Startup
response("init")
parse_morse = True

# Main loop
while parse_morse:
    response("reminder")
    user_str = input("Parse: ")
    if user_str:
        print("hells yeah")
        if (user_str.strip()).lower() == ":q":
            parse_morse = False
            print(performed_run)

        else:
            performed_run = True
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
