# Generated by Django 2.2.7 on 2019-12-11 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20191123_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweetspot',
            old_name='qt_tweets',
            new_name='qtd_tweets',
        ),
        migrations.AddField(
            model_name='tweetspot',
            name='qtd_negativos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweetspot',
            name='qtd_positivos',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tweetspot',
            name='coe_sent',
            field=models.FloatField(default=0),
        ),
    ]
