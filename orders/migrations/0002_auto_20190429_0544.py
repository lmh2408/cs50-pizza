# Generated by Django 2.2 on 2019-04-28 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner_platter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dinner_platter', models.CharField(max_length=50)),
                ('small_price', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('large_price', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pasta', models.CharField(max_length=50)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small_price', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('large_price', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza_topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_topping', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza_topping_number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_topping_number', models.CharField(max_length=50)),
                ('topping_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pizza_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salad', models.CharField(max_length=50)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=50)),
                ('small_price', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('large_price', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_extra', models.CharField(max_length=50)),
                ('small_price', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('large_price', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Dinner_platters',
        ),
        migrations.DeleteModel(
            name='Pastas',
        ),
        migrations.RemoveField(
            model_name='pizza_listing',
            name='pizza_sub_type',
        ),
        migrations.RemoveField(
            model_name='pizza_listing',
            name='pizza_type',
        ),
        migrations.DeleteModel(
            name='Salads',
        ),
        migrations.DeleteModel(
            name='Sub_extras',
        ),
        migrations.DeleteModel(
            name='Subs',
        ),
        migrations.DeleteModel(
            name='Toppings',
        ),
        migrations.DeleteModel(
            name='Pizza_listing',
        ),
        migrations.DeleteModel(
            name='Pizza_sub_types',
        ),
        migrations.DeleteModel(
            name='Pizza_types',
        ),
        migrations.AddField(
            model_name='pizza',
            name='pizza_topping_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza_topping_number'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='pizza_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza_type'),
        ),
    ]
