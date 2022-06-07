import random

# Empty set where completed nft generated lists will be stored, to be checked for uniqueness
traits_list_hash = set()
traits_list = []

chars_tracker = [0, 0, 0, 0]  # dict holding vars containing all chars. 0kappa 1okami 2oni 3tengu

# Yōkai 妖怪
characters = 4440
chars_list = []

# Lists holding traits and a weights var
bg = ["Navy 濃い青", "Light Blue 水色", "Pink 桃色", "Yellow 黄", "Green 緑", "Red 赤",
      "Orange 橙色", "Gold 金", "Platinum 白金", "Amethyst 紫水晶", "Saiké サイケ"]
bg_random = []
bg_nums = [803, 787, 612, 608, 462, 355, 263, 240, 133, 128, 53]  # - ronin traits. do for all traits. done.
# TODO: DETELE traits used for legendaries!

# COLOR 色
# different color set for each yokai char
# New ratio instead of 1533, 1264, 870, 777 total. 1532 : 383 .. 1264 : 316 .. 872 : 218 .. 776 : 194
kappa_color = ["Green 緑", "Blue 青", "Black 黒", "White 白"]
kappa_color_random = []
kappa_color_nums = [383, 316, 218, 193]

okami_color = ["Brown 茶色", "Slate Blue 炭青", "Black 黒", "White 白"]
okami_color_random = []
okami_color_nums = [383, 316, 218, 193]

oni_color = ["Pale Red 薄い赤", "Purple 紫", "Black 黒", "White 白"]
oni_color_random = []
oni_color_nums = [383, 316, 218, 193]

tengu_color = ["Red 赤", "Blue 青", "Black 黒", "White 白"]
tengu_color_random = []
tengu_color_nums = [383, 316, 218, 193]

# Head 頭
head = ["Plain 普通", "Sedge Hat 菅笠", "Cursed Hat 祟り笠", "Antlers 枝角 (Forest Nation)", "Veking Helmet ヴィキングメット",
        "Third Eye 顱頂眼", "Goken Helm 護拳甲" "Nezuko Horn 禰豆子の角", "Dark Goken 闇の護拳"]
head_random = []
head_nums = [1200, 700, 600, 500, 400, 394, 300, 250, 100]
# TODO: with the Goken Helm and Dark Goken, the face trait has to be "Plain" and no earring traits.

# Body 体  TODO: twilir gets eyes connected. the eyes are not a trait. just files (except goken helm, they're covered)
body = ["Plain 普通", "Scarred 傷", "Kimono 着物", "Hakui Kimono 白衣", "Twilir トワイリル"]
body_random = []
body_nums = [1285, 1002, 840, 801, 516]

# Face 顔
face = ["Plain 普通", "Face Paint 表面ペンキ", "Cloth Mask 布マスク", "Slit Mouth 口裂け", "Sukuna Eyes 宿儺眼",
        "Ninjaz Ghoul Mask 忍者グール面"]
face_random = []
face_nums = [1138, 951, 831, 755, 669, 100]

# Earring 耳飾り
earring = ["None 無し", "World of V V界", "Death 死", "Hanafuda 花札", "Flamingo 紅鶴", "Stardust 星屑",
           "Union Card 組合員証", "Fusion 融合", "Genesis 起源"]
earring_random = []
earring_nums = [1000, 700, 600, 500, 450, 394, 350, 250, 200]

# Companion 仲間
companion = ["None 無し", "Onibi 鬼火", "Kitsune 狐", "Kodama 木霊", "Koi 鯉", "Tatsu 龍 (dragon)"]
companion_random = []
companion_nums = []

# TODO: okay. So maybe make diamond hand out of here and add first to list to ensure 100 traits, not about 100?? wait
#   maybe not. Think it's already set nums my dood.
# Hand 手
hand = ["Spiked Club 金棒", "Naginata 薙刀", "Beast Mask 獣の面", "Mononoke Mask 物の怪面", "Dragon Egg 龍の卵",
        "Ramen Bowl ラーメン鉢", "Boar Mask 猪の面 (NPO)", "SHAman Staff シャマ杖", "Saké 酒", "Kaonashi Mask 顔無し面",
        "Diamond Hand 金剛者", "Guardian\'s Scythe 守護人の釜"]
hand_random = []
hand_nums = [409, 384, 371, 360, 328, 310, 283, 270, 240, 232, 100, 75]

# Chikara 力 1,111
chikara = ["None 無し", "Spirit Fire 神火", "Demon Energy 妖エネ", "Ice 氷", "Plant 草木", "Shadow 影"]
chikara_random = []
chikara_nums = [3333, 310, 260, 227, 200, 115]


# TODO: del. deprecated.
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


# Yōkai 妖怪
def gen_char_list():
    total_kappa = 1110
    total_okami = 1110
    total_oni = 1110
    total_tengu = 1110
    for i in range(total_kappa):
        chars_list.append("Kappa 河童")
    for i in range(total_okami):
        chars_list.append("Ōkami 狼")
    for i in range(total_oni):
        chars_list.append("Oni 鬼")
    for i in range(total_tengu):
        chars_list.append("Tengu 天狗")

    random.shuffle(chars_list)


