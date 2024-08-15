from django.db import models


class EducationModules(models.Model):
    number = models.IntegerField(unique=True, db_index=True, verbose_name='Номер модуля')
    name = models.CharField(max_length=30, unique=True, db_index=True, verbose_name='Название модуля')
    description = models.TextField(verbose_name='Описание модуля')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'
        ordering = ['number',]
