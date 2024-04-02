from django.db import models


class TimeStampedModel(models.Model):
    """
    Bazaviy model bo'lishi uchun TimeStampedModel yaratildi.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Abstract=True yaratilishini maqsadi ma'lumotlar ba'zasida model yaratilmasligini taminlaydi.
        """
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_img/')
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.name
