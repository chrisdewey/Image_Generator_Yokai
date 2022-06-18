import Create_Metadata
import Create_Images
import randomizer

# Creates txt file containing all image traits. (Alternatively pass list directly to the other functions.)
traits = randomizer.randomize_all()

Create_Metadata.yokai_metadata_from_file('traits.txt')

# first parameter is txt file containing traits. Second param is which image to start with
#   (used for restarting from a specific image if we run into errors and need to restart generating)
Create_Images.generate('traits.txt', 0)
