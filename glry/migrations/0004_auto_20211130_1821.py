# Generated by Django 3.2.8 on 2021-11-30 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('glry', '0003_photos_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='Location',
        ),
        migrations.AddField(
            model_name='photos',
            name='gallery_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='glry.gallery_category'),
        ),
    ]