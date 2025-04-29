from module import filter
import tkinter as tk
from tkinter import filedialog


def operasi(pilihan: int) -> None:
    if pilihan == 1:
        print("=========================================")
        print("|    1. Filter Mean Image Color         |")
        print("=========================================")
        
        root = tk.Tk()
        root.withdraw()
        
        file_path: str = filedialog.askopenfilename()
        
        filter.mean_filtering_greyscale()
        
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


