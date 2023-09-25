import os
from PIL import Image


def load_image(file_path):
    try:
        img = Image.open(file_path)
    except FileNotFoundError:
        print(f"Failed to load image: {file_path}\nPlease check the file path and try again.")
        exit(1)
    return img.convert('RGBA')


def rescale_image_width(image, rescale_width, rescale_height):
    width, height = image.size
    new_width = int(rescale_width)
    new_height = int(rescale_height)
    return image.resize((new_width, new_height), Image.LANCZOS)


def combine_letters3(input_folder, output_folder):
    print("Loading images..")

    rescale_width = 20  # 종성 이미지의 가로 길이를 조절합니다.

    consonants_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    consonants = [(i, load_image(os.path.join(input_folder, f'{i}.PNG'))) for i in consonants_index]
    vowels_1_index = [20, 21, 22, 23, 40]
    vowels_1 = [(j, load_image(os.path.join(input_folder, f'{j}.PNG'))) for j in vowels_1_index]
    vowels_2_index = [24, 25, 26, 27]
    vowels_2 = [(k, load_image(os.path.join(input_folder, f'{k}.PNG'))) for k in vowels_2_index]
    vowels_3_index =[28, 32]
    vowels_3 = [(m, load_image(os.path.join(input_folder, f'{m}.PNG'))) for m in vowels_3_index]
    vowels_4_index = [33, 37, 38]
    vowels_4 = [(n, load_image(os.path.join(input_folder, f'{n}.PNG'))) for n in vowels_4_index]
    vowels_5_index = [29, 30, 31]
    vowels_5 = [(o, load_image(os.path.join(input_folder, f'{o}.PNG'))) for o in vowels_5_index]
    rescaled_vowels_5 = [(m, rescale_image_width(img, 50, 40)) for m, img in vowels_5]
    vowels_6_index = [34, 35, 36, 39]
    vowels_6 = [(o, load_image(os.path.join(input_folder, f'{o}.PNG'))) for o in vowels_6_index]
    rescaled_vowels_6 = [(m, rescale_image_width(img, 45, 40)) for m, img in vowels_6]
    final_consonants_index = [1, 3, 6, 8, 10]
    final_consonants = [(l,load_image(os.path.join(input_folder, f'{l}.PNG'))) for l in final_consonants_index]
    rescaled_final_consonants = [(m, rescale_image_width(img, 20, 18)) for m, img in final_consonants]
    second_final_consonants_index = [1, 7, 8, 10, 13, 17, 18, 19]
    second_final_consonants = [(sfc, load_image(os.path.join(input_folder, f'{sfc}.PNG'))) for
                               sfc in second_final_consonants_index]
    rescaled_second_final_consonants = [(sfc_value, rescale_image_width(img, rescale_width, 18)) for
                                        sfc_value, img in second_final_consonants]
    print("All images loaded successfully.")
    second_final_consonant_gap = 5

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    background_file = './images/background.png'

    for sfc, (sfc_value, second_final_consonant) in enumerate(rescaled_second_final_consonants):
        for c, (c_value, consonant) in enumerate(consonants):
            for v, (v_value, vowel) in enumerate(vowels_1):
                for fc, (fc_value, final_consonant) in enumerate(rescaled_final_consonants):
                    if fc_value == 1 and sfc_value not in [1, 10]:
                        continue
                    elif fc_value == 3 and sfc_value not in [13, 19]:
                        continue
                    elif fc_value == 6 and sfc_value not in [1,7,8,10,17,18,19]:
                        continue
                    elif fc_value == 8 and sfc_value not in [10]:
                        continue
                    elif fc_value == 10 and sfc_value not in [10]:
                        continue
                    background = Image.open(background_file)

                    consonant_pos = (50, 50)
                    vowel_pos = (83, 45)
                    final_consonant_pos = (60, 80)

                    background.paste(consonant, consonant_pos, consonant)
                    background.paste(vowel, vowel_pos, vowel)
                    background.paste(final_consonant, final_consonant_pos, final_consonant)

                    # second_final_consonant = load_image(os.path.join(input_folder, '10.PNG'))  # 'ㅅ' 더하기
                    # second_final_consonant = rescale_image_width(second_final_consonant, rescale_width, 18)
                    second_final_consonant_pos = (55 + rescale_width + second_final_consonant_gap, 83)
                    background.paste(second_final_consonant, second_final_consonant_pos, second_final_consonant)

                    # output_filename = f"letter_{c_value}_{v_value}_{fc_value}_{sfc_value}.png"

                    output_filename = 'letter_' + str(c_value).zfill(2) + "_" + str(v_value).zfill(2) + "_" + str(
                        fc_value).zfill(2) + "_" + str(sfc_value).zfill(2) + ".PNG"
                    output_path = os.path.join(output_folder, output_filename)

                    background.save(output_path)

            for v, (v_value, vowel) in enumerate(vowels_2):
                for fc, (fc_value, final_consonant) in enumerate(rescaled_final_consonants):
                    if fc_value == 1 and sfc_value not in [1, 10]:
                        continue
                    elif fc_value == 3 and sfc_value not in [13, 19]:
                        continue
                    elif fc_value == 6 and sfc_value not in [1,7,8,10,17,18,19]:
                        continue
                    elif fc_value == 8 and sfc_value not in [10]:
                        continue
                    elif fc_value == 10 and sfc_value not in [10]:
                        continue
                    background = Image.open(background_file)

                    consonant_pos = (50, 50)
                    vowel_pos = (77, 45)
                    final_consonant_pos = (60, 80)

                    background.paste(consonant, consonant_pos, consonant)
                    background.paste(vowel, vowel_pos, vowel)
                    background.paste(final_consonant, final_consonant_pos, final_consonant)

                    # second_final_consonant = load_image(os.path.join(input_folder, '10.PNG'))  # 'ㅅ' 더하기
                    # second_final_consonant = rescale_image_width(second_final_consonant, rescale_width, 18)
                    second_final_consonant_pos = (55 + rescale_width + second_final_consonant_gap, 80)
                    background.paste(second_final_consonant, second_final_consonant_pos, second_final_consonant)


                    output_filename = 'letter_' + str(c_value).zfill(2) + "_" + str(v_value).zfill(2) + "_" + str(fc_value).zfill(2) + "_" + str(sfc_value).zfill(2) + ".PNG"
                    output_path = os.path.join(output_folder, output_filename)

                    background.save(output_path)

            for v, (v_value, vowel) in enumerate(vowels_3):
                for fc, (fc_value, final_consonant) in enumerate(rescaled_final_consonants):
                    if fc_value == 1 and sfc_value not in [1, 10]:
                        continue
                    elif fc_value == 3 and sfc_value not in [13, 19]:
                        continue
                    elif fc_value == 6 and sfc_value not in [1,7,8,10,17,18,19]:
                        continue
                    elif fc_value == 8 and sfc_value not in [10]:
                        continue
                    elif fc_value == 10 and sfc_value not in [10]:
                        continue

                    background = Image.open(background_file)

                    consonant_pos = (70, 40)
                    vowel_pos = (65, 65)
                    final_consonant_pos = (65, 85)

                    background.paste(consonant, consonant_pos, consonant)
                    background.paste(vowel, vowel_pos, vowel)
                    background.paste(final_consonant, final_consonant_pos, final_consonant)

                    # second_final_consonant = load_image(os.path.join(input_folder, '10.PNG'))  # 'ㅅ' 더하기
                    # second_final_consonant = rescale_image_width(second_final_consonant, rescale_width, 18)
                    second_final_consonant_pos = (55 + rescale_width + second_final_consonant_gap, 85)
                    background.paste(second_final_consonant, second_final_consonant_pos, second_final_consonant)

                    # output_filename = f"letter_{c_value}_{v_value}_{fc_value}_{sfc_value}.png"
                    output_filename = 'letter_' + str(c_value).zfill(2) + "_" + str(v_value).zfill(2) + "_" + str(
                        fc_value).zfill(2) + "_" + str(sfc_value).zfill(2) + ".PNG"
                    output_path = os.path.join(output_folder, output_filename)

                    background.save(output_path)

            for v, (v_value, vowel) in enumerate(vowels_4):
                for fc, (fc_value, final_consonant) in enumerate(rescaled_final_consonants):
                    if fc_value == 1 and sfc_value not in [1, 10]:
                        continue
                    elif fc_value == 3 and sfc_value not in [13, 19]:
                        continue
                    elif fc_value == 6 and sfc_value not in [1,7,8,10,17,18,19]:
                        continue
                    elif fc_value == 8 and sfc_value not in [10]:
                        continue
                    elif fc_value == 10 and sfc_value not in [10]:
                        continue

                    background = Image.open(background_file)

                    consonant_pos = (70, 43)
                    vowel_pos = (67, 74)
                    final_consonant_pos = (70, 93)

                    background.paste(consonant, consonant_pos, consonant)
                    background.paste(vowel, vowel_pos, vowel)
                    background.paste(final_consonant, final_consonant_pos, final_consonant)

                    # second_final_consonant = load_image(os.path.join(input_folder, '10.PNG'))  # 'ㅅ' 더하기
                    # second_final_consonant = rescale_image_width(second_final_consonant, rescale_width, 18)
                    second_final_consonant_pos = (65 + rescale_width + second_final_consonant_gap, 95)
                    background.paste(second_final_consonant, second_final_consonant_pos, second_final_consonant)

                    # output_filename = f"letter_{c_value}_{v_value}_{fc_value}_{sfc_value}.png"
                    output_filename = 'letter_' + str(c_value).zfill(2) + "_" + str(v_value).zfill(2) + "_" + str(
                        fc_value).zfill(2) + "_" + str(sfc_value).zfill(2) + ".PNG"
                    output_path = os.path.join(output_folder, output_filename)

                    background.save(output_path)

            for v, (v_value, vowel) in enumerate(rescaled_vowels_5):
                for fc, (fc_value, final_consonant) in enumerate(rescaled_final_consonants):
                    if fc_value == 1 and sfc_value not in [1, 10]:
                        continue
                    elif fc_value == 3 and sfc_value not in [13, 19]:
                        continue
                    elif fc_value == 6 and sfc_value not in [1,7,8,10,17,18,19]:
                        continue
                    elif fc_value == 8 and sfc_value not in [10]:
                        continue
                    elif fc_value == 10 and sfc_value not in [10]:
                        continue

                    background = Image.open(background_file)

                    consonant_pos = (60, 40)
                    vowel_pos = (65, 55)
                    final_consonant_pos = (72, 90)

                    background.paste(consonant, consonant_pos, consonant)
                    background.paste(vowel, vowel_pos, vowel)
                    background.paste(final_consonant, final_consonant_pos, final_consonant)

                    # second_final_consonant = load_image(os.path.join(input_folder, '10.PNG'))  # 'ㅅ' 더하기
                    # second_final_consonant = rescale_image_width(second_final_consonant, rescale_width, 18)
                    second_final_consonant_pos = (67 + rescale_width + second_final_consonant_gap, 90)
                    background.paste(second_final_consonant, second_final_consonant_pos, second_final_consonant)

                    # output_filename = f"letter_{c_value}_{v_value}_{fc_value}_{sfc_value}.png"
                    output_filename = 'letter_' + str(c_value).zfill(2) + "_" + str(v_value).zfill(2) + "_" + str(
                        fc_value).zfill(2) + "_" + str(sfc_value).zfill(2) + ".PNG"
                    output_path = os.path.join(output_folder, output_filename)

                    background.save(output_path)

            for v, (v_value, vowel) in enumerate(rescaled_vowels_6):
                for fc, (fc_value, final_consonant) in enumerate(rescaled_final_consonants):
                    if fc_value == 1 and sfc_value not in [1, 10]:
                        continue
                    elif fc_value == 3 and sfc_value not in [13, 19]:
                        continue
                    elif fc_value == 6 and sfc_value not in [1,7,8,10,17,18,19]:
                        continue
                    elif fc_value == 8 and sfc_value not in [10]:
                        continue
                    elif fc_value == 10 and sfc_value not in [10]:
                        continue

                    background = Image.open(background_file)

                    consonant_pos = (65, 40)
                    vowel_pos = (65, 55)
                    final_consonant_pos = (72, 90)

                    background.paste(consonant, consonant_pos, consonant)
                    background.paste(vowel, vowel_pos, vowel)
                    background.paste(final_consonant, final_consonant_pos, final_consonant)

                    # second_final_consonant = load_image(os.path.join(input_folder, '10.PNG'))  # 'ㅅ' 더하기
                    # second_final_consonant = rescale_image_width(second_final_consonant, rescale_width, 18)
                    second_final_consonant_pos = (67 + rescale_width + second_final_consonant_gap, 90)
                    background.paste(second_final_consonant, second_final_consonant_pos, second_final_consonant)

                    # output_filename = f"letter_{c_value}_{v_value}_{fc_value}_{sfc_value}.png"
                    output_filename = 'letter_' + str(c_value).zfill(2) + "_" + str(v_value).zfill(2) + "_" + str(
                        fc_value).zfill(2) + "_" + str(sfc_value).zfill(2) + ".PNG"
                    output_path = os.path.join(output_folder, output_filename)

                    background.save(output_path)



    print("Images combined successfully.")