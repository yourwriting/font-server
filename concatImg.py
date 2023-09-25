import os
import random
from PIL import Image, ImageOps


def concat_images(image_paths, size, shape=None):
    # Open images and resize them
    width, height = size
    images = map(Image.open, image_paths)

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