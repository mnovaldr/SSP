---

```markdown
# 🌐 Web Portofolio - Muhammad Noval Dwi Ramadhani

Ini adalah proyek web portofolio yang dibuat menggunakan Django sebagai tugas Ujian Tengah Semester (UTS) pada mata kuliah Pemrograman Web Lanjut. Website ini menampilkan informasi pribadi, karya-karya portofolio, serta tautan media sosial.

---

## 📌 Deskripsi Singkat

Website ini dibuat oleh mahasiswa yang menyukai kucing dan memiliki minat besar di dunia teknologi, terutama dalam pengembangan web. Proyek ini bertujuan untuk menampilkan informasi tentang diri pembuat dan beberapa proyek yang pernah dikerjakan selama belajar.

---

## 🛠️ Teknologi yang Digunakan

- Python 3.x
- Django 4.x
- HTML5 & CSS3
- Font Awesome (untuk ikon)
- Template Django
- File statis (gambar & CSS)

---

## 🗂️ Struktur Folder

```

portfolio/
├── manage.py
├── portfolio/         # Folder konfigurasi Django
│   ├── settings.py
│   ├── urls.py
├── website/           # Aplikasi utama
│   ├── static/        # File gambar, CSS, ikon
│   ├── templates/     # File HTML
│   ├── views.py
│   └── urls.py
├── db.sqlite3
└── README.md

````

---

## 🚀 Cara Menjalankan Proyek

1. **Clone repositori atau download kode:**
   ```bash
   git clone https://github.com/username/portfolio.git
   cd portfolio
````

2. **Aktifkan virtual environment (opsional tapi disarankan):**

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # Linux/macOS
   myenv\Scripts\activate     # Windows
   ```

3. **Install dependency:**

   ```bash
   pip install django
   ```

4. **Jalankan server Django:**

   ```bash
   python manage.py runserver
   ```

5. **Buka browser dan akses:**

   ```
   http://127.0.0.1:8000/
   ```

---

## 📄 Fitur Website

* **Halaman Utama (Hero)**: Menampilkan perkenalan diri dan foto.
* **About Me**: Informasi singkat tentang latar belakang, hobi, dan minat.
* **Portofolio**: Daftar proyek yang pernah dibuat, termasuk:

  * E-commerce Mama Frozen
  * Aplikasi restoran berbasis web
  * Aplikasi kalkulator menggunakan Flutter
* **Footer**: Tautan media sosial dan informasi kontak.

---

## 📱 Responsif

Website ini mendukung tampilan di berbagai ukuran layar (mobile-friendly). Elemen akan menyesuaikan secara otomatis untuk pengalaman pengguna yang lebih baik.

---

## 👨‍🎓 Profil Pembuat

* **Nama**: Muhammad Noval Dwi Ramadhani
* **NIM**: 23201188
* **Kelas**: C2
* **Hobi**: Menjelajah teknologi, bermain dengan kucing
* **Fokus**: Sistem Cerdas

---

## 📬 Kontak

* 📧 Email: [mnovaldr@gmail.com](mailto:mnovaldr@gmail.com)
* 💻 GitHub: [https://github.com/mnovaldr](https://github.com/mnovaldr)
* 📸 Instagram: [@mnvldr\_](https://instagram.com/mnvldr_)
* 💼 LinkedIn: \[Coming Soon]

---

## 📚 Lisensi

Proyek ini dibuat hanya untuk keperluan pembelajaran dan tugas UTS. Bebas digunakan kembali dengan atribusi yang sesuai.

