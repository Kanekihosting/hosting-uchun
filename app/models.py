from datetime import datetime

from django.db import models
from django.urls import reverse


# Create your models here.



class Hamkorlar(models.Model):
    hamkor_nomi = models.CharField(max_length=50)

    def __str__(self):
        return self.hamkor_nomi
class Visa(models.Model):
    visa_turi = models.CharField(max_length=10)
    visa_narxi = models.DecimalField(decimal_places=1, max_digits=10)

    def __str__(self):
        return self.visa_turi


class Dokument(models.Model):
    xujjat_nomi = models.CharField(max_length=100)
    slug = models.SlugField(max_length=300)
    turistlar_soni = models.DecimalField(max_digits=6, decimal_places=0)
    hamkor = models.ForeignKey(Hamkorlar, on_delete=models.CASCADE)
    visa = models.ForeignKey(Visa, on_delete=models.CASCADE)
    yaratilgan_vaqti = models.DateTimeField(default=datetime.today)

    class Meta:
        ordering = ["-yaratilgan_vaqti"]

    def __str__(self):
        return self.xujjat_nomi

    # def get_absolute_url(self):
    #     return reverse("doc_detail_page", args=[self.slug])




