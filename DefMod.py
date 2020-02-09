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

    def __init__(self, cls, lvl, mon, hp, atk, dfs, chp, klc):
        self.player_stats = {'CLASS': cls, 'LEVEL': lvl, 'MONEY': mon, 'HP': hp, 'ATTACK': atk, 'DEFENSE': dfs, 'CHAPTER': chp, 'KILLCOUNT': klc}

    def set_stat_value(self, stat_key, stat_new_value):
        self.player_stats[stat_key] = stat_new_value

    def get_player_stats(self):
        return self.player_stats


class Warrior(Player):

    def __init__(self, vig = 80):
        Player.__init__(self, cls = 'Warrior', lvl = 0, mon = 0, hp = 100, atk = 35, dfs = 35, chp = 'I: THE RUINS', klc = 0)
        self.player_stats["VIGOR"] = vig


class Soldier(Player):

    def __init__(self, vig = 90):
        Player.__init__(self, cls='Soldier', lvl=0, mon=0, hp=90, atk=40, dfs=60, chp = 'I: THE RUINS', klc = 0)
        self.player_stats["VIGOR"] = vig


class Gladiator(Player):

    def __init__(self, vig = 100):
        Player.__init__(self, cls='Gladiator', lvl=0, mon=0, hp=80, atk=35, dfs=35, chp = 'I: THE RUINS', klc = 0)
        self.player_stats["VIGOR"] = vig


class Mage(Player):

    def __init__(self, mana = 90):
        Player.__init__(self, cls='Mage', lvl=0, mon=0, hp=100, atk=25, dfs=35, chp = 'I: THE RUINS', klc = 0)
        self.player_stats["MANA"] = mana


class Sorcerer(Player):

    def __init__(self, mana = 80):
        Player.__init__(self, cls='Sorcerer', lvl=0, mon=0, hp=110, atk=30, dfs=30, chp = 'I: THE RUINS', klc = 0)
        self.player_stats["MANA"] = mana



class Priest(Player):

    def __init__(self, mana = 110):
        Player.__init__(self, cls='Priest', lvl=0, mon=0, hp=75, atk=20, dfs=25, chp = 'I: THE RUINS', klc = 0)
        self.player_stats["MANA"] = mana




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
    condition = 1
    while condition == 1:
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
            condition = 0

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


# Job Functions # ------------------------------------------------------------------------------------------------------

def player_entity_maker(player_list, pseudonyme, password):
    """
    Tied to 'check_answer_get_class_stats'
    adds a player with default settings to the player list
    """

    condition = 1
    while condition == 1:
        cls = check_answer_get_class_stats()
        if cls == 'Warrior':
            player_entity = Warrior()
            condition = 0
        elif cls == 'Mage':
            player_entity = Mage()
            condition = 0
        elif cls == 'Soldier':
            player_entity = Soldier()
            condition = 0
        elif cls == 'Sorcerer':
            player_entity = Sorcerer()
            condition = 0
        elif cls == 'Gladiator':
            player_entity = Gladiator()
            condition = 0
        elif cls == 'Priest':
            player_entity = Priest()
            condition = 0
        else:
            continue

    player_list[pseudonyme] = (password, player_entity)

    return player_list, pseudonyme, player_entity


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


def next_chapter():
    """
    changer les stats des mobs
    """

def player_attack():
    pass
    if "VIGOR" in ...:
        pass


def get_check_pseudonyme(pseudonyme):
    if len(pseudonyme) <= 4:
        print('')


def get_check_password(password):
    if len(password) <= 4:
        print('')

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

                return player_entity_maker(player_list, pseudonyme, password)

            else:
                login(player_list)

        else:
            print("You have to create a player")
            answer = check_answer_get_yes_no("Do you want to create a new player with the pseudonyme {} ?".format(pseudonyme))

            if answer == 'yes':
                password = input("""What is your password ?:
                        >>> """)

                return player_entity_maker(player_list, pseudonyme, password)

            else:
                login(player_list)

            password = input("""What is your password ?:
                    >>> """)

            return player_entity_maker(player_list, pseudonyme, password)

    else:
        password = input("""What is your password ?:
                >>> """)

        if check_login(player_list, pseudonyme, password) == True:
            player_entity = player_list[pseudonyme][1]
            return player_list, pseudonyme, player_entity


def main(player_list):
    start_screen()
    player_list, pseudonyme, player_entity = login(player_list)
    welcome(pseudonyme, player_entity.get_player_stats()['CHAPTER'])

player_list = charge_file()
main(player_list)
save_file(player_list)