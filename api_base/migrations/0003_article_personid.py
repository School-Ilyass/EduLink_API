# Generated by Django 5.0.6 on 2024-06-29 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_base', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='PersonID',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
    ]
