import csv
import json

path_to_json = 'output/metadata/updated2/'
path_to_csv = 'output/metadata/csv/'

full_json_lists = list()

rarity_list = dict()
rank_list = dict()


with open(path_to_csv + str(2) + ".csv", 'w', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["tokenId", "Rank", "Rarity", "Warrior 武士", "Background 背景", "Element 元素", "Clan 一族",
                     "Attire 服装", "Weapon 武器", "Earrings 耳飾り", "Eyes 目", "Face 顔", "Head 頭"])

    tokenId = 1

    for file_name in range(1, 3778):
        with open(path_to_json + str(file_name) + ".json", "r", encoding='utf-8') as json_file:

            data = json.load(json_file)

            rank = data['rank']
            rarity = data['rarity']

            for trait in data['attributes']:
                if trait['trait_type'] == "Warrior 武士":
                    warrior = trait['value']

                if trait['trait_type'] == "Background 背景":
                    bg = trait['value']

                if trait['trait_type'] == "Element 元素":
                    ele = trait['value']

                if trait['trait_type'] == "Clan 一族":
                    cl = trait['value']

                if trait['trait_type'] == "Attire 服装":
                    att = trait['value']

                if trait['trait_type'] == "Weapon 武器":
                    wep = trait['value']

                if trait['trait_type'] == "Head 頭":
                    h = trait['value']

                if trait['trait_type'] == "Earrings 耳飾り":
                    ear = trait['value']

                if trait['trait_type'] == "Face 顔":
                    face = trait['value']

                if trait['trait_type'] == "Eyes 目":
                    eye = trait['value']

            writer.writerow([str(tokenId), str(rank), str(rarity), warrior, bg, ele, cl, att, wep, ear, eye, face, h])

        tokenId += 1

"""
with open('traits.txt', 'r', encoding='utf-8') as f:
    traits_tups = ast.literal_eval(f.read())

traits_list = [list(x) for x in traits_tups]

for trait in traits_list:
    trait.pop(7)
    trait.insert(0, token_id)
    trait.insert(1, rank_list[token_id])
    trait.insert(2, rarity_list[token_id])
    token_id += 1

for i in range(len(traits_list)):
    token_id = i+1

with open(path_to_csv + str(2) + ".csv", 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["tokenId", "Rank", "Rarity", "Warrior 武士", "Background 背景", "Element 元素", "Clan 一族",
                     "Attire 服装", "Weapon 武器", "Earrings 耳飾り", "Eyes 目", "Face 顔", "Head 頭"])
    for trait in traits_list:
        writer.writerow(trait)
"""
