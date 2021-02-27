from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Application(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя заказчика')
    email = models.EmailField(max_length=70)
    phone_number = PhoneNumberField(blank=True, null=True)
    creation = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание проекта', help_text='Полное описание проекта')
    image_1 = models.ImageField(upload_to='posts/', help_text='Заглавная картинка проекта', null=False, default=0)
    image_2 = models.ImageField(upload_to='posts/', help_text='Вторая картинка проекта', null=False, default=0)
    image_3 = models.ImageField(upload_to='posts/', help_text='Третья картинка проекта', null=False)

    def __str__(self):
        return self.title
