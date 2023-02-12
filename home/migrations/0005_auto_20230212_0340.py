# Generated by Django 3.2.17 on 2023-02-11 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_appointments_appointment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='allergies',
        ),
        migrations.RemoveField(
            model_name='user',
            name='appointments',
        ),
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='user',
            name='hospital',
        ),
        migrations.RemoveField(
            model_name='user',
            name='invoices',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='user',
            name='weight',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Hospital',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
    ]
