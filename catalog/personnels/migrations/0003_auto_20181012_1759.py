# Generated by Django 2.1.2 on 2018-10-12 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personnels', '0002_auto_20181012_1309'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.AlterModelOptions(
            name='personnel',
            options={'verbose_name': 'personnel', 'verbose_name_plural': 'personnels'},
        ),
        migrations.RemoveField(
            model_name='personnel',
            name='personnel_permissions',
        ),
    ]