def hitungfpb(a,b):
    if b ==0 :
        return a
    else:
        return hitungfpb(b, a%b)

def hitungkpk (a,b):
    kpk = max(a,b)
    while True:
        if kpk % a == 0 and kpk % b == 0:
            return kpk
        else:
            kpk += 1

while True:
    print("Option : ")
    print("1. Hitun FPB")
    print("2. Hitung KPK")
    print("3. Keluar")

    pilihan = int(input("Masukkan pilihan anda : "))

    if pilihan == 1 :
        a = int(input("Masukkan bilangan pertama : "))
        b = int(input("Masukkan bilangan kedua : "))
        fpb=hitungfpb(a, b)
        print("FPB dari ", a, " dan ", b, " adalah ", fpb)
    elif pilihan == 2 :
        a = int(input("Masukkan bilangan pertama : "))
        b = int(input("Masukkan bilangan kedua : "))
        kpk=hitungkpk(a, b)
    elif pilihan == 3 :
        print("Terima Kasih")
        break
    else:
        print("Pilihan tidak valid")