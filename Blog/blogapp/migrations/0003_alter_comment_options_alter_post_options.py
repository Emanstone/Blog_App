# Generated by Django 4.2.7 on 2023-11-16 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_created']},
        ),
    ]