import os
import numpy as np
from scipy import ndimage
from PIL import Image

def sobel(file_path: str) -> None:
    image = os.path.basename(file_path)
    image = Image.open(file_path).convert('L')
    image = np.array(image).astype('int32')

    sobel_h = ndimage.sobel(image, 0)
    sobel_v = ndimage.sobel(image, 1)
    magnitude = np.sqrt(sobel_h ** 2 + sobel_v ** 2)
    magnitude *= 255.0 / np.max(magnitude)
    magnitude = magnitude.astype('uint8')

    output_file = os.path.join('Images', 'Output', file_path)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    image_save = Image.fromarray(magnitude)
    image_save.save(output_file)
    print(f'File disimpan pada {file_path}')

def prewitt(file_path: str) -> None:
    image = os.path.basename(file_path)

    image = Image.open(file_path).convert('L')
    image = np.array(image).astype('int32')

    prewitt_h = ndimage.prewitt(image, axis=0)
    prewitt_v = ndimage.prewitt(image, axis=1)
    magnitude = np.sqrt(prewitt_h ** 2 + prewitt_v ** 2)
    magnitude *= 255 / np.max(magnitude)
    magnitude = magnitude.astype('uint8')

    output_file = os.path.join('Image', 'Output', file_path)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    image_save = Image.fromarray(magnitude)
    image_save.save(output_file)
    print(f'File disimpan pada {file_path}')
