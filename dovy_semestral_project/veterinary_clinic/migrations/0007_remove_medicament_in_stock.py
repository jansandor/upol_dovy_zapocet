# Generated by Django 3.1.6 on 2021-02-06 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veterinary_clinic', '0006_auto_20210206_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicament',
            name='in_stock',
        ),
    ]