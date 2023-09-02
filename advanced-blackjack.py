import random
import time

print("Welcome to the game of Blackjack! You will get 2 cards dealt to you to start. The object of the game is to make sure all your cards add up to 21 without going over or busting. The dealer will give you 2 options: 1, Hit(get another card), 2, Stand(don't take a card). If the dealer's cards add up to more than yours or they get to 21 you lose.\n")

cards = {"2": 2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Jack":10,"Queen":10,"King":10,"Ace":1}

while True:
  card1 = random.randint(2,len(cards) -4)
  card2 = random.randint(2,len(cards) -4)
  
  card3 = random.randint(2,len(cards) -4)
  card4 = random.randint(2,len(cards) -4)
  
  continuegame = False
  
  players_cards = []
  
  players_cards.append(card1)
  players_cards.append(card2)
  
  dealers_cards = []
  
  dealers_cards.append(card3)
  

  print("Press Enter to play")
  input()
  print("Here is your hand")
  print(players_cards)
  if sum(players_cards) == 21:
    print("Blackjack!")
    
  if sum(players_cards) < 21:
    continuegame = True
  else:
    print("You busted!")
    
  while continuegame:
    hit_or_stand = input("Type in H to hit or S to stay:")
    if hit_or_stand == "H":
      continuegame = True
      card = random.randint(2,len(cards) -4)
      players_cards.append(card)
      print(players_cards)
      if sum(players_cards) == 21:
        print(card)
        print("You Win!")
        continuegame = False
        break
      if sum(players_cards) > 21:
        print("Here is your hand:")
        print(players_cards)
        print("You Busted!")
        continuegame = False
        break
    
    elif hit_or_stand == "S":
      print("Here is your hand:")
      print(players_cards)
      dealers_cards.append(card4)
      print("Here is dealer's hand:")
      print(dealers_cards)
      
      while continuegame:
        if sum(dealers_cards) > 21:
          print("Dealer busted, you win !!")
          continuegame = False
          break
        else:
          if sum(dealers_cards) > 17:
            print("Dealer has finalized his hand")
            print(dealers_cards)
            break
          else:
            card = random.randint(2,len(cards)-4)
            dealers_cards.append(card)
            print("Dealer chose hit.")
            time.sleep(2)
            print("Here is dealer's hand:")
            print(dealers_cards)
            continuegame = True
      if (continuegame):
        if sum(players_cards) < sum(dealers_cards):
          print("You lose :(")
        else:
          print("You win !")
          
      continuegame = False
      break
            
    else:
        print("Invalid input., please enter H or S.\n")
