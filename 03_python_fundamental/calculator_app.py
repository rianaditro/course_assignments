def calculator():
    try:
        
        angka1 = int(input("Masukkan angka 1 : "))
        operasi = str(input("Masukkan operasi (+, -, *, /, e for exit) : "))
        angka2 = int(input("Masukkan angka 2 : "))
        
        if operasi == "+":
            hasil = angka1 + angka2
        elif operasi == "-":
            hasil = angka1 - angka2
        elif operasi == "*":
            hasil = angka1 * angka2
        elif operasi == "/":
            if angka2 == 0:
                print("Operasi akan error karena pembagian 0")
            else:
                hasil = angka1 / angka2
            return
        else:
            print("Operasi tidak valid!!")
            return
        
        print(f"Hasilnya adalah {hasil}")
    except ValueError:
        print("Kalkulator Error")
        
calculator()
        