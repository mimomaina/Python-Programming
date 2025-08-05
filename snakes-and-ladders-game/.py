import random

# Define snakes and ladders
snakes = {
    17: 7,
    54: 34,
    62: 19,
    64: 60,
    87: 36,
    93: 73,
    95: 75,
    98: 79
}

ladders = {
    4: 14,
    9: 31,
    20: 38,
    28: 84,
    40: 59,
    63: 81,
    71: 91,
    80: 100
}

def dice_roll():
    """Simulate a dice roll (1-6)"""
    return random.randint(1, 6)

def snake_and_ladder(pos):
    """Check if position is at base of ladder or head of snake"""
    # Check for ladders
    if pos in ladders:
        print(f"Lucky! Climbed a ladder from {pos} to {ladders[pos]}")
        return ladders[pos]
    
    # Check for snakes
    if pos in snakes:
        print(f"Oops! Bitten by a snake! Slid from {pos} to {snakes[pos]}")
        return snakes[pos]
    
    return pos

def get_position(player, pos):
    """Get updated position after checking snakes and ladders"""
    print(f"{player}'s current position: {pos}")
    return snake_and_ladder(pos)

def play_game():
    """Main game function"""
    print("Welcome to Snake and Ladder Game")
    print("Version: 1.0.0")
    print()
    print("Rules:")
    print("  1. All players start at position 0.")
    print("  2. Take turns rolling the dice.")
    print("  3. Land on a ladder to climb up.")
    print("  4. Land on a snake to slide down.")
    print("  5. First to reach exactly 100 wins!")
    print("  6. If roll exceeds 100, no move is made.")
    print()
    
    # Get number of players
    while True:
        try:
            num_players = int(input("How many players? (1-4): "))
            if 1 <= num_players <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get player names
    players = []
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ").strip()
        if not name:
            name = f"Player {i+1}"
        players.append({"name": name, "position": 0})
    
    print()
    print("Let's begin!")
    print()
    
    # Game loop
    winner = None
    turn = 0
    
    while not winner:
        current_player = players[turn % num_players]
        player_name = current_player["name"]
        
        input(f"{player_name}, press Enter to roll the dice...")
        
        roll = dice_roll()
        print(f"You rolled a {roll}")
        
        new_position = current_player["position"] + roll
        
        if new_position > 100:
            print(f"{player_name}, your roll would exceed 100. Stay at {current_player['position']}")
        else:
            current_player["position"] = new_position
            print(f"You move to position {new_position}")
            
            # Check for snakes and ladders
            current_player["position"] = get_position(player_name, current_player["position"])
            
            # Check for win
            if current_player["position"] == 100:
                winner = player_name
        
        print()  # Empty line for readability
        turn += 1
    
    print(f"Congratulations {winner}! You won the game!")

# Run the game
if __name__ == "__main__":
    play_game()