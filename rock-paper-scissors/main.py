import random

def reset_score():
       score['user'] = 0
       score['computer'] = 0

lose_message = 'You lost!'
win_message = 'You won!'
tie_message = 'Tie!'

choices = ['rock', 'paper', 'scissors']
winner_matrix = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

user_input = ''
game_over = False
score = {'user': 0, 'computer': 0}
while not game_over:
       user_input = input('Type rock, paper, or scissors: ')
       computer_input = random.choice(choices)
       if user_input == computer_input:
              message = tie_message
       elif winner_matrix[user_input] == computer_input:
              message = win_message
              score['user'] += 1
       else:
              message = lose_message 
              score['computer'] += 1
       print(f'{message} You chose {user_input} and the computer chose {computer_input}. The current score is: You: {score["user"]} Computer: {score["computer"]}')
       
       # print result and restart game if user wants to play again
       if (score['user'] == 3 | score['computer'] == 3):
           if score['user'] == 3:
                  final_message = win_message
           else:
                  final_message = lose_message
           print(f'Game over!. {final_message} The final score is: You: {score["user"]} Computer: {score["computer"]}')
           game_over = input('Play again? (y/n) ') == 'n'
           reset_score()
           