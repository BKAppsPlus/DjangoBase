# Generated by Django 2.1.4 on 2019-01-17 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='active',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='consumer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consumer',
            name='created_by',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='consumer_Creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='consumer',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='consumer',
            name='modified_by',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='consumer_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='consumerprofile',
            name='active',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='consumerprofile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consumerprofile',
            name='created_by',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='consumerprofile_Creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='consumerprofile',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='consumerprofile',
            name='modified_by',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='consumerprofile_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='consumerprofile',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
