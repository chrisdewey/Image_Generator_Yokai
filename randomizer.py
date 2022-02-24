import random
import fnmatch
# I will need  a hash table to call so when I create a random guy if all the
# traits are already found in another char., then change one of the traits?
# .... I need to research randomizer algo
# hash table in python == a dict, also a set == a hash table w no key/val pairs.

# Empty set where completed nft generated lists will be stored, to be checked for uniqueness
traits_list_hash = set()
traits_list = []

# Num of Samurai to generate
# num_samurai = 1259

# Lists holding traits and a weights var
bg = ["Summer 夏", "Autumn 秋", "Winter 冬", "Spring 春", "Fuji 富士", "Ramen House / Izakaya 居酒屋", "Shrine 神社", "Saiké Isekai サイケ異世界", "Inverse Saiké サイケ逆界"]
bg_weights = [18.89, 16.99, 15.98, 15.29, 14.39, 10.85, 7.48, 0.091, 0.039]  # TODO don't need this! if var in bg_dict not null, then select it. can do random selections? don't need weighted choices?

banner = ["Ashikaga 足利", "Hōjō 北条", "Imagawa 今川", "Minamoto 源", "Sanada 真田", "Taira 平", "Takeda 武田"]  # TODO maybe change filename for Hojo for [:3] indices splitting. except it won't work were thehre are similar names like in hair
banner_weights = []  # even?

attire_sam = ["Armor 鎧", "Kimono 着物"]
attire_sam_weights = [20, 80]

kimono_sam = ["Clouds 雲", "Flower 花", "Waves 波"]  # if it's a Kimono, randomly select type.
kimono_sam_weights = []  # even?

earring_left_sam = ["Death 死", "Fusion 融合 1", "Hunter 狩り", "Slayer 鬼滅 1", "None"]  # some are right ear only! check if certain earrings in randomizer, then add left one as well.
earring_left_sam_weights = [10, 10, 15, 15, 50]

eyes_sam = ["Saiké サイケ", "Akuma 悪魔", "Angry 怒り", "Calm 静か", "Relaxed 静か", "Sharingan 写輪眼", "Twilir トワイリル"]
eyes_sam_weights = [0, 20, 20, 20, 20, 10, 10]  # TODO change from Saike 0 prob to something else.

face_sam = ["Armored 面頬", "Golden Oni 金の鬼", "Plain 普通", "Ghoul 喰種",
            "Ninja 忍び", "Oni 鬼", "Himura Scar 緋村の傷", "Kitsune 狐", "None"]
face_sam_weights = [10, 10, 10, 10, 10, 10, 10, 10, 20]

head_sam_armored = ["Chasen 茶筅 + Headband 鉢巻", "Disheveled 乱れ髪", "Disheveled 乱れ髪 + Headband 鉢巻",
                    "Kabuto 兜", "Topknot 髷 + Headband 鉢巻", "Chasen 茶筅", "Sedge Hat 菅笠 2", "Topknot 髷"]
head_sam_armored_weights = [10, 10, 10, 20, 10, 10, 10, 20]

head_sam = ["Chasen 茶筅 + Headband 鉢巻", "Disheveled 乱れ髪", "Disheveled 乱れ髪 + Headband 鉢巻",
            "Topknot 髷 + Headband 鉢巻", "Chasen 茶筅", "Sedge Hat 菅笠 2", "Topknot 髷"]
head_sam_weights = [30, 10, 10, 10, 10, 10, 20]

weapon_sam = ["Bow 弓", "Demon Sword 妖刀", "Katana 刀", "Naginata 薙刀", "Niten-Ichiryu 二天一流", "SHAman Bow シャマ弓"]
weapon_sam_weights = [20, 15, 25, 20, 15, 5]

# test = random.choices(attire_sam, attire_sam_weights)[0]
# print(test)

# Vars holding max trait nums. Should be even in the end. when a trait is selected, decrement these.

# CLAN/BANNER
ban_Ashikaga = 539
ban_Hojo = 539  # taken out non-ascii chars
ban_Imagawa = 539
ban_Minamoto = 539
ban_Sanada = 539
ban_Taira = 539
ban_Takeda = 539
ban_Ronin = 4  # taken out non-ascii chars. don't need to decrement?

# HEADS
# samurai head
num_sam_Topknot = 250
num_sam_Topknot_Headband = 226
num_sam_Chasen = 193
num_sam_Chasen_Headband = 165
num_sam_Disheveled = 140
num_sam_Disheveled_Headband = 120
num_sam_Sedge_Hat = 100
num_sam_Jingasa = 50
num_sam_Kabuto = 15
# musha head
num_mu_Bun = 250
num_mu_Bun_Headband = 226
num_mu_Ponytail = 193
num_mu_Ponytail_Headband = 165
num_mu_Loose = 140
num_mu_Loose_Headband = 120
num_mu_Sedge_Hat = 100
num_mu_Jingasa = 50
num_mu_Kabuto = 15
# ape head
num_ape_Short = 250
num_ape_Short_Headband = 226
num_ape_Messy = 193
num_ape_Messy_Headband = 165
num_ape_Spiked = 140
num_ape_Spiked_Headband = 120
num_ape_Sedge_Hat = 100
num_ape_Jingasa = 50
num_ape_Kabuto = 15

