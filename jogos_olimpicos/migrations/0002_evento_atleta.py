# Generated by Django 3.2.12 on 2022-03-30 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jogos_olimpicos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='atleta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jogos_olimpicos.atleta'),
            preserve_default=False,
        ),
    ]
