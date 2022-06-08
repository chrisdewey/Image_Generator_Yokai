import json
import ast


# Order = [char, bg, color, head, body, face, earring, companion, hand, chikara]
def yokai_metadata_from_file(traits_list_txt):

    with open(traits_list_txt, 'r', encoding='utf-8') as f:
        traits_list = ast.literal_eval(f.read())

    # Japanese for none: 無し
    for i in range(len(traits_list)):
        # token_id = i['tokenId']
        token_id = i+1
        token = {
            "image": "UkiyoeYokai#{}.png".format(token_id),
            "tokenId": token_id,
            "name": "Ukiyoe Yokai" + ' ' + str(token_id),
            "attributes": []
        }
        token["attributes"].append(
            {
                "trait_type": "Yōkai 妖怪",
                "value": traits_list[i][0]
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Background 背景",
                "value": traits_list[i][1]
            }
        )
        color = traits_list[i][2]
        if traits_list[i][0] == "Ōkami 狼" and color == "Slate Blue 炭青":
            color = "Slate 炭青"
        token["attributes"].append(
            {
                "trait_type": "Color 色",
                "value": color
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Head 頭",
                "value": traits_list[i][3]
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Body 体",
                "value": traits_list[i][4]
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Face 顔",
                "value": traits_list[i][5]
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Earring 耳飾り",
                "value": traits_list[i][6]
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Hand 手",
                "value": traits_list[i][8]
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Nakama 仲間",
                "value": traits_list[i][7]
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Chikara 力",
                "value": traits_list[i][9]
            }
        )

        with open('output/metadata/' + str(token_id) + ".json", 'w') as outfile:
            json.dump(token, outfile, indent=4)
