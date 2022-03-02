import random

# Empty set where completed nft generated lists will be stored, to be checked for uniqueness
traits_list_hash = set()
traits_list = []

chars_tracker = [0, 0, 0]  # dict holding vars containing all chars. 0sam 1mus 2ape

characters = 3773
chars_list = []

# Lists holding traits and a weights var
bg = ["Summer 夏", "Autumn 秋", "Winter 冬", "Spring 春", "Fuji 富士", "Ramen House ラーメン屋",
      "Shrine 神社", "Saiké Isekai サイケ異世界", "Inverse Saiké サイケ逆界"]
bg_random = []
bg_nums = [605, 525, 539, 510, 480, 401, 274, 34, 15]  # - ronin traits. do for all traits. done.

banner = ["Ashikaga 足利", "Hōjō 北条", "Imagawa 今川", "Minamoto 源", "Sanada 真田", "Taira 平", "Takeda 武田"]
clan_random = []
clan_nums = [539, 539, 539, 539, 539, 539, 539]

head_sam = ["Topknot 髷", "Topknot 髷 + Headband 鉢巻", "Chasen 茶筅", "Chasen 茶筅 + Headband 鉢巻", "Disheveled 乱れ髪",
            "Disheveled 乱れ髪 + Headband 鉢巻", "Sedge Hat 菅笠", "Jingasa 陣笠", "Kabuto 兜"]
sam_head_random = []
sam_head_nums = [280, 246, 193, 174, 139, 130, 100, 50, 15]

head_musha = ["Bun 髷", "Bun 髷 + Headband 鉢巻", "Ponytail 下げ髪", "Ponytail 下げ髪 + Headband 鉢巻", "Loose 垂髪",
            "Loose 垂髪 + Headband 鉢巻", "Sedge Hat 菅笠", "Jingasa 陣笠", "Kabuto 兜"]
musha_head_random = []
musha_head_nums = [250, 226, 193, 168, 150, 120, 100, 50, 15]

head_ape = ["Short 短毛", "Short 短毛 + Headband 鉢巻", "Messy ボサボサ", "Messy ボサボサ + Headband 鉢巻", "Spiked ツンツン",
            "Spiked ツンツン + Headband 鉢巻", "Sedge Hat 菅笠", "Jingasa 陣笠", "Kabuto 兜"]
ape_head_random = []
ape_head_nums = [250, 226, 193, 165, 140, 120, 99, 50, 15]

attire = ["Kimono Flowers 着物花", "Kimono Waves 着物波", "Kimono Clouds 着物曇", "Street Clothes 街着", "Armor 鎧"]
attire_random = []
attire_nums = [1001, 849, 749, 649, 549]

earring_left = ["None", "Death 死", "Fusion 融合 1", "WoV V界 1", "Hunter 狩り", "Slayer 鬼滅 1"]  # some are right ear only! check if certain earrings in randomizer, then add left one as well.
earring_random = []
earring_nums = [1430, 598, 452, 375, 326, 221]

eyes = ["Relaxed 静か", "Angry 怒り", "Akuma 悪魔", "Sharingan 写輪眼", "Twilir トワイリル", "Ghoul 喰種", "Saiké サイケ"]
eyes_random = []
eyes_nums = [1120, 849, 598, 459, 255, 150, 49]

face = ["Plain 普通", "Himura Scar 緋村の傷", "Ninja 忍び", "Oni 鬼",
        "Armored 面頬", "Ghoul 喰種", "Golden Oni 金の鬼", "Kitsune 狐"]
face_weights = [31.8, 19.7, 15.8, 13.2, 11.9, 7.6, 0, 0]
face_random = []
face_nums = [1147, 699, 609, 519, 469, 290, 100, 10]

weapons = ["Katana 刀", "Bow 弓", "Niten-Ichiryū 二天一流",
           "Boar Blades 猪の剣", "SHAman Bow シャマ弓", "Demon Sword 妖刀"]
weapons_weights = [40, 33.1, 24.1, 2.8, 0, 0]
weapons_random = []
weapons_nums = [1391, 1060, 840, 99, 24, 19]

elements = ["None", "Air 風", "Earth 地", "Water 水", "Fire 火", "Lightning 雷"]
elements_random = []
elements_num = [2615, 300, 219, 161, 99, 4]  # 3000-385 for first 355 not having any. append afterward


def swap_helmet(char_num, char):
    if char == "Samurai 侍":
        for i in range(char_num+1, len(sam_head_random)):
            if sam_head_random[i] != "Kabuto 兜":
                new_index = i
                sam_head_random[char_num], sam_head_random[i] = sam_head_random[i], sam_head_random[char_num]
                return

    if char == "Musha 武者":
        for i in range(char_num+1, len(musha_head_random)):
            if musha_head_random[i] != "Kabuto 兜":
                new_index = i
                musha_head_random[char_num], musha_head_random[i] = musha_head_random[i], musha_head_random[char_num]
                return

    if char == "Ape 猿":
        for i in range(char_num+1, len(ape_head_random)):
            if ape_head_random[i] != "Kabuto 兜":
                new_index = i
                ape_head_random[char_num], ape_head_random[i] = ape_head_random[i], ape_head_random[char_num]
                return

    raise IOError("There was no helmet left for it to be switched to!")


