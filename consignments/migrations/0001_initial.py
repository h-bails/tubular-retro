# Generated by Django 3.2.20 on 2023-09-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(max_length=1000)),
                ('date_submitted', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('1', 'Submitted'), ('2', 'Approved'), ('3', 'Declined')], default='1', max_length=20)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'ordering': ['-date_submitted'],
            },
        ),
    ]