def gen_lists():
    for i in range(len(bg_nums)):
        for j in range(bg_nums[i]):
            bg_random.append(bg[i])

    for i in range(len(kappa_color_nums)):
        for j in range(kappa_color_nums[i]):
            kappa_color_random.append(kappa_color[i])

    for i in range(len(okami_color_nums)):
        for j in range(okami_color_nums[i]):
            okami_color_random.append(okami_color[i])

    for i in range(len(oni_color_nums)):
        for j in range(oni_color_nums[i]):
            oni_color_random.append(oni_color[i])

    for i in range(len(tengu_color_nums)):
        for j in range(tengu_color_nums[i]):
            tengu_color_random.append(tengu_color[i])

    for i in range(len(head_nums)):
        for j in range(head_nums[i]):
            head_random.append(head[i])

    for i in range(len(body_nums)):
        for j in range(body_nums[i]):
            body_random.append(body[i])

    for i in range(len(face_nums)):
        for j in range(face_nums[i]):
            face_random.append(face[i])

    for i in range(len(earring_nums)):
        for j in range(earring_nums[i]):
            earring_random.append(earring[i])

    for i in range(len(companion_nums)):
        for j in range(companion_nums[i]):
            companion_random.append(companion[i])

    for i in range(len(hand_nums)):
        for j in range(hand_nums[i]):
            hand_random.append(hand[i])

    for i in range(len(chikara_nums)):
        for j in range(chikara_nums[i]):
            chikara_random.append(chikara[i])

    random.shuffle(bg_random)
    random.shuffle(kappa_color_random)
    random.shuffle(okami_color_random)
    random.shuffle(oni_color_random)
    random.shuffle(tengu_color_random)
    random.shuffle(head_random)
    random.shuffle(body_random)
    random.shuffle(face_random)
    random.shuffle(earring_random)
    random.shuffle(companion_random)
    random.shuffle(hand_random)


def generate_yokai(char_num):
    new_yokai = []  # dict to hold traits for single samurai

    # For color, the item is popped from the list so that the next iter, the first item in list is new
    character = chars_list[char_num]
    if character == "Kappa 河童":
        chars_tracker[0] += 1
        color = kappa_color_random.pop(0)
    if character == "Ōkami 狼":
        chars_tracker[1] += 1
        color = okami_color_random.pop(0)
    if character == "Oni 鬼":
        chars_tracker[2] += 1
        color = oni_color_random.pop(0)
    if character == "Tengu 天狗":
        chars_tracker[3] += 1
        color = tengu_color_random.pop(0)

    new_yokai.append(character)

    background = bg_random[char_num]
    new_yokai.append(background)

    new_yokai.append(color)

    head1 = head_random[char_num]
    new_yokai.append(head1)

    body1 = body_random[char_num]
    new_yokai.append(body1)

    face1 = face_random[char_num]
    new_yokai.append(face1)

    earring1 = earring_random[char_num]
    new_yokai.append(earring1)

    companion1 = companion_random[char_num]
    new_yokai.append(companion1)

    hand1 = hand_random[char_num]
    new_yokai.append(hand1)


    """
    if earring in ["Fusion 融合", "Slayer 鬼滅 1", "WoV V界 1"] and character != "Ape 猿":
        earring = earring.replace(earring[len(earring) - 1], '2')  # replace last char from 1 to 2
        new_yokai.append(earring)  # Add the right earring
    else:
        new_yokai.append("None")
    

    if character == "Samurai 侍":
        index = char_num-chars_tracker[1]-chars_tracker[2]
        if clothes != "Armor 鎧" and sam_head_random[index] == "Kabuto 兜":
            swap_helmet(index, character)
        head = sam_head_random[index]
        new_yokai.append(head)

    if character == "Musha 武者":
        index = char_num-chars_tracker[0]-chars_tracker[2]
        if clothes != "Armor 鎧" and musha_head_random[index] == "Kabuto 兜":
            swap_helmet(index, character)
        head = musha_head_random[index]
        new_yokai.append(head)

    if character == "Ape 猿":
        index = char_num-chars_tracker[0]-chars_tracker[1]
        if clothes != "Armor 鎧" and ape_head_random[index] == "Kabuto 兜":
            swap_helmet(index, character)
        head = ape_head_random[index]
        new_yokai.append(head)
    """

    tups = tuple(new_yokai)
    key = hash(tups)

    if key in traits_list_hash:
        print("CONFLICT")

        # new_yokai = reroll(new_yokai, char_num)

        tups = tuple(new_yokai)
        key = hash(tups)

        if key not in traits_list_hash:
            print(" Definitely RESOLVED")
        return tups
    else:
        return tups


# TODO: fix this broth. deprecated changes
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
    gen_lists()

    gen_char_list()

    for i in range(num_to_gen):
        new_yokai = generate_yokai(i)

        traits_list_hash.add(hash(new_yokai))
        traits_list.append(new_yokai)

    with open("traits.txt", "w", encoding='utf-8') as output:
        output.write(str(traits_list))

    return traits_list
