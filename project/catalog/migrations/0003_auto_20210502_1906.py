# Generated by Django 3.2 on 2021-05-02 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210502_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('discount', models.CharField(blank=True, choices=[('', 'ללא הנחה'), ('/static/assets/catalog/imgs/discount_10.gif', '10% הנחה'), ('/static/assets/catalog/imgs/discount_20.gif', '20% הנחה')], default='', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumImageThrough',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_order', models.PositiveIntegerField(default=0)),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.catalogalbum')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.catalogimage')),
            ],
            options={
                'ordering': ('my_order',),
            },
        ),
        migrations.AddField(
            model_name='catalogalbum',
            name='images',
            field=models.ManyToManyField(through='catalog.AlbumImageThrough', to='catalog.CatalogImage'),
        ),
    ]