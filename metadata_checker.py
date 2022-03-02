import sys
import json
from collections import defaultdict

traits_warrior = dict()
traits_background = dict()
traits_element = dict()
traits_clan = dict()
traits_attire = dict()
traits_weapon = dict()
traits_head = dict()
traits_earrings = dict()
traits_face = dict()
traits_eyes = dict()

traits_warrior_tracker = defaultdict(list)
traits_background_tracker = defaultdict(list)
traits_element_tracker = defaultdict(list)
traits_clan_tracker = defaultdict(list)
traits_attire_tracker = defaultdict(list)
traits_weapon_tracker = defaultdict(list)
traits_head_tracker = defaultdict(list)
traits_earrings_tracker = defaultdict(list)
traits_face_tracker = defaultdict(list)
traits_eyes_tracker = defaultdict(list)

path_to_json = 'output/metadata/'
for file_name in range(1, 3778):
    with open(path_to_json + str(file_name) + ".json", "r", encoding='utf-8') as json_file:

        data = json.load(json_file)

        for trait in data['attributes']:
            if trait['trait_type'] == "Warrior 武士":
                if trait['value'] not in traits_warrior:
                    traits_warrior[trait['value']] = 1
                else:
                    traits_warrior[trait['value']] = traits_warrior[trait['value']] + 1

            if trait['trait_type'] == "Background 背景":
                if trait['value'] not in traits_background:
                    traits_background[trait['value']] = 1
                else:
                    traits_background[trait['value']] = traits_background[trait['value']] + 1

            if trait['trait_type'] == "Element 元素":
                if trait['value'] not in traits_element:
                    traits_element[trait['value']] = 1
                else:
                    traits_element[trait['value']] = traits_element[trait['value']] + 1

            if trait['trait_type'] == "Clan 一族":
                if trait['value'] not in traits_clan:
                    traits_clan[trait['value']] = 1
                else:
                    traits_clan[trait['value']] = traits_clan[trait['value']] + 1

            if trait['trait_type'] == "Attire 服装":
                if trait['value'] not in traits_attire:
                    traits_attire[trait['value']] = 1
                else:
                    traits_attire[trait['value']] = traits_attire[trait['value']] + 1

            if trait['trait_type'] == "Weapon 武器":
                if trait['value'] not in traits_weapon:
                    traits_weapon[trait['value']] = 1
                else:
                    traits_weapon[trait['value']] = traits_weapon[trait['value']] + 1

            if trait['trait_type'] == "Head 頭":
                if trait['value'] not in traits_head:
                    traits_head[trait['value']] = 1
                else:
                    traits_head[trait['value']] = traits_head[trait['value']] + 1

            if trait['trait_type'] == "Earrings 耳飾り":
                if trait['value'] not in traits_earrings:
                    traits_earrings[trait['value']] = 1
                else:
                    traits_earrings[trait['value']] = traits_earrings[trait['value']] + 1

            if trait['trait_type'] == "Face 顔":
                if trait['value'] not in traits_face:
                    traits_face[trait['value']] = 1
                else:
                    traits_face[trait['value']] = traits_face[trait['value']] + 1

            if trait['trait_type'] == "Eyes 目":
                if trait['value'] not in traits_eyes:
                    traits_eyes[trait['value']] = 1
                else:
                    traits_eyes[trait['value']] = traits_eyes[trait['value']] + 1

            #  START of tracker checkers
            if trait['trait_type'] == "Warrior 武士":
                traits_warrior_tracker[trait['value']].append(data['tokenId'])

            if trait['trait_type'] == "Background 背景":
                traits_background_tracker[trait['value']].append(data['tokenId'])

            if trait['trait_type'] == "Element 元素":
                traits_element_tracker[trait['value']].append(data['tokenId'])

            if trait['trait_type'] == "Clan 一族":
                traits_clan_tracker[trait['value']].append(data['tokenId'])

            if trait['trait_type'] == "Attire 服装":
                traits_attire_tracker[trait['value']].append(data['tokenId'])

            if trait['trait_type'] == "Weapon 武器":
                traits_weapon_tracker[trait['value']].append(data['tokenId'])

            if trait['trait_type'] == "Head 頭":
                traits_head_tracker[trait['value']].append(data['tokenId'])

            if trait['trait_type'] == "Earrings 耳飾り":
                traits_earrings_tracker[trait['value']].append(data['tokenId'])

            if trait['trait_type'] == "Face 顔":
                traits_face_tracker[trait['value']].append(data['tokenId'])

            if trait['trait_type'] == "Eyes 目":
                traits_eyes_tracker[trait['value']].append(data['tokenId'])

print('shaman bow:')
print(traits_weapon_tracker['SHAman Bow シャマ弓'])

print('demon sword:')
print(traits_weapon_tracker['Demon Sword 妖刀'])

print('boar blades:')
print(traits_weapon_tracker['Boar Blades 猪の剣'])

print('Lightning element:')
print(traits_element_tracker['Lightning 雷'])

print('fire element:')
print(traits_element_tracker['Fire 火'])

print('Water element:')
print(traits_element_tracker['Water 水'])

print('Saiké Isekai サイケ異世界 background:')
print(traits_background_tracker['Saiké Isekai サイケ異世界'])

print('Inverse Saiké サイケ逆界 background:')
print(traits_background_tracker['Inverse Saiké サイケ逆界'])

print('Kabuto 兜 head:')
print(traits_head_tracker['Kabuto 兜'])

print('Jingasa 陣笠 head:')
print(traits_head_tracker['Jingasa 陣笠'])

print('Kitsune 狐 face:')
print(traits_face_tracker['Kitsune 狐'])

print('Golden Oni 金の鬼 face:')
print(traits_face_tracker['Golden Oni 金の鬼'])

print('Saiké サイケ eyes:')
print(traits_eyes_tracker['Saiké サイケ'])

engaging = False
while engaging:
    text_cat = input("enter category: ")
    text_trait = input("enter trait: ")

    if text_cat == "Warrior 武士":
        print(traits_warrior_tracker[text_trait])

    if text_cat == "Background 背景":
        print(traits_background_tracker[text_trait])

    if text_cat == "Element 元素":
        print(traits_element_tracker[text_trait])

    if text_cat == "Clan 一族":
        print(traits_clan_tracker[text_trait])

    if text_cat == "Attire 服装":
        print(traits_attire_tracker[text_trait])

    if text_cat == "Weapon 武器":
        print('okay')
        print(traits_weapon_tracker[text_trait])

    if text_cat == "Head 頭":
        print(traits_head_tracker[text_trait])

    if text_cat == "Earrings 耳飾り":
        print(traits_earrings_tracker[text_trait])

    if text_cat == "Face 顔":
        print(traits_face_tracker[text_trait])

    if text_cat == "Eyes 目":
        print(traits_eyes_tracker[text_trait])

    if input('done?') == "yes":
        engaging = False
