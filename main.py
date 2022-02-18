# This image generator is created for generating images for the Ukiyoe Warriors NFT project.
# There will be two sections: The image generator, in which multiple png files are placed together,
#   along with some masking effects. Secondly, there will be a randomization function.

import Create_Samurai
import Create_Metadata
import randomizer

# Image_Creation.testing()
# Create_Samurai.first()

traits = randomizer.randomize_samurai(100)  # Should i call create_nftdoods directly in the randomizer funcs?

Create_Samurai.generate(traits)

Create_Metadata.samurai(traits)
# or should i make list = randomizer.samurai() and then create_samurai.generate(list)?
#
# print(traits)
print("order:\n bg\n banner\n attire\n eyes\n face\n earring l\n earring r\n head\n weapon")
