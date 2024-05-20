from django.db import models


class Requirements(models.Model):
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
        db_table = 'Requirements'


class FAQ(models.Model):
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)

    def __str__(self):
        return self.question


class Contacts(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ('first_name',)
        verbose_name_plural = 'Contacts'
        verbose_name = 'Contact'



