# Generated by Django 4.1.2 on 2022-10-29 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_books', '0003_alter_book_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]
