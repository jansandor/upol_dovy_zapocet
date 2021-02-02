# Generated by Django 3.1.5 on 2021-02-01 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veterinary_clinic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='medicaments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='veterinary_clinic.medicament', verbose_name='podané léky'),
        ),
    ]
