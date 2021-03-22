# Generated by Django 3.1.7 on 2021-03-10 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('number', models.BigIntegerField()),
                ('address', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('idc', models.BooleanField(default=False)),
            ],
        ),
    ]