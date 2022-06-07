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
bg_nums = [802, 786, 611, 607, 462, 355, 263, 240, 133, 128, 53]  # - ronin traits. do for all traits. done.

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
head = ["Plain 普通", "Nezuko Horn 禰豆子の角", "Third Eye 顱頂眼", "Sedge Hat 菅笠", "Antlers 枝角",
        "Veking Helmet ヴィキングメット", "Goken Helm 護拳甲", "Cursed Hat 祟り笠", "Dark Goken 闇の護拳"]
head_random = []
head_nums = [1238, 748, 529, 471, 429, 428, 333, 240, 24]
# TODO: with the Goken Helm and Dark Goken, the face trait has to be "Plain" and no earring traits.

# Body 体  TODO: twilir gets eyes connected. the eyes are not a trait. just files (except goken helm, they're covered)
body = ["Plain 普通", "Scarred 傷", "Kimono 着物", "Hakui Kimono 白衣", "Twilir トワイリル"]
body_random = []
body_nums = [1584, 1051, 889, 700, 216]

# Face 顔
face = ["Plain 普通", "Face Paint 表面ペンキ", "Cloth Mask 布マスク", "Slit Mouth 口裂け", "Sukuna Eyes 宿儺眼",
        "Ninjaz Ghoul Mask 忍者グール面"]
face_random = []
face_nums = [1137, 950, 830, 754, 669, 100]

# Earring 耳飾り
earring = ["None 無し", "World of V V界", "Death 死", "Hanafuda 花札", "Flamingo 紅鶴", "Stardust 星屑",
           "Union Card 組合員証", "Fusion 融合", "Genesis 起源"]
earring_random = []
earring_nums = [999, 699, 599, 499, 450, 394, 350, 250, 200]

# Companion 仲間
companion = ["None 無し", "Onibi 鬼火", "Kitsune 狐", "Kodama 木霊", "Koi 鯉", "Tatsu 龍"]
companion_random = []
companion_nums = [2444, 578, 522, 444, 408, 44]

# Hand 手
hand = ["Spiked Club 金棒", "Naginata 薙刀", "Boar Mask 猪の面", "Mononoke Mask 物の怪面", "Dragon Egg 龍の卵",
        "Ramen Bowl ラーメン鉢", "Beast Mask 獣の面", "SHAman Staff シャマ杖", "Saké 酒", "Kaonashi Mask 顔無し面",
        "Diamond Hand 金剛者", "Guardian\'s Scythe 守護人の釜"]
hand_random = []
hand_nums = [610, 547, 495, 479, 426, 416, 377, 361, 321, 233, 100, 75]

# Chikara 力 1,111
chikara = ["None 無し", "Spirit Fire 神火", "Demon Energy 妖エネ", "Ice 氷", "Plant 草木", "Shadow 影"]
chikara_random = []
chikara_nums = [3333, 309, 259, 226, 198, 115]


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


# TODO: with the Goken Helm and Dark Goken, the face trait has to be "Plain" and no earring traits.
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

    tups = tuple(new_yokai)
    key = hash(tups)

    if key in traits_list_hash:
        print("CONFLICT")

        new_yokai = reroll(new_yokai, char_num)

        tups = tuple(new_yokai)
        key = hash(tups)

        if key not in traits_list_hash:
            print(" Definitely RESOLVED")
        return tups
    else:
        return tups


# TODO: BUG here with recursion. If trait isn't fixed can infinite loop. rerunning can avoid the issue since only needed
#   once.
def reroll(new_yokai, char_num):
    next_char = char_num + 1

    if (new_yokai[3] not in ["Goken Helm 護拳甲", "Dark Goken 闇の護拳"]
            and head_random[next_char]not in ["Goken Helm 護拳甲", "Dark Goken 闇の護拳"]
            and new_yokai[3] != head_random[next_char]):
        trouble_trait = new_yokai[3]
        new_yokai[3] = head_random[next_char]
        head_random[next_char] = trouble_trait

    tups = tuple(new_yokai)
    key = hash(tups)
    if key not in traits_list_hash:
        print("RESOLVED")
    else:
        reroll(new_yokai, char_num)

    return new_yokai


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
