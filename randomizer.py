from numpy import random
# I will need  a hash table to call so when I create a random guy if all the
# traits are already found in another char., then change one of the traits?
# .... I need to research randomizer algo
# hash table in python == a dict, also a set == a hash table w no key/val pairs.

# Empty set where completed nft generated lists will be stored, to be checked for uniqueness
traits_list = set()

# Num of Samurai to generate
# num_samurai = 1259

# Lists holding traits and a weights var
bg = ["Fuji 富士", "None"]
bg_weights = [100, 0]

banner = ["Ashikaga 足利", "Hōjō 北条", "Imagawa 今川", "Minamoto 源", "Sanada 真田", "Taira 平", "Takeda 武田"]
banner_weights = []  # even?

attire_sam = ["Armor 鎧", "Kimono 着物"]
attire_sam_weights = [20, 80]

kimono_sam = ["Checkered チェック", "Clouds 雲", "Flower 花", "Plain 一色", "Stripes ストライプ", "Waves 波"]  # if it's a Kimono, randomly select type.
kimono_sam_weights = []  # even?

earring_right_sam = ["Death 死", "Fusion 融合 1", "Hunter 狩り", "Slayer 鬼滅 1", "None"]  # some are right ear only! check if certain earrings in randomizer, then add left one as well.
earring_right_sam_weights = [10, 10, 15, 15, 50]

eyes_sam = ["Saiké サイケ", "Akuma 悪魔", "Angry 怒り", "Calm 静か", "Relaxed 静か", "Sharingan 写輪眼", "Twilir トワイリル"]
eyes_sam_weights = [10, 10, 20, 20, 20, 10, 10]

face_sam = ["Armored 面頬", "Golden Oni Mask 鬼の面（金）", "Golden Oni 金の鬼",
             "Ninja Mask 忍者の面", "Ninja 忍び", "Oni Mask 鬼の面", "Oni 鬼", "None"]
face_sam_weights = [10, 10, 10, 10, 10, 10, 10, 30]

head_sam = ["Kabuto 兜", "Topknot 髷 + Headband 鉢巻", "Sedge Hat 菅笠 2", "Sedge Hat 菅笠", "Topknot 髷"]
head_sam_weights = [10, 30, 20, 20, 20]

weapon_sam = ["Bow 弓", "Demon Sword 妖刀", "Katana 刀", "Naginata 薙刀", "Niten-Ichiryu 二天一流", "SHAman Bow シャマ弓"]
weapon_sam_weights = [20, 15, 25, 20, 15, 5]


def generate_samurai():

    new_samurai = {}  # dict to hold traits for single samurai

    new_samurai["bg"] = random.choice(bg, bg_weights)
    new_samurai["banner"] = random.choice(banner, banner_weights)

    if random.choice(attire_sam, attire_sam_weights) == "Kimono 着物":
        new_samurai["attire"] = random.choice(kimono_sam, kimono_sam_weights)
    else:
        new_samurai["attire"] = "Armor 鎧"

    new_samurai["earring_right"] = random.choice(earring_right_sam, earring_right_sam_weights)

    if new_samurai["earring_right"] ==


def randomize_samurai(num_to_gen):
    for i in range(num_to_gen):
        new_samurai = generate_samurai()

        traits_list.add(new_samurai)
