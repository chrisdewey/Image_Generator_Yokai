import random
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
bg = ["Fuji 富士", "None"]
bg_weights = [100, 0]

banner = ["Ashikaga 足利", "Hōjō 北条", "Imagawa 今川", "Minamoto 源", "Sanada 真田", "Taira 平", "Takeda 武田"]
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


def generate_samurai():
    # need to add left earring with checks!!
    # maybe make a dictionary literal??
    new_samurai = []  # dict to hold traits for single samurai

    new_samurai.append(random.choices(bg, bg_weights)[0])
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

    earring = random.choices(earring_left_sam, earring_left_sam_weights)[0]
    new_samurai.append(earring)
    if earring in ["Fusion 融合", "Slayer 鬼滅 1"]:
        earring = earring.replace(earring[len(earring) - 1], '2')  # replace last char from 1 to 2
        new_samurai.append(earring)
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


def randomize_samurai(num_to_gen):
    for i in range(num_to_gen):
        new_samurai = generate_samurai()

        traits_list_hash.add(hash(new_samurai))
        traits_list.append(new_samurai)

    return traits_list
