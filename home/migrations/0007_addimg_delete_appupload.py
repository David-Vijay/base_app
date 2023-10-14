# Generated by Django 4.1.7 on 2023-10-13 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_appupload_delete_addimage_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='addImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=20)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='appUpload',
        ),
    ]
