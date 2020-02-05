# Generated by Django 3.0.2 on 2020-02-04 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0003_contractor_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.IntegerField(blank='True', null='True')),
                ('nid', models.CharField(max_length=200)),
                ('salary', models.IntegerField(blank='True', null='True')),
                ('grade', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
