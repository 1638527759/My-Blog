# Generated by Django 3.2 on 2022-02-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220222_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='passwords',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=128),
        ),
    ]
