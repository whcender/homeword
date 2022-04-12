import sqlite3

from colorama import Cursor

connect = sqlite3.connect("studens.db")

cursor = connect.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students(ogrencino INT, isim TEXT, soyisim TEXT, anneadı TEXT, babaadı TEXT, dogumtarihi INT, cinsiyet TEXT, adres TEXT, telefon INT, email TEXT)")

                                    # VERİ EKLEME #

# cursor.execute("INSERT INTO students VALUES(1, 'Adem', 'Mutlu', 'Gül', 'Recep', 2002, 'Erkek','İstanbul', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(2, 'Asu', 'Tekin', 'Ayşe', 'Şaban', 2001, 'Kadın','İstanbul', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(3, 'Pelin', 'Aslan', 'Ahsen', 'Kemal', 2001, 'Kadın','İstanbul', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(4, 'Serhat', 'Teke', 'Gülnur', 'Ramazan', 2001, 'Erkek','Bursa', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(5, 'Osman', 'Kartal', 'Fatma', 'Kamil', 2001, 'Erkek','Erzurum', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(6, 'Serhat', 'Karaoğlu', 'Sude', 'Dursun', 2001, 'Erkek','Ağrı', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(7, 'Büşra', 'Pekmez', 'Rana', 'Adem', 2001, 'Kadın','Kars', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(8, 'Eylül', 'Türkoğlu', 'Beyza', 'Tekin', 2002, 'Kadın','Antalya', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(9, 'Bergen', 'Apa', 'Betül', 'Fatih', 2002, 'Kadın','Antalya', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(10, 'Ender', 'Tekin', 'Sema', 'Dursun', 2002, 'Erkek','Hatay', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(11, 'Alp', 'Aras', 'Gül', 'Hamit', 2002, 'Erkek','Adana', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(12, 'İsa', 'Demir', 'Pelin', 'Efe', 2002, 'Erkek','Edirne', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(13, 'Talha', 'Demirtaş', 'Merve', 'Efecan', 2002, 'Erkek','Kastamonu', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(14, 'Ege', 'Taş', 'Ahsen', 'Buğra', 2002, 'Erkek','Malatya', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(15, 'Adnan', 'Kaplan', 'Ahu', 'Bahadır', 2001, 'Erkek','İzmir', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(16, 'Bekir', 'Buğra', 'Arzu', 'Caner', 2002, 'Erkek','İzmit', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(17, 'Fevzi', 'Tekin', 'Meryem', 'Haydar', 2002, 'Erkek','İzmit', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(18, 'Asel', 'Aslan', 'Berna', 'Polat', 2001, 'Kadın','İstanbul', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(19, 'Ela', 'Sever', 'Fulya', 'Demirkan', 2001, 'Kadın','Gaziantep', '05290000000', 'Email')")
# cursor.execute("INSERT INTO students VALUES(20, 'Hale', 'Polat', 'Kevser', 'Fadıl', 2002, 'Kadın','Ankara', '05290000000', 'Email')")



                                    # VERİ ÇEKME #

chose = int(input("işlem seçin: \n1. Numaraya Göre Veri Al \n2. İsme Göre Veri Al \n3. Yaşa Göre Veri Al \n4. Kompleks Arama \n5. İptal \nİşlem Seçin:"))

if chose == 1:
    number = int(input("Numarayı Girin (1-20): "))

    cursor.execute(f"SELECT * from students WHERE ogrencino == {number}")
    for data in cursor.fetchall():
        print(data)

elif chose == 2:
    name = input("İsmi girin: ")

    cursor.execute(f"SELECT * from students WHERE isim == '{name.capitalize()}'")
    for data in cursor.fetchall():
        print(data)

elif chose == 3:
    age = int(input("Yaş Değerini Girin (sadece yıl): "))

    cursor.execute(f"SELECT * from students WHERE dogumtarihi == {age}")
    for data in cursor.fetchall():
        print(data)

elif chose == 4: 
    print("****************************************************************************************************")
    search1 = input("1. Arama Filtresini Seçin (isim, soyisim, anneadı, babaadı): ")
    search1 = search1.lower()

    search2 = input("2. Arama Filtresini Seçin (isim, soyisim, anneadı, babaadı): ")
    search2 = search2.lower()

    find1 = input("1. filtrenin aramasını girin: ")
    find2 = input("2. filtrenin aramasını girin: ")

    cursor.execute(f"SELECT * from students WHERE {search1} == '{find1.capitalize()}' AND {search2} == '{find2.capitalize()}'")
    for data in cursor.fetchall():
        print(data)

elif(chose) == 5:
    print("İşlem İptal Edildi")

else:
    raise ValueError("Geçersiz İşlem ID")


connect.commit()

connect.close()
