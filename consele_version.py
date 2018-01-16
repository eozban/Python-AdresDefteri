#!/usr/bin/env python
# -*- coding: utf8 -*-

from Database import *


def main():
    db = Database()

    while True:
        try:

            print("""
                   Yapılacak Işlemi Seçiniz...
                   -----------------
                   1) Tümünü Listele
                   2) Adres Ekle
                   3) Adres Sil
                   4) Adres ARA
                   5) Çıkış
                   """)

            girdi = input("Lütfen bir işlem seçiniz: ")

            if girdi == 1:
                liste = db.list_all()
                FORMAT = '%-8s%-18s%-18s%-18s%-20s'
                print(FORMAT % ('Sıra', 'Isim', 'SoyIsim', 'Telefon', 'Email Adresi'))
                print('-' * 50)
                for row in liste:
                    print(FORMAT % row)

            elif girdi == 2:
                name = raw_input("Isim: ").decode('utf8')
                lastname = raw_input("Soyisim: ").decode('utf8')
                phone_number = raw_input("Telefon Numarasi: ").decode('utf8')
                email_address = raw_input("Email Adresi: ").decode('utf8')
                db.add_record(name, lastname, phone_number, email_address)
                print("\nKayıt Eklenmiştir.")

            elif girdi == 3:
                girdi = raw_input("Silinecek kaydın sıra numarasını giriniz: ")
                db.delete_record(girdi)
                print("\nKayıt silinmiştir.")

            elif girdi == 4:
                print("""
                   Arama Şeklini Seçiniz...
                   -----------------
                   1) Id'ye göre (varsayılan)
                   2) Ad Soyad'a göre
                   3) Telefon Numarasına Göre
                   4) E-Mail Adresine göre
                   """)
                aramasekli = raw_input("Lütfen bir işlem seçiniz (1): ") or "1"
                aranacakmetin = raw_input("Lütfen Aranacak metni giriniz: ")

                if aramasekli == "2":
                    record = db.fromname(aranacakmetin)
                elif aramasekli == "3":
                    record = db.fromphone(aranacakmetin)
                elif aramasekli == "4":
                    record = db.fromemail(aranacakmetin)
                else:
                    record = db.fromid(aranacakmetin)

                FORMAT = '%-8s%-18s%-18s%-18s%-20s'
                print(FORMAT % ('Sıra', 'Isim', 'SoyIsim', 'Telefon', 'Email Adresi'))
                print('-' * 50)
                for row in record:
                    print(FORMAT % row)
            else:
                quit()
        except (SyntaxError, KeyboardInterrupt):  # Herhangi bir işlem seçmeden Ctrl+C  yada enter tuşuna basılırsa
            print("\n UYARI !! Lütfen bir işlem seçiniz. Programı kapamak için çıkış yapınız")


if __name__ == '__main__':
    main()
