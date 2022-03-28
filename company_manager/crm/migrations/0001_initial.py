# Generated by Django 4.0.3 on 2022-03-28 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(blank=True, max_length=200, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('N', 'New'), ('L', 'Lead'), ('O', 'Opportunity'), ('C', 'Active Customer'), ('FC', 'Former Customer'), ('I', 'Inactive')], default='N', max_length=2)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('identification_number', models.CharField(max_length=100)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.address')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('primary_company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.company')),
            ],
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('1', 'Prospecting'), ('2', 'Analysis'), ('3', 'Proposal'), ('4', 'Negotiation'), ('5', 'Closed Won'), ('0', 'Closed Lost')], default='1', max_length=2)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='crm.company')),
                ('primary_contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.contact')),
                ('sales_manager', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
