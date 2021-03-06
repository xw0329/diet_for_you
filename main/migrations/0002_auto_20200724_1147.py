# Generated by Django 3.0 on 2020-07-24 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_data',
            name='text',
        ),
        migrations.AddField(
            model_name='post_data',
            name='calories',
            field=models.FloatField(default=2000.0),
        ),
        migrations.AddField(
            model_name='post_data',
            name='height',
            field=models.FloatField(default=180),
        ),
        migrations.AddField(
            model_name='post_data',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='post_data',
            name='weight',
            field=models.FloatField(default=75),
        ),
        migrations.AlterField(
            model_name='post_data',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
