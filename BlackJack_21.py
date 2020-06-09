import random
import pyfiglet
banner = pyfiglet.figlet_format("Blackjack", font = "larry3d")
congrats = pyfiglet.figlet_format("Winner Winner", font = "big")
loser = pyfiglet.figlet_format("Loserrr", font = "cosmic")
print(banner)
print("BlackJack 21 ends when you either reach $5,000 or lose everything. Good luck!")
#Betting System
starting_bank = 500 
running_bank = starting_bank
# Dealer & Player cards
dealer_cards = []
player_cards = []
game_play = []
#Game is looping until scores are reached
while running_bank < 5000 and running_bank > 0:
    place_bet = (int(input(f"You currently have ${running_bank}. Place your bet $ ")))
    if place_bet <= running_bank:
        # Deal the cards
        running_bank = running_bank - place_bet
        while len(dealer_cards) != 2:
            dealer_cards.append(random.randint(1, 11))
            if len(dealer_cards) == 2:
                print("Dealer has ", dealer_cards[0], "and Unknown." )
        # Player Cards
        while len(player_cards) != 2:
            player_cards.append(random.randint(1, 11))
            if len(player_cards) == 2:
                print("You are showing a ", player_cards)
        # Sum of the Dealer cards
        if sum(dealer_cards) == 21:
            print("Dealer has 21 and wins!")
        # Sum of the Player cards
        if sum(player_cards) == 21 and sum(dealer_cards) == 21:
            print ("This round is a push")
        #Hit or Stay
        while sum(player_cards) < 21 and game_play != "end":
            action_taken = str(input("Do you want to stay or hit?  "))
            if action_taken == "hit" or action_taken == "h" :
                player_cards.append(random.randint(1, 11))
                print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
            else:
                print("The dealer is showing a " + str(sum(dealer_cards)) + " with ", dealer_cards)
                print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
                game_play = "end"
        #Dealer hits until surpasses 16
        while sum(dealer_cards) < 17 and sum(player_cards) <22:
            dealer_cards.append(random.randint(1, 11))
            print("Dealer flipped a ", dealer_cards[-1], dealer_cards, "with a total of ", sum(dealer_cards))

        # Winning Conditions between player and dealer
        if sum(player_cards) == sum(dealer_cards):
            print("It's a push")
        if sum(dealer_cards) <= 21 and sum(dealer_cards) > sum(player_cards):
            print("The House Wins!")
            running_bank = running_bank - place_bet
        if sum(player_cards) <= 21 and sum(player_cards)> sum(dealer_cards):
            print("You win!")
            running_bank = place_bet*2 + running_bank 
        if sum(dealer_cards) > 21:
            print("Dealer Busts with a ", sum(dealer_cards))
            running_bank = place_bet*2 + running_bank 
        if sum(player_cards) > 21:
            print("Player Busts")
            running_bank = running_bank - place_bet
        #Breaks while loop so that game can end
        if running_bank == 0 or running_bank >= 5000:
            break

        running_bank = running_bank + place_bet
        dealer_cards = []
        player_cards = []
        game_play = "alive"
    else:
        print("You don't have that much.")
if running_bank >= 5000:
    print(congrats)
else:
    print(loser)





