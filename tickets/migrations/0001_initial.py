# Generated by Django 4.0.3 on 2022-03-10 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('head', models.CharField(blank=True, default='', max_length=100)),
                ('body', models.CharField(blank=True, default='', max_length=300)),
                ('ticket_class', models.CharField(blank=True, default='', max_length=50)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]