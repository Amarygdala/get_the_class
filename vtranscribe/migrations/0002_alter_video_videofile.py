# Generated by Django 3.2 on 2021-05-02 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtranscribe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videofile',
            field=models.FileField(default=1, upload_to='videos/'),
            preserve_default=False,
        ),
    ]
