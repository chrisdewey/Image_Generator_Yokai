# This image generator is created for generating images for the Ukiyoe Warriors NFT project.
# There will be two sections: The image generator, in which multiple png files are placed together,
#   along with some masking effects. Secondly, there will be a randomization function.

import Create_Samurai
import randomizer

# Image_Creation.testing()
Create_Samurai.first()

randomizer.samurai()  # Should i call create_nftdoods directly in the randomizer funcs?
# or should i make list = randomizer.samurai() and then create_samurai.generate(list)?
#
