import json


def samurai(traits_list):

    # Japanese for none: 無し
    for i in range(len(traits_list)):
        # token_id = i['tokenId']
        token_id = i
        token = {
            "image": "Samurai#{}.png".format(i),
            "tokenId": token_id,
            "name": "Ukiyoe Warriors" + ' ' + str(token_id),
            "attributes": []
        }
        token["attributes"].append(
            {
                "trait_type": "Character",
                "value": "Samurai"  # TODO make dynamic?? unless we're keeping samurai as the function and repeating...
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Background",
                "value": traits_list[i][0]
            }
        )
        # print(traits_list[i])
        token["attributes"].append(
            {
                "trait_type": "Clan",
                "value": traits_list[i][1]
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Attire",
                "value": traits_list[i][2]
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Eyes",
                "value": traits_list[i][3]
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Face",
                "value": traits_list[i][4]
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Earring(s)",
                "value": traits_list[i][5]
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Headwear/Hair",  # TODO change to head wear/ hair???
                "value": traits_list[i][7]
            }
        )
        token["attributes"].append(
            {
                "trait_type": "Weapon",
                "value": traits_list[i][8]
            }
        )

        with open('output/metadata/' + str(token_id) + ".json", 'w') as outfile:
            json.dump(token, outfile, indent=4)
