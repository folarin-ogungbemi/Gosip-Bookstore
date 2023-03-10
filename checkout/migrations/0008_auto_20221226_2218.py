# Generated by Django 3.2.16 on 2022-12-26 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_alter_order_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='first_name',
            new_name='address_line_1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='street',
            new_name='address_line_2',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='last_name',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='postal_address',
            new_name='zip',
        ),
        migrations.RemoveField(
            model_name='order',
            name='house_number',
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
