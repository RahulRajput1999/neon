# Generated by Django 2.2.11 on 2020-04-12 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20200411_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internalresult',
            name='sess1_att',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='internalresult',
            name='sess2_att',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='internalresult',
            name='sess3_att',
            field=models.CharField(max_length=10),
        ),
    ]
