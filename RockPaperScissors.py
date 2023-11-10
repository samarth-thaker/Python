import random
def play():
    user = input(" Your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    if user==computer:
        return "tie"
    if isWin(user, computer):
        return 'You won'
   
    return "You lost"
def isWin(player, opponent):
    if(player=='r' and opponent=='s') or (player=='p' and opponent == 'r') or (player=='s' and opponent=='p'):
        return True
    
    