class Dinosaur:

    def __init__(self):
        self.name = "Dino"
        self.attack_power_point_reducer = 20
        self.health = 100

    def attack(self, robot):
        
        robot.health -= self.active_weapon.attack_power_point_reducer * 5
        print(f"{self.name} attacked {robot.name} for {self.active_weapon.attack_power_point_reducer}")


