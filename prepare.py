from PIL import Image, ImageChops
import os
import cv2
import numpy as np



# 글자 가장자리 여백을 자르는 함수
def crop(image):
    white = Image.new(image.mode, image.size, image.getpixel((0, 0)))
    diff = ImageChops.difference(image, white)
    diff = ImageChops.add(diff, diff, 2.0, -35)
    bbox = diff.getbbox()
    # if bbox:
    #     return image.crop(bbox)
    # else:  # 이미지가 너무 작을 경우 bbox값이 없을 수도 있음
    #     print("crop fail")
    #     return
    if bbox:
        cropped_image = image.crop(bbox)
        # PIL 이미지를 NumPy 배열로
        cropped_image_np = np.array(cropped_image)
        cropped_image_cv = cv2.cvtColor(cropped_image_np, cv2.COLOR_RGB2BGR)
        # 그레이스케일 이미지로 변환
        gray_image = cv2.cvtColor(cropped_image_cv, cv2.COLOR_BGR2GRAY)
        # 이진화 처리
        _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

        return Image.fromarray(binary_image.astype(np.uint8))

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


def rescale_image_width(image, rescale_width, rescale_height):
    width, height = image.size
    new_width = int(rescale_width)
    new_height = int(rescale_height)
    return image.resize((new_width, new_height), Image.LANCZOS)


def rescale_image_ratio(image, rescale_width=None, rescale_height=None):
    width, height = image.size

    if rescale_width is not None:
        # Calculate new height preserving aspect ratio
        aspect_ratio = width / height
        new_width = int(rescale_width)
        new_height = int(new_width / aspect_ratio)
    elif rescale_height is not None:
        # Calculate new width preserving aspect ratio
        aspect_ratio = height / width
        new_height = int(rescale_height)
        new_width = int(new_height / aspect_ratio)
    else:
        raise ValueError("Either 'rescale_width' or 'rescale_height' must be provided.")

    return image.resize((new_width, new_height), Image.LANCZOS)


def run():
    for i in range(1, 41):
        # 이미지 파일 읽기
        image = Image.open("./images/" + str(i) + ".PNG")

        # 가장자리 여백 자르기
        image = crop(image)
        image = Image.fromarray(image)

        # 흰 배경 투명화
        # image = transparent(image)
        rescale_image_width(image, 20, 20)
        image.save("./crops/" + str(i) + ".PNG")


def transletters():
    files_path = os.path.abspath("./combinations")
    image_list = [os.path.join(files_path, f) for f in os.listdir(files_path) if f.lower().endswith('.png')]
    
    letters_dir = "./letters"
    if not os.path.exists(letters_dir):
        os.makedirs(letters_dir)
    
    for img_path in image_list:
        image = Image.open(img_path)
        cropped_image = crop(image)
        result = transparent(cropped_image)
        file_name = os.path.basename(img_path)
        result_path = os.path.join("./letters", file_name)
        result.save(result_path, "PNG")
    files_path2 = os.path.abspath("./letters")
    image_list2 = [os.path.join(files_path2, f) for f in os.listdir(files_path2) if f.endswith('.PNG')]
    image_list2 = sorted(image_list2)

    letters_dir = "./letters2"
    if not os.path.exists(letters_dir):
        os.makedirs(letters_dir)

    # print(image_list2)
    for img_path2 in image_list2:
        background_file = './images/background.png'
        background = Image.open(background_file)
        image = Image.open(img_path2)

        # Get the size of both images
        bg_width, bg_height = background.size
        img_width, img_height = image.size

        # Calculate new size based on the longer dimension of the image.
        if img_width > img_height:
            new_width = bg_width - 10  # leave a small margin
            scale_factor = new_width / img_width
            new_height = int(scale_factor * img_height)

        else:
            new_height = bg_height - 10
            scale_factor = new_height / img_height
            new_width = int(scale_factor * img_width)

            # if (new_width > bg_width):  # Check whether it exceeds other dimension of background.
            #     new_width = bg_width - 10
            #     scale_factor = new_width / img_width
            #     new_height = int(scale_factor * img_height)

        # Resize and center align the image.
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        pos_x = (bg_width - new_width) // 2
        pos_y = (bg_height - new_height) // 2

        pos_centered = (pos_x, pos_y)
        background.paste(resized_image, pos_centered, resized_image)
        # background.paste(image, img_pos)
        background_np = np.array(background)
        background_cv = cv2.cvtColor(background_np, cv2.COLOR_RGB2BGR)
        gray_image = cv2.cvtColor(background_cv, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
        # Normalize image
        normalized_image = cv2.equalizeHist(binary_image)
        file_name = os.path.basename(img_path2)
        result_path = os.path.join('./letters2', file_name)
        # normalized_image.save(result_path, 'PNG')
        cv2.imwrite(result_path, normalized_image)