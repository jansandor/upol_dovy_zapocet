# Generated by Django 3.1.6 on 2021-02-06 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veterinary_clinic', '0002_auto_20210205_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='jméno')),
                ('description', models.TextField(verbose_name='popis')),
            ],
        ),
        migrations.AlterField(
            model_name='examination',
            name='diagnosis',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='veterinary_clinic.diagnosis', verbose_name='diagnóza'),
        ),
    ]
