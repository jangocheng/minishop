# Generated by Django 2.0.6 on 2018-07-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jielong',
            options={'verbose_name': '接龙表', 'verbose_name_plural': '接龙表'},
        ),
        migrations.AddField(
            model_name='jielong',
            name='display_order',
            field=models.IntegerField(default=1, help_text='值越大越靠前', verbose_name='显示排序'),
        ),
    ]
