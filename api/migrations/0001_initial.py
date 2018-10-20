# Generated by Django 2.1.2 on 2018-10-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('status', models.CharField(choices=[('want', '0'), ('want_and_have', '1'), ('recommend', '2')], max_length=2)),
            ],
        ),
    ]
