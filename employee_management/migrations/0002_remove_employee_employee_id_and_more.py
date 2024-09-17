# Generated by Django 5.1.1 on 2024-09-13 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10),
        ),
    ]
