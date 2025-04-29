import tkinter as tk
from tkinter import filedialog
from module import filter, edge_detection, image_enhancement

def operasi(pilihan: int) -> None:
    if pilihan == 1:
        print("=========================================")
        print("|    1. Filter Mean Image Color         |")
        print("=========================================")
        
        root = tk.Tk()
        root.withdraw()
        
        file_path: str = filedialog.askopenfilename()
        
        filter.mean_filtering_color(file_path)
        
    elif pilihan == 2:
        print("========================================")
        print("|    2. Filter Mean Image Greyscale    |")
        print("========================================")
        
        root = tk.Tk()
        root.withdraw()
        
        file_path: str = filedialog.askopenfilename()
        
        filter.mean_filtering_greyscale(file_path)
        
    elif pilihan == 3:
        print("========================================")
        print("|    3. Filter median Image            |")
        print("========================================")
        
        root = tk.Tk()
        root.withdraw()
        
        file_path: str = filedialog.askopenfilename()
        
        filter.median_filtering(file_path)
        
    elif pilihan == 4:
        print("========================================")
        print("|    4. Filter Maximum Image           |")
        print("========================================")
        
        root = tk.Tk()
        root.withdraw()
        
        file_path: str = filedialog.askopenfilename()
        
        filter.maximum_filtering(file_path)
        
    elif pilihan == 5:
        print("=========================================")
        print("|    5. Filter Minimum Image            |")
        print("=========================================")
        
        root = tk.Tk()
        root.withdraw()
        
        file_path: str = filedialog.askopenfilename()
        
        filter.minimum_filtering(file_path)
     
    elif pilihan == 6:
        print("=========================================")
        print("|    6. Edge Detection Sobel            |")
        print("=========================================")
        
        root = tk.Tk()
        root.withdraw()
        
        file_path: str = filedialog.askopenfilename()
        
        edge_detection.sobel(file_path)
    
    elif pilihan == 7:
        print("=========================================")
        print("|    7. Edge Detection Prewitt          |")
        print("=========================================")
        
        root = tk.Tk()
        root.withdraw()
        
        file_path: str = filedialog.askopenfilename()

        edge_detection.prewitt(file_path)

    elif pilihan == 8:
        print("=========================================")
        print("|    8. Inverse Image                  |")
        print("=========================================")
        
        root = tk.Tk()
        root.withdraw()
        
        file_path: str = filedialog.askopenfilename()

        image_enhancement.brightness_image(file_path)

    elif pilihan == 0:
        print("TERIMA KASIH")
        exit()

def displayMenu() -> None:
    print("===========================================")
    print("|    1. Filter Mean Image Color           |")
    print("|    2. Filter Mean Image Greyscale       |")
    print("|    3. Filter Median Image               |")
    print("|    4. Filter Maximum Image              |")
    print("|    5. Filter Minimum Image              |")
    print("|    6. Edge Detection Sobel              |")
    print("|    7. Edge Detection Prewitt            |")
    print("|    0. Exit                              |")
    print("===========================================")

if __name__ == "__main__":
    print("====== Image Filter =======")
    
    while(True):
        displayMenu()
        
        pilihan = int(input("Masukkan pilihan: "))
        
        operasi(pilihan)
