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


def add_texture(base):
    add_layer = Image.open('images/Ukiyoe Warriors/- Textures -/1. Add Layer.png')

    # base.paste(add_layer, add_layer)

    add_layer = add_layer.resize(base.size)

    # Convert base to numpy array as float for blend_modes functionality
    base_array = numpy.array(base)
    base_array_float = base_array.astype(float)

    # Convert texture layer to numpy array as float for blend_modes functionality
    add_layer = numpy.array(add_layer)
    add_layer_float = add_layer.astype(float)

    # Blend Images
    opacity = 1  # okay... can i not use add_layer's alpha channel as mask????
    blended_img_float = addition(base_array_float, add_layer_float, opacity)

    # Convert blended image back into PIL image
    blended_img = numpy.uint8(blended_img_float)
    blended_img_raw = Image.fromarray(blended_img)

    mask_textures(blended_img_raw)


def mult_texture(base):
    mult_layer = Image.open('images/Ukiyoe Warriors/- Textures -/2. Multiply Layer.png')

    # base.paste(add_layer, add_layer)

    mult_layer = mult_layer.resize(base.size)

    # Convert base to numpy array as float for blend_modes functionality
    base_array = numpy.array(base)
    base_array_float = base_array.astype(float)

    # Convert texture layer to numpy array as float for blend_modes functionality
    mult_layer = numpy.array(mult_layer)
    mult_layer_float = mult_layer.astype(float)

    # Blend Images
    opacity = 1  # okay... can i not use add_layer's alpha channel as mask????
    blended_img_float = multiply(base_array_float, mult_layer_float, opacity)

    # Convert blended image back into PIL image
    blended_img = numpy.uint8(blended_img_float)
    blended_img_raw = Image.fromarray(blended_img)

    add_texture(blended_img_raw)


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

    return stamp(mask_texture)


def stamp(base):
    stamp = Image.open('images/Ukiyoe Warriors/Stamp.png')
    stamp = stamp.resize(base.size)

    base.paste(stamp, stamp)

    return base

"""
def first():  # test
    base = Image.open('images/Ukiyoe Warriors/- Backgrounds 背景 -/Fuji 富士.png')
    skin = Image.open('images/Ukiyoe Warriors/Samurai 侍/Skin Base.png')
    clothes = Image.open('images/Ukiyoe Warriors/Samurai 侍/Attire 服装/Kimono 着物/Checkered チェック/Checkered - Ashikaga.png')
    earringL = Image.open('images/Ukiyoe Warriors/Samurai 侍/Earrings 耳飾り/Earring 1 (Left)/Death 死.png')
    earringR = Image.open('images/Ukiyoe Warriors/Samurai 侍/Earrings 耳飾り/Earring 2 (Right)/Fusion 融合.png')
    eyes = Image.open('images/Ukiyoe Warriors/Samurai 侍/Eyes 目/Calm 静か.png')
    face = Image.open('images/Ukiyoe Warriors/Samurai 侍/Face 顔/Golden Oni Mask 鬼の面（金）.png')
    head = Image.open('images/Ukiyoe Warriors/Samurai 侍/Head 頭/Sedge Hat 菅笠.png')
    weapon = Image.open('images/Ukiyoe Warriors/Samurai 侍/Weapons 武器/Katana 刀/Ashikaga.png')
    banner = Image.open('images/Ukiyoe Warriors/- Banners 指物 -/Ashikaga 足利.png')

    base = base.convert("RGBA")
    skin = skin.convert("RGBA")
    clothes = clothes.convert("RGBA")
    earringL = earringL.convert("RGBA")
    earringR = earringR.convert("RGBA")
    eyes = eyes.convert("RGBA")
    face = face.convert("RGBA")
    head = head.convert("RGBA")
    weapon = weapon.convert("RGBA")
    banner = banner.convert("RGBA") 

    base.paste(skin, skin)
    base.paste(banner, banner)
    base.paste(clothes, clothes)
    base.paste(earringL, earringL)
    base.paste(eyes, eyes)
    base.paste(earringR, earringR)
    base.paste(face, face)
    base.paste(head, head)
    base.paste(weapon, weapon)

    overlay_textures(base)


def create_single(char_traits, roster_number):
    print('okay')
    bg = char_traits[0]
    clan = char_traits[1]
    base = Image.open('images/Ukiyoe Warriors/Samurai 侍/{}.png').format(bg)

    skin = Image.open('images/Ukiyoe Warriors/Samurai 侍/Skin Base.png')
    base.paste(skin, skin)

    banner = Image.open('images/Ukiyoe Warriors/Samurai 侍/{}.png').format(char_traits[3])
    base.paste(banner, banner)

    clothing = Image.open('images/Ukiyoe Warriors/Samurai 侍/{}.png').format(char_traits[4])
    base.paste(clothing, clothing)

    if not char_traits[5]:
        earring_left = Image.open('images/Ukiyoe Warriors/Samurai 侍/{}.png').format(char_traits[5])
        base.paste(earring_left, earring_left)

    if not char_traits[6]:
        earring_right = Image.open('images/Ukiyoe Warriors/Samurai 侍/{}.png').format(char_traits[6])
        base.paste(earring_right, earring_right)

    overlay_textures(base)
    base.save('Samurai {}.png').format(roster_number)
"""

def add_banner(base, char_traits):
    banner = Image.open('images/Ukiyoe Warriors/Samurai 侍/{}.png').format(char_traits[3])
    base.paste(banner, banner)

    return base


