import random

def is_win(player, opponent):
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
            return True

def play():
    user = input("Make your choice! 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return "You Won!"
    return "You LOST! :("

    

print(play())