# Generated by Django 3.2.20 on 2023-08-16 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('description', models.TextField(max_length=1000)),
                ('measurements', models.CharField(max_length=254)),
                ('condition', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sku', models.CharField(max_length=254)),
                ('date_added', models.DateField(auto_now=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_1_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_2_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]