from django.db import models

from apps.references.models import Status, Type, Category, SubCategory


class Record(models.Model):
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, verbose_name='Статус')
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, verbose_name='Тип')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    subcategory = models.ManyToManyField(SubCategory, verbose_name='Подкатегории')
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Сумма')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')
    
    def __str__(self):
        return f'{self.created_at.strftime("%d.%m.%Y %H:%M")} | {self.amount} руб | {self.status.name}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'