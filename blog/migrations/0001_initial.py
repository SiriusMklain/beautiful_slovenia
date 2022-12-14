# Generated by Django 4.1.4 on 2022-12-11 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.FileField(upload_to='image')),
                ('location_image', models.CharField(choices=[('right', 'Справа'), ('left', 'Слева')], max_length=250, verbose_name='Положение фото')),
                ('location_text', models.CharField(choices=[('right', 'Справа'), ('left', 'Слева')], max_length=250, verbose_name='Положение текста')),
                ('status_article', models.CharField(choices=[('active', 'Активен'), ('dont_active', 'Не активен')], max_length=250, verbose_name='Активно/Не активно')),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
            },
        ),
    ]
