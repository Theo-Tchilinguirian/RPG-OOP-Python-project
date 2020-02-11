###################################################
# This module defines the functions used in-game
# Made by Théo Tchilinguirian, Saturday 08/02/2020
###################################################


# Imports # ------------------------------------------------------------------------------------------------------------

import os
import pickle
import random
# import pygame
# import tkinter


# Classes Definitions # ------------------------------------------------------------------------------------------------

class Player:

    def __init__(self, cls, lvl, mon, hp, atk, dfs, chp, klc, bhp, kcm):

        self.player_stats = {'CLASS': cls, 'LEVEL': lvl, 'MONEY': mon, 'HP': hp, 'ATTACK': atk, 'DEFENSE': dfs,
                              'CHAPTER': chp, 'KILLCOUNT': klc, 'BASEHP': bhp, 'KILLCOUNTMAX': kcm}

    def set_stat_value(self, stat_key, stat_new_value):

        self.player_stats[stat_key] = stat_new_value


    def get_player_stats(self):

        return self.player_stats


    def set_current_new_chapter(self, player_list, pseudonyme):

        current_chapter = self.player_stats['CHAPTER']

        if current_chapter == 'I: THE RUINS':
            new_chapter = 'II: DESOLATED LAND'

        elif current_chapter == 'II: DESOLATED LAND':
            new_chapter = 'III: CURSED TOWER'

        elif current_chapter == 'II: DESOLATED LAND':
            new_chapter = 'III: CURSED TOWER'

        elif current_chapter == 'III: CURSED TOWER':
            new_chapter = 'IV: MISTYC STAGE'

        self.set_stat_value('CHAPTER', new_chapter)

        player_entity = self
        player_list[pseudonyme][1] = player_entity

        return player_list, player_entity


    def act_player_attacking(self):

        pass
        if 'VIGOR' in self.player_stats:
            pass
        elif 'MANA' in self.player_stats:
            pass


    def player_level_up(self, player_list, pseudonyme):

        kill_count_max = self.player_stats['KILLCOUNTMAX']
        current_player_kill_count = self.get_player_stats()['KILLCOUNT']

        if current_player_kill_count % kill_count_max == 0:

            for stat_key, current_stat_value in self.player_stats.items():

                if stat_key == 'LEVEL' or stat_key == 'KILLCOUNTMAX':
                    self.set_stat_value(stat_key, current_stat_value + 1)

                elif stat_key == 'BASEHP':
                    new_stat_value = round(current_stat_value + (current_stat_value * 15) / 100)
                    self.set_stat_value(stat_key, new_stat_value)
                    self.set_stat_value('HP', new_stat_value)  # The player gets full hp every level

                elif stat_key == 'BASEMANA' or stat_key == 'BASEMANA' or stat_key == 'BASEVIGOR':
                    new_stat_value = round(current_stat_value + (current_stat_value * 15) / 100)
                    self.set_stat_value(stat_key, new_stat_value)
                    self.set_stat_value(stat_key[4:], new_stat_value)

                elif stat_key == 'ATTACK' or stat_key == 'DEFENSE':
                    new_stat_value = round(current_stat_value + (current_stat_value / 10))
                    self.set_stat_value(stat_key, new_stat_value)

        player_entity = self
        player_list[pseudonyme][1] = player_entity

        current_level = self.player_stats['LEVEL']
        print("Congrats ! You are now level {}.".format(current_level))

        return player_list, player_entity


class Warrior(Player):

    def __init__(self, vig = 80, bvg = 80):
        Player.__init__(self, cls = 'Warrior', lvl = 1, mon = 0, hp = 100, atk = 35, dfs = 35, chp = 'I: THE RUINS', klc = 0, bhp = 100, kcm = 5)
        self.set_stat_value('VIGOR', vig)
        self.set_stat_value('BASEVIGOR', bvg)


class Soldier(Player):

    def __init__(self, vig = 90, bvg = 90):
        Player.__init__(self, cls='Soldier', lvl = 1, mon = 0, hp = 90, atk = 40, dfs = 60, chp = 'I: THE RUINS', klc = 0, bhp = 90, kcm = 5)
        self.set_stat_value('VIGOR', vig)
        self.set_stat_value('BASEVIGOR', bvg)


class Gladiator(Player):

    def __init__(self, vig = 100, bvg = 100):
        Player.__init__(self, cls='Gladiator', lvl = 1, mon = 0, hp = 80, atk = 35, dfs = 35, chp = 'I: THE RUINS', klc = 0, bhp = 80, kcm = 5)
        self.set_stat_value('VIGOR', vig)
        self.set_stat_value('BASEVIGOR', bvg)


