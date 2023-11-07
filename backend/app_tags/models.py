from django.db import models


class Tags(models.Model):
    name_tag = models.CharField(
        verbose_name='Название тега', max_length=150, unique=True
    )
    desc_tag = models.TextField(
        verbose_name='Описание тега', max_length=1500, blank=True
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


    def __str__(self) -> str:
        return self.name_tag
    