# Generated by Django 2.2 on 2020-03-28 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0003_auto_20200328_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='status_test',
            new_name='status_text',
        ),
    ]
