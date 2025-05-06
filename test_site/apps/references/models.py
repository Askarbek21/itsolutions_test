from django.db import models


#Абстрактный класс для наследования
class Base(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Название')

    class Meta:
        abstract = True 

    def __str__(self):
        return self.name 


class Status(Base):
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Type(Base):
    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы' 


class Category(Base):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories', verbose_name='Тип') 

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(Base):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', verbose_name='Категория')

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'