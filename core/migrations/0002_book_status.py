# Generated by Django 3.2.15 on 2022-08-30 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('N', 'New'), ('U', 'Used')], default='N', max_length=1),
        ),
    ]
