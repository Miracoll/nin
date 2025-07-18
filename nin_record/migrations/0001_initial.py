# Generated by Django 5.2.4 on 2025-07-11 02:17

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NINProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nin', models.CharField(max_length=11, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('nationality', models.CharField(default='Nigeria', max_length=100)),
                ('state_of_origin', models.CharField(max_length=100)),
                ('lga_of_origin', models.CharField(max_length=100)),
                ('place_of_birth', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('passport_photo', models.ImageField(blank=True, null=True, upload_to='nin_photos/')),
                ('fingerprint_reference', models.TextField(blank=True, null=True)),
                ('date_registered', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_name', models.CharField(max_length=255)),
                ('officer_name', models.CharField(max_length=255)),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NextOfKin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_of_kin_surname', models.CharField(max_length=50)),
                ('next_of_kin_first_name', models.CharField(max_length=50)),
                ('next_of_kin_middel_name', models.CharField(max_length=50)),
                ('next_of_kin_relationship', models.CharField(max_length=50)),
                ('next_of_kin_country', models.CharField(max_length=50)),
                ('next_of_kin_state', models.CharField(max_length=50)),
                ('next_of_kin_lga', models.CharField(max_length=50)),
                ('next_of_kin_town', models.CharField(max_length=50)),
                ('next_of_kin_street_address', models.CharField(max_length=50)),
                ('next_of_kin_nin', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('nin_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nin_record.ninprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_surname', models.CharField(max_length=50)),
                ('father_first_name', models.CharField(max_length=50)),
                ('father_middle_name', models.CharField(max_length=50)),
                ('father_nin', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('nin_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='nin_record.ninprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_surname', models.CharField(max_length=50)),
                ('father_first_name', models.CharField(max_length=50)),
                ('father_middle_name', models.CharField(max_length=50)),
                ('father_nin', models.CharField(max_length=50)),
                ('mother_surname', models.CharField(max_length=50)),
                ('mother_first_name', models.CharField(max_length=50)),
                ('mother_middle_name', models.CharField(max_length=50)),
                ('mother_nin', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('nin_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='nin_record.ninprofile')),
            ],
        ),
        migrations.AddField(
            model_name='ninprofile',
            name='registration_center',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nin_record.registrationcenter'),
        ),
        migrations.CreateModel(
            name='SupportingDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=100)),
                ('document_number', models.CharField(max_length=100)),
                ('exp_month', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
                ('exp_year', models.IntegerField(choices=[(2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040), (2041, 2041), (2042, 2042), (2043, 2043), (2044, 2044), (2045, 2045), (2046, 2046), (2047, 2047), (2048, 2048), (2049, 2049), (2050, 2050)])),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('nin_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nin_record.ninprofile')),
            ],
        ),
    ]
