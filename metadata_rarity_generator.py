# TODO: merge with Create_Metadata.py. No reason to have them separated. Currently creates 3x metadata files, only need
#   one set. Need to calculate rarity by looping through list before creating the json files.

import json

traits_yokai = {}
traits_background = {}
traits_color = {}
traits_head = {}
traits_body = {}
traits_face = {}
traits_earring = {}
traits_companion = {}
traits_hand = {}
traits_chikara = {}

path_to_json = 'output/metadata/'
for file_name in range(1, 4445):
    with open(path_to_json + str(file_name) + ".json", "r", encoding='utf-8') as json_file:

        data = json.load(json_file)

        for trait in data['attributes']:
            if trait['trait_type'] == "Yōkai 妖怪":
                if trait['value'] not in traits_yokai:
                    traits_yokai[trait['value']] = 1
                else:
                    traits_yokai[trait['value']] = traits_yokai[trait['value']] + 1

            if trait['trait_type'] == "Background 背景":
                if trait['value'] not in traits_background:
                    traits_background[trait['value']] = 1
                else:
                    traits_background[trait['value']] = traits_background[trait['value']] + 1

            if trait['trait_type'] == "Color 色":
                if trait['value'] not in traits_color:
                    traits_color[trait['value']] = 1
                else:
                    traits_color[trait['value']] = traits_color[trait['value']] + 1

            if trait['trait_type'] == "Head 頭":
                if trait['value'] not in traits_head:
                    traits_head[trait['value']] = 1
                else:
                    traits_head[trait['value']] = traits_head[trait['value']] + 1

            if trait['trait_type'] == "Body 体":
                if trait['value'] not in traits_body:
                    traits_body[trait['value']] = 1
                else:
                    traits_body[trait['value']] = traits_body[trait['value']] + 1

            if trait['trait_type'] == "Face 顔":
                if trait['value'] not in traits_face:
                    traits_face[trait['value']] = 1
                else:
                    traits_face[trait['value']] = traits_face[trait['value']] + 1

            if trait['trait_type'] == "Earring 耳飾り":
                if trait['value'] not in traits_earring:
                    traits_earring[trait['value']] = 1
                else:
                    traits_earring[trait['value']] = traits_earring[trait['value']] + 1

            if trait['trait_type'] == "Hand 手":
                if trait['value'] not in traits_hand:
                    traits_hand[trait['value']] = 1
                else:
                    traits_hand[trait['value']] = traits_hand[trait['value']] + 1

            if trait['trait_type'] == "Nakama 仲間":
                if trait['value'] not in traits_companion:
                    traits_companion[trait['value']] = 1
                else:
                    traits_companion[trait['value']] = traits_companion[trait['value']] + 1

            if trait['trait_type'] == "Chikara 力":
                if trait['value'] not in traits_chikara:
                    traits_chikara[trait['value']] = 1
                else:
                    traits_chikara[trait['value']] = traits_chikara[trait['value']] + 1


for file_name in range(1, 4445):
    with open(path_to_json + str(file_name) + ".json", "r", encoding='utf-8') as json_file:

        data = json.load(json_file)

        scores = []

        rarity = 0

        for trait in data['attributes']:
            if trait['trait_type'] == "Yōkai 妖怪":
                perc = traits_yokai[trait['value']] / 4444
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Yōkai 妖怪",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Background 背景":
                perc = traits_background[trait['value']] / 4444
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Background 背景",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Color 色":
                perc = traits_color[trait['value']] / 4444
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Color 色",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Head 頭":
                perc = traits_head[trait['value']] / 4444
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Head 頭",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Body 体":
                perc = traits_body[trait['value']] / 4444
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Body 体",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Face 顔":
                perc = traits_face[trait['value']] / 4444
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Face 顔",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Earring 耳飾り":
                perc = traits_earring[trait['value']] / 4444
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Earring 耳飾り",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Hand 手":
                perc = traits_hand[trait['value']] / 4444
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Hand 手",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Nakama 仲間":
                perc = traits_companion[trait['value']] / 4444
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Nakama 仲間",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Chikara 力":
                perc = traits_chikara[trait['value']] / 4444
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Chikara 力",
                        "value": score
                    }
                )
                rarity = rarity + score



    new_data = {}
    new_data['rarity'] = rarity
    new_data['scores'] = scores
    new_data.update(scores)
    new_data.update(data)

    #data.update(scores)

    with open(path_to_json + 'updated/' + str(file_name) + ".json", "w", encoding='utf-8') as json_file:
        json.dump(new_data, json_file, indent=4)

ranking = {}
for i in range(1, 4445):
    with open(path_to_json + 'updated/' + str(i) + ".json", "r", encoding='utf-8') as json_file:
        data = json.load(json_file)
        ranking[i] = data["rarity"]

new_ranking = {k: b for k, b in sorted(ranking.items(), key=lambda element: element[1], reverse=True)}
# new_ranking = sorted(ranking.items(), key=operator.itemgetter(1))

for file_name in range(1, 4445):
    with open(path_to_json + 'updated/' + str(file_name) + ".json", "r", encoding='utf-8') as json_file:

        data = json.load(json_file)

    new_data = {}
    rank = 0
    for index, d in enumerate(new_ranking):
        if d == data['tokenId']:
            rank = index + 1
    new_data['rank'] = rank
    new_data.update(data)

    with open(path_to_json + 'ranked/' + str(file_name) + ".json", "w", encoding='utf-8') as json_file:
        json.dump(new_data, json_file, indent=4)

print(ranking)
print(new_ranking)
