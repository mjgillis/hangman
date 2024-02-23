import random
import os

os.system("clear")
list_of_words = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

word_chosen = random.choice(list_of_words).lower()
hidden_word = len(word_chosen) * "_"
lives = 5
guesses = []

print("Welcome to Hangman!")
print()
print(f"{hidden_word}")
#print(f"{word_chosen}") #Uncomment this to see answer

while lives > 0:
  win_condition = hidden_word.find("_")
  if win_condition == -1:
    print("Congratulations, you've won!")
    break
  else:
    print()
    print(f"You have {lives} lives remaining, choose wisely!")
    correct = False
    guess = input("Choose a letter: ").strip().lower()
    if guess in guesses:
      print("You've already guessed that letter")
      continue
    guesses.append(guess)
    print(f"Previous guesses: {guesses}")
    
    print()  
    for i in range(len(word_chosen)):
      if word_chosen[i] == guess:
        hidden_word = hidden_word[:i] + guess + hidden_word[i+1:]
        correct = True
        #print("You've chosen a correct letter!")
    print()
    print(f"{hidden_word}")
    
    if correct == False:
      lives -= 1
      print("You have guessed incorrectly")

if win_condition != -1:
  print("You have run out of lives!")
  print("Game over! Run program to try again")