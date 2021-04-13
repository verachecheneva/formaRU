# Generated by Django 3.1.7 on 2021-03-28 09:12

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя заказчика')),
                ('email', models.EmailField(error_messages={'invalid': 'Введите правильный адрес электронной почты', 'required': 'Заполните поле, иначе мы не сможем с вами связаться'}, max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(error_messages={'invalid': 'Номер телефона указан неверно. Пример: +79999999999', 'required': 'Заполните поле, иначе мы не сможем с вами связаться'}, max_length=128, region=None)),
                ('creation', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Телефон компании', max_length=128, region=None)),
                ('email', models.EmailField(help_text='Почта компании', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('num', models.IntegerField(blank=True, help_text='Номер вопроса на странице', null=True, unique=True)),
            ],
            options={
                'ordering': ('num',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='tags')),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_project', models.SlugField(max_length=20, unique=True)),
                ('title', models.CharField(max_length=100, verbose_name='Название проекта')),
                ('description', models.TextField(help_text='Полное описание проекта', verbose_name='Описание проекта')),
                ('customer', models.CharField(max_length=100, verbose_name='Заказчик')),
                ('main_image', models.ImageField(help_text='Первая картинка проекта', upload_to='posts/')),
                ('num', models.IntegerField(blank=True, help_text='Номер проекта на странице', null=True, unique=True)),
                ('tag', models.ManyToManyField(related_name='projects', to='content.Tag')),
            ],
            options={
                'ordering': ('num',),
            },
        ),
        migrations.CreateModel(
            name='ImageProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Другие картинки проекта', upload_to='posts/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='content.project')),
            ],
        ),
    ]
