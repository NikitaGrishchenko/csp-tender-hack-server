# Generated by Django 3.2.9 on 2021-11-26 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('priority', models.CharField(choices=[('low', 'Низкий приоритет'), ('middle', 'Средний приоритет'), ('high', 'Высокий приоритет')], max_length=50, verbose_name='Приоритет')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_version', models.IntegerField(verbose_name='Номер версии уведомления')),
                ('desc_version', models.CharField(max_length=150, verbose_name='Описание отличия версии')),
                ('text', models.CharField(max_length=350, null=True, verbose_name='Основной текст')),
                ('img', models.ImageField(blank=True, null=True, upload_to='notice-img', verbose_name='Картинка')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notice.event', verbose_name='Событие')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления',
            },
        ),
        migrations.CreateModel(
            name='SendNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_send', models.DateField(default=django.utils.timezone.now, verbose_name='Дата отправки')),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notice.notice', verbose_name='Отпарвленное уведомление')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Отправка уведомления',
                'verbose_name_plural': 'Отправка уведомления',
            },
        ),
    ]
