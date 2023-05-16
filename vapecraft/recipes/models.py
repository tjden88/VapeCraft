from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
import os, uuid

def get_file_path(instance, filename):
    """Получить уникальное имя изображения
    Returns:
        str: имя к файлу
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(instance.img_path, filename)


class Recipe(models.Model):
    name = models.CharField("Название", max_length=50, unique=True)
    description = models.TextField("Описание", blank=True, null=True)
    rating = models.IntegerField('Рейтинг', validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    image = models.ImageField('Изображение', upload_to=get_file_path, height_field=None, width_field=None, max_length=None, blank=True)
    created = models.DateTimeField("Создан", auto_now_add=True)
    modified = models.DateTimeField("Обновлён", auto_now=True)
    img_path = 'img/recipes/'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("recipe-details", kwargs={'pk': self.pk})

    class Meta:
        verbose_name='Рецепт'
        verbose_name_plural='Рецепты'
        
        
