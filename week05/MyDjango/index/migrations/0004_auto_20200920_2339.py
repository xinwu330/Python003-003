# Generated by Django 2.2.13 on 2020-09-21 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(),
        ),
    ]
