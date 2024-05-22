from django.db import models
from users.models import CustomUser, AbstractUser


class Requirements(models.Model):
    requirements_parts_uz = models.CharField(max_length=100)
    requirements_parts_en = models.CharField(max_length=100)
    requirements_title_uz = models.TextField()
    requirements_title_en = models.TextField()
    requirements_description_uz = models.TextField()
    requirements_description_en = models.TextField()
    # connection = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.requirements_parts_uz

    class Meta:
        verbose_name = 'Requirement'
        verbose_name_plural = 'Requirements'
        db_table = 'requirements'


class FAQ(models.Model):
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)

    def __str__(self):
        return self.question


class Contacts(models.Model):
    first_name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ('first_name',)
        verbose_name_plural = 'Contacts'
        verbose_name = 'Contact'


class JournalMain(models.Model):
    edition_logo = models.ImageField(upload_to='images_journal/')
    description = models.TextField()


class PaperMain(models.Model):
    title = models.CharField(max_length=250)
    edition_logo = models.ImageField(upload_to='images_journal/', null=True)
    description = models.TextField()
    contact = models.ForeignKey(JournalMain, on_delete=models.CASCADE)


class Paper(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Link to the user
    field_name = models.CharField(max_length=150)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=120)
    year = models.IntegerField()
    number_views = models.IntegerField()
    description = models.TextField()
    references = models.TextField()
    keywords = models.TextField()
    file = models.FileField(upload_to='media/files_journal/', null=True)

    def __str__(self):
        return f"{self.field_name} | {self.title} "

    class Meta:
        verbose_name_plural = 'Papers'
        db_table = 'paper'


class Publication(models.Model):
    journal_name_uz = models.CharField(max_length=250)
    journal_name_en = models.CharField(max_length=250)
    journal_description_uz = models.CharField(max_length=500)
    journal_description_en = models.CharField(max_length=500)
    journal_file = models.FileField(upload_to='media/files_journal/', null=True)
    journal_avatar = models.ImageField(upload_to='media/images_files/')
    paper = models.ForeignKey(Paper, related_name='publications', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.journal_name_uz} | {self.journal_description_uz}"

    class Meta:
        verbose_name_plural = 'Publications'
        db_table = 'publications'






# class Main(models.Model):
#     title = models.CharField(max_length=250)
#     etion_logo = models.ImageField(upload_to='images_journal/')
#     description = models.TextField()
#     number_views = models.IntegerField(default=0)
#     data_time = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.title



