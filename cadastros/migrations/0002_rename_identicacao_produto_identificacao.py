# Generated by Django 3.2.9 on 2021-12-21 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='identicacao',
            new_name='identificacao',
        ),
    ]
