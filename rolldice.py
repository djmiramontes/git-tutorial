import random

def roll_dice():
    # Generate three random numbers between 1 and 10
    roll1 = random.randint(1, 7)
    roll2 = random.randint(1, 7)
    roll3 = random.randint(1, 7)

    # Display the rolls
    print(f"Rolls: {roll1}, {roll2}, {roll3}")

    # Check if all three numbers match
    if roll1 == roll2 == roll3:
        if roll1 == 7:
            print("Congratulations! You won the jackpot!")
        else:
            print("Congratulations! You got three of a kind!")
    else:
        print("No match, try again!")

# Run the game
roll_dice()
