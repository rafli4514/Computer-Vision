import numpy as np
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
                    
    output = np.clip(brightness_img, 0, 255).astype(np.uint8)
    output_image = Image.fromarray(output)
    
    save_image(file_path, output_image, file_name)                

def inverse_image(file_path: str) -> None:
    image_array, file_name = open_image(file_path)
    height, width, _ = image_array
    L: int = 256  
    inverse: np.zeros = np.zeros((height, width, 3), dtype=np.int32)
    
    for i in range(height):
        for j in range(width):
            for k in range(3):
                inverse[i][j][k] = L - 1 - image_array[i][j][k]
    
    output = np.clip(inverse, 0, 255).astype(np.uint8)
    output_image = Image.fromarray(output)
    
    save_image(file_path, output_image, file_name)
    
def power_law_transform(file_path: str) -> None:
    image_array, file_name = open_image(file_path)
    height, width, _ = image_array.shape
    
    c: int = 255
    gamma: float = float(input("Masukkan gamma: "))
    
    s = np.zeros((height, width, 3), dtype=np.float32)
    norm = image_array / 255.0
    
    for i in range(height):
        for j in range(width):
            for k in range(3):
                s[i][j][k] = c * (norm[i][j][k] ** gamma)
    
    output = np.clip(s, 0, 255).astype(np.uint8)
    output_image = Image.fromarray(output)
    
    save_image(file_path, output_image, file_name)

def log_transformation(file_path: str) -> None:
    image_array, file_name = open_image(file_path)
    height, width, _ = image_array.shape
    
    L: int = 256
    K = (L - 1) / np.log(1 + np.max(image_array))

    t = np.zeros((height, width, 3), dtype=np.float32)
    
    for i in range(height):
        for j in range(width):
            for k in range(3):
                t[i][j][k] = K * np.log(1 + image_array[i][j][k])
    
    output = np.clip(t, 0, 255).astype(np.uint8)
    output_image = Image.fromarray(output)
    
    save_image(file_path, output_image, file_name)
    
def histogram_equalizer(file_path) -> None:
    image_array, file_name = open_image(file_path)
    height, width, _ = image_array.shape
    
    L: int = 256
    s = np.zeros((height, width, 3), dtype=np.int32)
    
    unique, counts = np.unique(image_array, return_counts=True)
    freq_number = dict(zip(unique, counts))
    
    total_pixel = height * width
    
    pdf = {key: count / total_pixel for key, count in freq_number.items()}

    cdf = {}
    cumulative_sum = 0
    for key in sorted(pdf.keys()):
        cumulative_sum += pdf[key]
        cdf[key] = cumulative_sum
        
    for i in range(height):
        for j in range(width):
            for k in range(3):
                s[i][j][k] = np.round((L - 1) * cdf[image_array[i][j][k]])
                
    output = np.clip(s, 0, 255).astype(np.uint8)
    output_image = Image.fromarray(output)
    
    save_image(file_path, output_image, file_name)
    

def contrast_streching(file_path):
    image_array, file_name = open_image(file_path)
    height, width, _ = image_array.shape
    
    a = np.min(image_array)
    b = np.max(image_array)
    
    t = np.zeros((height, width, 3), dtype=np.float32)
    
    for i in range(height):
        for j in range(width):
            for k in range(3):
                t[i][j][k] = 255 * (image_array[i][j][k] - a) / (b - a)
    
    output = np.clip(t, 0, 255).astype(np.uint8)
    output_image = Image.fromarray(output)
    
    save_image(file_path, output_image, file_name)
    
