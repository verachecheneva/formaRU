from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CompanyData(models.Model):
    phone_number = PhoneNumberField(help_text='Телефон компании')
    email = models.EmailField(help_text='Почта компании')


class Application(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя заказчика')
    email = models.EmailField(error_messages={'invalid': 'Введите правильный адрес электронной почты',
                                              'required': 'Заполните поле, иначе мы не сможем с вами связаться'})
    phone_number = PhoneNumberField(error_messages={'invalid': 'Номер телефона указан неверно. Пример: +79999999999',
                                                    'required': 'Заполните поле, иначе мы не сможем с вами связаться'})
    creation = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name='tags')
    slug = models.SlugField(max_length=20, unique=True)


class Project(models.Model):
    slug_project = models.SlugField(max_length=20, unique=True)
    title = models.CharField(max_length=100, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание проекта', help_text='Полное описание проекта')
    customer = models.CharField(max_length=100, verbose_name='Заказчик')
    main_image = models.ImageField(upload_to='posts/', help_text='Первая картинка проекта', null=False)
    image_1 = models.ImageField(upload_to='posts/', help_text='Первая картинка проекта', null=False, default=0)
    image_2 = models.ImageField(upload_to='posts/', help_text='Вторая картинка проекта', null=False, default=0)
    image_3 = models.ImageField(upload_to='posts/', help_text='Третья картинка проекта', null=False)
    tag = models.ManyToManyField(Tag, related_name='projects')
    num = models.IntegerField(unique=True, null=True, blank=True, help_text='Номер проекта на странице')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('num', )


class Questions(models.Model):
    question = models.TextField(blank=False, null=False)
    answer = models.TextField(blank=False, null=False)
    num = models.IntegerField(unique=True, null=True, blank=True, help_text='Номер вопроса на странице')

    class Meta:
        ordering = ('num',)
