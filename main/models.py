from django.db import models
from django.utils.translation import gettext_lazy as _
from car.minixs import TranslateMixin



class New(TranslateMixin, models.Model):
    translate_attributes = ['subject', 'content']
    subject_uz = models.CharField(max_length=100,verbose_name=_("Nomi(uz)"))
    subject_ru = models.CharField(max_length=100,verbose_name=_("Nomi(ru)"))
    content_uz = models.TextField(verbose_name=_("Informatsiya (uz)"))
    content_ru = models.TextField(verbose_name=_("Informatsiya (ru)"))
    read = models.IntegerField(default=0)
    image = models.ImageField(verbose_name="Rasm")
