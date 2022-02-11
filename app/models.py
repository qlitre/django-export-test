from django.db import models


class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=12)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('タイトル', max_length=32)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
