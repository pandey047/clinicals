# Generated by Django 2.1.5 on 2021-08-09 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componentName', models.CharField(max_length=20)),
                ('componentValue', models.CharField(max_length=20)),
                ('measureDateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='clinicalsdata',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicalsApp.Patient'),
        ),
    ]
