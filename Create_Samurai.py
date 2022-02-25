# import os
from PIL import Image
import numpy
from blend_modes import addition, multiply, overlay


def testing():
    test = Image.open('images/Ukiyoe Warriors/- Backgrounds 背景 -/Fuji 富士.png')
    test.show()


def add_test(base):
    add_layer = Image.open('images/Ukiyoe Warriors/- Textures -/1. Add Layer.png')

    base.paste(add_layer, add_layer)
    base.show()


def add_texture(base, texture):
    add_layer = texture

    img_in = numpy.array(base)
    img_in_float = img_in.astype(float)

    add_layer = numpy.array(add_layer)
    add_layer_float = add_layer.astype(float)

    blended_img_float = addition(img_in_float, add_layer_float, 1)

    blended_img = numpy.uint8(blended_img_float)
    blended_img_raw = Image.fromarray(blended_img)

    return blended_img_raw


def hard_light(base, texture):
    add_layer = texture

    img_in = numpy.array(base)
    img_in_float = img_in.astype(float)

    add_layer = numpy.array(add_layer)
    add_layer_float = add_layer.astype(float)

    blended_img_float = hard_light(img_in_float, add_layer_float)

    blended_img = numpy.uint8(blended_img_float)
    blended_img_raw = Image.fromarray(blended_img)

    return blended_img_raw


def overlay_textures(base):
    overlay_texture = Image.open('images/Ukiyoe Warriors/- Textures -/1. Overlay Texture.png')

    # Convert base to numpy array as float for blend_modes functionality
    base_array = numpy.array(base)
    base_array_float = base_array.astype(float)

    # Convert texture layer to numpy array as float for blend_modes functionality
    overlay_texture = numpy.array(overlay_texture)
    overlay_texture_float = overlay_texture.astype(float)

    # Blend Images
    opacity = 1  # okay... can i not use add_layer's alpha channel as mask????
    blended_img_float = overlay(base_array_float, overlay_texture_float, opacity)

    # Convert blended image back into PIL image
    blended_img = numpy.uint8(blended_img_float)
    blended_img_raw = Image.fromarray(blended_img)

    return mask_textures(blended_img_raw)


def mask_textures(base):  # DID THIS ACTUALLY WORK BRO?? It creates the clipping mask effect found in other image
                          # Editing programs by pasting the base image OVER the mask, using the masks alpha channel.
    mask_texture = Image.open('images/Ukiyoe Warriors/- Textures -/2. Mask Texture.png')

    mask_texture.paste(base, mask_texture)

    return mask_texture


def stamp(base):
    stamp = Image.open('images/Ukiyoe Warriors/Stamp.png')
    stamp = stamp.resize(base.size)

    base.paste(stamp, stamp)

    return base


def clean_clan(clan_dirty):
    if clan_dirty == "Ashikaga 足利":
        return "Ashikaga"
    elif clan_dirty == "Hōjō 北条":
        return "Hojo"
    elif clan_dirty == "Imagawa 今川":
        return "Imagawa"
    elif clan_dirty == "Minamoto 源":
        return "Minamoto"
    elif clan_dirty == "Sanada 真田":
        return "Sanada"
    elif clan_dirty == "Taira 平":
        return "Taira"
    elif clan_dirty == "Takeda 武田":
        return "Takeda"
    else:
        raise IOError("Error in cleaning clan name.")


