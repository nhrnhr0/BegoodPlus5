# Generated by Django 3.2 on 2021-05-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalogalbum',
            options={'ordering': ['my_order']},
        ),
        migrations.RemoveField(
            model_name='catalogalbum',
            name='order',
        ),
        migrations.AddField(
            model_name='catalogalbum',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
