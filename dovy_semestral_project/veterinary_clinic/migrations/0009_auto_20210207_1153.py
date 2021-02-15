# Generated by Django 3.1.6 on 2021-02-07 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veterinary_clinic', '0008_auto_20210207_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='diagnosis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='veterinary_clinic.diagnosis', verbose_name='diagnóza'),
        ),
    ]
