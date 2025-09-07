import random

def get_choices():
    player_choice = input("Enter a choice (Rock, Paper, Scissors:")
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    choices = {""}