import random  # For random movement

class Fish:
    def __init__(self):
        self.health = 100  # Health of the fish
        self.is_alive = True  # Status of the fish
        self.position = self.random_position()  # Random initial position

    def random_position(self):
        return (random.randint(0, 800), random.randint(0, 600))  # Random position within screen bounds

    def move(self):
        # Logic for fish movement
        if self.is_alive:
            new_x = self.position[0] + random.choice([-1, 1])
            new_y = self.position[1] + random.choice([-1, 1])
            # Boundary checks
            self.position = (max(0, min(new_x, 800)), max(0, min(new_y, 600)))  # Keep within bounds

    def take_damage(self):
        if self.is_alive:  # Only take damage if the fish is alive
            self.health -= 50  # Reduce health on attack
            if self.health <= 0:
                self.health = 0  # Ensure health does not drop below zero
                self.is_alive = False  # Fish dies
                effects.show_blood_effect()  # Show blood effect

    def reset(self):
        self.health = 100  # Reset health
        self.is_alive = True  # Reset status
        self.position = self.random_position()  # Reset position
