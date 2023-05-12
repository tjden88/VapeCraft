from django.db import models

class Recipe(models.Model):
    name = models.CharField("Название", max_length=50, unique=True)
    description = models.TextField("Описание", blank=True, null=True)
    rating = models.IntegerField('Рейтинг')
    image = models.ImageField('Изображение', upload_to='img/recipes/', height_field=None, width_field=None, max_length=None)

    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name='Рецепт'
        verbose_name_plural='Рецепты'
