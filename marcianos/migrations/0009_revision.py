# Generated by Django 3.1.3 on 2020-12-18 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marcianos', '0008_auto_20201213_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_revisor', models.CharField(max_length=400)),
                ('num_pasajeros', models.IntegerField()),
                ('fecha_revision', models.DateField()),
                ('aeronave_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revisa_a', to='marcianos.aeronave')),
            ],
        ),
    ]
