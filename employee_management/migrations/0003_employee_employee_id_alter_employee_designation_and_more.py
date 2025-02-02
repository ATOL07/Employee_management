# Generated by Django 5.1.1 on 2024-09-13 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management', '0002_remove_employee_employee_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(default=0, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
