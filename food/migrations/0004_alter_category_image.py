# Generated by Django 4.1.7 on 2023-03-19 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_image'),
        ),
    ]
