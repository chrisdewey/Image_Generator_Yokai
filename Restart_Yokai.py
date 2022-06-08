# import os
from PIL import Image
import numpy
import ast
from blend_modes import addition, multiply, overlay


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


def add_texture_80(base, texture):
    add_layer = texture

    img_in = numpy.array(base)
    img_in_float = img_in.astype(float)

    add_layer = numpy.array(add_layer)
    add_layer_float = add_layer.astype(float)

    blended_img_float = addition(img_in_float, add_layer_float, .8)

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


def mask_textures(base):
    mask_texture = Image.open('images/Ukiyoe Warriors/- Textures -/2. Mask Texture.png')

    mask_texture.paste(base, mask_texture)

    return mask_texture


def generate(traits_list_txt, restart_from):
    yokai_number = restart_from

    with open(traits_list_txt, 'r', encoding='utf-8') as f:
        traits_list = ast.literal_eval(f.read())

    for index, traits in enumerate(traits_list):
        if index < restart_from-1:
            continue
        # Order = [char, bg, color, head, body, face, earring, companion, hand, chikara]
        print(yokai_number)

        background = traits[1]

        color = traits[2]
        yokai = traits[0]
        hand_clothing = traits[4]  # TODO if its twilir then == plain?? check with chase for confirmation.
        #                              (for above, maybe if(body_trait not in list of folders):
        #                              then body folder for hands = plain;
        body = Image.open('/input/{0}/Body 体/{1}/{2}.png'.format(yokai, traits[4], color))
        head = Image.open('/input/{0}/Head 頭/{1}.png'.format(yokai, traits[3]))
        face = Image.open('/input/{0}/Face 顔/{1}.png'.format(yokai, traits[5]))
        earring = Image.open('/input/{0}/Earring 耳飾り/{1}.png'.format(yokai, traits[6]))
        companion = Image.open('/input/- Nakama 仲間 -/{}.png'.format(traits[7]))
        hand = Image.open('/input/{0}/Hand 手/{1}/{2}/{3}.png'.format(yokai, traits[8], hand_clothing, color))
        weapon = Image.open('/input/{0}/Hand 手/{1}/{2}.png'.format(yokai, traits[8], traits[8]))
        chikara = Image.open('/input/- Chikara 力 -/{}.png'.format(traits[9]))

        # TODO add these differentials => earring trait is overlain on the head trait for tengu
        companion_back = ["Kodama 木霊", "Onibi 鬼火"]

        base = Image.open('/input/- Background 背景 -/{}.png'.format(background))  # Base == bg
        base = base.convert('RGBA')

        if companion in companion_back:
            base.paste(companion, companion)

        base.paste(weapon, weapon)
        base.paste(hand, hand)
        base.paste(body, body)
        base.paste(face, face)

        # Earring trait pasted on top of head for Tengu only.
        if yokai == "Tengu 天狗":
            base.paste(earring, earring)
            base.paste(head, head)
        else:
            base.paste(head, head)
            base.paste(earring, earring)

        # twilir eye isn't used for goken helms.
        if traits[4] == "Twilir トワイリル" and traits[3] not in ["Goken Helm 護拳甲", "Dark Goken 闇の護拳"]:
            twil_eyes = Image.open('/input/{0}/Body 体/{1}/{2}.png'.format(yokai, traits[4], "Twilir Eye"))
            base.paste(twil_eyes, twil_eyes)

        base.paste(chikara)

        if companion not in companion_back:
            base.paste(companion, companion)

        base = overlay_textures(base)

        base.save("output/UkiyoeWarrior#{}.png".format(yokai_number))
        yokai_number += 1
