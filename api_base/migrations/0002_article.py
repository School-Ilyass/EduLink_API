# Generated by Django 5.0.6 on 2024-06-29 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('Ref', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=40)),
                ('Link', models.CharField(max_length=40)),
                ('Image', models.CharField(max_length=400)),
                ('Theme', models.CharField(max_length=40)),
                ('JournalID', models.CharField(max_length=40)),
            ],
        ),
    ]
