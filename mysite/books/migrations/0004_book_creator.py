# Generated by Django 2.0.7 on 2019-03-08 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190227_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='creator',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]