def add_earring_left(base, char_traits):
    earring_left = Image.open('images/Ukiyoe Warriors/Samurai 侍/{}.png').format(char_traits[3])
    base.paste()

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
        print("Error in cleaning clan name.")


# should i do each  race as it's own class? or is that excessive mem usage?
def generate(traits_list):  # create as samurai first? maybe make separate funcs for each race?
    # loop through traits list.
    # discover clan firstly
    # clan = traits_list.clan  # obviously make this work or reword/rewrite.
    # loop through the traits going through bottom-most layer first, and if it exists,
    # then add it to the image
    # finish with textures and stamp
    # save file with passed in file number... then calculate rarity? not sure yet.
    samurai_number = 0

    for traits in traits_list:
        print(samurai_number)
        clan_dirty = traits[1]
        clan = clean_clan(clan_dirty)

        base = Image.open('images/Ukiyoe Warriors/- Backgrounds 背景 -/{}.png'.format(traits[0]))  # Base == bg
        banner = Image.open('images/Ukiyoe Warriors/- Banners 指物 -/{}.png'.format(traits[1]))
        skin = Image.open('images/Ukiyoe Warriors/Samurai 侍/Skin Base.png')
        skin_and_head = Image.open('images/Ukiyoe Warriors/Samurai 侍/Head Base.png')

        clothes_type = traits[2]

        if clothes_type == "Armor 鎧":
            clothes = Image.open('images/Ukiyoe Warriors/Samurai 侍//Attire 服装/Armor 鎧/{}.png'.format(clan))
        else:
            clothes = Image.open('images/Ukiyoe Warriors/Samurai 侍/Attire 服装/Kimono 着物/{0}/{1}.png'.format(clothes_type, clan))

        eyes_trait = traits[3]
        
        if eyes_trait == "Saiké サイケ":
            # TODO saike it up.. must be correct order though???
            print("saike")
            eyes = Image.open('images/Ukiyoe Warriors/Samurai 侍/Eyes 目/Calm 静か.png')
        else:
            eyes = Image.open('images/Ukiyoe Warriors/Samurai 侍/Eyes 目/{}.png'.format(eyes_trait))

        face_trait = traits[4]
        if face_trait == "None":
            face = None
        else:
            face = Image.open('images/Ukiyoe Warriors/Samurai 侍/Face 顔/{}.png'.format(face_trait))

        earring_l_trait = traits[5]
        if earring_l_trait == "None":
            earring_l = None
        else:
            earring_l = Image.open('images/Ukiyoe Warriors/Samurai 侍/Earrings 耳飾り/Earring 1 (Left)/{}.png'.format(earring_l_trait))

        earring_r_trait = traits[6]
        if earring_r_trait == "None":
            earring_r = None
        else:
            earring_r = Image.open('images/Ukiyoe Warriors/Samurai 侍/Earrings 耳飾り/Earring 2 (Right)/{}.png'.format(earring_r_trait))

        head_trait = traits[7]
        if head_trait in ["Chasen 茶筅", "Sedge Hat 菅笠 2", "Topknot 髷"]:  # No back
            head = Image.open('images/Ukiyoe Warriors/Samurai 侍/Head 頭/{}.png'.format(head_trait))
            head_back = None
        elif head_trait in ["Disheveled 乱れ髪 + Headband 鉢巻", "Kabuto 兜"]:  # Back and Clan
            head = Image.open('images/Ukiyoe Warriors/Samurai 侍/Head 頭/{0}/Front/{1}.png'.format(head_trait, clan))
            head_back = Image.open('images/Ukiyoe Warriors/Samurai 侍/Head 頭/{0}/Back.png'.format(head_trait))
        elif head_trait in ["Chasen 茶筅 + Headband 鉢巻", "Topknot 髷 + Headband 鉢巻"]:  # NO Back and Clan
            head = Image.open('images/Ukiyoe Warriors/Samurai 侍/Head 頭/{0}/{1}.png'.format(head_trait, clan))
            head_back = None
        else:  # Back and NO Clan
            head = Image.open('images/Ukiyoe Warriors/Samurai 侍/Head 頭/{0}/Front.png'.format(head_trait))
            head_back = Image.open('images/Ukiyoe Warriors/Samurai 侍/Head 頭/{0}/Back.png'.format(head_trait))

        weapon = Image.open('images/Ukiyoe Warriors/Samurai 侍/Weapons 武器/Katana 刀/{}.png'.format(clan))  # TODO change this
        if clothes_type == "Armor 鎧":
            weapon_addon = Image.open('images/Ukiyoe Warriors/Samurai 侍/Weapons 武器/Katana 刀/Obi 帯/w_ Armor.png')
        else:
            weapon_addon = Image.open('images/Ukiyoe Warriors/Samurai 侍/Weapons 武器/Katana 刀/Obi 帯/w_ Kimono.png')

        base.paste(banner, banner)
        base.paste(skin, skin)
        base.paste(clothes, clothes)
        if head_back is not None:
            base.paste(head_back, head_back)
        if earring_r is not None:
            base.paste(earring_r, earring_r)
        base.paste(skin_and_head, skin_and_head)
        base.paste(eyes, eyes)
        if face is not None:
            base.paste(face, face)
        if earring_l is not None:
            base.paste(earring_l, earring_l)
        base.paste(head, head)
        base.paste(weapon, weapon)
        base.paste(weapon_addon, weapon_addon)

        base = overlay_textures(base)

        base.save("output/Samurai#{}.png".format(samurai_number))
        samurai_number += 1
# TODO add an Image.close() for each png layer????? after each iter.
