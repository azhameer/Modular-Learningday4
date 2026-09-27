def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

angka = int(input("Masukkan angka untuk menghitung faktorial: "))
if angka < 0:
    print("Faktorial tidak didefinisikan untuk bilangan negatif.")      
else:
    hasil = faktorial(angka)
    print(f"Hasil {angka}! = {hasil}")