from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur()
        self.robot = Robot()
      
    
    
          
    def run_game(self):
        self.display_welcome()
        self.battle_phase
     
    def display_welcome(self):
        print("\nwelcome to an epic battle for the ages!\nOnly one side can win!\n")

    def battle_phase(self):
        # self.attack_power_point_reducer = 20 (20x2=100hp) means dino lose all 100hp=0
        
        
        while self.dinosaur.attack:
            if self.active.weapon == "laser beam":
                print("dinosaur.health -= self.active_weapon.attack_power_point_reducer *  2")
    
        
    print("STARTING BATTLEPHASE!!!")
       
    def display_winner(self, Robot):
        self.winner = Robot


    print("Robot wins!!!")     
