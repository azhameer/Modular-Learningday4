n = int(input("Masukkan jumlah bilangan: "))

total = 0

for i in range(1, n + 1):
    angka = float(input(f"Masukkan bilangan ke-{i}: "))
    total += angka

if n > 0:
    rata_rata = total / n
    print(f"\nRata-rata dari {n} bilangan yang Anda masukkan adalah: {rata_rata}")
else:
    print("Bilangan tidak valid, rata-rata tidak dapat dihitung.")