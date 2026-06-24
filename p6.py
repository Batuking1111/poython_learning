print("""
**************************

Geometril şeki hesaplama

1.Üçgen

2.Dötgen

**************************
""")

işlem = input("Bir işlem seçin: ")

if işlem == "1":
    print("Lütfen kenarları girin")
    a = int(input("1.Kenar: "))
    b = int(input("2.Kenar: "))
    c = int(input("3.Kenar: "))
    if a == b == c:
        print("Bu eşkenar bir üçgendir.")
    elif ((a+b) > c and (a+c) > b and (b+c) > a):
        if a == b or a == c or b == c:
            print("Bu ikizkenar bir üçgendir.")
        else:
            print("Bu sıradan bir üçgen.")
    else:
        print("Bu bir üçggen değildir.")
elif işlem == "2":
    print("Lütfen kenarları girin")
    a = int(input("1.Kenar: "))
    b = int(input("2.Kenar: "))
    c = int(input("3.Kenar: "))
    d = int(input("4.Kenar: "))
    if a == b == c == d:
        print("Bu bir karedir.")
    elif a == c and b == d:
        print("Bu bir dikdörtgendir.")
    else:
        print("Bu bir sıradan dörtgendir.")
else:
    print("Geçersiz işlem.")



