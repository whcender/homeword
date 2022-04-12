import sqlite3

connect = sqlite3.connect("studens.db")

cursor = connect.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students(ogrencino INT, isim TEXT, anneadı TEXT, babaadı TEXT, dogumtarihi INT, cinsiyet TEXT, adres TEXT, telefon INT, email TEXT)")

                                    # VERİ EKLEME # 

# cursor.execute("INSERT INTO students VALUES(549398123, 'adem mutlu', 'Gül', 'Recep', 01.02.2002, 'Erkek','İstanbul', '05290000001', 'Email')")
# cursor.execute("INSERT INTO students VALUES(172312839, 'asu tekin', 'Ayşe', 'Şaban', 14.05.2001, 'Kadın','İstanbul', '05290000002', 'Email')")
# cursor.execute("INSERT INTO students VALUES(629123989, 'pelin aslan', 'Ahsen', 'Kemal', 26.06.2001, 'Kadın','İstanbul', '05290000003', 'Email')")
# cursor.execute("INSERT INTO students VALUES(716239012, 'ender tekin', 'Gülnur', 'Ramazan', 01.01.2002, 'Erkek','Bursa', '05290000004', 'Email')")
# cursor.execute("INSERT INTO students VALUES(887431912, 'osman kartal', 'Fatma', 'Kamil', 04.02.2002, 'Erkek','Erzurum', '05290000005', 'Email')")
# cursor.execute("INSERT INTO students VALUES(634417361, 'serhat karaoğlu', 'Sude', 'Dursun', 19.08.2001, 'Erkek','Ağrı', '05290000006', 'Email')")
# cursor.execute("INSERT INTO students VALUES(837120832, 'büşra pekmez', 'Rana', 'Adem', 26.09.2001, 'Kadın','Kars', '05290000007', 'Email')")
# cursor.execute("INSERT INTO students VALUES(939813823, 'eylül türkoğlu', 'Beyza', 'Tekin', 19.12.2002, 'Kadın','Antalya', '05290000008', 'Email')")
# cursor.execute("INSERT INTO students VALUES(123879173, 'bergen apa', 'Betül', 'Fatih', 25.11.2002, 'Kadın','Antalya', '05290000009', 'Email')")
# cursor.execute("INSERT INTO students VALUES(834719283, 'ender tekin', 'Sema', 'Dursun', 01.02.2002, 'Erkek','Hatay', '05290000010', 'Email')")
# cursor.execute("INSERT INTO students VALUES(973927123, 'alp aras', 'Gül', 'Hamit', 04.04.2002, 'Erkek','Adana', '05290000011', 'Email')")
# cursor.execute("INSERT INTO students VALUES(457638212, 'isa demir', 'Pelin', 'Efe', 11.11.2002, 'Erkek','Edirne', '05290000012', 'Email')")
# cursor.execute("INSERT INTO students VALUES(268612361, 'talha demirtaş', 'Merve', 'Efecan', 26.07.2002, 'Erkek','Kastamonu', '05290000013', 'Email')")
# cursor.execute("INSERT INTO students VALUES(762361937, 'ege taş', 'Ahsen', 'Buğra', 03.09.2002, 'Erkek','Malatya', '05290000014', 'Email')")
# cursor.execute("INSERT INTO students VALUES(737240180, 'adnan kaplan', 'Ahu', 'Bahadır', 07.09.2001, 'Erkek','İzmir', '05290000015', 'Email')")
# cursor.execute("INSERT INTO students VALUES(734129379, 'bekir buğra', 'Arzu', 'Caner', 01.12.2002, 'Erkek','İzmit', '05290000016', 'Email')")
# cursor.execute("INSERT INTO students VALUES(548719272, 'fevzi tekin', 'Meryem', 'Haydar', 09.03.2002, 'Erkek','İzmit', '05290000017', 'Email')")
# cursor.execute("INSERT INTO students VALUES(621681263, 'asel aslan', 'Berna', 'Polat', 09.03.2001, 'Kadın','İstanbul', '05290000018', 'Email')")
# cursor.execute("INSERT INTO students VALUES(347612321, 'ela sever', 'Fulya', 'Demirkan', 05.10.2001, 'Kadın','Gaziantep', '05290000019', 'Email')")
# cursor.execute("INSERT INTO students VALUES(873246812, 'hale polat', 'Kevser', 'Fadıl', 19.10.2002, 'Kadın','Ankara', '05290000020', 'Email')")



                                    # VERİ ÇEKME #

chose = int(input("işlem seçin: \n1. Numaraya Göre Veri Al \n2. İsme Göre Veri Al \n3. Telefona Göre Veri Al \n4. İptal \nİşlem Seçin:"))

if chose == 1:
    number = int(input("Numarayı Girin (1-20): "))

    cursor.execute(f"SELECT * from students WHERE ogrencino == {number}")
    for data in cursor.fetchall():
        print(data)

elif chose == 2:
    name = input("İsmi Soyismi girin (küçük harf kullanın): ")

    cursor.execute(f"SELECT * from students WHERE isim == '{name}'")
    for data in cursor.fetchall():
        print(f"( numara: {data[0]}, isim soyisim: {data[1]}, anne adı:{data[2]}, baba adı: {data[3]}, doğum tarihi: {data[4]}, cinsiyet: {data[5]}, adres: {data[6]}, telefon: {data[7]}, email: {data[8]} )")


elif chose == 3: 
    telephone = int(input("Telefon numarası girin: "))
    
    cursor.execute(f"SELECT * from students WHERE telefon == {telephone}")
    for data in cursor.fetchall():
        print(data)


elif(chose) == 4:
    print("İşlem İptal Edildi")

else:
    raise ValueError("Geçersiz İşlem ID")


connect.commit()
connect.close()
