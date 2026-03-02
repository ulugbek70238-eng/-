from django.db import models

class Category(models.Model):
    name_category = models.CharField(max_length=32, verbose_name='Название категории')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name_category

class Theme(models.Model):
    name_theme = models.CharField(max_length=32, verbose_name='Название статьи')
    theme_dec = models.TextField(max_length=256, verbose_name="Описание статьи")
    theme_photo = models.ImageField(upload_to='media', verbose_name="Фото статьи")
    theme_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name_theme