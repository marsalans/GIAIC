import random

def play():
    print("Choose any one: \n")
    user = input("'r' for Rock, 'p' for Paper, 's' for Scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a Tie!"
    
    if is_win(user, computer):
        return "You won!"
    else:
        return "You lost!"

def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

print(play())
