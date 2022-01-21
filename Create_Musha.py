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
    overlay_texture = Image.open('images/Ukiyoe Warriors/- Textures -/3. Overlay Texture.png')

    # base.paste(add_layer, add_layer)

    overlay_texture = overlay_texture.resize(base.size)

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

    mult_texture(blended_img_raw)


def mask_textures(base):  # DID THIS ACTUALLY WORK BRO?? It creates the clipping mask effect found in other image
                          # Editing programs by pasting the base image OVER the mask, using the masks alpha channel.
    mask_texture = Image.open('images/Ukiyoe Warriors/- Textures -/4. Mask Texture.png')
    mask_texture = mask_texture.resize(base.size)

    mask_texture.paste(base, mask_texture)
    mask_texture.show()
    mask_texture.save('images/Ukiyoe Warriors/test.png')


def first():  # USE A LOOP TO COMBINE IMAGES
    base = Image.open('images/Ukiyoe Warriors/- Backgrounds 背景 -/Fuji 富士.png')
    skin = Image.open('images/Ukiyoe Warriors/Samurai 侍/Skin Base.png')
    clothes = Image.open('images/Ukiyoe Warriors/Samurai 侍/Attire 服装/Kimono 着物/Checkered チェック/Checkered - Ashikaga.png')
    earringL = Image.open('images/Ukiyoe Warriors/Samurai 侍/Earrings 耳飾り/Earring 1 (Left)/Death 死.png')
    earringR = Image.open('images/Ukiyoe Warriors/Samurai 侍/Earrings 耳飾り/Earring 2 (Right)/Fusion 融合.png')
    eyes = Image.open('images/Ukiyoe Warriors/Samurai 侍/Eyes 目/Calm 静か.png')
    face = Image.open('images/Ukiyoe Warriors/Samurai 侍/Face 顔/Golden Oni Mask 鬼の面（金）.png')
    head = Image.open('images/Ukiyoe Warriors/Samurai 侍/Head 頭/Sedge Hat 菅笠.png')
    weapon = Image.open('images/Ukiyoe Warriors/Samurai 侍/Weapon 武器/Katana 刀/Ashikaga.png')
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


# should i do each  race as it's own class? or is that excessive mem usage?
def generate(trait_list, roster_number):  # create as samurai first? maybe make separate funcs for each race?
    # loop through traits list.
    # discover clan firstly
    clan = trait_list.clan  # obviously make this work or reword/rewrite.
    # loop through the traits going through bottom-most layer first, and if it exists,
    # then add it to the image
    # finish with textures and stamp
    # save file with passed in file number... then calculate rarity? not sure yet.
    musha_number = roster_number
