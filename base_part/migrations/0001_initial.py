# Generated by Django 4.0 on 2022-01-04 16:34

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloth_type', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='base/')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2022, 1, 4, 16, 34, 58, 62485, tzinfo=utc), verbose_name='date published')),
                ('description', models.TextField(max_length=200)),
                ('price', models.FloatField()),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.userprofile')),
            ],
        ),
    ]
