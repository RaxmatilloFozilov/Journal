from django.db import models
from users.models import CustomUser, AbstractUser
from app_journal.models import Paper
from django.contrib.auth import get_user_model


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        abstract = True
        db_table = 'abstract_model'


class Requirements(AbstractBaseModel):
    connection = models.ForeignKey(Paper, on_delete=models.CASCADE)
    requirements_parts_uz = models.CharField(max_length=100)
    requirements_parts_en = models.CharField(max_length=100)
    requirements_title_uz = models.TextField()
    requirements_title_en = models.TextField()
    requirements_description_uz = models.TextField()
    requirements_description_en = models.TextField()

    def __str__(self):
        return self.requirements_parts_uz

    class Meta:
        verbose_name = 'Requirement'
        verbose_name_plural = 'Requirements'
        db_table = 'requirements'


class Category(AbstractBaseModel):
    connection = models.ForeignKey(Paper, on_delete=models.CASCADE)
    category = models.CharField(max_length=250)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'categories'


