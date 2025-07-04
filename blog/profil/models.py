from django.db import models
from django.core.exceptions import ValidationError

#Jenis
class Jenis(models.Model):
    nama = models.CharField(max_length=50)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama

#Barang
class Barang(models.Model):
    kdbrg = models.CharField(max_length=8)
    nama = models.CharField(max_length=75)
    stok = models.IntegerField()
    harga = models.BigIntegerField()
    link_gbr = models.CharField(max_length=150, blank=True)
    waktu_post = models.DateTimeField(auto_now_add=True)
    jenis = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama

#Portfolio
class Portofolio(models.Model):
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='portofolio/', blank=True, null=True)
    link_sumber = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.judul
    
#Hero 
class Hero(models.Model):
    judul = models.CharField(max_length=100)
    subjudul = models.CharField(max_length=100, default='Subjudul')
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='hero/', blank=True, null=True)

    def __str__(self):
        return self.judul

#About
class About(models.Model):
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField()
    instagram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.judul