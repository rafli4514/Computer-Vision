import os
import numpy as np
import tkinter as tk
from tkinter import filedialog
import scipy.ndimage
from PIL import Image


def mean_filtering_greyscale(file_path: str) -> None:
    file_name = os.path.basename(file_path)
    
    image = Image.open(file_path).convert('L')  
    
    kernel = np.ones((5,5)) / 25  
    B = scipy.ndimage.convolve(image, kernel)
        
    B = Image.fromarray(B.astype(np.uint8))  
    
    output_path = os.path.join('Images', 'Output', file_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  
    B.save(output_path)
    print(f"Filtered grayscale image saved as {output_path}")
    

def mean_filtering_color(file_path: str) -> None:
    file_name = os.path.basename(file_path)
    
    image = Image.open(file_path)
    
    image_array = np.array(image)
    
    kernel = np.ones((5, 5)) / 25  
    
    R = scipy.ndimage.convolve(image_array[:,:,0], kernel, mode='constant', cval=0)
    G = scipy.ndimage.convolve(image_array[:,:,1], kernel, mode='constant', cval=0)
    B = scipy.ndimage.convolve(image_array[:,:,2], kernel, mode='constant', cval=0)
    
    filtered_array = np.stack([R, G, B], axis=2).astype(np.uint8)  
    output_path = os.path.join('Computer_vision', 'Images', 'Output', file_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  
    image_filtered = Image.fromarray(filtered_array)
    image_filtered.save(output_path)
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
