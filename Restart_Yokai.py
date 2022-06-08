# import os
from PIL import Image
import numpy
import ast
from blend_modes import addition, multiply, overlay
import numpy as np


def mask_textures(base):
    mask_texture = Image.open('input/- Textures -/2. Mask Texture.png')

    mask_texture.paste(base, mask_texture)

    return mask_texture


def add_noise(base):
    image = np.array(base).astype(np.uint8)

    mean = 0
    var = .1
    sigma = var**0.5
    noise = np.random.normal(mean, sigma, image.shape)

    noisy_array = image + noise
    noisy = Image.fromarray(noisy_array.astype(np.uint8))

    return noisy


def generate(traits_list_txt, restart_from):
    yokai_number = restart_from

    with open(traits_list_txt, 'r', encoding='utf-8') as f:
        traits_list = ast.literal_eval(f.read())

    for index, traits in enumerate(traits_list):
        if index < restart_from:
            continue
        # Order = [char, bg, color, head, body, face, earring, companion, hand, chikara]
        print(yokai_number)

        background = traits[1]

        color = traits[2]
        yokai = traits[0]

        body = Image.open('input/{0}/Body 体/{1}/{2}.png'.format(yokai, traits[4], color))
        if yokai == "Tengu 天狗":
            head = Image.open('input/{0}/Head 頭/{1}/{2}.png'.format(yokai, traits[3], color))
        elif yokai == "Ōkami 狼" and traits[3] == "Plain 普通":
            head = None
        else:
            head = Image.open('input/{0}/Head 頭/{1}.png'.format(yokai, traits[3]))

        if traits[5] == "Cloth Mask 布マスク" and traits[4] in ["Hakui Kimono 白衣", "Kimono 着物"] and yokai != "Ōkami 狼":
            face = Image.open('input/{0}/Face 顔/{1}/w- Kimono/{2}.png'.format(yokai, traits[5], color))
        elif yokai == "Tengu 天狗" and traits[5] == "Ninjaz Ghoul Mask 忍者グール面":
            face = Image.open('input/{0}/Face 顔/{1}/{2}.png'.format(yokai, "Plain 普通", color))
        else:
            face = Image.open('input/{0}/Face 顔/{1}/{2}.png'.format(yokai, traits[5], color))

        if traits[6] != "None 無し":
            earring = Image.open('input/{0}/Earring 耳飾り/{1}.png'.format(yokai, traits[6]))
        else:
            earring = None

        if traits[7] != "None 無し":
            companion = Image.open('input/- Nakama 仲間 -/{}.png'.format(traits[7]))
        else:
            companion = None

        plain_scar_list = ["Beast Mask 獣の面", "Boar Mask 猪の面", "Diamond Hand 金剛者", "Dragon Egg 龍の卵",
                           "Kaonashi Mask 顔無し面", "Mononoke Mask 物の怪面", "Ramen Bowl ラーメン鉢"]
        if traits[8] in plain_scar_list:
            if traits[4] != "Scarred 傷":
                hand_clothing = "Plain 普通"
            else:
                hand_clothing = "Scarred 傷"
        else:
            if traits[4] == "Twilir トワイリル":
                hand_clothing = "Plain 普通"
            else:
                hand_clothing = traits[4]

        hand = Image.open('input/{0}/Hand 手/{1}/{2}/{3}.png'.format(yokai, traits[8], hand_clothing, color))
        if traits[8] in ["Kanabō 金棒", "Naginata 薙刀", "SHAman Staff シャマ杖"]:
            weapon = Image.open('input/{0}/Hand 手/{1}/{2}.png'.format(yokai, traits[8], traits[8]))
        else:
            weapon = None

        if traits[9] != "None 無し":
            chikara = Image.open('input/- Chikara 力 -/{}.png'.format(traits[9]))
        else:
            chikara = None

        companion_back = ["Kodama 木霊", "Onibi 鬼火"]

        base = Image.open('input/- Background 背景 -/{}.png'.format(background))  # Base == bg
        base = base.convert('RGBA')

        if companion and traits[7] in companion_back:
            base.paste(companion, companion)

        if weapon:
            base.paste(weapon, weapon)

        base.paste(hand, hand)

        base.paste(body, body)

        base.paste(face, face)
        # Tengu Ninjaz Ghoul Mask adjustment
        if yokai == "Tengu 天狗" and traits[5] == "Ninjaz Ghoul Mask 忍者グール面":
            ninjaz_mask = Image.open('input/Tengu 天狗/Face 顔/Ninjaz Ghoul Mask 忍者グール面.png')
            base.paste(ninjaz_mask, ninjaz_mask)

        # Earring trait pasted on top of head for Tengu only.
        if yokai == "Tengu 天狗":
            if earring:
                base.paste(earring, earring)
            base.paste(head, head)
        else:
            if head:
                base.paste(head, head)
            if earring:
                base.paste(earring, earring)

        # twilir eye isn't used for goken helms.
        if traits[4] == "Twilir トワイリル" and traits[3] not in ["Goken Helm 護拳甲", "Dark Goken 闇の護拳"]:
            twil_eyes = Image.open('input/{0}/Body 体/{1}/{2}.png'.format(yokai, traits[4], "Twilir Eye"))
            base.paste(twil_eyes, twil_eyes)

        if chikara:
            base.paste(chikara, chikara)

        if companion and traits[7] not in companion_back:
            base.paste(companion, companion)

        # TODO: adjust the overlay textures.
        base = mask_textures(base)

        base.save("output/UkiyoeYokai#{}.png".format(yokai_number+1))
        yokai_number += 1
