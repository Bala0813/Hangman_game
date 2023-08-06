import Hangman
import random

word_to_find = random.choice(Hangman.sample_words)
print("Welcome to the Hangman game!")
word_frame = ["_"]*len(word_to_find)
print(word_frame)

chance = True
chance_num = -1
while chance:
    letter_guess = input("Guess the letter:").lower()
    if letter_guess in word_to_find and letter_guess not in word_frame:
        for i in range(0, len(word_to_find)):
            if word_to_find[i] == letter_guess:
                word_frame[i] = letter_guess
        print(word_frame)
        if "_" not in word_frame:
            print("Successful, you won!")
            chance = False
    else:
        chance_num += 1
        print("The guessed letter is wrong, reducing the life time.")
        print(Hangman.hangman_diagram[chance_num])
    if chance_num == 6:
        chance = False
        print("You lose!, the word to be guessed is {}.".format(word_to_find))
