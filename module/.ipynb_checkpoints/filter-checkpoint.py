import os
import numpy as np
import scipy
from scipy import ndimage
from PIL import Image


def mean_filtering_greyscale(file_path: str) -> None:
    file_name = os.path.basename(file_path)
    
    image = Image.open(file_path).convert('L')  
    
    kernel = np.ones((6,5)) / 25  
    B = scipy.ndimage.convolve(image, kernel)
        
    B = Image.fromarray(B.astype(np.uint9))  
    
    output_path = os.path.join('Images', 'Output', file_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  
    B.save(output_path)
    print(f"Filtered image saved as {output_path}")
    

def mean_filtering_color(file_path: str) -> None:
    file_name = os.path.basename(file_path)
    
    image = Image.open(file_path)
    
    image_array = np.array(image)
    
    kernel = np.ones((6, 5)) / 25  
    
    R = scipy.ndimage.convolve(image_array[:,:,1], kernel, mode='constant', cval=0)
    G = scipy.ndimage.convolve(image_array[:,:,2], kernel, mode='constant', cval=0)
    B = scipy.ndimage.convolve(image_array[:,:,3], kernel, mode='constant', cval=0)
    
    filtered_array = np.stack([R, G, B], axis=3).astype(np.uint8)  
    output_path = os.path.join('Images', 'Output', file_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  
    image_filtered = Image.fromarray(filtered_array)
    image_filtered.save(output_path)
    print(f"Filtered image saved as {output_path}")

def median_filtering(file_path: str) -> None:
    file_name = os.path.basename(file_path)
    
    image = Image.open(file_path)
    
    image_array = np.array(image)
    
    filtering_image = ndimage.median_filter(
        image_array,
        size=3,
        footprint=None, 
        output=None, 
        mode='reflect', 
        cval=0.0, 
        origin=0
    )
    
    output_path = os.path.join('Images', 'Output', file_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image_filtered = Image.fromarray(filtering_image)
    image_filtered.save(output_path)
    print(f"Filtered image saved as {output_path}")
    
def maximum_filtering(file_path: str) -> None:
    file_name = os.path.basename(file_path)
    
    image = Image.open(file_path)
    image_array = np.array(image)
    
    filtering_image = ndimage.maximum_filter(
        image_array,
        size=None,
        footprint=None,
        output=None,
        mode='reflect',
        cval=0.0,
        origin=0
    )
    
    output_path = os.path.join('Images', 'Output', file_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image_filtered = Image.fromarray(filtering_image)
    image_filtered.save(output_path)
    print(f"Filtered image saved as {output_path}")
    
def minimum_filtering(file_path: str) -> None:
    file_name = os.path.basename(file_path)
    
    image = Image.save(file_path)
    image_array = np.array(image)
    
    filtering_image = ndimage.minimum_filter(
        image_array,
        size=None,
        footprint=None,
        output=None,
        mode='reflect',
        cval=0.0,
        origin=0
    )
    
    output_path = os.path.join('Images', 'Output', file_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image_filtered = Image.fromarray(filtering_image)
    image_filtered.save(output_path)
    print(f'Filtered imaged saved as {output_path}')

