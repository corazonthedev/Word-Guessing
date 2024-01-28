import random

#-----------------------------------------------------------------------------------------------------------------

def line():
    for i in range(20):
        print("-",end="")
    print()

def get_word():
    words = ["dog","cat","car","sea","beach","horse"]
    return random.choice(words)
   
def display_word(word,guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print(f"word is {display}")

def display_guessed_letters(guessed_letters):
    guessed_letters.sort(key=lambda x: x.lower()) #SORT GUESEED
    print("guessed letters = ",end="")
    for letter in guessed_letters:
        print(f"{letter},",end="")
    print()
    
def check_guess(guess,guessed_letters,target_word):
    global life
    if guess in guessed_letters:
        print("alredy guessed!")
    elif guess.isdigit():
        print("no numbers allowed")
    elif guess in target_word and len(guess) == 1:
        print("correct! ",end="")
        guessed_letters.append(guess)             
    elif guess not in target_word and len(guess) == 1:
        print("wrong! ",end="")
        life -= 1
        guessed_letters.append(guess) 
    else:
        print("error")

def win(guessed_letters,target_word):
    global life, won
    if all(letter in "".join(guessed_letters) for letter in target_word):
        print(f"\nwon with {life} lifes!")
        won = True
        life = 0
        print("returning to main menu...\n")
        main_menu()
    else:
        won = False

def game_wordguess():
    global life, won
    life = 5
    won = False
    target_word = get_word()
    guessed_letters = [] 
    line()
    while life > 0 and won == False:
        print(f"current life is = {life}")
        display_word(target_word,guessed_letters) 
        guess = input("guess a letter: ").lower() 
        line()
        check_guess(guess,guessed_letters,target_word)
        display_guessed_letters(guessed_letters)
        win(guessed_letters,target_word)
    if life <= 0 and won == False:
        print("eliminated!")

#-----------------------------------------------------------------------------------------------------------------

def main_menu():
    selected = False
    while selected == False:
        try:
            select = input("play word guessing game(y/n): ").lower()
            selected = True
        except ValueError:
            print("Value Error")
    if select == "y":
        game_wordguess()
    elif select == "n":
        print("shutting down...")
    else:
        print("try again")
        main_menu()
        
def main():
    main_menu()
main()