class Pokemon:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = level * 10
        self.current_health = level * 10
        self.is_knocked_out = False
    
    def knock_out(self):
        self.is_knocked_out = True
        self.current_health = 0
    
    def revive(self):
        self.is_knocked_out = False
        self.current_health = self.max_health
    
    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            self.knock_out()
    
    def attack(self, other_pokemon):
        if self.is_knocked_out:
            print(f'{self.name} is knocked out and cannot attack!')
            return
        
        if self.type == 'fire' and other_pokemon.type == 'grass':
            other_pokemon.take_damage(self.level * 2)
            print(f'{self.name} attacked {other_pokemon.name} with a fire attack!')
        elif self.type == 'grass' and other_pokemon.type == 'water':
            other_pokemon.take_damage(self.level * 2)
            print(f'{self.name} attacked {other_pokemon.name} with a grass attack!')
        elif self.type == 'water' and other_pokemon.type == 'fire':
            other_pokemon.take_damage(self.level * 2)
            print(f'{self.name} attacked {other_pokemon.name} with a water attack!')
        else:
            other_pokemon.take_damage(self.level)
            print(f'{self.name} attacked {other_pokemon.name} with a normal attack!')

class Trainer:
    def __init__(self, name, pokemon_list, potions):
        self.name = name
        self.pokemon_list = pokemon_list
        self.potions = potions
        self.current_pokemon = 0
    
    def use_potion(self):
        if self.potions > 0:
            self.pokemon_list[self.current_pokemon].current_health += 10
            self.potions -= 1
            print(f'{self.name} used a potion on {self.pokemon_list[self.current_pokemon].name}!')
        else:
            print(f'{self.name} has no potions left!')
    
    def attack(self, other_trainer):
        my_pokemon = self.pokemon_list[self.current_pokemon]
        their_pokemon = other_trainer.pokemon_list[other_trainer.current_pokemon]
        my_pokemon.attack(their_pokemon)
        
        if their_pokemon.is_knocked_out:
            print(f'{their_pokemon.name} is knocked out!')
            other_trainer.choice

    def switch_pokemon(self, new_pokemon):
        if self.pokemon_list[new_pokemon].is_knocked_out:
            print(f'{self.pokemon_list[new_pokemon].name} is knocked out and cannot be switched in!')
            return
        
        if self.current_pokemon == new_pokemon:
            print(f'{self.pokemon_list[new_pokemon].name} is already in battle!')
            return
        
        self.current_pokemon = new_pokemon
        print(f'{self.name} switched to {self.pokemon_list[self.current_pokemon].name}!')

pikachu = Pokemon('Pikachu', 5, 'electric')
charmander = Pokemon('Charmander', 5, 'fire')
bulbasaur = Pokemon('Bulbasaur', 5, 'grass')
squirtle = Pokemon('Squirtle', 5, 'water')

ash = Trainer('Ash', [pikachu, charmander, bulbasaur, squirtle], 10)
misty = Trainer('Misty', [pikachu, charmander, bulbasaur, squirtle], 10)

ash.attack(misty)
misty.attack(ash)

ash.use_potion()
misty.use_potion()

ash.switch_pokemon(2)
misty.switch_pokemon(3)

ash.attack(misty)
misty.attack(ash)


    def choose_pokemon(self):
        print(f'{self.name} has the following Pokemon:')
        for i in range(len(self.pokemon_list)):
            print(f'{i + 1}. {self.pokemon_list[i].name}')
        
        choice = int(input('Choose a Pokemon: ')) - 1
        if choice < 0 or choice >= len(self.pokemon_list):
            print('Invalid choice!')
            return
        
        self.switch_pokemon(choice)

pikachu = Pokemon('Pikachu', 5, 'electric')
charmander = Pokemon('Charmander', 5, 'fire')
bulbasaur = Pokemon('Bulbasaur', 5, 'grass')
squirtle = Pokemon('Squirtle', 5, 'water')

ash = Trainer('Ash', [pikachu, charmander, bulbasaur, squirtle], 10)
misty = Trainer('Misty', [pikachu, charmander, bulbasaur, squirtle], 10)

ash.attack(misty)
misty.attack(ash)

ash.use_potion()
misty.use_potion()

ash.switch_pokemon(2)
misty.switch_pokemon(3)

ash.attack(misty)
misty.attack(ash)

ash.choose_pokemon()
misty.choose_pokemon()

