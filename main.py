import Create_Samurai
import Create_Metadata
import randomizer

traits = randomizer.randomize_all(3773)  # Should i call create_nftdoods directly in the randomizer funcs?
Create_Metadata.samurai(traits)
Create_Samurai.generate(traits)
