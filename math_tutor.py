# import modules
from random import randrange as r
from time import time as t
# ask how many questions user wants
num_questions = int(input('How many questions your want? '))
# ask the highest number from the user 
max_num = int(input('What the highest number should be? '))
# set score start at zero
score = 0
# capturing time before the game
time_before = t()
# creating empty list which we will populated with records
records = []
# loop through number of questions
for i in range(num_questions):
# create two random numbers and calc answer
    num1 = r(1,max_num + 1) # suppose the num is 5
    num2 = r(1,max_num + 1) # suppose the num is 2
    answer = num1 * num2 # suppose the num is 10
    # capture answer and modify user score
    user_answer = int(input((f"{num1} X {num2} = ")))
    # save the question and its answer vs your answer
    records.append(f'{num1} X {num2} = {answer}, your answer was: {user_answer}.')
    if answer == user_answer:
        score += 1
percentage_score = round(score / num_questions * 100)
# capturing time after the game
time_after = t()
time_spent = round(time_after - time_before, 2)
# output final score 
print(f'Thanks for playing. Your score is {score} out of {num_questions}. \nYour percentage is {percentage_score}.Time spent: {time_spent} seconds.')
# loop through the list and show each record line by line
for record in records:
    print(record)