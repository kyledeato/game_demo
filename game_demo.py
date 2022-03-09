#developers: Kyle Deato, Yusan Yin, Peter Burnham, Alex Rodriguez, Logan Erspamer
import random

class Game:
    def __init__(self):
        self.status = 'Ongoing'
        self.turn_count = 0
    
    def show_matchup(self, player1, player2):
        player1.show_stats()
        player2.show_stats()
        return self

    def get_turn_count(self):
        print(self.turn_count)

    def check_status(self, player1, player2):
        if player1.health <= 0 or player2.health <= 0:
            self.status = 'Over'
            print('\nGame Over\n')
        if player1.health <= 0:
            print(f'{player2.name} has defeated {player1.name}!')
        elif player2.health <= 0:
            print(f'{player1.name} has defeated {player2.name}!')

class Player:
    def __init__( self , name ):
        self.name = name
        self.strength = 1
        self.speed = 1
        self.health = 10
        self.status = 'alive'

    def show_stats( self ):
        if self.health >= 0:
            print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        else:
            print(f"{self.name} is dead.")
            self.status = 'dead'

    def check_health(self):
        if self.health >= 0:
            print(f"{self.name} has {self.health} health remaining.\n")
        else:
            print(f"{self.name} is dead.")
            self.status = 'dead'

    def attack(self, game, other):
        if self.status == 'alive':
            print(f'Turn: {game.turn_count}')
            game.turn_count+= 1
            if other.status == 'alive':
                print(f'{self.name} attacks {other.name}.')
                hit_chance = random.randrange(1,10)
                crit_chance = random.randrange(1,10)
                move_selection = random.randrange(0,len(self.moveset))
                damage_dealt = self.moveset[move_selection].strength
            if hit_chance >= other.speed:
                if crit_chance > 7:
                    damage_dealt *= 2
                print('Critical Hit!!!')
                other.health -= damage_dealt
                print(f'{self.name} used {self.moveset[move_selection].name} on {other.name} and dealt {damage_dealt} damage')
            else:
                print(f'{self.name} used {self.moveset[move_selection].name} on {other.name} and missed!')
            other.check_health()
        return self

# A Move class has a name and strength we use to calculate damage dealt
class Move():
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

class Ninja(Player):
    def __init__(self, name):
        super(Ninja, self).__init__(name)
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.moveset = [Move('a Kunai', 8), Move('a Shuriken', 12), Move('Rasengan', 50)]
        # A moveset attribute is an array with a Move object in each

class Pirate(Player):
    def __init__(self, name):
        super(Pirate, self).__init__(name)
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.moveset = [Move('a Dagger', 8), Move('a Cutlass', 12), Move('a Gun', 40)]

game1 = Game()
ninja1 = Ninja('Naruto')
pirate1 = Pirate('Jack Sparrow')
game1.show_matchup(ninja1, pirate1)
print('Game Start\n')

while (game1.status == 'Ongoing'):
    ninja1.attack(game1, pirate1)
    pirate1.attack(game1, ninja1)
    game1.check_status(ninja1, pirate1)