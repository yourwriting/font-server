import os
import shutil
from PIL import Image
import prepare

def rescale_image_width(image, rescale_width, rescale_height):
    width, height = image.size
    new_width = int(rescale_width)
    new_height = int(rescale_height)
    return image.resize((new_width, new_height), Image.LANCZOS)


source_dir = "./images"
target_dir = "./combinations"

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

for i in range(1, 41):
    source_file = os.path.join(source_dir, f"{i}.PNG")
    target_file = os.path.join(target_dir, 'letter_' + str(i).zfill(2)+".PNG")

    shutil.copy(source_file, target_file)


final_consonants_index = [1, 3, 6, 8, 10]
final_consonants = [(l,Image.open(os.path.join(source_dir, f'{l}.PNG'))) for l in final_consonants_index]
rescaled_final_consonants = [(m, rescale_image_width(img, 160, 150)) for m, img in final_consonants]

second_final_consonants_index = [1, 7, 8, 10, 13, 17, 18, 19]
second_final_consonants = [(sfc, Image.open(os.path.join(source_dir, f'{sfc}.PNG'))) for
                           sfc in second_final_consonants_index]
rescaled_second_final_consonants = [(sfc_value, rescale_image_width(img, 160, 160)) for
                                    sfc_value, img in second_final_consonants]

background_file = './images/background.png'

for sfc, (sfc_value, second_final_consonant) in enumerate(rescaled_second_final_consonants):
    for fc, (fc_value, final_consonant) in enumerate(rescaled_final_consonants):
        if fc_value == 1 and sfc_value not in [1, 10]:
            continue
        elif fc_value == 3 and sfc_value not in [13, 19]:
            continue
        elif fc_value == 6 and sfc_value not in [1, 7, 8, 10, 17, 18, 19]:
            continue
        elif fc_value == 8 and sfc_value not in [10]:
            continue
        elif fc_value == 10 and sfc_value not in [10]:
            continue
        background = Image.open(background_file)

        final_consonant_pos = (0, 30)
        second_final_consonant_pos = (50, 33)

        background.paste(final_consonant, final_consonant_pos, final_consonant)
        background.paste(second_final_consonant, second_final_consonant_pos, second_final_consonant)


        output_filename = 'letter_' + str(fc_value).zfill(2) + "_" + str(sfc_value).zfill(2) + ".PNG"
        output_path = os.path.join(target_dir, output_filename)
        background.save(output_path)

