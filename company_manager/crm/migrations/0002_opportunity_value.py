# Generated by Django 4.0.3 on 2022-03-28 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
