# 21-01-Sikemas
Repository ini digunakan untuk menyimpan artefak proyek mata kuliah 12S3101 Pemrograman dan Pengujian Aplikasi Web di Institut Teknologi Del. Topik: Sistem Informasi Kepuasan Masyarakat

# Sikemas
SIKEMAS adalah aplikasi untuk melakukan survei kepuasan masyarakat kepada pengguna layanan dengan mengukur kepuasan masyarakat pengguna layanan. 
Adapun tujuan dibangunnya Sistem Informasi Survei Kepuasan Masyarakat adalah:
1.	Mendorong partisipasi masyarakat sebagai pengguna layanan dalam menilai kinerja penyelenggara pelayanan.
2.	Mendorong penyelenggara pelayanan untuk meningkatkan kualitas pelayanan publik. 
3.	Mendorong penyelenggara pelayanan menjadi lebih inovatif dalam menyelenggarakan pelayanan publik.
4.	Mengukur kecenderungan tingkat kepuasan masyarakat terhadap pelayanan publik.

#Struktur Kerja
Berikut adalah rancangan kerja aplikasi Sikemas yang dibangun dengan python dan menggunakan Django Framework.


![image](https://user-images.githubusercontent.com/78084196/136371668-20d65f88-8198-4096-a8cb-873181a2c887.png)

#Struktur Database

![Struktur_Database](https://user-images.githubusercontent.com/78084196/136371820-3bcf7d31-1979-429c-8830-93ec16f7b33a.jpeg)

#Instalasi dan Konfigurasi Sikemas
1. Installation
Untuk menjalankan repository ini, terlebih dahulu clone repository ini ke lokal komputer anda dan pastikan telah melakukan instalasi django framework pada komputer anda.
Langkah-langkah instalasi django framework yaitu:
- Download dan install python pada komputer anda (download disini https://www.python.org/downloads/  )
- Setelah di install, lakukan pengecekan versi python yang menandakan bahwa python berhasil di install dengan cara menjalankan perintah berikut pada command prompt
    python --version

- Kemudian lakulan instalasi django framework dengan menjalankan perintah berikut pada command prompt
		pip install django ==3.2.8		
*Untuk beberapa kasus, saat perintah diatas dijalankan akan mucul error yang mengatakan bahwa perintah ‘pip’ tidak ditemukan. Maka anda perlu melakukan instalasi ‘pip’ dengan menjalankan perintah berikut pada command prompt
		py get-pip.py	

- Django mendukung berbagai macam server basis data dan didukung dengan PostgreSQL, MariaDB, MySQL,HeidiSQL, Oracle and SQLite. Silahkan melakukan instalasi untuk salah satu aplikasi database yang tersebut.  
- Kemudian lakukan instalasi sqlclient yang nantinya akan berguna untuk menghubungkan antara django dan sql yang digunakan dengan menjalankan perintah berikut pada command prompt
		python -m pip install mysqlclient


2.Configuration

- Pada aplikasi database yang anda install, silahkan untuk membuat database baru dengan nama ‘sikemasdb’. 
- Silahkan untuk men-dump skrip basis data yang terdapat pada folder sikemasdb.sql pada repository ini. Username yang digunakan adalah  ‘’‘myroot’’’ dengan password  ‘’’kelompok1’’’. 
- Pada command line tempat repository ini anda clone, jalankan perintah berikut untuk melakukan migrasi informasi dari file models.py ke basis data sikemasdb pada lokal komputer.
		py manage.py makemigrations

- Setelah perintah diatas berhasil dijalankan, kemudian pada command line yang sama jalankan perintah berikut
		py manage.py migrate

- Selanjutnya, jalankan django framework internal web server dengan menjalankan perintah berikut pada command line
		py manage.py runserver
