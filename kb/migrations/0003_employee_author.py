# Generated by Django 4.0 on 2022-02-20 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('kb', '0002_employee_content_employee_date_posted_employee_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='author',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
