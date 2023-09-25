from PIL import Image, ImageChops


# 글자 가장자리 여백을 자르는 함수
def crop(image):
    white = Image.new(image.mode, image.size, image.getpixel((0, 0)))
    diff = ImageChops.difference(image, white)
    diff = ImageChops.add(diff, diff, 2.0, -35)
    bbox = diff.getbbox()

    if bbox:
        return image.crop(bbox)
    else:  # 이미지가 너무 작을 경우 bbox값이 없을 수도 있음
        print("crop fail")
        return


# 흰 배경을 투명화시키는 함수
def transparent(image):
    image = image.convert("RGBA")
    data = image.getdata()

    new_data = []
    cut_off = 150

    for datum in data:
        if datum[0] >= cut_off and datum[1] >= cut_off and datum[2] >= cut_off:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(datum)

    image.putdata(new_data)
    return image


def run():
    for i in range(1, 41):
        # 이미지 파일 읽기
        image = Image.open("./images/" + str(i) + ".PNG")

        # 가장자리 여백 자르기
        image = crop(image)

        # 흰 배경 투명화
        image = transparent(image)
        image.save("./crops/" + str(i) + ".PNG")
