# Generated by Django 4.1.7 on 2023-04-03 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_alter_category_id_alter_item_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coupon',
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='item',
            name='store',
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='HaircutSubscription',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='Store',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
