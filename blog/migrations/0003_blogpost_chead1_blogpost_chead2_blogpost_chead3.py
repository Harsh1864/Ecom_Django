# Generated by Django 5.0.2 on 2024-08-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_head3'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='chead1',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead3',
            field=models.CharField(default='', max_length=500),
        ),
    ]