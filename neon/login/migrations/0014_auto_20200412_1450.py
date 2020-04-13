# Generated by Django 2.2.11 on 2020-04-12 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_exam_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='exam_id',
        ),
        migrations.RemoveField(
            model_name='internalresult',
            name='result_id',
        ),
        migrations.RemoveField(
            model_name='regularresult',
            name='result_id',
        ),
        migrations.AddField(
            model_name='exam',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='internalresult',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regularresult',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
