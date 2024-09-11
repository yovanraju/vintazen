![alt text](133647932_228993715297370_3584102809877965900_n-removebg.png)

<div style="text-align: center; font-weight: bold; font-size:50px;">
    VINTAZEN
</div>



## 🔗 LINK WEB

[![link](https://img.shields.io/badge/Link_di_Samping-Klik_di_Sini-red?labelColor=blue)](http://yovan-raju-vintazen.pbp.cs.ui.ac.id/)

## JAWABAN

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. <div style="text-align: justify">
    Pada pertama kali saya mendownload django dan menginstalnya, serta beberapa library dan package lainnya yang digunakan dalam contoh program saya ada di `"requirements.txt"`. Saya membuat proyek dengan format django seperti berikut `django-admin startproject <nama_project> .` dan nama project saya adalah vintazen setelah itu otomatis akan terbuat direktori vintazen
</div> 


2. <div style="text-align: justify">
    Kedua saya menuliskan perintah `python manage.py startapp main` yang dimana ini berguna untuk membuat direktori main yang berisikan struktur Django
</div> 


3. <div style="text-align: justify">
    Ketiga kita harus menambahkan 'main' pada file `setting.py` dalam direktori vintazen dan juga mengatur routing URL pada direktori main, di dalam file `urls.py` untuk melakukan routing agar dapat menjalankan aplikasi main
</div>


4. <div style="text-align: justify">
    Keempat karena kita disuruh memiliki atribut wajib yaitu name, price, description yang dimana harus kita buat dalam file `models.py` di dalam direktori main untuk variabel name berisi models.`name = CharField(max_length=255)` dimana max_length=255 ini opsional dalam arti angkanya tetapi harus ada max lengthnya, untuk variabel price berisikan `price = models.IntegerField()` dan variabel description berisikan `description = models.TextField()`
</div>


5. <div style="text-align: justify">
    Untuk menampilkan nama aplikasi serta nama dan kelas saya menambahkan fungsi render dari modul django.shortcuts fungsi render ini untuk menampilkan data yang kita berikan.
</div>


6. <div style="text-align: justify">
    Saya membuat fungsi di `views.py` dalam main untuk merender template HTML. Setelah itu membuat file HTML di direktori main untuk nampilin data. Saya juga menambahkan `urls.py` di main untuk menghubungkan ke URL vintazen. untuk mengecek itu saya menjalankan http://localhost:8000/
</div>


7. <div style="text-align: justify">
    Saya membuat proyek baru di PWS bernama vintazen, lalu simpan credentials yang diberikan. Setelah itu, menambahkan URL deployment PWS di ALLOWED_HOSTS di `settings.py` proyek Django. Setelah itu saya melakukan `git add`, `commit`, dan `push` ke GitHub, lalu menjalankan perintah dari informasi Project Command di PWS. Setelah itu, ubah nama branch utama menjadi main dengan perintah `git branch -M main`. Terakhir, cek status deployment di PWS, dan akses aplikasi melalui URL deployment yang diberikan.
</div>


## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.

![alt text](<Blank diagram.png>)
<div style="text-align: justify">
    Jadi untuk yang pertama client akan membuka URL dengan browser yang mereka gunakan yang dimana itu akan mengirimkan request ke server Django. Kemudian akan terjadi routing yang dimana akan memeriksa URL dengan urls.py. Jika URL benar maka request akan diteruskan ke views.py yang dimana akan terjadi view logic yaitu pengecekan logika sesuai denghan request dan memanggil model dari database, setelah data sudah ada maka akan digabungkan menggunakan template HTML. Setelah selesai di render maka berkas HTML akan dibalikan ke client dalam browsernya sesuai dengan yang client request.
</div>


## Jelaskan fungsi git dalam pengembangan perangkat lunak!

<div style="text-align: justify">
    Git adalah sistem kontrol yang paling banyak digunakan dalam pengembangan perangkat lunak. Git berfungsi untuk membantu dalam pengembangan dalam mengelola versi dari setiap kode terutama saat banyak kontributor dalam proyek. Dengan git setiap progammer dapat melihat perubahan dari setiap kode dan dapat mengembalikan kode ke sebelumnya jika terjadi error atau bug. Git sendiri menyediakan branch yang dimana kita dapat memperbaiki bug / error secara terpisah dari dari kode utama.
</div>


## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

<div style="text-align: justify">
    Alasan mengapa Django dijadikan permulaan belajar karena Django menggunakan bahasa pemrograman Python yang dimana suda dipelajari di DPP-1 dan Pyhton juga dapat dibilang bahasa pemrograman dasar yang relatif mudah. Django sendiri dibuat untuk membantu progammer dalam membangun proyek dengan fitur out-of-the-box yang dimana dapat membantu pengembang membangun aplikasi yang kuat dan lebih sedikit kode dan waktu pengerjaan. Django juga memiliki komunitas yang besar dan aktif dimana kita dapat menemukan sumber daya pembelajaran, dokumentasi, dan dukungan dari pengguna-pengguna Django.
</div>


## Mengapa model pada Django disebut sebagai ORM?

<div style="text-align: justify">
    Dengan django memungkinkan progammer dapat mengakses database menggunakan objek Python, itu membuat Django dapat disebut dengan ORM. Dalam Django mode adalah representasi dari tabel dalam basis data dan setiap model tersebut tertulis sebagai kelas Python. ORM ini memungkinkan pengembang untuk melakukan operasi Create, Read, Update, Delete pada data di database dengan menggunakan bahasa pemrograman Python.Dengan ORM  membuat pengelolaan database menjadi lebih intuitif dan terintegrasi langsung dengan kode, tanpa perlu menulis SQL manual. Dengan alasan itulah mengapa Django dapat disebut sebagai ORM.
</div>
