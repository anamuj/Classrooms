# Generated by Django 2.1.5 on 2019-02-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20190212_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='exam_grade',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=40),
        ),
    ]