class Mage(Player):

    def __init__(self, mana = 90, bmn = 90):
        Player.__init__(self, cls='Mage', lvl = 1, mon = 0, hp = 100, atk = 25, dfs = 35, chp = 'I: THE RUINS', klc = 0, bhp = 100, kcm = 5)
        self.set_stat_value('MANA', mana)
        self.set_stat_value('BASEMANA', bmn)


class Sorcerer(Player):

    def __init__(self, mana = 80, bmn = 80):
        Player.__init__(self, cls='Sorcerer', lvl = 1, mon = 0, hp = 110, atk = 30, dfs = 30, chp = 'I: THE RUINS', klc = 0, bhp = 110, kcm = 5)
        self.set_stat_value('MANA', mana)
        self.set_stat_value('BASEMANA', bmn)



class Priest(Player):

    def __init__(self, mana = 110, bmn = 110):
        Player.__init__(self, cls='Priest', lvl = 1, mon = 0, hp = 75, atk = 20, dfs = 25, chp = 'I: THE RUINS', klc = 0, bhp = 75, kcm = 5)
        self.set_stat_value('MANA', mana)
        self.set_stat_value('BASEMANA', bmn)


# Ennemy Entities #

class Ennemy:

    def __init__(self, typ, hp, atk, dfs, chp):
        self.ennemy_stats = {'TYPE': typ, 'HP': hp, 'ATTACK': atk, 'DEFENSE': dfs, 'CHAPTER': chp}


    def set_stat_value(self, stat_key, stat_new_value):
        self.ennemy_stats[stat_key] = stat_new_value


    def get_ennemy_stats(self):

        return self.ennemy_stats


