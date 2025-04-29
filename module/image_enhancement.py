import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import os

def open_image(file_path: str):
    file_name = os.path.basename(file_path)
    image = Image.open(file_path).convert('RGB')
    
    image_array = np.array(image, dtype=np.int32)
    
    return image_array, file_name
    
def save_image(file_path: str, output_image: list, file_name: str) -> None:
    output_path = os.path.join('Images', 'Output', file_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    output_image.save(output_path)
    print(f'File disimpan: {output_path}')

def brightness_image(file_path: str):
    image_array, file_name = open_image(file_path)
    
    height, width, _ = image_array.shape
    
    brightness: int = int(input("Masukkan jumlah brightness: "))
    
    brightness_img = np.zeros((height, width, 3), dtype=np.int32)
    
    for i in range(height):
        for j in range(width):
            for k in range(3):
                brightness_img[i][j][k] = image_array[i][j][k] + brightness
                brightness_image = np.clip(brightness_img, 0, 255)
    
    output = np.clip(brightness_image, 0, 255).astype(np.uint8)
    output_image = Image.fromarray(output)
    
    save_image(file_path, output_image, file_name)                

def inverse_image(file_path: str) -> None:
    image_array, file_name = open_image(file_path)

    height, width, _ = image_array
    
    L: int = 256  
    inverse = np.zeros((height, width, 3), dtype=np.int32)
    
    for i in range(height):
        for j in range(width):
            for k in range(3):
                inverse[i][j][k] = L - 1 - image_array[i][j][k]
    
    output = np.clip(inverse, 0, 255).astype(np.uint8)
    output_image = Image.fromarray(output)
    
    save_image(file_path, output_image, file_name)