# Generated by Django 4.0.4 on 2022-05-29 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0003_persona_altura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
    ]
