# Generated by Django 4.2.8 on 2024-05-18 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='deposit',
            field=models.ManyToManyField(blank=True, related_name='deposit_joined', to='deposits.depositproducts'),
        ),
    ]