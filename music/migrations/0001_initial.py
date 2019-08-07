# Generated by Django 2.2 on 2019-06-14 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Name', models.CharField(max_length=250)),
                ('Address', models.CharField(max_length=250)),
                ('Contacts', models.FloatField(max_length=250)),
                ('Moving_Date', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funiture', models.CharField(max_length=200)),
                ('shoes', models.CharField(max_length=200)),
                ('clothes', models.CharField(max_length=200)),
                ('itemation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Costumer')),
            ],
        ),
    ]