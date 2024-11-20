# Generated by Django 3.1.1 on 2024-10-15 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='Facility',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='app.facility'),
        ),
    ]