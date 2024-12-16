class Fish:
    def __init__(self, health):
        self.health = health
        self.is_alive = True

    def take_damage(self, damage):
        if self.is_alive:
            self.health -= damage
            if self.health <= 0:
                self.health = 0
                self.is_alive = False

class Fisher:
    def __init__(self):
        self.attack_power = 50  # Attack power of the fisher

    def attack(self, fish):
        if isinstance(fish, Fish) and fish.is_alive:
            fish.take_damage(self.attack_power)  # Attack the fish
