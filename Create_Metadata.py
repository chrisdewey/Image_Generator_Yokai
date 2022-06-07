import json


def yokai(traits_list):

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
        ele_val = traits_list[i][2]
        if ele_val == "None":
            ele_val = ele_val + " 無し"
        token["attributes"].append(
            {
                "trait_type": "Element 元素",
                "value": ele_val
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Clan 一族",
                "value": traits_list[i][3]
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Attire 服装",
                "value": traits_list[i][4]
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Weapon 武器",
                "value": traits_list[i][5]
            }
        )
        head_val = traits_list[i][10]
        if head_val == "None":
            head_val = head_val + " 無し"
        token["attributes"].append(
            {
                "trait_type": "Head 頭",
                "value": head_val
            }
        )
        ear_val = traits_list[i][6]
        if ear_val == "None":
            ear_val = ear_val + " 無し"
        token["attributes"].append(
            {
                "trait_type": "Earrings 耳飾り",
                "value": ear_val
            }
        )
        face_val = traits_list[i][9]
        if face_val == "None":
            face_val = face_val + " 無し"
        token["attributes"].append(
            {
                "trait_type": "Face 顔",
                "value": face_val
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Eyes 目",
                "value": traits_list[i][8]
            }
        )

        with open('output/metadata/' + str(token_id) + ".json", 'w') as outfile:
            json.dump(token, outfile, indent=4)
