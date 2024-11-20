# Generated by Django 3.1.1 on 2024-10-15 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20241015_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='app.hospital')),
            ],
        ),
    ]
