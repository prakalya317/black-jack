############### Blackjack Project #####################

import art
import random
from replit import clear

def want_to_play_again():
  play_again = input("Do you want to start again? Type 'yes' or 'no': ")
  if play_again == 'yes':
    clear()
    black_jack()

def black_jack():
  should_continue = True
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  print(art.logo)
  player_cards = []
  computer_cards = []
  player_cards_sum = 0
  computer_cards_sum = 0
  for i in range (2):
    player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
  for card in player_cards:
    player_cards_sum += card

  print(f"Your cards: {player_cards}, current score: {player_cards_sum}")
  print(f"Computer's first card: {computer_cards[0]}")

  for card in computer_cards:
    computer_cards_sum += card

  if computer_cards_sum == 21:
    print("You lose😭 \nOpponent won with a blackjack..")
    want_to_play_again()
    
  elif player_cards_sum == 21:
    print("Win with a Blackjack😎")
    print(f"Your final hand: {player_cards}, your final score: {player_cards_sum}")
    print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_cards_sum}")
    want_to_play_again()

  while should_continue:
    cont = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if cont == 'y':
      new_card = random.choice(cards)
      if new_card == 11 and player_cards_sum >= 21:
        new_card == 1
      player_cards.append(new_card)
      player_cards_sum += new_card
      if player_cards_sum > 21:
        print("Bust.. You went over. You lose😭")
        print(f"Your final hand: {player_cards}, your final score: {player_cards_sum}")
        print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_cards_sum}")
        should_continue = False
        want_to_play_again()
      else:
        print(f"Your cards: {player_cards}, current score: {player_cards_sum}")
        print(f"Computer's first card: {computer_cards[0]}")
       # print(computer_cards)
  
    elif cont == 'n':
      should_continue = False
      while computer_cards_sum < 17:
        new_card_comp = random.choice(cards)
        computer_cards.append(new_card_comp)
        computer_cards_sum += new_card_comp
        if computer_cards_sum < player_cards_sum and player_cards_sum <= 21:
          print("YOU WIN!😎")
          print(f"Your final hand: {player_cards}, your final score: {player_cards_sum}")
          print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_cards_sum}")
          want_to_play_again()
        elif player_cards_sum > 21:
          print("Bust.. You went over. You lose😭")
          print(f"Your final hand: {player_cards}, your final score: {player_cards_sum}")
          print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_cards_sum}")
          want_to_play_again()
        elif computer_cards_sum == player_cards_sum:
          print("It is a draw")
          print(f"Your final hand: {player_cards}, your final score: {player_cards_sum}")
          print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_cards_sum}")
          want_to_play_again()
        elif computer_cards_sum > player_cards_sum and player_cards_sum <= 21 and computer_cards_sum > 21:
          print("YOU WIN!😎")
          print(f"Your final hand: {player_cards}, your final score: {player_cards_sum}")
          print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_cards_sum}")
          want_to_play_again()
        elif computer_cards_sum < 21 and computer_cards_sum > player_cards_sum and player_cards_sum < 21:
          print("You lose😭")
          print(f"Your final hand: {player_cards}, your final score: {player_cards_sum}")
          print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_cards_sum}")
          want_to_play_again()     
            
print("WELCOME TO THE GAME OF BLACKJACK")
option = input("Type 'rules' to read the rules or 'yes' to play the game. ").lower()
if option == 'rules':
  print("The deck is unlimited in size. \nThere are no jokers. \nThe Jack/Queen/King all count as 10.\nThe the Ace can count as 11 or 1.\nCards are not removed from the deck as they are drawn.\nThe computer is the dealer.")
  black_jack()
elif option == 'yes':   
  black_jack()
