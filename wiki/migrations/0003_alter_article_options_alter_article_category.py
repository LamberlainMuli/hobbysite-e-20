# Generated by Django 5.0.3 on 2024-03-20 09:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['updated_on']},
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Category', to='wiki.articlecategory'),
        ),
    ]
