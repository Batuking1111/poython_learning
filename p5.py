print("""
********************
Hesap Makinesi
İşlemler;

1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme
********************
""")

a = int(input("Birinci sayıyı gir: "))
b = int(input("İkinci sayıyı gir: "))

islem = input("İşlemi gir: ")

if islem == "1":
    print("{} ile {} nin toplamı {} dır".format(a,b,a+b))
elif islem == "2":
    print("{} dan {} i çıkarlımasının sonucu {} dır".format(a,b,a-b))
elif islem == "3":
    print("{} ile {} nin çarpımı {} dır".format(a,b,a*b))
elif islem == "2":
    print("{} yı {} e bölünmesinin sonucu {} dır".format(a,b,a/b))
else:
    print("Hatalı işlem girildi!")