# 1 자음 + 모음
from PIL import Image


path = './combinations'

# ㅏ ㅐ ㅑ ㅒ ㅣ
def combine_letters_1():
    for j in [20, 21, 22, 23, 40]:
        for i in range(1, 20):
            background = Image.open('./images/background.png')
            consonant = Image.open('./crops/' + str(i) + '.PNG')
            vowel = Image.open('./crops/' + str(j) + '.PNG')

            background.paste(consonant, (60, 30))
            background.paste(vowel, (100, 25))
            background.save(path + '/letter_' + str(i).zfill(2) + "_" + str(j).zfill(2) + ".PNG")


# ㅓ ㅔ ㅕ ㅖ
def combine_letters_2():
    for j in [24, 25, 26, 27]:
        for i in range(1, 20):
            background = Image.open('./images/background.png')
            consonant = Image.open('./crops/' + str(i) + '.PNG')
            vowel = Image.open('./crops/' + str(j) + '.PNG')

            width, height = consonant.size

            background.paste(consonant, (60, 30))
            background.paste(vowel, (60 + width, 25))
            background.save(path + '/letter_' + str(i).zfill(2) + "_" + str(j).zfill(2) + ".PNG")


# ㅗ ㅛ
def combine_letters_3():
    for j in [28, 32]:
        for i in range(1, 20):
            background = Image.open('./images/background.png')
            consonant = Image.open('./crops/' + str(i) + '.PNG')
            vowel = Image.open('./crops/' + str(j) + '.PNG')

            width, height = consonant.size

            background.paste(consonant, (60, 30))
            background.paste(vowel, (58, 30 + height))
            background.save(path + '/letter_' + str(i).zfill(2) + "_" + str(j).zfill(2) + ".PNG")


# ㅜ ㅠ ㅡ
def combine_letters_4():
    for j in [33, 37, 38]:
        for i in range(1, 20):
            background = Image.open('./images/background.png')
            consonant = Image.open('./crops/' + str(i) + '.PNG')
            vowel = Image.open('./crops/' + str(j) + '.PNG')

            width, height = consonant.size

            background.paste(consonant, (60, 30))
            background.paste(vowel, (58, 30 + height + int(height / 10)))
            background.save(path + '/letter_' + str(i).zfill(2) + "_" + str(j).zfill(2) + ".PNG")


# ㅘ ㅙ ㅚ ㅞ ㅝ ㅟ ㅢ
def combine_letters_5():
    # ㅗ + ㅏ ㅐ ㅣ
    index = 29
    for j in [20, 21, 40]:
        for i in range(1, 20):
            background = Image.open('./images/background.png')
            consonant = Image.open('./crops/' + str(i) + '.PNG')
            vowel = Image.open('./crops/28.PNG')
            vowel2 = Image.open('./crops/' + str(j) + '.PNG')

            width, height = consonant.size
            width2, height2 = vowel.size
            new_width, height3 = vowel2.size

            new_height = height + height2

            # Resize the second vowel image with a specified filter
            vowel2_resized = vowel2.resize((new_width, new_height), Image.LANCZOS)

            background.paste(consonant, (60, 30))
            background.paste(vowel, (58, 30 + height))
            background.paste(vowel2, (58 + width2, 30))
            background.save(path + '/letter_' + str(i).zfill(2) + "_" + str(index).zfill(2) + ".PNG")
        index += 1

    # ㅜ + ㅓ ㅔ ㅣ
    index = 34
    for j in [24, 25, 40]:
        for i in range(1, 20):
            background = Image.open('./images/background.png')
            consonant = Image.open('./crops/' + str(i) + '.PNG')
            vowel = Image.open('./crops/33.PNG')
            vowel2 = Image.open('./crops/' + str(j) + '.PNG')

            width, height = consonant.size
            width2, height2 = vowel.size
            new_width, height3 = vowel2.size

            new_height = height + height2

            # Resize the second vowel image with a specified filter
            vowel2_resized = vowel2.resize((new_width, new_height), Image.LANCZOS)

            background.paste(consonant, (60, 30))
            background.paste(vowel, (58, 30 + height + int(height / 10)))
            background.paste(vowel2, (58 + width2, 30))
            background.save(path + '/letter_' + str(i).zfill(2) + "_" + str(index).zfill(2) + ".PNG")
        index += 1

    # ㅡ + ㅣ
    for i in range(1, 20):
        background = Image.open('./images/background.png')
        consonant = Image.open('./crops/' + str(i) + '.PNG')
        vowel = Image.open('./crops/38.PNG')
        vowel2 = Image.open('./crops/40.PNG')

        width, height = consonant.size
        width2, height2 = vowel.size

        background.paste(consonant, (60, 30))
        background.paste(vowel, (58, 30 + height + int(height / 10)))
        background.paste(vowel2, (58 + width2, 30))
        background.save(path + '/letter_' + str(i).zfill(2) + "_39.PNG")


def run():
    combine_letters_1()
    combine_letters_2()
    combine_letters_3()
    combine_letters_4()
    combine_letters_5()