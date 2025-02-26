def penjumlahan(x: float, y: float) -> float:
    return x + y

def pengurangan(x: float, y: float) -> float:
    return x - y

def perkalian(x: float, y: float) -> float:
    return x * y

def pembagian(x: float, y:float) -> float:
    try:
        return x / y
    except:
        print("Error!!")

def modulus(x: int, y: int) -> int:
    return x % y

# def akar(x: int) -> float:
    

def pangkat(x: int, y: int) -> int:
    hasil: int = 1
    
    for i in range(y):
        hasil *= x

    return hasil

def displayKalkulator() -> None:
    print("==========================")
    print("|    1. Penjumlahan      |")
    print("|    2. Pengurangan      |")
    print("|    3. perkalian        |")
    print("|    4. pembagian        |")
    print("|    5. modulus          |")
    print("|    6. perpangkatan     |")
    print("==========================")

def operasi(pilihan: int) -> None:
    x: int
    y: int  
    
    if pilihan == 1:
        print("==========================")
        print("|    1. Penjumlahan      |")
        print("==========================")
        
        x = float(input("Masukkan angka pertama: "))
        y = float(input("Masukkan angka kedua: "))
        hasil: float = penjumlahan(x, y)
        print(f"Hasil: {hasil}")
        
    elif pilihan == 2:
        print("==========================")
        print("|    2. Pengurangan      |")
        print("==========================")
        
        x = float(input("Masukkan angka pertama: "))
        y = float(input("Masukkan angka kedua: "))
        hasil: float = pengurangan(x, y)
        print(f"Hasil: {hasil}")
        
    elif pilihan == 3:
        print("==========================")
        print("|    3. Perkalian        |")
        print("==========================")
        x = float(input("Masukkan angka pertama: "))
        y = float(input("Masukkan angka kedua: "))
        hasil: float = perkalian(x, y)
        print(f"Hasil: {hasil}")
        
    elif pilihan == 4:
        print("==========================")
        print("|    4. Pembagian        |")
        print("==========================")
        x = float(input("Masukkan angka pertama: "))
        y = float(input("Masukkan angka kedua: "))
        hasil: float = pembagian(x, y)
        print(f"Hasil: {hasil}")
        
    elif pilihan == 5:
        print("==========================")
        print("|    5. Modulus          |")
        print("==========================")
        x = float(input("Masukkan angka pertama: "))
        y = float(input("Masukkan angka kedua: "))
        hasil: float = pembagian(x, y)
        print(f"Hasil: {hasil}")
        
    elif pilihan == 6:
        print("==========================")
        print("|    6. Perpangkatan     |")
        print("==========================")  
        x = int(input("Masukkan angka: "))
        y = int(input("Dipangkatkan: "))
        hasil: int = pangkat(x, y)
        print(f"Hasil: {hasil}") 

if __name__ == "__main__":
    angka1: int
    angka2: int
    pilihan: int
    print("======Kalkulator Sederhana=======")
    
    while(True):
        displayKalkulator()
        
        pilihan = int(input("Masukkan pilihan: "))
        
        operasi(pilihan)