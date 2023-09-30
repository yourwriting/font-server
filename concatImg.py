import os
import random
from PIL import Image, ImageOps, ImageChops


def concat_images(image_paths, size, shape=None):
    # Open images and resize them
    width, height = size
    images = map(Image.open, image_paths)

    # images = [crop(i, 5) for i in images]

    images = [ImageOps.fit(i, size, Image.LANCZOS)
              for i in images]

    # Create canvas for the final image with total size
    shape = shape if shape else (1, len(images))
    image_size = (width * shape[1], height * shape[0])
    result = Image.new('RGB', image_size)

    idx = 0
    # Paste images into final image
    for row in range(shape[0]):
        for col in range(shape[1]):
            offset = width * col, height * row
            # print(offset)
            # idx = row * shape[1] + col
            # print(idx)
            result.paste(images[idx], offset)
            idx = idx + 1

    result.save("./concat.PNG")
    print("concat 끝")
    return result


def crop(image, margin=10):
    width, height = image.size
    white = Image.new(image.mode, image.size, image.getpixel((0, 0)))
    diff = ImageChops.difference(image ,white)
    diff = ImageChops.add(diff,diff ,2.0,-35)
    bbox = diff.getbbox()

    if bbox:
        left = max(0, bbox[0] - margin)      # Don't go below zero
        top = max(0, bbox[1] - margin)       # Don't go below zero
        right = min(width, bbox[2] + margin)     # Don't exceed image width
        bottom = min(height, bbox[3] + margin)   # Don't exceed image height

        cropped_image = image.crop((left,top,right,bottom))

        size_diff = abs(cropped_image.width - cropped_image.height)

        if cropped_image.width > cropped_image.height:
            padding_top_bottom_half_size_diff = size_diff // 2
            padding_color=(255,) * len(cropped_image.getbands())  # Set padding color to white (255 for each channel)
            padded_cropped_image=ImageOps.expand(cropped_image,border=(padding_top_bottom_half_size_diff , 0),fill=padding_color)

        elif cropped_image.width < cropped_image.height:
            padding_left_right_half_size_diff=size_diff // 2
            padding_color=(255,) * len(cropped_image.getbands())  # Set padding color to white (255 for each channel)
            padded_cropped_image=ImageOps.expand(cropped_image,border=(0,padding_left_right_half_size_diff),fill=padding_color)

        else: 
            padded_cropped_image=cropped_image
        
        return padded_cropped_image

        
    else:      
        print("crop fail")
        return image