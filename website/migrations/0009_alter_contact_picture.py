# Generated by Django 4.1.4 on 2024-03-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_contact_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Picture',
            field=models.ImageField(default='/static/images/placeholder.webp', max_length=2000, upload_to='uploadedMedia'),
        ),
    ]
