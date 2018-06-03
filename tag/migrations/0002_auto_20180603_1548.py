# Generated by Django 2.0.4 on 2018-06-03 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repository',
            old_name='repository',
            new_name='repository_url',
        ),
        migrations.AddField(
            model_name='repository',
            name='repository_name',
            field=models.CharField(default=123, max_length=20),
            preserve_default=False,
        ),
    ]
