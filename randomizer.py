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
bg = ["Summer 夏", "Autumn 秋", "Winter 冬", "Spring 春", "Fuji 富士", "Ramen House / Izakaya 居酒屋",
      "Shrine 神社", "Saiké Isekai サイケ異世界", "Inverse Saiké サイケ逆界"]
bg_random = []
bg_nums = [710, 630, 599, 570, 540, 401, 274, 34, 15]  # - ronin traits. do for all traits. done.

banner = ["Ashikaga 足利", "Hōjō 北条", "Imagawa 今川", "Minamoto 源", "Sanada 真田", "Taira 平", "Takeda 武田"]  # TODO maybe change filename for Hojo for [:3] indices splitting. except it won't work were thehre are similar names like in hair
clan_random = []
clan_nums = [539, 539, 539, 539, 539, 539, 539]

head_sam = ["Topknot 髷", "Topknot 髷 + Headband 鉢巻", "Chasen 茶筅", "Chasen 茶筅 + Headband 鉢巻", "Disheveled 乱れ髪",
            "Disheveled 乱れ髪 + Headband 鉢巻", "Sedge Hat 菅笠", "Jingasa 陣笠", "Kabuto 兜"]
sam_head_random = []
sam_head_nums = [250, 226, 193, 164, 139, 120, 100, 50, 15]
# TODO make sure to add, if attire != armor, check next in the sam_head_random list, if not kabuto, swap (else increment position)

head_musha = ["Bun 髷", "Bun 髷 + Headband 鉢巻", "Ponytail 下げ髪", "Ponytail 下げ髪 + Headband 鉢巻", "Loose 垂髪",
            "Loose 垂髪 + Headband 鉢巻", "Sedge Hat 菅笠", "Jingasa 陣笠", "Kabuto 兜"]
musha_head_random = []
musha_head_nums = [250, 226, 193, 164, 140, 120, 100, 50, 15]
# TODO make sure to add, if attire != armor, check next in the sam_head_random list, if not kabuto, swap (else increment position)

head_ape = ["Short 短毛", "Short 短毛 + Headband 鉢巻", "Messy ボサボサ", "Messy ボサボサ + Headband 鉢巻", "Spiked ツンツン",
            "Spiked ツンツン + Headband 鉢巻", "Sedge Hat 菅笠", "Jingasa 陣笠", "Kabuto 兜"]
ape_head_random = []
ape_head_nums = [250, 226, 193, 165, 140, 120, 99, 50, 15]
# TODO make sure to add, if attire != armor, check next in the sam_head_random list, if not kabuto, swap (else increment position)

attire = ["Kimono Flowers 着物花", "Kimono Waves 着物波", "Kimono Clouds 着物曇", "Street Clothes 街着", "Armor 鎧"]
attire_random = []
attire_nums = [998, 844, 744, 644, 543]  # TODO make sure to go over all ronin traits and subtract.

earring_left = ["None", "Death 死", "Fusion 融合 1", "WoV V界 1", "Hunter 狩り", "Slayer 鬼滅 1"]  # some are right ear only! check if certain earrings in randomizer, then add left one as well.
earring_random = []
earring_nums = [1800, 599, 450, 379, 323, 222]

eyes = ["Relaxed 静か", "Angry 怒り", "Akuma 悪魔", "Sharingan 写輪眼", "Twilir トワイリル", "Ghoul 喰種", "Saiké サイケ"]
eyes_random = []
eyes_nums = [1300, 949, 626, 449, 250, 150, 49]

face = ["Plain 普通", "Himura Scar 緋村の傷", "Ninja 忍び", "Oni 鬼",
        "Armored 面頬", "Ghoul 喰種", "Golden Oni 金の鬼", "Kitsune 狐"]
face_random = []
face_nums = [1127, 699, 599, 499, 449, 290, 100, 10]

weapons = ["Katana 刀", "Bow 弓", "Katana 刀", "Niten Ichi-ryū 二天一流",
          "Boar Blades 猪の剣", "SHAman Bow シャマ弓", "Demon Sword 妖刀"]
weapons_random = []
weapons_nums = [1531, 1200, 900, 99, 24, 19]

elements = ["None", "Air 風", "Earth 地", "Water 水", "Fire 火", "Lightning 雷"]
elements_random = []
elements_num = [3000, 300, 219, 151, 99, 4]


def gen_lists(num):
    for i in range(len(bg_nums)):
        for j in range(bg_nums[i]):
            bg_random.append(bg[i])

    for i in range(len(clan_nums)):
        for j in range(clan_nums[i]):
            clan_random.append(banner[i])

    for i in range(len(sam_head_nums)):
        for j in range(sam_head_nums[i]):
            sam_head_random.append(head_sam[i])

    for i in range(len(musha_head_nums)):
        for j in range(musha_head_nums[i]):
            musha_head_random.append(head_musha[i])

    for i in range(len(ape_head_nums)):
        for j in range(ape_head_nums[i]):
            ape_head_random.append(head_ape[i])

    for i in range(len(earring_nums)):
        for j in range(earring_nums[i]):
            earring_random.append(earring_left[i])

    for i in range(len(attire_nums)):
        for j in range(attire_nums[i]):
            attire_random.append(attire[i])

    for i in range(len(face_nums)):
        for j in range(face_nums[i]):
            face_random.append(face[i])

    for i in range(len(eyes_nums)):
        for j in range(eyes_nums[i]):
            eyes_random.append(eyes[i])

    for i in range(len(weapons_nums)):
        for j in range(weapons_nums[i]):
            weapons_random.append(weapons[i])

    for i in range(len(elements_num)):
        for j in range(elements_num[i]):
            elements_random.append(elements[i])

    random.shuffle(bg_random)


def generate_samurai(char_num):
    # need to add left earring with checks!!
    # maybe make a dictionary literal??
    new_samurai = []  # dict to hold traits for single samurai

    background = bg_random[char_num]
    new_samurai.append(background)

    element = elements[char_num]
    if element != "None":
        # element back goes in
        new_samurai.append(element)

    clan = clan_random[char_num]
    # Banner signifies the clan the samurai belongs to.
    new_samurai.append(clan)

    # CHARACTERS STARTS HERE 1 attire, 2, weapons, 3, earrings, eyes, face, head

    # Choose clothing. If Kimono, then return append type. Else append armor.
    clothes = attire_random[char_num]
    new_samurai.append(clothes)

    weapon = weapons_random[char_num]
    new_samurai.append(weapon)

    earring = earring_random[char_num]
    new_samurai.append(earring)

    new_samurai.append(earring)
    if earring in ["Fusion 融合", "Slayer 鬼滅 1", "WoV V界 1"]:
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