# should i do each  race as it's own class? or is that excessive mem usage?
def generate(traits_list):  # create as samurai first? maybe make separate funcs for each race?
    # loop through traits list.
    # discover clan firstly
    # clan = traits_list.clan  # obviously make this work or reword/rewrite.
    # loop through the traits going through bottom-most layer first, and if it exists,
    # then add it to the image
    # finish with textures and stamp
    # save file with passed in file number... then calculate rarity? not sure yet.
    samurai_number = 1

    for traits in traits_list:
        if traits[0] == "Samurai 侍":
            print(samurai_number)
            clan_dirty = traits[3]
            clan = clean_clan(clan_dirty)

            background = traits[1]

            if background == "Autumn 秋":
                foreground = Image.open('images/Ukiyoe Warriors/- Backgrounds 背景 -/Foreground Elements/Autumn_ Falling Leaves.png')
            elif background == "Spring 春":
                foreground = Image.open(
                    'images/Ukiyoe Warriors/- Backgrounds 背景 -/Foreground Elements/Spring_ Sakura Petals.png')
            elif background == "Summer 夏":
                foreground = Image.open(
                    'images/Ukiyoe Warriors/- Backgrounds 背景 -/Foreground Elements/Summer_ Sunshine (add).png')
            elif background == "Winter 冬":
                foreground = Image.open(
                    'images/Ukiyoe Warriors/- Backgrounds 背景 -/Foreground Elements/Winter_ Snow.png')
            elif background == "Inverse Saiké サイケ逆界":
                foreground = Image.open(
                    'images/Ukiyoe Warriors/- Backgrounds 背景 -/Foreground Elements/(Inverse) Saiké_ Splatter.png')
            else:
                foreground = None

            if traits[2] != "None":
                element_back = Image.open('images/Ukiyoe Warriors/- Elements 元素 -/{}/Back.png'.format(traits[2]))
                element_front = Image.open('images/Ukiyoe Warriors/- Elements 元素 -/{}/Front.png'.format(traits[2]))
            else:
                element_back = None
                element_front = None

            banner = Image.open('images/Ukiyoe Warriors/- Banners 指物 -/{}.png'.format(traits[3]))

            skin = Image.open('images/Ukiyoe Warriors/Samurai 侍/Skin Base.png')
            skin_and_head = Image.open('images/Ukiyoe Warriors/Samurai 侍/Head Base.png')

            clothes_type = traits[4]

            if clothes_type == "Armor 鎧":
                clothes = Image.open('images/Ukiyoe Warriors/Samurai 侍/Attire 服装/Armor 鎧/{}.png'.format(clan))
                gauntlets = Image.open('images/Ukiyoe Warriors/Samurai 侍/Attire 服装/Armor 鎧/Gauntlets 籠手/{0}/{1}.png'.format(traits[5], clan))
            elif clothes_type == "Street Clothes 街着":
                clothes = Image.open('images/Ukiyoe Warriors/Samurai 侍/Attire 服装/Street Clothes 街着/{}.png'.format(clan))
                gauntlets = Image.open(
                    'images/Ukiyoe Warriors/Samurai 侍/Attire 服装/Street Clothes 街着/Sleeves 籠手/{0}/{1}.png'.format(traits[5], clan))
            elif clothes_type == "Kimono Flowers 着物花":
                clothes = Image.open('images/Ukiyoe Warriors/Samurai 侍/Attire 服装/Kimono 着物/Flower 花/{}.png'.format(clan))
                gauntlets = None
            elif clothes_type == "Kimono Waves 着物波":
                clothes = Image.open('images/Ukiyoe Warriors/Samurai 侍/Attire 服装/Kimono 着物/Waves 波/{}.png'.format(clan))
                gauntlets = None
            else:
                clothes = Image.open('images/Ukiyoe Warriors/Samurai 侍/Attire 服装/Kimono 着物/Clouds 雲/{}.png'.format(clan))
                gauntlets = None

            wep = traits[5]
            if wep == "Bow 弓":
                weapon = Image.open('images/Ukiyoe Warriors/Samurai 侍/Weapons 武器/Bow 弓/{}.png'.format(clan))
                obi = None
            elif wep == "Demon Sword 妖刀":
                weapon = Image.open('images/Ukiyoe Warriors/Samurai 侍/Weapons 武器/Demon Sword 妖刀/Demon Sword 妖刀.png')
                if clothes == "Armor 鎧":
                    obi = Image.open('images/Ukiyoe Warriors/Samurai 侍/Weapons 武器/Demon Sword 妖刀/Obi 帯/w_Armor.png')
                elif clothes == "Street Clothes 街着":
                    obi = Image.open('images/Ukiyoe Warriors/Samurai 侍/Weapons 武器/Demon Sword 妖刀/Obi 帯/w_Street Clothes.png')
                else:
                    obi = Image.open('images/Ukiyoe Warriors/Samurai 侍/Weapons 武器/Demon Sword 妖刀/Obi 帯/w_Kimono.png')
            elif wep == "Katana 刀":
                weapon = Image.open('images/Ukiyoe Warriors/Samurai 侍/Weapons 武器/Katana 刀/{}.png'.format(clan))
                if clothes == "Armor 鎧":
                    obi = Image.open('images/Ukiyoe Warriors/Samurai 侍/Weapons 武器/Katana 刀/Obi 帯/w_Armor.png')
                elif clothes == "Street Clothes 街着":
                    obi = Image.open('images/Ukiyoe Warriors/Samurai 侍/Weapons 武器/Katana 刀/Obi 帯/w_Street Clothes.png')
                else:
                    obi = Image.open('images/Ukiyoe Warriors/Samurai 侍/Weapons 武器/Katana 刀/Obi 帯/w_Kimono.png')
            elif wep == "Niten-Ichiryu 二天一流":
                weapon = Image.open('images/Ukiyoe Warriors/Samurai 侍/Weapons 武器/Niten-Ichiryu 二天一流/{}.png'.format(clan))
                obi = None
            elif wep == "Boar Blades 猪の剣":
                weapon = Image.open('images/Ukiyoe Warriors/Samurai 侍/Weapons 武器/Boar Blades 猪の剣.png')
                obi = None
            else:
                weapon = Image.open('images/Ukiyoe Warriors/Samurai 侍/Weapons 武器/SHAman Bow シャマ弓.png')
                obi = None

            earring_l_trait = traits[6]
            if earring_l_trait != "None":
                earring_l = Image.open('images/Ukiyoe Warriors/Samurai 侍/Earrings 耳飾り/Earring 1 (Left)/{}.png'.format(earring_l_trait))
            else:
                earring_l = None
            if traits[7] != "None":
                earring_r = Image.open('images/Ukiyoe Warriors/Samurai 侍/Earrings 耳飾り/Earring 2 (Right)/{}.png'.format(traits[7]))
            else:
                earring_r = None

            eyes_trait = traits[8]
            if eyes_trait == "Saiké サイケ":
                # TODO saike it up.. must be correct order though???
                print("saike")
                eyes = Image.open('images/Ukiyoe Warriors/Samurai 侍/Eyes 目/Saiké サイケ/Eyes.png')
            else:
                eyes = Image.open('images/Ukiyoe Warriors/Samurai 侍/Eyes 目/{}.png'.format(eyes_trait))

            face_trait = traits[9]
            if face_trait == "None":
                face = None
            else:
                face = Image.open('images/Ukiyoe Warriors/Samurai 侍/Face 顔/{}.png'.format(face_trait))

            head_trait = traits[10]
            if head_trait in ["Chasen 茶筅", "Sedge Hat 菅笠", "Topknot 髷"]:  # No back No clan
                head = Image.open('images/Ukiyoe Warriors/Samurai 侍/Head 頭/{}.png'.format(head_trait))
                head_back = None
            elif head_trait in ["Disheveled 乱れ髪 + Headband 鉢巻", "Kabuto 兜"]:  # Back and Clan
                head = Image.open('images/Ukiyoe Warriors/Samurai 侍/Head 頭/{0}/Front/{1}.png'.format(head_trait, clan))
                head_back = Image.open('images/Ukiyoe Warriors/Samurai 侍/Head 頭/{0}/Back.png'.format(head_trait))
            elif head_trait in ["Chasen 茶筅 + Headband 鉢巻", "Topknot 髷 + Headband 鉢巻", "Jingasa 陣笠"]:  # NO Back and Clan
                head = Image.open('images/Ukiyoe Warriors/Samurai 侍/Head 頭/{0}/{1}.png'.format(head_trait, clan))
                head_back = None
            else:  # Back and NO Clan  DISHEVELED ONLY
                head = Image.open('images/Ukiyoe Warriors/Samurai 侍/Head 頭/{0}/Front.png'.format(head_trait))
                head_back = Image.open('images/Ukiyoe Warriors/Samurai 侍/Head 頭/{0}/Back.png'.format(head_trait))

            base = Image.open('images/Ukiyoe Warriors/- Backgrounds 背景 -/{}.png'.format(background))  # Base == bg
            base = base.convert('RGBA')

            if element_back is not None:
                base.paste(element_back, element_back)

            base.paste(banner, banner)  # clan banner

            if head_back is not None:
                base.paste(head_back, head_back)

            base.paste(skin, skin)
            base.paste(clothes, clothes)
            base.paste(weapon, weapon)

            if obi is not None:
                base.paste(obi, obi)

            if gauntlets is not None:
                base.paste(gauntlets, gauntlets)

            if earring_r is not None:
                base.paste(earring_r, earring_r)

            base.paste(skin_and_head, skin_and_head)
            base.paste(eyes, eyes)  # TODO make sure to add if saike at end!

            if face is not None:
                base.paste(face, face)

            if earring_l is not None:
                base.paste(earring_l, earring_l)

            base.paste(head, head)

            if eyes_trait == "Saiké サイケ":
                saike_1 = Image.open('images/Ukiyoe Warriors/Samurai 侍/Eyes 目/Saiké サイケ/Glow 1 (add).png')
                saike_2 = Image.open('images/Ukiyoe Warriors/Samurai 侍/Eyes 目/Saiké サイケ/Glow 2 (add).png')
                base = add_texture(base, saike_1)
                base = add_texture(base, saike_2)

            if element_front is not None:
                base.paste(element_front, element_front)

            if foreground is not None:
                if background == "Summer 夏":
                    foreground = foreground.convert('RGBA')
                    base = add_texture(base, foreground)
                elif background == "Winter 冬":
                    foreground = foreground.convert('RGBA')
                    base = hard_light(base, foreground)
                else:
                    foreground = foreground.convert('RGBA')
                    base.paste(foreground, foreground)

            base = overlay_textures(base)

            base.save("output/UkiyoeWarrior#{}.png".format(samurai_number))
            samurai_number += 1

        elif traits[0] == "Musha 武者":
            print(samurai_number)
            clan_dirty = traits[3]
            clan = clean_clan(clan_dirty)

            background = traits[1]

            if background == "Autumn 秋":
                foreground = Image.open(
                    'images/Ukiyoe Warriors/- Backgrounds 背景 -/Foreground Elements/Autumn_ Falling Leaves.png')
            elif background == "Spring 春":
                foreground = Image.open(
                    'images/Ukiyoe Warriors/- Backgrounds 背景 -/Foreground Elements/Spring_ Sakura Petals.png')
            elif background == "Summer 夏":
                foreground = Image.open(
                    'images/Ukiyoe Warriors/- Backgrounds 背景 -/Foreground Elements/Summer_ Sunshine (add).png')
            elif background == "Winter 冬":
                foreground = Image.open(
                    'images/Ukiyoe Warriors/- Backgrounds 背景 -/Foreground Elements/Winter_ Snow.png')
            elif background == "Inverse Saiké サイケ逆界":
                foreground = Image.open(
                    'images/Ukiyoe Warriors/- Backgrounds 背景 -/Foreground Elements/(Inverse) Saiké_ Splatter.png')
            else:
                foreground = None

            if traits[2] != "None":
                element_back = Image.open('images/Ukiyoe Warriors/- Elements 元素 -/{}/Back.png'.format(traits[2]))
                element_front = Image.open('images/Ukiyoe Warriors/- Elements 元素 -/{}/Front.png'.format(traits[2]))
            else:
                element_back = None
                element_front = None

            banner = Image.open('images/Ukiyoe Warriors/- Banners 指物 -/{}.png'.format(traits[3]))

            skin = Image.open('images/Ukiyoe Warriors/Musha 武者/Skin Base.png')
            skin_and_head = Image.open('images/Ukiyoe Warriors/Musha 武者/Head Base.png')

            clothes_type = traits[4]

            if clothes_type == "Armor 鎧":
                clothes = Image.open('images/Ukiyoe Warriors/Musha 武者/Attire 服装/Armor 鎧/{}.png'.format(clan))
                gauntlets = Image.open(
                    'images/Ukiyoe Warriors/Musha 武者/Attire 服装/Armor 鎧/Gauntlets 籠手/{}.png'.format(traits[5]))
            elif clothes_type == "Street Clothes 街着":
                clothes = Image.open(
                    'images/Ukiyoe Warriors/Musha 武者/Attire 服装/Street Clothes 街着/{}.png'.format(clan))
                gauntlets = None
            elif clothes_type == "Kimono Flowers 着物花":
                clothes = Image.open(
                    'images/Ukiyoe Warriors/Musha 武者/Attire 服装/Kimono 着物/Flower 花/{}.png'.format(clan))
                gauntlets = None
            elif clothes_type == "Kimono Waves 着物波":
                clothes = Image.open('images/Ukiyoe Warriors/Musha 武者/Attire 服装/Kimono 着物/Waves 波/{}.png'.format(clan))
                gauntlets = None
            else:
                clothes = Image.open(
                    'images/Ukiyoe Warriors/Musha 武者/Attire 服装/Kimono 着物/Clouds 雲/{}.png'.format(clan))
                gauntlets = None

            wep = traits[5]
            if wep == "Bow 弓":
                weapon = Image.open('images/Ukiyoe Warriors/Musha 武者/Weapons 武器/Bow 弓/{}.png'.format(clan))
                obi = None
            elif wep == "Demon Sword 妖刀":
                weapon = Image.open('images/Ukiyoe Warriors/Musha 武者/Weapons 武器/Demon Sword 妖刀/Demon Sword 妖刀.png')
                if clothes == "Armor 鎧":
                    obi = Image.open('images/Ukiyoe Warriors/Musha 武者/Weapons 武器/Demon Sword 妖刀/Obi 帯/w_Armor.png')
                elif clothes == "Street Clothes 街着":
                    obi = Image.open(
                        'images/Ukiyoe Warriors/Musha 武者/Weapons 武器/Demon Sword 妖刀/Obi 帯/w_Street Clothes.png')
                else:
                    obi = Image.open('images/Ukiyoe Warriors/Musha 武者/Weapons 武器/Demon Sword 妖刀/Obi 帯/w_Kimono.png')
            elif wep == "Katana 刀":
                weapon = Image.open('images/Ukiyoe Warriors/Musha 武者/Weapons 武器/Katana 刀/{}.png'.format(clan))
                if clothes == "Armor 鎧":
                    obi = Image.open('images/Ukiyoe Warriors/Musha 武者/Weapons 武器/Katana 刀/Obi 帯/w_Armor.png')
                elif clothes == "Street Clothes 街着":
                    obi = Image.open('images/Ukiyoe Warriors/Musha 武者/Weapons 武器/Katana 刀/Obi 帯/w_Street Clothes.png')
                else:
                    obi = Image.open('images/Ukiyoe Warriors/Musha 武者/Weapons 武器/Katana 刀/Obi 帯/w_Kimono.png')
            elif wep == "Niten-Ichiryu 二天一流":
                weapon = Image.open(
                    'images/Ukiyoe Warriors/Musha 武者/Weapons 武器/Niten-Ichiryu 二天一流/{}.png'.format(clan))
                obi = None
            elif wep == "Boar Blades 猪の剣":
                weapon = Image.open('images/Ukiyoe Warriors/Musha 武者/Weapons 武器/Boar Blades 猪の剣.png')
                obi = None
            else:
                weapon = Image.open('images/Ukiyoe Warriors/Musha 武者/Weapons 武器/SHAman Bow シャマ弓.png')
                obi = None

            earring_l_trait = traits[6]
            if earring_l_trait != "None":
                earring_l = Image.open(
                    'images/Ukiyoe Warriors/Musha 武者/Earrings 耳飾り/Earring 1 (Left)/{}.png'.format(earring_l_trait))
            else:
                earring_l = None
            if traits[7] != "None":
                earring_r = Image.open(
                    'images/Ukiyoe Warriors/Musha 武者/Earrings 耳飾り/Earring 2 (Right)/{}.png'.format(traits[7]))
            else:
                earring_r = None

            eyes_trait = traits[8]
            if eyes_trait == "Saiké サイケ":
                # TODO saike it up.. must be correct order though???
                print("saike")
                eyes = Image.open('images/Ukiyoe Warriors/Musha 武者/Eyes 目/Saiké サイケ/Eyes.png')
            else:
                eyes = Image.open('images/Ukiyoe Warriors/Musha 武者/Eyes 目/{}.png'.format(eyes_trait))

            face_trait = traits[9]
            if face_trait == "None":
                face = None
            else:
                face = Image.open('images/Ukiyoe Warriors/Musha 武者/Face 顔/{}.png'.format(face_trait))

            head_trait = traits[10]
            if head_trait in ["Chasen 茶筅", "Sedge Hat 菅笠", "Topknot 髷"]:  # No back No clan
                head = Image.open('images/Ukiyoe Warriors/Musha 武者/Head 頭/{}.png'.format(head_trait))
                head_back = None
            elif head_trait in ["Disheveled 乱れ髪 + Headband 鉢巻", "Kabuto 兜"]:  # Back and Clan
                head = Image.open('images/Ukiyoe Warriors/Musha 武者/Head 頭/{0}/Front/{1}.png'.format(head_trait, clan))
                head_back = Image.open('images/Ukiyoe Warriors/Musha 武者/Head 頭/{0}/Back.png'.format(head_trait))
            elif head_trait in ["Chasen 茶筅 + Headband 鉢巻", "Topknot 髷 + Headband 鉢巻", "Jingasa 陣笠"]:  # NO Back and Clan
                head = Image.open('images/Ukiyoe Warriors/Musha 武者/Head 頭/{0}/{1}.png'.format(head_trait, clan))
                head_back = None
            else:  # Back and NO Clan  DISHEVELED ONLY
                head = Image.open('images/Ukiyoe Warriors/Musha 武者/Head 頭/{0}/Front.png'.format(head_trait))
                head_back = Image.open('images/Ukiyoe Warriors/Musha 武者/Head 頭/{0}/Back.png'.format(head_trait))

            base = Image.open('images/Ukiyoe Warriors/- Backgrounds 背景 -/{}.png'.format(background))  # Base == bg
            base = base.convert('RGBA')

            if element_back is not None:
                base.paste(element_back, element_back)

            base.paste(banner, banner)  # clan banner

            if head_back is not None:
                base.paste(head_back, head_back)

            base.paste(skin, skin)
            base.paste(clothes, clothes)
            base.paste(weapon, weapon)

            if obi is not None:
                base.paste(obi, obi)

            if gauntlets is not None:
                base.paste(gauntlets, gauntlets)

            if earring_r is not None:
                base.paste(earring_r, earring_r)

            base.paste(skin_and_head, skin_and_head)
            base.paste(eyes, eyes)  # TODO make sure to add if saike at end!

            if face is not None:
                base.paste(face, face)

            if earring_l is not None:
                base.paste(earring_l, earring_l)

            base.paste(head, head)

            if eyes_trait == "Saiké サイケ":
                saike_1 = Image.open('images/Ukiyoe Warriors/Musha 武者/Eyes 目/Saiké サイケ/Glow 1 (add).png')
                saike_2 = Image.open('images/Ukiyoe Warriors/Musha 武者/Eyes 目/Saiké サイケ/Glow 2 (add).png')
                base = add_texture(base, saike_1)
                base = add_texture(base, saike_2)

            if element_front is not None:
                base.paste(element_front, element_front)

            if foreground is not None:
                if background == "Summer 夏":
                    foreground = foreground.convert('RGBA')
                    base = add_texture(base, foreground)
                elif background == "Winter 冬":
                    foreground = foreground.convert('RGBA')
                    base = hard_light(base, foreground)
                else:
                    foreground = foreground.convert('RGBA')
                    base.paste(foreground, foreground)

            base = overlay_textures(base)

            base.save("output/UkiyoeWarrior#{}.png".format(samurai_number))
            samurai_number += 1
        else:  # Ape 猿
            print(samurai_number)
            clan_dirty = traits[3]
            clan = clean_clan(clan_dirty)

            background = traits[1]

            if background == "Autumn 秋":
                foreground = Image.open(
                    'images/Ukiyoe Warriors/- Backgrounds 背景 -/Foreground Elements/Autumn_ Falling Leaves.png')
            elif background == "Spring 春":
                foreground = Image.open(
                    'images/Ukiyoe Warriors/- Backgrounds 背景 -/Foreground Elements/Spring_ Sakura Petals.png')
            elif background == "Summer 夏":
                foreground = Image.open(
                    'images/Ukiyoe Warriors/- Backgrounds 背景 -/Foreground Elements/Summer_ Sunshine (add).png')
            elif background == "Winter 冬":
                foreground = Image.open(
                    'images/Ukiyoe Warriors/- Backgrounds 背景 -/Foreground Elements/Winter_ Snow.png')
            elif background == "Inverse Saiké サイケ逆界":
                foreground = Image.open(
                    'images/Ukiyoe Warriors/- Backgrounds 背景 -/Foreground Elements/(Inverse) Saiké_ Splatter.png')
            else:
                foreground = None

            if traits[2] != "None":
                element_back = Image.open('images/Ukiyoe Warriors/- Elements 元素 -/{}/Back.png'.format(traits[2]))
                element_front = Image.open('images/Ukiyoe Warriors/- Elements 元素 -/{}/Front.png'.format(traits[2]))
            else:
                element_back = None
                element_front = None

            banner = Image.open('images/Ukiyoe Warriors/- Banners 指物 -/{}.png'.format(traits[3]))

            skin = Image.open('images/Ukiyoe Warriors/Ape 猿/Skin Base.png')
            # skin_and_head = Image.open('images/Ukiyoe Warriors/Ape 猿/Head Base.png')

            clothes_type = traits[4]

            if clothes_type == "Armor 鎧":
                clothes = Image.open('images/Ukiyoe Warriors/Ape 猿/Attire 服装/Armor 鎧/{}.png'.format(clan))
                gauntlets = Image.open(
                    'images/Ukiyoe Warriors/Ape 猿/Attire 服装/Armor 鎧/Gauntlets 籠手/{0}/{1}.png'.format(traits[5],
                                                                                                          clan))
            elif clothes_type == "Street Clothes 街着":
                clothes = Image.open(
                    'images/Ukiyoe Warriors/Ape 猿/Attire 服装/Street Clothes 街着/{}.png'.format(clan))
                gauntlets = None
            elif clothes_type == "Kimono Flowers 着物花":
                clothes = Image.open(
                    'images/Ukiyoe Warriors/Ape 猿/Attire 服装/Kimono 着物/Flower 花/{}.png'.format(clan))
                gauntlets = None
            elif clothes_type == "Kimono Waves 着物波":
                clothes = Image.open('images/Ukiyoe Warriors/Ape 猿/Attire 服装/Kimono 着物/Waves 波/{}.png'.format(clan))
                gauntlets = None
            else:
                clothes = Image.open(
                    'images/Ukiyoe Warriors/Ape 猿/Attire 服装/Kimono 着物/Clouds 雲/{}.png'.format(clan))
                gauntlets = None

            wep = traits[5]
            if wep == "Bow 弓":
                weapon = Image.open('images/Ukiyoe Warriors/Ape 猿/Weapons 武器/Bow 弓/{}.png'.format(clan))
                obi = None
            elif wep == "Demon Sword 妖刀":
                weapon = Image.open('images/Ukiyoe Warriors/Ape 猿/Weapons 武器/Demon Sword 妖刀/Demon Sword 妖刀.png')
                if clothes == "Armor 鎧":
                    obi = Image.open('images/Ukiyoe Warriors/Ape 猿/Weapons 武器/Demon Sword 妖刀/Obi 帯/w_Armor.png')
                elif clothes == "Street Clothes 街着":
                    obi = Image.open(
                        'images/Ukiyoe Warriors/Ape 猿/Weapons 武器/Demon Sword 妖刀/Obi 帯/w_Street Clothes.png')
                else:
                    obi = Image.open('images/Ukiyoe Warriors/Ape 猿/Weapons 武器/Demon Sword 妖刀/Obi 帯/w_Kimono.png')
            elif wep == "Katana 刀":
                weapon = Image.open('images/Ukiyoe Warriors/Ape 猿/Weapons 武器/Katana 刀/{}.png'.format(clan))
                if clothes == "Armor 鎧":
                    obi = Image.open('images/Ukiyoe Warriors/Ape 猿/Weapons 武器/Katana 刀/Obi 帯/w_Armor.png')
                elif clothes == "Street Clothes 街着":
                    obi = Image.open('images/Ukiyoe Warriors/Ape 猿/Weapons 武器/Katana 刀/Obi 帯/w_Street Clothes.png')
                else:
                    obi = Image.open('images/Ukiyoe Warriors/Ape 猿/Weapons 武器/Katana 刀/Obi 帯/w_Kimono.png')
            elif wep == "Niten-Ichiryu 二天一流":
                weapon = Image.open(
                    'images/Ukiyoe Warriors/Ape 猿/Weapons 武器/Niten-Ichiryu 二天一流/{}.png'.format(clan))
                obi = None
            elif wep == "Boar Blades 猪の剣":
                weapon = Image.open('images/Ukiyoe Warriors/Ape 猿/Weapons 武器/Boar Blades 猪の剣.png')
                obi = None
            else:
                weapon = Image.open('images/Ukiyoe Warriors/Ape 猿/Weapons 武器/SHAman Bow シャマ弓.png')
                obi = None

            earring_l_trait = traits[6]
            if earring_l_trait != "None":
                earring_l = Image.open(
                    'images/Ukiyoe Warriors/Ape 猿/Earrings 耳飾り/Earring 1 (Left)/{}.png'.format(earring_l_trait))
            else:
                earring_l = None
            earring_r = None

            eyes_trait = traits[8]
            if eyes_trait == "Saiké サイケ":
                # TODO saike it up.. must be correct order though???
                print("saike")
                eyes = Image.open('images/Ukiyoe Warriors/Ape 猿/Eyes 目/Saiké サイケ/Eyes.png')
            else:
                eyes = Image.open('images/Ukiyoe Warriors/Ape 猿/Eyes 目/{}.png'.format(eyes_trait))

            face_trait = traits[9]
            if face_trait == "None":
                face = None
            else:
                face = Image.open('images/Ukiyoe Warriors/Ape 猿/Face 顔/{}.png'.format(face_trait))

            head_trait = traits[10]

            # ape head base
            if head_trait == "Short 短毛":
                head = None
                skin_and_head = Image.open('images/Ukiyoe Warriors/Ape 猿/Head 頭/Head Base/Short 短毛.png')
                kabuto = None
            elif head_trait == "Short 短毛 + Headband 鉢巻":
                head = Image.open('images/Ukiyoe Warriors/Ape 猿/Head 頭/Headband 鉢巻/{}.png'.format(clan))
                skin_and_head = Image.open('images/Ukiyoe Warriors/Ape 猿/Head 頭/Head Base/{}.png'.format(head_trait))
                kabuto = None
            elif head_trait == "Messy ボサボサ":
                head = None
                skin_and_head = Image.open('images/Ukiyoe Warriors/Ape 猿/Head 頭/Head Base/{}.png'.format(head_trait))
                kabuto = None
            elif head_trait == "Messy ボサボサ + Headband 鉢巻":
                head = Image.open('images/Ukiyoe Warriors/Ape 猿/Head 頭/Headband 鉢巻/{}.png'.format(clan))
                skin_and_head = Image.open('images/Ukiyoe Warriors/Ape 猿/Head 頭/Head Base/{}.png'.format(head_trait))
                kabuto = None
            elif head_trait == "Spiked ツンツン":
                head = None
                skin_and_head = Image.open('images/Ukiyoe Warriors/Ape 猿/Head 頭/Head Base/{}.png'.format(head_trait))
                kabuto = None
            elif head_trait == "Spiked ツンツン + Headband 鉢巻":
                head = Image.open('images/Ukiyoe Warriors/Ape 猿/Head 頭/Headband 鉢巻/{}.png'.format(clan))
                skin_and_head = Image.open('images/Ukiyoe Warriors/Ape 猿/Head 頭/Head Base/{}.png'.format(head_trait))
                kabuto = None
            elif head_trait == "Sedge Hat 菅笠":
                head = Image.open('images/Ukiyoe Warriors/Ape 猿/Head 頭/Sedge Hat.png')
                skin_and_head = Image.open('images/Ukiyoe Warriors/Ape 猿/Head 頭/Head Base/Short 短毛.png')
                kabuto = None
            elif head_trait == "Jingasa 陣笠":
                head = Image.open('images/Ukiyoe Warriors/Ape 猿/Head 頭/Jingasa 陣笠/{}.png'.format(clan))
                skin_and_head = Image.open('images/Ukiyoe Warriors/Ape 猿/Head 頭/Head Base/Short 短毛.png')
                kabuto = None
            elif head_trait == "Kabuto 兜":
                head = Image.open('images/Ukiyoe Warriors/Ape 猿/Head 頭/Kabuto 兜/Front/{}.png'.format(clan))
                skin_and_head = Image.open('images/Ukiyoe Warriors/Ape 猿/Head 頭/Head Base/Short 短毛.png')
                kabuto = Image.open('images/Ukiyoe Warriors/Ape 猿/Head 頭/Kabuto 兜/Back.png')
            else:
                head = None
                skin_and_head = None
                kabuto = None
                raise IOError('missed something?')

            base = Image.open('images/Ukiyoe Warriors/- Backgrounds 背景 -/{}.png'.format(background))  # Base == bg
            base = base.convert('RGBA')

            if element_back is not None:
                base.paste(element_back, element_back)

            base.paste(banner, banner)  # clan banner

            if kabuto is not None:
                base.paste(kabuto, kabuto)

            base.paste(skin, skin)
            base.paste(clothes, clothes)
            base.paste(weapon, weapon)

            if obi is not None:
                base.paste(obi, obi)

            if gauntlets is not None:
                base.paste(gauntlets, gauntlets)

            if earring_r is not None:
                base.paste(earring_r, earring_r)

            base.paste(skin_and_head, skin_and_head)
            base.paste(eyes, eyes)  # TODO make sure to add if saike at end!

            if face is not None:
                base.paste(face, face)

            if earring_l is not None:
                base.paste(earring_l, earring_l)

            base.paste(head, head)

            if eyes_trait == "Saiké サイケ":
                saike_1 = Image.open('images/Ukiyoe Warriors/Ape 猿/Eyes 目/Saiké サイケ/Glow 1 (add).png')
                saike_2 = Image.open('images/Ukiyoe Warriors/Ape 猿/Eyes 目/Saiké サイケ/Glow 2 (add).png')
                base = add_texture(base, saike_1)
                base = add_texture(base, saike_2)

            if element_front is not None:
                base.paste(element_front, element_front)

            if foreground is not None:
                if background == "Summer 夏":
                    foreground = foreground.convert('RGBA')
                    base = add_texture(base, foreground)
                elif background == "Winter 冬":
                    foreground = foreground.convert('RGBA')
                    base = hard_light(base, foreground)
                else:
                    foreground = foreground.convert('RGBA')
                    base.paste(foreground, foreground)

            base = overlay_textures(base)

            base.save("output/UkiyoeWarrior#{}.png".format(samurai_number))
            samurai_number += 1
# TODO add an Image.close() for each png layer????? after each iter.
