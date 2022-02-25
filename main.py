# This image generator is created for generating images for the Ukiyoe Warriors NFT project.
# There will be two sections: The image generator, in which multiple png files are placed together,
#   along with some masking effects. Secondly, there will be a randomization function.

import Create_Samurai
import Create_Metadata
import randomizer

# Image_Creation.testing()
# Create_Samurai.first()

traits = randomizer.randomize_all(3773)  # Should i call create_nftdoods directly in the randomizer funcs?
#traits = [('Samurai 侍', 'Winter 冬', 'None', 'Imagawa 今川', 'Kimono Flowers 着物花', 'Bow 弓', 'None', 'None', 'Saiké サイケ', 'Ninja 忍び', 'Topknot 髷')]

#Create_Samurai.generate(traits)
# Create_Metadata.samurai(traits)
# or should i make list = randomizer.samurai() and then create_samurai.generate(list)?
#
# print(traits)
print("order:\n bg\n banner\n attire\n eyes\n face\n earring l\n earring r\n head\n weapon")
