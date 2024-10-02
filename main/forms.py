from django.forms import ModelForm
from main.models import ProductEntry

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["name", "description", "price", 'image']
        # Perubahan: Menambahkan field 'image' ke dalam daftar fields