from Database import *

def main():
    db_ = Database()

    while True:
        try:

            print("""
                   Yapılacak Işlemi Seçiniz...
                   -----------------
                   1) Adresleri Listele
                   2) Adres Ekle
                   3) Adres Sil
                   4) Id'den Getir
                   5) Çıkış
                   """)

            girdi = input("Lütfen bir işlem seçiniz: ")

            if girdi == 1:
                liste = db_.list_all()
                FORMAT = '%-8s%-18s%-18s%-20s'
                print(FORMAT % ('Sıra', 'Isim Soyisim', 'Telefon', 'Email Adresi'))
                print('-' * 50)
                for row in liste:
                    print(FORMAT % row)

            elif girdi == 2:
                name = raw_input("Isim Soyisim: ")
                phone_number = raw_input("Telefon Numarasi: ")
                email_address = raw_input("Email Adresi: ")
                db_.add_record(name, phone_number, email_address)
                print("\nKayıt Eklenmiştir.")

            elif girdi == 3:
                girdi = raw_input("Silinecek kaydın sıra numarasını giriniz: ")
                db_.delete_record(girdi)
                print("\nKayıt silinmiştir.")

            elif girdi == 4:
                girdi = raw_input("Lütfen id numarasını giriniz: ")
                otp = db_.get_record(girdi)
                FORMAT = '%-8s%-18s%-18s%-20s'
                print(FORMAT % ('Sıra', 'Isim Soyisim', 'Telefon', 'Email Adresi'))
                print('-' * 50)
                for row in otp:
                    print(FORMAT % row)
            else:
                quit()
        except (SyntaxError, KeyboardInterrupt):  # Herhangi bir işlem seçmeden Ctrl+C  yada enter tuşuna basılırsa
            print("\n UYARI !! Lütfen bir işlem seçiniz. Programı kapamak için çıkış yapınız")
