# Generated by Django 3.0.5 on 2020-05-18 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0011_auto_20200517_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='logo',
            field=models.ImageField(default='default.png', upload_to='logos'),
        ),
    ]