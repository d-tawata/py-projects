import random
       
def check_game_end(score):
        game_end = score['user'] == 3 | score['computer'] == 3
        if (game_end):
            win_status = 'won!' if score['user'] == 3 else 'lost!'
            print(f'Game over!. You {win_status} The final score is: You: {score["user"]} Computer: {score["computer"]}')
        return game_end
        
def play_round(user_input, computer_input, score):
        lose_message = 'You lost!'
        win_message = 'You won!'
        tie_message = 'Tie!'
        
        winner_matrix = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    
        if user_input == computer_input:
                message = tie_message
        elif winner_matrix[user_input] == computer_input:
                message = win_message
                score['user'] += 1
        else:
                message = lose_message 
                score['computer'] += 1
        print(f'{message} You chose {user_input} and the computer chose {computer_input}. The current score is: You: {score["user"]} Computer: {score["computer"]}')
            
def main():
    choices = ['rock', 'paper', 'scissors']
    score = {'user': 0, 'computer': 0}
    
    while True:
        user_input = input('Type rock, paper, or scissors: ').lower()
        while user_input not in choices:
            user_input = input('Invalid input. Type rock, paper, or scissors: ').lower()
        computer_input = random.choice(choices)
        play_round(user_input, computer_input, score)
        
        if check_game_end(score):
            if input('Do you want to play again? (y/n) ') == 'n':
                break
            score = {'user': 0, 'computer': 0}
    
if __name__ == '__main__':
    main()