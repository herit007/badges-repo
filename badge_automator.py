import webbrowser
import time
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    print("\n" + "="*50)
    print(f" {title}")
    print("="*50)

def automate_heart():
    print_header("Step 1: Heart On Your Sleeve ❤️")
    print("I am opening a GitHub Discussion for you.")
    print("ACTION: Click the ❤️ emoji on any comment.")
    time.sleep(2)
    webbrowser.open("https://github.com/orgs/community/discussions")
    input("\nPress Enter once you've clicked a heart...")

def automate_galaxy_brain():
    print_header("Step 2: Galaxy Brain 🧠")
    print("I am opening unanswered questions in Tailwind CSS.")
    print("\nCOPY THIS ANSWER:")
    print("-" * 20)
    print("It looks like you might need to check your tailwind.config.js to ensure the path to your files is correctly included in the content array. Also, try restarting your dev server to see if the styles apply correctly!")
    print("-" * 20)
    print("\nACTION: Find a question, paste that answer, and ask them to 'Mark as Answer'.")
    time.sleep(2)
    webbrowser.open("https://github.com/tailwindlabs/tailwindcss/discussions/categories/q-a?discussions_q=is%3Aopen+category%3AQ%26A+is%3Aunanswered")
    input("\nPress Enter once you've posted your answer...")

def automate_open_sourcerer():
    print_header("Step 3: Open Sourcerer 🧙‍♂️")
    print("I am opening a search for README typos.")
    print("ACTION: Click a file, click the pencil icon, fix a typo, and submit.")
    time.sleep(2)
    webbrowser.open("https://github.com/search?q=is%3Aopen+is%3Aissue+label%3Adocumentation+typo&type=issues")
    input("\nPress Enter once you've submitted your PR...")

def main():
    clear_screen()
    print("Welcome to the GitHub Badge Automator!")
    print("I will open the pages and give you the text to paste.")
    print("This is the fastest way to get your badges.")

    input("\nReady to start? Press Enter...")

    automate_heart()
    automate_galaxy_brain()
    automate_open_sourcerer()

    print_header("CONGRATULATIONS! 🎉")
    print("You've done the work. Now just wait 24-48 hours for GitHub to update your profile.")
    print("For 'Starstruck', remember to share this repo with 16 friends!")

if __name__ == "__main__":
    main()
