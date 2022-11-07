# Generated by Django 4.1.2 on 2022-10-30 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_coment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='coment',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.comment'),
        ),
    ]