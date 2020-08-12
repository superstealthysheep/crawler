import math
import random
import puzzle #Am I supposed to write .puzzle or not???

class Attack:
    #Future idea: healing moves could also fit into this class. I'd just need to make it so enemies don't avoid using it on themselves then.
    def __init__(self, name, base_damage):
        self.name = name
        self.base_damage = base_damage

punch = Attack("punch", 5)
kick = Attack("kick", 10)



    #def attack(self, target):

class Character: #Could I fit enemy and player both under a different class later? Maybe?
    id_counter = 0

    def __init__(self):
        self.health = 20
        self.attack_list = [punch, kick]
        self.attack_damage = 5 #maybe turn into leveling multiplier?
        self.species = "Lobster" #or may
        self.name = "Bobby"
        self.playable = False

        self.id = Character.id_counter
        Character.id_counter += 1

    def __str__(self):
        return("{} the {}".format(self.name, self.species))

    def carry_out_attack(self, target, attack, attack_damage): #come up with a better name for this
        target.health -= attack_damage
        print("{} used {} on {}, dealing {} damage! {} health left. \n".format(self.name, attack.name, target.name, attack_damage, target.health))

    def attack(self):
        #This is the part of the attack that is shared by both players and npcs
        print("{} is attaking.".format(self.name))

class Player(Character): #player is a subclass of Character
    def __init__(self):
        super().__init__() #first initializes Player as a Character
        self.playable = True #Then sets the playable attribute to True
        self.name = "Robby"

    def attack(self, combatants):

        super().attack()

        #======attack picking
        print("Pick attack:")
        str_attack_list = []
        for attack in self.attack_list:
            str_attack_list.append(attack.name)
        print(" ".join(str_attack_list)) # displays the attack list

        attack = None
        while attack == None:
            attack_input = input("> ") #try to find out if I can make a multiple choice selector?
            for atk_candidate in self.attack_list:
                if attack_input.upper() == atk_candidate.name.upper():
                    attack = atk_candidate
                    break
            if attack == None:
                print("That attack isn't on the list")

        #======target picking
        #THIS CODE IS PRETTY MUCH A COPY OF WHAT'S ABOVE. MAKE IT NOT REPEAT PLS
        print("Pick target:")
        str_target_list = []
        for target in combatants:
            str_target_list.append(target.name)
        print(" ".join(str_target_list)) # displays the attack list

        target = None
        while target == None:
            target_input = input("> ")
            for tgt_candidate in combatants:
                if target_input.upper() == tgt_candidate.name.upper():
                    target = tgt_candidate
                    break
            if target == None:
                print("That target isn't on the list")

        #======determining attack multiplier
        #This will eventually depend upon answering a question or something
        #attack_multiplier = 1
        attack_multiplier = puzzle.alg_puzzle()

        #======calculating attack damage
        attack_damage = math.floor(attack.base_damage * attack_multiplier)

        #======carrying out attack
        self.carry_out_attack(target, attack, attack_damage)


class Enemy(Character):
    def __init__(self):
        super().__init__()

    def attack(self, combatants):

        super().attack()

        #======attack picking
        attack = random.choice(self.attack_list) #picks an attack at random

        #======target picking
        possible_targets = combatants.copy() #have to do this copying to make these lists independent from each other\
        possible_targets.remove(self)
        #OLD CODE: why doesn't it work? possible_targets = combatants.copy().remove(self). SOLVED! Because .remove() doesn't return a value; it edits the list.

        #future: remove other combatants other than selves (e.g. teammates)
        print(possible_targets)
        target = random.choice(possible_targets)

        #======determining attack multiplier
        attack_multiplier = 2 * random.random()

        #======calculating attack damage
        attack_damage = math.floor(attack_multiplier * attack.base_damage)

        #======carrying out attack
        self.carry_out_attack(target, attack, attack_damage)
        #if

class Fight:
    def __init__(self, combatants):
        self.combatants = combatants
        self.winner = None

    def begin(self):
        """Begins the fight."""
        print("Fight!!!")
        #print(self.combatants)
        fight_over = False
        remaining_combatants = self.combatants.copy() #have to do this copying to make these lists independent from each other
        while not fight_over:
            for comb in remaining_combatants:

                if len(remaining_combatants) <= 1:
                    fight_over = True
                    continue #would it be better to put break here?

                if comb.health <= 0:
                    remaining_combatants.remove(comb)
                    print("{} was knocked out".format(comb.name))
                    continue
                comb.attack(remaining_combatants)



        self.winner = remaining_combatants[0]
        print("Fight over! Winner: {}".format(self.winner.name))

test = Enemy()
test2 = Player()
#print(test)
#print(test2.name)

fight1 = Fight([test, test2])
#fight1.begin()
l = [test, test2]

#test2.attack(l)
