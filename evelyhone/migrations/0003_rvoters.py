# Generated by Django 3.1.4 on 2021-01-02 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evelyhone', '0002_auto_20210101_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rvoters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('password', models.CharField(max_length=10)),
                ('confirmpassword', models.CharField(max_length=10)),
            ],
        ),
    ]