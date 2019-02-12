# Generated by Django 2.1.4 on 2019-01-19 01:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0013_auto_20190117_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('active', models.BooleanField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='client_Creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='client_modified_by', to=settings.AUTH_USER_MODEL)),
                ('primary_user', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClientType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('active', models.BooleanField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='clienttype_Creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='clienttype_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='consumer',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='consumer',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='consumer',
            name='primary_user',
        ),
        migrations.RemoveField(
            model_name='consumer',
            name='type',
        ),
        migrations.RemoveField(
            model_name='consumertype',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='consumertype',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='address',
            name='consumer',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='consumer',
        ),
        migrations.RemoveField(
            model_name='household',
            name='consumer',
        ),
        migrations.DeleteModel(
            name='Consumer',
        ),
        migrations.DeleteModel(
            name='ConsumerType',
        ),
        migrations.AddField(
            model_name='client',
            name='type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='base.ClientType'),
        ),
        migrations.AddField(
            model_name='address',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.Client'),
        ),
        migrations.AddField(
            model_name='facility',
            name='client',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='base.Client'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='household',
            name='client',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='base.Client'),
            preserve_default=False,
        ),
    ]
