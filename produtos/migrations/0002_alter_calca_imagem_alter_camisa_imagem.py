# Generated by Django 5.1.7 on 2025-03-26 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calca',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='media/calca1'),
        ),
        migrations.AlterField(
            model_name='camisa',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='media/camisa1'),
        ),
    ]
