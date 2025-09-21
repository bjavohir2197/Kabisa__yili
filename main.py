yil = int(input("Yil kiritng: "))

if yil % 4 == 0:
    if yil % 100 != 0 or yil % 400 == 0:
        print("Kabisa yili")
    else:
        print("Kabisa yili emas")
else:
    print("Kabisa yili emas")