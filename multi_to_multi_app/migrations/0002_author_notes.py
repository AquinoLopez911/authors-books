# Generated by Django 2.2.5 on 2019-09-14 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_to_multi_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.CharField(default='An author to a book or two', max_length=255),
            preserve_default=False,
        ),
    ]