def gen_char_list(num):
    total_samurai = 1257
    total_musha = 1258
    total_ape = 903  # - 355 for wl
    for i in range(total_samurai):
        chars_list.append("Samurai 侍")
    for i in range(total_musha):
        chars_list.append("Musha 武者")
    for i in range(total_ape):
        chars_list.append("Ape 猿")

    random.shuffle(chars_list)

    for i in range(355):
        chars_list.insert(0, "Ape 猿")


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
    random.shuffle(clan_random)
    random.shuffle(sam_head_random)
    random.shuffle(musha_head_random)
    random.shuffle(ape_head_random)
    random.shuffle(earring_random)
    random.shuffle(attire_random)
    random.shuffle(face_random)
    random.shuffle(eyes_random)
    random.shuffle(weapons_random)
    random.shuffle(elements_random)

    for i in range(385):
        elements_random.insert(0, "None")
    """
    for i in range(385):
        if weapons_random[i] == "Demon Sword 妖刀":
            # swap with first non demon sword after 355
            for j in range(686, len(weapons_random)-1):
                if weapons_random[j] != "Demon Sword 妖刀":
                    weapons_random[i], weapons_random[j] = weapons_random[j], weapons_random[i]
                    break
    """
    for i in range(140):
        weapons_random.insert(0, "Katana 刀")
        weapons_random.insert(0, "Bow 弓")
        if i > 79:
            weapons_random.insert(0, "Niten-Ichiryū 二天一流")

    for i in range(371):
        earring_random.insert(0, "None")
    earring_random.insert(0, "Death 死")

    for i in range(105):
        bg_random.insert(0, "Summer 夏")
        bg_random.insert(0, "Autumn 秋")
    for i in range(60):
        bg_random.insert(0, "Winter 冬")
        bg_random.insert(0, "Spring 春")
        bg_random.insert(0, "Fuji 富士")

    for i in range(200):
        eyes_random.insert(0, "Relaxed 静か")
        if i > 99:
            eyes_random.insert(0, "Angry 怒り")
            if i > 149:
                eyes_random.insert(0, "Akuma 悪魔")


def generate_samurai(char_num):
    new_samurai = []  # dict to hold traits for single samurai

    character = chars_list[char_num]
    if character == "Samurai 侍":
        chars_tracker[0] += 1
    if character == "Musha 武者":
        chars_tracker[1] += 1
    if character == "Ape 猿":
        chars_tracker[2] += 1

    new_samurai.append(character)

    background = bg_random[char_num]
    new_samurai.append(background)

    element = elements_random[char_num]
    new_samurai.append(element)

    clan = clan_random[char_num]
    # Banner signifies the clan the samurai belongs to.
    new_samurai.append(clan)

    # CHARACTERS STARTS HERE 1 attire, 2, weapons, 3, earrings, eyes, face, head

    # Choose clothing. If Kimono, then return append type. Else append armor.
    clothes = attire_random[char_num]
    new_samurai.append(clothes)

    #print(weapons_random)
    weapon = weapons_random[char_num]
    new_samurai.append(weapon)

    earring = earring_random[char_num]
    new_samurai.append(earring)

    if earring in ["Fusion 融合", "Slayer 鬼滅 1", "WoV V界 1"] and character != "Ape 猿":
        earring = earring.replace(earring[len(earring) - 1], '2')  # replace last char from 1 to 2
        new_samurai.append(earring)  # Add the right earring
    else:
        new_samurai.append("None")

    eye = eyes_random[char_num]
    new_samurai.append(eye)

    char_face = face_random[char_num]
    new_samurai.append(char_face)

    if character == "Samurai 侍":
        index = char_num-chars_tracker[1]-chars_tracker[2]
        if clothes != "Armor 鎧" and sam_head_random[index] == "Kabuto 兜":
            swap_helmet(index, character)
        head = sam_head_random[index]
        new_samurai.append(head)

    if character == "Musha 武者":
        index = char_num-chars_tracker[0]-chars_tracker[2]
        if clothes != "Armor 鎧" and musha_head_random[index] == "Kabuto 兜":
            swap_helmet(index, character)
        head = musha_head_random[index]
        new_samurai.append(head)

    if character == "Ape 猿":
        index = char_num-chars_tracker[0]-chars_tracker[1]
        if clothes != "Armor 鎧" and ape_head_random[index] == "Kabuto 兜":
            swap_helmet(index, character)
        head = ape_head_random[index]
        new_samurai.append(head)





    tups = tuple(new_samurai)
    key = hash(tups)

    if key in traits_list_hash:
        print("CONFLICT")

        new_samurai = reroll(new_samurai, char_num)

        tups = tuple(new_samurai)
        key = hash(tups)

        if key not in traits_list_hash:
            print(" Definitely RESOLVED")
        return tups
    else:
        return tups


def reroll(new_samurai, char_num):
    new_samurai[5] = random.choices(weapons, weapons_weights)[0]
    new_samurai[9] = random.choices(face, face_weights)[0]

    tups = tuple(new_samurai)
    key = hash(tups)
    if key not in traits_list_hash:
        print("RESOLVED")
    else:
        reroll(new_samurai, char_num)

    return new_samurai


def randomize_all(num_to_gen):
    gen_lists(num_to_gen)

    gen_char_list(num_to_gen)

    for i in range(num_to_gen):
        new_samurai = generate_samurai(i)

        traits_list_hash.add(hash(new_samurai))
        traits_list.append(new_samurai)

    with open("traits.txt", "w", encoding='utf-8') as output:
        output.write(str(traits_list))

    return traits_list
