# Generated by Django 2.2 on 2019-05-03 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190503_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='item',
            field=models.CharField(max_length=100),
        ),
    ]
