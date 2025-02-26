import os
import numpy as np
import tkinter as tk
from tkinter import filedialog
import scipy.ndimage
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

def operasi(pilihan: int) -> None:
    if pilihan == 1:
        print("=========================================")
        print("|    1. Filter Mean Image Color         |")
        print("=========================================")
        
        root = tk.Tk()
        root.withdraw()
        
        file_path: str = filedialog.askopenfilename()
        
        mean_filtering_color(file_path)
        
    elif pilihan == 2:
        print("========================================")
        print("|    2. Filter Mean Image Greyscale     |")
        print("========================================")
        
        root = tk.Tk()
        root.withdraw()
        
        file_path: str = filedialog.askopenfilename()
        
        mean_filtering_greyscale(file_path)
    
    elif pilihan == 3:
        print("Exiting the program.")
        exit()

def displayMenu() -> None:
    print("======================================")
    print("|    1. Filter Mean Image Color      |")
    print("|    2. Filter Mean Image Greyscale  |")
    print("|    3. Exit                         |")
    print("======================================")

if __name__ == "__main__":
    print("====== Image Filter =======")
    
    while(True):
        displayMenu()
        
        pilihan = int(input("Masukkan pilihan: "))
        
        operasi(pilihan)
