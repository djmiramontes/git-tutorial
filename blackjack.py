import random

# function to get a card's value
def get_card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

# Function to calculate the total score of a hand, handling Aces
def calculate_score(hand):
    score = sum(get_card_value(card) for card in hand)
    # Adjust for Aces if score is over 21
    num_aces = hand.count('A')
    while score > 21 and num_aces > 0:
        score -= 10  # Change Ace from 11 to 1
        num_aces -= 1
    return score

# Initialize a deck of cards
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

# Function to draw a hand of two cards
def draw_hand():
    return [random.choice(deck) for _ in range(2)]

# Deal initial hands
player_hand = draw_hand()
dealer_hand = draw_hand()

# Calculate scores
player_score = calculate_score(player_hand)
dealer_score = calculate_score(dealer_hand)

# Display hands and scores
print(f"Player's hand: {player_hand} (Score: {player_score})")
print(f"Dealer's hand: {dealer_hand} (Score: {dealer_score})")

# Determine the winner
if player_score > 21:
    print("Player busts! Dealer wins.")
elif dealer_score > 21:
    print("Dealer busts! Player wins.")
elif player_score > dealer_score:
    print("Congratulations! Player wins.")
elif dealer_score > player_score:
    print("Dealer wins.")
else:
    print("It's a tie!")
