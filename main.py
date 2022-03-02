import Create_Samurai
import Create_Metadata
import Restart_Samurai
import randomizer
import ast
import metadata_rarity_generator

# traits = randomizer.randomize_all(3773)  # Should i call create_nftdoods directly in the randomizer funcs?
# ^ okay so i've made the traits list. if i need to redo it, then i just have to read that file into a list
# and then keep going where i left off. also don't need to remake metadata
"""
traits = [("Musha \u6b66\u8005", "Spring \u6625", "None", "Takeda \u6b66\u7530", "Kimono Flowers \u7740\u7269\u82b1",
           "Bow \u5f13", "Fusion 融合 1", "Fusion 融合 2", "Angry \u6012\u308a", "Plain 普通",
           "Bun \u9af7 + Headband \u9262\u5dfb")]
"""
"""
traits = [("Ape \u733f", "Spring \u6625", "None", "Takeda \u6b66\u7530", "Kimono Flowers \u7740\u7269\u82b1",
           "Niten-Ichi-ryū 二天一流", "None", "None", "Angry \u6012\u308a", "Plain 普通",
           "Spiked ツンツン + Headband 鉢巻")]
"""
# Create_Metadata.samurai(traits)
# Create_Samurai.generate(traits)
# Restart_Samurai.generate('traits.txt', 741)



"""  # This is to change things in the traits list...
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
