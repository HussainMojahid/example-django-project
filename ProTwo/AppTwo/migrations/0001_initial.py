# Generated by Django 3.2.4 on 2021-06-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=70)),
                ('lname', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
            ],
        ),
    ]
