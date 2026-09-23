#Sistem Parkir Otomatis

#Aturan
#Kendaraan yang valid hanya Motor atau Mobil
#Motor dikenakan tarif 2000/J untuk 2 jam pertama, lalu 1000/J untuk jam berikutnya
#Mobil dikenakan tarif 5000/J untuk 2 jam pertama, lalu 3000/J untuk jam berikutnya
#Jika jam parkir >12 Jam maka dikenakan denda +50000
#Jam parkir harus diantara >=0 dan <24 atau jam parkir tidak valid.

#Input 
jenis = input("Mobil atau Motor? (mobil/motor): ").lower().strip()
jam_masuk = float(input("Jam Masuk (0-23): "))
jam_keluar = float(input("Jam Keluar (0-23): "))

#Cek Jenis kendaraan
if jam_masuk < 0 or jam_masuk >= 24 or jam_keluar < 0 or jam_keluar >= 24:
        print ("Jam Parkir Tidak Valid!")

elif jenis != "motor" and jenis != "mobil":
    print("Jenis Kendaraan Tidak Valid!")


else:
#Cek Durasi Parkir
    if jam_keluar >= jam_masuk:
        durasi = jam_keluar - jam_masuk
    else:
        durasi = (24 - jam_masuk) + jam_keluar

    print("Durasi Parkir :", durasi, "Jam")

    #Validasi durasi parkir

    #Tarif parkir motor
    if jenis == "motor":
        if durasi <= 2:
            biaya = durasi * 2000
        else:
            biaya = (2 * 2000) + ((durasi - 2) * 1000)

    else:
        if durasi <= 2:
            biaya = durasi * 5000
        else:
            biaya = (2 * 5000) + ((durasi - 2) * 3000)

    #Denda Parkir
    if durasi > 12:
        biaya = biaya + 50000
        print("Durasi Melebihi 12 Jam Denda Rp.50000")

    #Hasil AKhir
    print("Tarif Parkir : Rp.", biaya)