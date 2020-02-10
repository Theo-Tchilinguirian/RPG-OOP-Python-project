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

                elif stat_key == 'ATTACK' or stat_key == 'DEFENSE':
                    new_stat_value = round(current_stat_value + (current_stat_value / 10))
                    self.set_stat_value(stat_key, new_stat_value)

                print(stat_key, current_stat_value)
        player_entity = self
        player_list[pseudonyme][1] = player_entity

        return player_list, player_entity


# mana? vigueur?

class Warrior(Player):

    def __init__(self, vig = 80):
        Player.__init__(self, cls = 'Warrior', lvl = 1, mon = 0, hp = 100, atk = 35, dfs = 35, chp = 'I: THE RUINS', klc = 0, bhp = 100, kcm = 5)
        self.set_stat_value('VIGOR', vig)


class Soldier(Player):

    def __init__(self, vig = 90):
        Player.__init__(self, cls='Soldier', lvl = 1, mon = 0, hp = 90, atk = 40, dfs = 60, chp = 'I: THE RUINS', klc = 0, bhp = 90, kcm = 5)
        self.set_stat_value('VIGOR', vig)


class Gladiator(Player):

    def __init__(self, vig = 100):
        Player.__init__(self, cls='Gladiator', lvl = 1, mon = 0, hp = 80, atk = 35, dfs = 35, chp = 'I: THE RUINS', klc = 0, bhp = 80, kcm = 5)
        self.set_stat_value('VIGOR', vig)


class Mage(Player):

    def __init__(self, mana = 90):
        Player.__init__(self, cls='Mage', lvl = 1, mon = 0, hp = 100, atk = 25, dfs = 35, chp = 'I: THE RUINS', klc = 0, bhp = 100, kcm = 5)
        self.set_stat_value('MANA', mana)


class Sorcerer(Player):

    def __init__(self, mana = 80):
        Player.__init__(self, cls='Sorcerer', lvl = 1, mon = 0, hp = 110, atk = 30, dfs = 30, chp = 'I: THE RUINS', klc = 0, bhp = 110, kcm = 5)
        self.set_stat_value('MANA', mana)



class Priest(Player):

    def __init__(self, mana = 110):
        Player.__init__(self, cls='Priest', lvl = 1, mon = 0, hp = 75, atk = 20, dfs = 25, chp = 'I: THE RUINS', klc = 0, bhp = 75, kcm = 5)
        self.set_stat_value('MANA', mana)




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

        answer = check_answer_get_yes_no("You are level {}. Do you want do go to the next level ?". format(player_current_level))
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
    print(player_list)

player_list = charge_file()
main(player_list)
save_file(player_list)