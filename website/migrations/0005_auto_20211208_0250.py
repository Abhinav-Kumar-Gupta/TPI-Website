# Generated by Django 3.2.9 on 2021-12-07 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_noticeboard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticeboard',
            old_name='companyName',
            new_name='compName',
        ),
        migrations.RenameField(
            model_name='noticeboard',
            old_name='publishDate',
            new_name='pubDate',
        ),
    ]
