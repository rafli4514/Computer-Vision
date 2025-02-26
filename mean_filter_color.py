import numpy as np
import tkinter as tk
from tkinter import filedialog
import scipy.ndimage
from PIL import Image


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
image = Image.open(file_path)

image_array = np.array(image)  
print(image_array)

K = np.ones((5,5)) / 30


R = scipy.ndimage.convolve(image_array[:,:,0], K, mode='constant', cval=0)
G = scipy.ndimage.convolve(image_array[:,:,1], K, mode='constant', cval=0)
B = scipy.ndimage.convolve(image_array[:,:,2], K, mode='constant', cval=0)

filtered_array = np.stack([R, G, B], axis=2).astype(np.uint8)

filtered_image = Image.fromarray(filtered_array)

filtered_image.save(f'Images/Output/gambar')
