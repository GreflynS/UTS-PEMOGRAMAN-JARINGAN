# UTS-PEMOGRAMAN-JARINGAN

# SOAL

Buatlah sebuah permainan yang menggunakan soket dan protokol UDP. Permainannya cukup sederhana, dengan 1 server dapat melayani banyak klien (one-to-many). Setiap 10 detik, server akan mengirimkan kata warna acak dalam bahasa Inggris kepada semua klien yang terhubung. Setiap klien harus menerima kata yang berbeda (unik). Selanjutnya, klien memiliki waktu 5 detik untuk merespons dengan kata warna dalam bahasa Indonesia. Setelah itu, server akan memberikan nilai feedback 0 jika jawabannya salah dan 100 jika benar.


syarat UTS :
1. Kerjakan dengan menggunakan bahasa pemrograman python
2. Menggunakan protokol UDP
3. Code untuk server dan client dikumpulkan di github repository masing masing
4. Pada readme.md silahkan beri penjelaskan how code works. 
5. Pada readme.md silahkan beri screenshoot cara penggunaaan serta contoh ketika program berjalan
6. Test case : 1 server 10 client.
7. Pastikan memahami soal.
8. Silahkan kumpulkan link github repository di assignment ini.
   *--- JANGAN TELAT ! ---*
   
# PENJELASAN CODINGAN

# 1. Server
![image](https://github.com/GreflynS/UTS-PEMOGRAMAN-JARINGAN/assets/163794459/902e3ce9-609b-49c7-9c2c-00f08271e763)


Ada 4 import yang dipakai ;

import socket: Mengimpor modul socket yang menyediakan antarmuka untuk berkomunikasi dengan soket.

import random: Mengimpor modul random yang menyediakan fungsi untuk melakukan operasi acak.

import threading : Menyediakan fasilitas untuk bekerja dengan thread dalam Python. Dengan modul ini, Anda dapat membuat, mengelola, dan berinteraksi dengan thread dalam program Python, memungkinkan program untuk melakukan tugas-tugas secara paralel

