import random

# Function to create dice faces
def create_dice():
    dice_faces = {
        1: """
        +-------+
        |   1   |
        |   ●   |
        |       |
        +-------+
        """,
        2: """
        +-------+
        | ●     |
        |   2   |
        |     ● |
        +-------+
        """,
        3: """
        +-------+
        | ●  3  |
        |   ●   |
        |     ● |
        +-------+
        """,
        4: """
        +-------+
        | ●   ● |
        |   4   |
        | ●   ● |
        +-------+
        """,
        5: """
        +-------+
        | ● 5 ● |
        |   ●   |
        | ●   ● |
        +-------+
        """,
        6: """
        +-------+
        | ●   ● |
        | ● 6 ● |
        | ●   ● |
        +-------+
        """
    }
    return dice_faces

# Function to get valid number of players
def get_number_of_players():
    while True:
        try:
            players = int(input('Enter the number of players (2-4): '))
            if players < 2 or players > 4:
                print("Please enter a valid number of players (2-4).")
            else:
                return players
        except ValueError:
            print("Invalid input, please enter an integer between 2 and 4.")

# Function to handle a player's dice roll
def roll_dice(dice_faces):
    roll_value = random.randint(1, 6)  # Roll the dice
    print(f"You rolled: {roll_value}")
    print(dice_faces[roll_value])  # Display the dice face
    return roll_value

# Function to update player's score after rolling the dice
def update_score(roll_value, player_scores, current_player):
    
    player_scores[current_player] += roll_value  # Add roll to the player's total score
    print(f"Player {current_player + 1}'s current score: {player_scores[current_player]}")

# Function to check if a player has won the game
def check_winner(player_scores, max_score):
    for i, score in enumerate(player_scores):
        if score >= max_score:
            print(f"\nPlayer {i + 1} wins with {score} points!")
            return True  # Return True if there's a winner
    return False  # Return False if no one has won yet

# Function to handle the player's turn
def player_turn(current_player, player_scores, dice_faces, max_score):
    roll_option = input(f"Player {current_player + 1}, would you like to roll (y/n): ").lower()
    
    if roll_option == 'n':
        print(f"Player {current_player + 1} has chosen to skip their turn.")
    elif roll_option == 'y':
        total_roll = 0
        roll_value = roll_dice(dice_faces)  # Roll the dice and get the roll value
        total_roll += roll_value
        
        # Check if player rolled a 6 and allow a bonus roll
        while roll_value == 6:
            print("Bonus Roll! You rolled a 6, roll again!")
            roll_value = roll_dice(dice_faces)  # Bonus roll
            total_roll += roll_value

        update_score(total_roll, player_scores, current_player)  # Update the score based on the total rolls
        
        if check_winner(player_scores, max_score):  # Check if the player has won
            return True  # If someone won, end the game
    else:
        print("Invalid input. Please enter 'y' to roll or 'n' to skip the turn.")
    
    return False  # Continue game if no one has won

# Function to display current scores of all players
def display_scores(player_scores):
    print("\nCurrent scores:")
    for i, score in enumerate(player_scores):
        print(f"Player {i + 1}: {score} points")

# Main game loop
def roll():
    max_score = 20  # Set the maximum score to 20
    players = get_number_of_players()  # Get the number of players
    player_scores = [0] * players  # Initialize a list to store each player's score
    dice_faces = create_dice()  # Create dice faces

    # Game loop
    while True:
        for current_player in range(players):
            print(f"\nPlayer {current_player + 1}'s turn")

            if player_turn(current_player, player_scores, dice_faces, max_score):  # Check if someone won
                return  # End the game if there's a winner

            display_scores(player_scores)  # Display updated scores after each turn

# Run the main game loop
def main():
    roll()
    print("Game Over!😁👌")

# Start the game
main()
