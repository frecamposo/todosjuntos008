# Generated by Django 4.1.5 on 2023-05-09 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webPerris', '0004_categoria_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='comentario',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mascota',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='idMascota',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('idFoto', models.AutoField(primary_key=True, serialize=False)),
                ('foto', models.ImageField(null=True, upload_to='galeria')),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webPerris.mascota')),
            ],
        ),
    ]