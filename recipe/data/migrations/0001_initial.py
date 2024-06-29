# Generated by Django 5.0.6 on 2024-06-26 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_title', models.CharField(max_length=100)),
                ('recipe_description', models.TextField()),
                ('recipe_img', models.ImageField(upload_to='data/')),
            ],
        ),
    ]