class Bat(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Bat', hp = 5, atk = 3, dfs = 0, chp = 'I: THE RUINS')


class Slime(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Slime', hp = 10, atk = 5, dfs = 0, chp = 'I: THE RUINS')


class Spider(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Spider', hp = 15, atk = 8, dfs = 3, chp = 'I: THE RUINS')


class RabidWolf(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Rabid Wolf', hp = 25, atk = 12, dfs = 5, chp = 'II: DESOLATED LAND')


class DarkWizard(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Dark Wizard', hp = 50, atk = 20, dfs = 10, chp = 'II: DESOLATED LAND')


class CorruptedSpirit(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Corrupted Spirit', hp = 75, atk = 25, dfs = 8, chp = 'II: DESOLATED LAND')


class Skeleton(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Skeleton', hp = 40, atk = 10, dfs = 5, chp = 'III: CURSED TOWER')


class Goblin(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Goblin', hp = 10, atk = 5, dfs = 8, chp = 'III: CURSED TOWER')


class FallenWarrior(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Fallen Warrior', hp = 65, atk = 25, dfs = 15, chp = 'III: CURSED TOWER')


class Dragon(Ennemy):

    def __init__(self):
        Ennemy.__init__(self, typ = 'Dragon', hp = 250, atk = 45, dfs = 25, chp = 'IV: MISTYC STAGE')


# File Manipulation Functions Definitions # ----------------------------------------------------------------------------

def charge_file():
    if os.path.exists('../DataPack/DataFile'):
        with open('../DataPack/DataFile', 'rb') as charge_file:
            file_depickler = pickle.Unpickler(charge_file)
            player_list = file_depickler.load()
    else:
        player_list = dict()

    return player_list


def save_file(player_list):
    with open('../DataPack/DataFile', 'wb') as save_file:
        file_pickler = pickle.Pickler(save_file)
        file_pickler.dump(player_list)


# Input/Print and Conditions Functions # -------------------------------------------------------------------------------

def check_answer_get_yes_no(question):
    answer = ""
    while answer.lower() != 'yes' and answer.lower() != 'no':
        print(question)
        answer = input(">>> ")
        if answer.lower() != 'yes' and answer.lower() != 'no':
            print("Answer by 'yes' or 'no'.")

    return answer.lower()


def start_screen():
    print(100 * '-' + '\n' + "Welcome to... 'RPG-The Game' !!".center(100) + '\n' + (75 * '-').center(100) + '\n')


def welcome(pseudonyme, chapter):
    print(100 * '-' + '\n' + "Welcome, {}, to CHAPTER {} . . .".center(100).format(pseudonyme, chapter) + '\n' + (75 * '-').center(100))


def show_player_list(player_list):
    print("Player list:")
    for players in player_list.keys():
        print(players)


def check_answer_get_class_stats():
    end = False
    while end == False:
        try:
            answer_class = int(input("""What class do you want to be ?
            EASY:
            1. Warrior
            2. Mage

            MEDIUM:
            3. Soldier
            4. Sorcerer

            HARD:
            5. Gladiator
            6. Priest
            >>> """))
            end = True

        except ValueError:
            print("Your answer is not correct. Choose a number between 1 and 6")
            continue

        if answer_class == 1:
            return 'Warrior'
        elif answer_class == 2:
            return 'Mage'
        elif answer_class == 3:
            return 'Soldier'
        elif answer_class == 4:
            return 'Sorcerer'
        elif answer_class == 5:
            return 'Gladiator'
        elif answer_class == 6:
            return 'Priest'
        else:
            print("Your answer is not correct. Choose a number between 1 and 6")
            continue


def ask_change_chapter(player_list, pseudonyme, player_entity):
    player_current_level = player_entity.get_player_stats()['LEVEL']
    player_current_chapter = player_entity.get_player_stats()['CHAPTER']
    if player_current_level % 5 == 0 and player_current_chapter != 'IV: MISTYC STAGE':

        answer = check_answer_get_yes_no("You are level {}. Do you want do go to the next chapter ?". format(player_current_level))
        if answer == 'yes':
            player_entity.set_current_new_chapter(player_list, pseudonyme)
        else:
            print("I won't be there for you at any time...")


# Job Functions # ------------------------------------------------------------------------------------------------------

def player_entity_maker(player_list, pseudonyme, password):
    """
    Tied to 'check_answer_get_class_stats'
    adds a player with default settings to the player list
    """

    end = False
    while end == False:
        cls = check_answer_get_class_stats()
        if cls == 'Warrior':
            player_entity = Warrior()
            end = True
        elif cls == 'Mage':
            player_entity = Mage()
            end = True
        elif cls == 'Soldier':
            player_entity = Soldier()
            end = True
        elif cls == 'Sorcerer':
            player_entity = Sorcerer()
            end = True
        elif cls == 'Gladiator':
            player_entity = Gladiator()
            end = True
        elif cls == 'Priest':
            player_entity = Priest()
            end = True
        else:
            continue

    player_list[pseudonyme] = [password, player_entity]

    return player_list, pseudonyme, password, player_entity


def current_ennemy_entity_maker(player_list, pseudonyme):
    player_entity = player_list[pseudonyme][1]
    current_chapter = player_entity.get_player_stats()['CHAPTER']
    current_ennemy_spawned_type_range = random.randint(1, 100)

    if current_chapter == 'I: THE RUINS':
        if 0 < current_ennemy_spawned_type_range <= 40:  # 40% chances to appear
            current_ennemy = Slime()

        elif 40 < current_ennemy_spawned_type_range <= 75:
            current_ennemy = Bat()

        elif 75 < current_ennemy_spawned_type_range <= 100:
            current_ennemy = Spider()

    elif current_chapter == 'II: DESOLATED LAND':
        if 0 < current_ennemy_spawned_type_range <= 75:
            current_ennemy = RabidWolf()

        elif 75 < current_ennemy_spawned_type_range <= 90:
            current_ennemy = DarkWizard()

        elif 90 < current_ennemy_spawned_type_range <= 100:
            current_ennemy = CorruptedSpirit()

    elif current_chapter == 'III: CURSED TOWER':
        if 0 < current_ennemy_spawned_type_range <= 25:
            current_ennemy = Skeleton()

        elif 25 < current_ennemy_spawned_type_range <= 85:
            current_ennemy = Goblin()

        elif 85 < current_ennemy_spawned_type_range <= 100:
            current_ennemy = FallenWarrior()

    elif current_chapter == 'IV: MISTYC STAGE':  # 100% chances to appear
        current_ennemy = Dragon()

    return current_ennemy


def check_login(player_list, pseudonyme, password):
    if player_list[pseudonyme][0] == password:
        return True
    else:
        return False


def player_in_player_list(player_list, pseudonyme):
    if pseudonyme in player_list.keys():
        return True
    else:
        return False


def ennemy_entity_maker(Type, hp, ):
    pass
    # if Type == Undead and player.cls == "Priest":
    #     damage_done += damage_done / 10  # 10% more damage done by the priest on undead ennemies


def next_level():
    pass
    """
    changer les stats des persos
    """
    # if lvl == 5:
    #     if perso[class] == gladiator:
    #         perso[class] == hoplite, puis au lvl 10: spartiate


def get_check_pseudonyme(pseudonyme):
    if len(pseudonyme) <= 4:
        print('')


def get_check_password(password):
    if len(password) <= 4:
        print('')


def get_player_attack_points_on_ennemy(player_entity, current_ennemy):
    player_attack_points = player_entity.get_player_stats()['ATTACK']
    current_ennemy_defense_points = current_ennemy.get_ennemy_stats()['DEFENSE']

    if player_attack_points > current_ennemy_defense_points:
        player_attack_points_on_ennemy = player_attack_points - current_ennemy_defense_points

    else:
        player_attack_points_on_ennemy = 1

    return player_attack_points_on_ennemy


def get_ennemy_attack_points_on_player(player_entity, current_ennemy):
    current_ennemy_attack_points = current_ennemy.get_ennemy_stats()['ATTACK']
    player_defense_points = player_entity.get_player_stats()['DEFENSE']

    if current_ennemy_attack_points > player_defense_points:
        current_ennemy_attack_points_on_player = current_ennemy_attack_points - player_defense_points

    else:
        current_ennemy_attack_points_on_player = 1

    return current_ennemy_attack_points_on_player


def player_attack_on_ennemy(player_attack_points_on_ennemy, current_ennemy):
    current_ennemy_hp = current_ennemy.get_ennemy_stats()['HP']

    if current_ennemy_hp <= player_attack_points_on_ennemy:
        current_ennemy_new_hp = 0

    else:
        current_ennemy_new_hp = current_ennemy_hp - player_attack_points_on_ennemy

    current_ennemy.set_stat_value('HP', current_ennemy_new_hp)

    # Does not return anything, works directly on the ennemy object that stays changed even out of the function


def ennemy_attack_on_player(current_ennemy_attack_points_on_player, player_entity):
    player_hp = player_entity.get_player_stats()['HP']

    if player_hp <= current_ennemy_attack_points_on_player:
        player_new_hp = 0

    else:
        player_new_hp = player_hp - current_ennemy_attack_points_on_player

    player_entity.set_stat_value('HP', player_new_hp)

    # Does not return anything, works directly on the player object that stays changed even out of the function


def get_who_attacks_first():
    random_half = random.randint(1, 100)

    if 0 < random_half <= 100:
        return 'PLAYER'

    else:
        return 'ENNEMY'

# Main Functions # ------------------------------------------------------------------------------------------------------

def login(player_list):
    """
    This function is used by the 'player_entity_maker' function to create a new player
    It is the input function associated with the 'player_entity_maker'
    It is the first function runned after the start screen
    It allows to create players depending on conditions
    """

    if len(player_list) > 0:
        show_player_list(player_list)

    pseudonyme = input("""What is your pseudonyme?:
            >>> """)

    if player_in_player_list(player_list, pseudonyme) == False:

        if len(player_list) > 0:
            show_player_list(player_list)

            answer = check_answer_get_yes_no("Do you want to create a new player with the pseudonyme {} ?".format(pseudonyme))

            if answer == 'yes':
                password = input("""What is your password ?:
                        >>> """)

                player_list, pseudonyme, password, player_entity = player_entity_maker(player_list, pseudonyme, password)
                return player_list, pseudonyme, password, player_entity

            else:
                login(player_list)

        else:
            print("You have to create a player")
            answer = check_answer_get_yes_no("Do you want to create a new player with the pseudonyme {} ?".format(pseudonyme))

            if answer == 'yes':
                password = input("""What is your password ?:
                        >>> """)

                player_list, pseudonyme, password, player_entity = player_entity_maker(player_list, pseudonyme, password)
                return player_list, pseudonyme, password, player_entity

            else:
                login(player_list)

            password = input("""What is your password ?:
                    >>> """)

            player_list, pseudonyme, password, player_entity = player_entity_maker(player_list, pseudonyme, password)
            return player_list, pseudonyme, password, player_entity

    else:
        end = False
        while end == False:
            password = input("""What is your password ?:
                    >>> """)

            if check_login(player_list, pseudonyme, password) == True:
                end = True

            else:
                print("Wrong password")
                continue

        player_entity = player_list[pseudonyme][1]
        password = player_list[pseudonyme][0]
        return player_list, pseudonyme, password, player_entity


def main(player_list):
    start_screen()
    player_list, pseudonyme, password, player_entity = login(player_list)
    welcome(pseudonyme, player_entity.get_player_stats()['CHAPTER'])
    player_entity.player_level_up(player_list, pseudonyme)
    ask_change_chapter(player_list, pseudonyme, player_entity)
    print(player_entity.player_stats)
    current_ennemy = current_ennemy_entity_maker(player_list, pseudonyme)
    print(current_ennemy.ennemy_stats)
    player_attack_points_on_ennemy = get_player_attack_points_on_ennemy(player_entity, current_ennemy)
    current_ennemy_attack_points_on_player = get_ennemy_attack_points_on_player(player_entity, current_ennemy)
    player_attack_on_ennemy(player_attack_points_on_ennemy, current_ennemy)
    print(current_ennemy.ennemy_stats)
    ennemy_attack_on_player(current_ennemy_attack_points_on_player, player_entity)
    print(player_entity.player_stats)

player_list = charge_file()
main(player_list)
save_file(player_list)