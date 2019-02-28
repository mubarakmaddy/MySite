# Generated by Django 2.1.7 on 2019-02-27 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20190220_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookid', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]