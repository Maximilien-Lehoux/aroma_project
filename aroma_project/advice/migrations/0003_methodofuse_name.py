# Generated by Django 3.2 on 2021-04-24 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advice', '0002_auto_20210423_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='methodofuse',
            name='name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
