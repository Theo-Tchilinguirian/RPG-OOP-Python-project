###################################################
# This is the main frame of the game
# Made by Théo Tchilinguirian, Sunday 09/02/2020
###################################################


# Imports #
import DataPack.DefMod


# Loading Data Files #

player_list = DataPack.DefMod.charge_file()

# Main Program #

print(player_list)
DataPack.DefMod.main(player_list, player_list[pseudonyme][1]['CHAPTER'])

# Saving Data Files #


DataPack.DefMod.save_file(player_list)
DataPack.DefMod.os.system('pause')
