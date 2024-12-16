import fish  # Import fish management
import fisher  # Import fisher behavior
import effects  # Import effects handling
import random  # For random generation
import time  # For managing game duration

class Game:
    def __init__(self, victory_condition=10):
        self.fish_list = []  # List to hold fish objects
        self.score = 0  # Player's score
        self.time_left = 60  # Game duration in seconds
        self.fisher = fisher.Fisher()  # Create a fisher instance
        self.victory_condition = victory_condition  # Configurable victory condition

    def start_game(self):
        self.generate_fish()  # Generate initial fish
        start_time = time.time()  # Record the start time
        timer = self.time_left  # Initialize timer

        while timer > 0:
            self.update_game()  # Update game state
            self.check_victory()  # Check if player has won
            timer = self.time_left - (time.time() - start_time)  # Update remaining time
            ui.update_display(self.score, max(0, int(timer)))  # Update UI display
            time.sleep(1)  # Delay for a second for game loop

        if self.score < self.victory_condition:
            print("Time's up! You didn't win.")

    def generate_fish(self):
        for _ in range(5):  # Generate 5 fish initially
            new_fish = fish.Fish()  # Create a new fish
            self.fish_list.append(new_fish)  # Add to fish list

    def update_game(self):
        # Logic to update fish positions and check for attacks
        for f in self.fish_list:
            f.move()  # Move each fish
        # Handle user input for attacks
        if ui.check_attack():  # Check if the player has attacked
            self.handle_attack()  # Handle the attack

    def handle_attack(self):
        if not self.fish_list:  # Check if fish list is empty
            print("No fish to attack!")
            return

        for f in self.fish_list:
            if f.is_alive:  # Check if the fish is alive
                self.fisher.attack(f)  # Attack the fish
                if not f.is_alive:  # If the fish is dead
                    self.score += 1  # Increase score
                    effects.capture_feedback()  # Show capture feedback
                break  # Exit after attacking one fish

    def check_victory(self):
        if self.score >= self.victory_condition:  # Check victory condition
            print("You win!")
            self.time_left = 0  # End game

game_instance = Game(victory_condition=10)  # Create a game instance
