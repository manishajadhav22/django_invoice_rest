# Generated by Django 4.2.1 on 2023-08-02 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField()),
                ('invoce_no', models.IntegerField(max_length=100)),
                ('cust_name', models.CharField(max_length=10)),
            ],
        ),
    ]