# Earrings
earrings_None = 1800
earrings_Death = 600  # sm
earrings_Fusion = 450  # sma
earrings_WoV = 380
earrings_Hunter = 324  # sma
earrings_Slayer = 223  # sma

# attire
attire_Kimono_Flowers = 999
attire_Kimono_Waves = 845
attire_Kimono_Clouds = 745
attire_Street_Clothes = 644
attire_Armor = 544

# bg
bg_random = []
bg_nums = [710, 630, 600, 570, 540, 402, 275, 35, 15]
"""bg_dict = {
    "bg_Sum": 710,
    "bg_Aut": 630,
    "bg_Win": 600,
    "bg_Spr": 570,
    "bg_Fuj": 540,
    "bg_Ram": 402,
    "bg_Shr": 275,
    "bg_Sai": 35,  # taken out non-ascii char in Saiké
    "bg_Inv": 15  # taken out non-ascii char in Saiké
}"""

# face
face_Plain = 1127
face_Himura_Scar = 700
face_Ninja = 600
face_Oni = 500
face_Armored = 450
face_Ghoul = 290
face_Golden_Oni = 100
face_Kitsune = 10

# eyes
eye_Relaxed = 1300
eye_Angry = 950
eye_Akuma = 627
eye_Sharingan = 450
eye_Twilir = 250
eye_Ghoul = 150
eye_Saike = 50  # taken out non-ascii char in Saiké

# weapon
wep_Katana = 1532
wep_Bow = 1200
wep_Niten = 900
wep_Boar_Blades = 100
wep_SHAman_Bow = 25
wep_Demon_Sword = 20  # s

# elements
ele_None = 3000
ele_Air = 300
ele_Earth = 220
ele_Water = 152
ele_Fire = 100
ele_Lightning = 5


def find_index(substring, lst):

    for names in lst:
        if substring in names:
            return lst.index(names)

    return None


def remove_item(index, lst, wlst):

    lst.pop(index)
    wlst.pop(index)


def gen_lists(num):
    for i in range(len(bg_nums)):
        for j in range(bg_nums[i]):
            bg_random.append(bg[i])

    random.shuffle(bg_random)


def generate_samurai(char_num):
    # need to add left earring with checks!!
    # maybe make a dictionary literal??
    new_samurai = []  # dict to hold traits for single samurai

    """
    background = random.choices(bg, bg_weights)[0]

    background_frs = "bg_" + background[:3]

    while bg_dict[background_frs] < 1:  # this basically won't happen. failsafe.
        background = random.choices(bg, bg_weights)[0]
        background_frs = "bg_" + background[:3]
        print("RE-ROLL background")
    
    bg_dict[background_frs] -= 1

    if bg_dict[background_frs] < 1 and bg:
        # print('empty')
        index = find_index(background[:3], bg)
        remove_item(index, bg, bg_weights)
        print(bg)"""

    background = bg_random[char_num]

    new_samurai.append(background)
    # Banner signifies the clan the samurai belongs to.
    new_samurai.append(random.choices(banner)[0])

    # Choose clothing. If Kimono, then return append type. Else append armor.
    attire = random.choices(attire_sam, attire_sam_weights)[0]
    if attire == "Kimono 着物":
        new_samurai.append(random.choices(kimono_sam)[0])
    else:
        new_samurai.append("Armor 鎧")

    new_samurai.append(random.choices(eyes_sam, eyes_sam_weights)[0])
    new_samurai.append(random.choices(face_sam, face_sam_weights)[0])

    earring = random.choices(earring_left_sam, earring_left_sam_weights)[0]  # left earring
    new_samurai.append(earring)
    if earring in ["Fusion 融合", "Slayer 鬼滅 1"]:
        earring = earring.replace(earring[len(earring) - 1], '2')  # replace last char from 1 to 2
        new_samurai.append(earring)  # Add the right earring
    else:
        new_samurai.append("None")

    if attire == "Armor 鎧":
        new_samurai.append(random.choices(head_sam_armored, head_sam_armored_weights)[0])
    else:
        new_samurai.append(random.choices(head_sam, head_sam_weights)[0])

    new_samurai.append(random.choices(weapon_sam, weapon_sam_weights)[0])

    # print(new_samurai)
    tups = tuple(new_samurai)
    # print(tups)
    key = hash(tups)

    if key in traits_list_hash:
        print("CONFLICT")
        return generate_samurai()
    else:
        return tups


def randomize_all(num_to_gen):
    gen_lists(num_to_gen)

    for i in range(num_to_gen):
        new_samurai = generate_samurai(i)

        traits_list_hash.add(hash(new_samurai))
        traits_list.append(new_samurai)

    return traits_list
