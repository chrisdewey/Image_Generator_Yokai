import Create_Yokai
import Create_Metadata
import Restart_Samurai
import randomizer
import ast
# import metadata_rarity_generator

traits = randomizer.randomize_all(4440)

# Create_Metadata.yokai(traits)
# Create_Samurai.generate(traits)
# Restart_Samurai.generate('traits.txt', 741)


""" 
# This is to change things in the traits list...
with open('traits.txt', 'r', encoding='utf-8') as f:
    new_traits_list = ast.literal_eval(f.read())


for i in range(len(new_traits_list)):
    if new_traits_list[i][6].endswith('1'):
        # get tuple
        tup = new_traits_list[i]
        # convert to list
        lis = list(tup)
        # remove extra number
        lis[6] = lis[6][:-2]
        # change back to tup
        new_tup = lis
        # place tup over previous tup
        new_traits_list[i] = new_tup
    #print(new_traits_list)

Create_Metadata.samurai(new_traits_list)
"""
