# Generated by Django 4.2 on 2023-04-17 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=200)),
                ('doc_img', models.ImageField(upload_to='pics')),
                ('doc_spec', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=150)),
                ('p_ph', models.CharField(max_length=50)),
                ('booking_date', models.DateField()),
                ('booked_on', models.DateField(auto_now=True)),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hsptlapp.doctors')),
            ],
        ),
    ]
