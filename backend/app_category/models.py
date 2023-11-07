from django.db import models


class Category(models.Model):
    name_category = models.CharField(verbose_name='Наименование категории', max_length=150, unique=True)
    desc_category = models.TextField(verbose_name='Описание категории', max_length=1000, blank=True)
    # 
    # 
    # какие еще поля могут быть полезны в модели категории?
    # 
    # 
    # 

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name_category
    