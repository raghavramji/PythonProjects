import random
import time

# reads words into list
f = open("wordsmith_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()

letters = []

for i in range(7):
  startNum = ord('a')
  endNum = ord('z')
  randomNum = random.randint(startNum, endNum)
  letter = chr(randomNum)
  letters.append(letter)

score = 0


words = set()
print("Welcome to Wordsmith! In this game, come up woth as many words as you can using the 7 letters you are given. Press Enter to begin!")
print("Ready....")
time.sleep(1)
print("Set.....")
time.sleep(1)
print("Go!")


print("Your random letters are:")
print(letters)
  

while True:
  word_guess = input("Enter a word:")
  valid = True 
  for letter in word_guess:
    if letter not in letters:
      valid = False
  if valid:
    if word_guess in validWords and word_guess not in words:
      score += len(word_guess)
      words.add(word_guess)
      print("Valid word! Your score: " + str(score) + "\n")
    elif word_guess in words:
      print("You already entered this word! Your score: " + str(score) + "\n")
    else:
      print("Invalid word! Your score: " + str(score) + "\n")
  else:
    print("You can only use the 7 letters you were given!\n")












  
  


