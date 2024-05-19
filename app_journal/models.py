from django.db import models


class Requirements(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Requirements'
        verbose_name = 'Requirement'


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



