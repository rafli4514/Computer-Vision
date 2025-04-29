import os
import numpy as np
from PIL import Image

def mean_filtering_greyscale(file_path: str) -> None:
    file_name = os.path.basename(file_path)
    image = Image.open(file_path).convert('L') 
    
    image_array = np.array(image, dtype=np.float32)
    output = np.zeros_like(image_array)
    
    kernel = np.ones((3, 3)) / 9.0 
    rows, cols = image_array.shape
    pad_r, pad_c = 1, 1  
    
    for i in range(pad_r, rows - pad_r):
        for j in range(pad_c, cols - pad_c):
            total = 0.0
            for k in range(-pad_r, pad_r + 1):
                for l in range(-pad_c, pad_c + 1):
                    kr = pad_r + k
                    kc = pad_c + l
                    total += image_array[i + k, j + l] * kernel[kr, kc]
            output[i, j] = total 
    
    output = np.clip(output, 0, 255).astype(np.uint8)
    output_image = Image.fromarray(output)
    
    output_path = os.path.join('Images', 'Output', file_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    output_image.save(output_path)
    print(f"Filtered grayscale image saved as {output_path}")

def median_filtering(file_path: str) -> None:
    file_name = os.path.basename(file_path)
    image = Image.open(file_path)
    
    image_array = np.array(image, dtype=np.float32)
    output = np.zeros_like(image_array)
    
    kernel = 3
    rows, cols = image_array.shape
    pad = kernel // 2
    
    for i in range(pad_r, rows - pad_r):
        for j in range(pad_c, cols - pad_c):
            
            for k in range(-pad_r, pad_c + 1):
                for l in range(-pad_c, pad_c + 1):
                      
    
def mean_filtering_color(file_path: str) -> None:
    file_name = os.path.basename(file_path)
    image = Image.open(file_path).convert('RGB')
    
    image_array = np.array(image, dtype=np.float32)
    output = np.copy(image_array)
    
    kernel = np.ones((3, 3)) / 9.0
    rows, cols, channels = image_array.shape
    pad_r, pad_c = 1, 1
    
    for i in range(pad_r, rows - pad_r):
        for j in range(pad_c, cols - pad_c):
            total = np.zeros(channels, dtype=np.float32)
            
            for k in range(-pad_r, pad_r + 1):
                for l in range(-pad_c, pad_c + 1):
                    pixel = image_array[i + k, j + l]
                    kernel_value = kernel[k + pad_r, l + pad_c]
                    total += pixel * kernel_value
                    
            output[i, j] = total 
    
    output = np.clip(output, 0, 255).astype(np.uint8)
    output_image = Image.fromarray(output)
    
    output_path = os.path.join('Images', 'Output', file_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    output_image.save(output_path)
    print(f"Filtered color image saved as {output_path}")

