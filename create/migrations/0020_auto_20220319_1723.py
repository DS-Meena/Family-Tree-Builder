# Generated by Django 3.0.6 on 2022-03-19 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0019_auto_20220319_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='user',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
