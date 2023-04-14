import string
import base64

def atbash_sifreleme(metin):
    atbash_cevirici = string.ascii_uppercase[::-1] + string.ascii_lowercase[::-1]
    return metin.translate(str.maketrans(string.ascii_letters, atbash_cevirici))

def sezar_sifreleme(metin, kaydirma):
    sezar_cevirici = string.ascii_uppercase[kaydirma:] + string.ascii_uppercase[:kaydirma] + string.ascii_lowercase[kaydirma:] + string.ascii_lowercase[:kaydirma]
    return metin.translate(str.maketrans(string.ascii_letters, sezar_cevirici))

def vernam_sifreleme(metin, anahtar):
    return "".join(chr(ord(t) ^ ord(k)) for t, k in zip(metin, anahtar))

def anahtar_olustur(metin, anahtar):
    if len(anahtar) >= len(metin):
        return anahtar
    else:
        for _ in range(len(metin) - len(anahtar)):
            anahtar += anahtar
        return anahtar[:len(metin)]

def sifrele(metin, anahtar, sezar_shift):
    atbash_sifrelenmis = atbash_sifreleme(metin)
    sezar_sifrelenmis = sezar_sifreleme(atbash_sifrelenmis, sezar_shift)
    genisletilmis_anahtar = anahtar_olustur(sezar_sifrelenmis, anahtar)
    vernam_sifrelenmis = vernam_sifreleme(sezar_sifrelenmis, genisletilmis_anahtar)
    return base64.b64encode(vernam_sifrelenmis.encode()).decode()

def sifre_coz(sifreli_metin, anahtar, sezar_shift):
    vernam_cozulmus = base64.b64decode(sifreli_metin).decode()
    genisletilmis_anahtar = anahtar_olustur(vernam_cozulmus, anahtar)
    sezar_cozulmus = vernam_sifreleme(vernam_cozulmus, genisletilmis_anahtar)
    atbash_cozulmus = sezar_sifreleme(sezar_cozulmus, -sezar_shift)
    return atbash_sifreleme(atbash_cozulmus)

acik_metin = input("sifrelenecek metni giriniz: ")
anahtar = input("Mesaj ile ayni uzunlukta anahtar giriniz: ")
sezar_shift = 3

sifreli_metin = sifrele(acik_metin, anahtar, sezar_shift)
print("Şifreli:", sifreli_metin)

cozulmus_metin = sifre_coz(sifreli_metin, anahtar, sezar_shift)
print("Çözülmüş:", cozulmus_metin)