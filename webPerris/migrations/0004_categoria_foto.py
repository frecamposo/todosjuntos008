# Generated by Django 4.1.5 on 2023-05-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webPerris', '0003_alter_mascota_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='foto',
            field=models.ImageField(null=True, upload_to='fotos'),
        ),
    ]
