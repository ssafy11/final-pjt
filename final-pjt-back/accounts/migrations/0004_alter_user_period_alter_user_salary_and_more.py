# Generated by Django 4.2.8 on 2024-05-17 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_user_userid_user_name_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='period',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='wealth',
            field=models.IntegerField(default=0),
        ),
    ]