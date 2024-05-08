# Generated by Django 5.0.2 on 2024-05-06 18:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commission',
            name='people_required',
        ),
        migrations.AddField(
            model_name='commission',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commission',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Full', 'Full'), ('Completed', 'Completed'), ('Discontinued', 'Discontinued')], default='Open', max_length=20),
        ),
        migrations.AlterField(
            model_name='commission',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('manpower_required', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Full', 'Full')], default='Open', max_length=10)),
                ('commission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='commissions.commission')),
            ],
            options={
                'ordering': ['status', '-manpower_required', 'role'],
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='commissions.job')),
            ],
            options={
                'ordering': ['status', '-applied_on'],
            },
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
