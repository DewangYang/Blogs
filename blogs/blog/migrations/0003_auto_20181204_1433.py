# Generated by Django 2.1.1 on 2018-12-04 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181130_1220'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time']},
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
