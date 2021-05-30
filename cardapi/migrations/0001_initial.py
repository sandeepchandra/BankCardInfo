# Generated by Django 3.2.3 on 2021-05-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('brand', models.CharField(max_length=10)),
                ('prepaid', models.BooleanField()),
                ('country', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]
