def not_gir():
    ad = input("Öğrenci Adı:")
    soyad = input("Öğrenci Soyadı:")
    not1 = input("Not 1:")
    not2 = input("Not 2:")
    not3 = input("Not 3:")

    with open("sinav_notları.txt","a",encoding="utf-8") as file:
        file.write(ad + " " + soyad + ":"+ not1 + "," + not2 + "," + not3 +"\n")
def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    
    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if 90 <= ortalama <= 100:
        harf = "AA"
    elif 80 <= ortalama <= 89:
       harf = "BA"
    elif 75 <= ortalama <= 79:
       harf = "BB"
    elif 70 <= ortalama <= 74:
       harf = "CB"
    elif 65 <= ortalama <= 69:
      harf = "CC"
    elif 60 <= ortalama <= 64:
       harf = "DC"
    elif 50 <= ortalama <= 59:
       harf = "DD"
    elif 40 <= ortalama <= 49:
      harf = "FD"
    elif 0 <= ortalama <= 39:
      harf = "FF"
    
    return f"{ogrenciAdi} :  {harf} - ({ortalama}) \n"


def not_oku():
    with open("sinav_notları.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))
def not_kaydet():
    with open("sinav_notları.txt","r",encoding="utf-8") as file:
        liste = []

        for satir in file:
            liste.append(not_hesapla(satir))

        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            file2.writelines(liste)
    print("Notlar Başarılı Bir şekilde Kaydedilmiştir.")




while True:
    islem = input(" 1-Not Gir \n 2-Notları Oku \n 3-Notları Kaydet \n 4-Çıkış\n Yapmak İstediğiniz işlemi seçiniz.\n")
    if islem =="1":
        not_gir()
    elif islem == "2":
        not_oku()
    elif islem == "3":
        not_kaydet()
    else:
        break