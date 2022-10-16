from django.contrib.auth import get_user_model
from django.core.validators import (MinValueValidator, MaxValueValidator,
                                    RegexValidator)
from django.db import models
from django.db.models import UniqueConstraint

User = get_user_model()


class Ingredient(models.Model):
    """Модель ингредиента"""
    name = models.CharField(
        verbose_name='Ингридиент',
        max_length=200,
        db_index=True
    )
    measurement_unit = models.CharField(
        verbose_name='Единицы измерения',
        max_length=200
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Tag(models.Model):
    """Модель тега"""
    name = models.CharField(
        verbose_name='Тег',
        max_length=50,
        unique=True
    )
    color = models.CharField(
        verbose_name='Цвет в HEX',
        max_length=7,
        unique=True,
        validators=[
            RegexValidator(
                regex="#[A-Fa-f0-9]{6}",
                message='Укажите значение в HEX формате!',
                code='invalid_color'
            )
        ]
    )
    slug = models.SlugField(
        verbose_name='Slug',
        max_length=50,
        unique=True
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Модель рецепта"""
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        db_index=True
    )
    author = models.ForeignKey(
        User,
        related_name='recipes',
        verbose_name='Автор рецепта',
        on_delete=models.CASCADE,
        null=True
    )
    text = models.TextField(
        verbose_name='Описание рецепта'
    )
    image = models.ImageField(
        verbose_name='Изображение рецепта',
        upload_to='recipes/'
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления',
        validators=[
            MinValueValidator(1, message='Минимальное значение 1'),
            MaxValueValidator(600, message='Максимальное значение 600')
        ]
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientInRecipe',
        related_name='recipes',
        verbose_name='Ингредиенты'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Теги'
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-id',)

    def __str__(self):
        return self.name


class IngredientInRecipe(models.Model):
    """Модель ингредиентов в рецепте"""
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredient_list',
        verbose_name='Рецепт',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент в рецепте',
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        validators=[
            MinValueValidator(1, message='Минимальное количество 1'),
            MaxValueValidator(100, message='Максимальное значение 2000')
        ]
    )

    class Meta:
        verbose_name = 'Количество ингридиента'
        verbose_name_plural = 'Количество ингридиентов'

    def __str__(self):
        return (
            f'{self.ingredient.name} ({self.ingredient.measurement_unit})'
            f' - {self.amount} '
        )


class Favourite(models.Model):
    """Модель избранного"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Рецепт',
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        constraints = [
            UniqueConstraint(fields=['user', 'recipe'],
                             name='unique_favourite')
        ]

    def __str__(self):
        return f'{self.user} добавил "{self.recipe}" в Избранное'


class ShoppingCart(models.Model):
    """Модель списка покупок"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Рецепт',
    )

    class Meta:
        verbose_name = 'Корзина покупок'
        verbose_name_plural = 'Корзина покупок'
        constraints = [
            UniqueConstraint(fields=['user', 'recipe'],
                             name='unique_shopping_cart')
        ]

    def __str__(self):
        return f'{self.user} добавил "{self.recipe}" в Корзину покупок'
