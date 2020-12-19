# Generated by Django 3.1.3 on 2020-12-19 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marcianos', '0012_remove_aeronave_marcianos_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasajero',
            name='aeronave_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subido_en', to='marcianos.aeronave'),
        ),
    ]
