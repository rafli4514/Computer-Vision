import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2
import threading

class ImageProcessor:
    @staticmethod
    def apply_filter(img_array, filter_name, kernel_size=3):
        """
        Apply filter dengan optimasi khusus untuk performa real-time
        Return: numpy array gambar yang sudah diproses
        """
        if filter_name == "Original":
            return img_array
        
        # Konversi ke grayscale jika diperlukan
        if filter_name == "Grayscale":
            return ImageProcessor._grayscale(img_array)
        
        # Optimasi kernel size ganjil
        kernel_size = kernel_size if kernel_size % 2 == 1 else kernel_size + 1
        
        try:
            if filter_name == "Mean":
                return ImageProcessor._mean_filter(img_array, kernel_size)
            elif filter_name == "Median":
                return ImageProcessor._median_filter(img_array, kernel_size)
            elif filter_name == "Max":
                return ImageProcessor._max_filter(img_array, kernel_size)
            elif filter_name == "Min":
                return ImageProcessor._min_filter(img_array, kernel_size)
            elif filter_name == "Edge Detection":
                return ImageProcessor._edge_detection(img_array)
        except Exception as e:
            print(f"Filter error: {e}")
            return img_array

    @staticmethod
    def _grayscale(img_array):
        if len(img_array.shape) == 3:
            return cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        return img_array

    @staticmethod
    def _mean_filter(img_array, kernel_size):
        # Pastikan kernel ganjil
        kernel_size = kernel_size if kernel_size % 2 == 1 else kernel_size + 1
        return cv2.blur(img_array, (kernel_size, kernel_size))

    @staticmethod
    def _median_filter(img_array, kernel_size):
        # Optimasi khusus untuk kernel kecil
        if kernel_size <= 3:
            return cv2.medianBlur(img_array, kernel_size)
        else:
            return ndimage.median_filter(img_array, size=kernel_size)

    @staticmethod
    def _max_filter(img_array, kernel_size):
        return ndimage.maximum_filter(img_array, size=kernel_size)

    @staticmethod
    def _min_filter(img_array, kernel_size):
        return ndimage.minimum_filter(img_array, size=kernel_size)

    @staticmethod
    def _edge_detection(img_array):
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY) if len(img_array.shape) == 3 else img_array
        return cv2.Canny(gray, 100, 200)

    @staticmethod
    def array_to_image(img_array):
        return Image.fromarray(img_array)
    
    