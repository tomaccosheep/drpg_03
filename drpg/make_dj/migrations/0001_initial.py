# Generated by Django 2.0.2 on 2018-03-05 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Play_Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('unique_id', models.CharField(max_length=32, null=True, unique=True)),
                ('con_001', models.CharField(max_length=16, null=True)),
            ],
        ),
    ]
