from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Recipe(models.Model):
    name = models.CharField("Название", max_length=50, unique=True)
    description = models.TextField("Описание", blank=True, null=True)
    rating = models.IntegerField('Рейтинг', validators=[MinValueValidator(0), MaxValueValidator(5)])
    image = models.ImageField('Изображение', upload_to='img/recipes/', height_field=None, width_field=None, max_length=None, blank=True)
    created = models.DateTimeField("Создан", auto_now_add=True)
    modified = models.DateTimeField("Обновлён", auto_now=True)

    def __str__(self) -> str:
        return self.name


    def get_absolute_url(self):
        return reverse("recipe-details", kwargs={'pk': self.pk})
    


    class Meta:
        verbose_name='Рецепт'
        verbose_name_plural='Рецепты'
