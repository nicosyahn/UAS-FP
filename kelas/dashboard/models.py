from django.db import models

# Create your models here.

class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kodebrg=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.CharField(max_length=50)
    link_gbr=models.CharField(max_length=150, blank=True, default="img/Toodlers#.jpg")
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)

class Level(models.Model):
    level=models.IntegerField()
    bonus=models.TextField()

    def __str__(self):
        return "{}. {}".format(self.level, self.bonus)

class Status(models.Model):
    status=models.TextField()

    def __str__(self):
        return self.status

class Membership(models.Model):
    kodemem=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    status=models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    waktu_posting=models.DateTimeField(auto_now_add=True)
    level_id=models.ForeignKey(Level, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{}. {}. {}".format(self.kodemem, self.nama, self.status)

    def __str__(self):
        return "{}. {}. {}".format(self.kodebrg, self.nama, self.harga)

class Transaksi(models.Model):
    kodetrans=models.CharField(max_length=10)
    tgltrans=models.DateTimeField(auto_now_add=True)
    total=models.BigIntegerField()

    def __str__(self):
        return self.kodetrans

class Detailtrans(models.Model):
    kodetrans=models.CharField(max_length=10)
    kodebrg=models.CharField(max_length=8)
    qty=models.IntegerField()
    subtotal=models.BigIntegerField()
    
    def __str__(self):
        return "{}. {}".format(self.kodetrans, self.kodebrg)