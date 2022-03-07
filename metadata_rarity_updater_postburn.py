import json

traits_warrior = {}
traits_background = {}
traits_element = {}
traits_clan = {}
traits_attire = {}
traits_weapon = {}
traits_head = {}
traits_earrings = {}
traits_face = {}
traits_eyes = {}

path_to_json = 'output/metadata/'
list_of_burns = [3114, 1, 2, 3, 4, 5]
total_after_burn = 3777 - len(list_of_burns)
for file_name in range(1, 3778):
    if file_name in list_of_burns:
        continue

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

for file_name in range(1, 3778):
    if file_name in list_of_burns:
        continue

    with open(path_to_json + str(file_name) + ".json", "r", encoding='utf-8') as json_file:

        data = json.load(json_file)

        scores = []

        rarity = 0

        for trait in data['attributes']:
            if trait['trait_type'] == "Warrior 武士":
                perc = traits_warrior[trait['value']] / total_after_burn
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Warrior 武士",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Background 背景":
                perc = traits_background[trait['value']] / total_after_burn
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Background 背景",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Element 元素":
                perc = traits_element[trait['value']] / total_after_burn
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Element 元素",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Clan 一族":
                perc = traits_clan[trait['value']] / total_after_burn
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Clan 一族",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Attire 服装":
                perc = traits_attire[trait['value']] / total_after_burn
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Attire 服装",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Weapon 武器":
                perc = traits_weapon[trait['value']] / total_after_burn
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Weapon 武器",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Head 頭":
                perc = traits_head[trait['value']] / total_after_burn
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Head 頭",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Earrings 耳飾り":
                perc = traits_earrings[trait['value']] / total_after_burn
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Earrings 耳飾り",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Face 顔":
                perc = traits_face[trait['value']] / total_after_burn
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Face 顔",
                        "value": score
                    }
                )
                rarity = rarity + score

            if trait['trait_type'] == "Eyes 目":
                perc = traits_eyes[trait['value']] / total_after_burn
                score = 1 / perc
                scores.append(
                    {
                        "trait_type": "Eyes 目",
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

    with open(path_to_json + 'postburn/' + str(file_name) + ".json", "w", encoding='utf-8') as json_file:
        json.dump(new_data, json_file, indent=4)

ranking = {}
for i in range(1, 3778):
    if i in list_of_burns:
        continue

    with open(path_to_json + 'postburn/' + str(i) + ".json", "r", encoding='utf-8') as json_file:
        data = json.load(json_file)
        ranking[i] = data["rarity"]

new_ranking = {k: b for k, b in sorted(ranking.items(), key=lambda element: element[1], reverse=True)}
# new_ranking = sorted(ranking.items(), key=operator.itemgetter(1))

for file_name in range(1, 3778):
    if file_name in list_of_burns:
        continue

    with open(path_to_json + 'postburn/' + str(file_name) + ".json", "r", encoding='utf-8') as json_file:

        data = json.load(json_file)

    new_data = {}
    rank = 0
    for index, d in enumerate(new_ranking):
        if d == data['tokenId']:
            rank = index + 1
    new_data['rank'] = rank
    new_data.update(data)

    with open(path_to_json + 'postburn2/' + str(file_name) + ".json", "w", encoding='utf-8') as json_file:
        json.dump(new_data, json_file, indent=4)

print(ranking)
print(new_ranking)
