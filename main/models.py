from django.db import models
from django.contrib.auth.models import User
import uuid

class ProductEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    # Perubahan: Menambahkan field 'image' untuk menyimpan gambar produk
    # Sekarang: Menambahkan ImageField dengan opsi upload_to, blank, dan null
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

