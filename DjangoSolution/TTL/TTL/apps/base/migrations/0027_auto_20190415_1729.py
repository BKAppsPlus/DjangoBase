# Generated by Django 2.1.4 on 2019-04-16 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('base', '0026_auto_20190415_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminuser',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='adminuser',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='adminuser',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='parentuser',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='parentuser',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='parentuser',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='provideruser',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='provideruser',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='provideruser',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='AdminUser',
        ),
        migrations.DeleteModel(
            name='ParentUser',
        ),
        migrations.DeleteModel(
            name='ProviderUser',
        ),
    ]