# Generated by Django 5.0.3 on 2024-05-06 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_article_header_image_article_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='entry',
            field=models.TextField(max_length=255),
        ),
    ]