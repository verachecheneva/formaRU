from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import EmailValidator


class Application(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя заказчика')
    email = models.EmailField(error_messages={'invalid': 'Введите правильный адрес электронной почты',
                                              'required': 'Заполните поле, иначе мы не сможем с вами связаться'})
    phone_number = PhoneNumberField(error_messages={'invalid': 'Номер телефона указан неверно. Пример: +79999999999',
                                                    'required': 'Заполните поле, иначе мы не сможем с вами связаться'})
    creation = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание проекта', help_text='Полное описание проекта')
    customer = models.CharField(max_length=100, verbose_name='Заказчик')
    main_image = models.ImageField(upload_to='posts/', help_text='Первая картинка проекта', null=False)
    image_1 = models.ImageField(upload_to='posts/', help_text='Первая картинка проекта', null=False, default=0)
    image_2 = models.ImageField(upload_to='posts/', help_text='Вторая картинка проекта', null=False, default=0)
    image_3 = models.ImageField(upload_to='posts/', help_text='Третья картинка проекта', null=False)

    def __str__(self):
        return self.title
