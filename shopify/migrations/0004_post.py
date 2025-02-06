# Generated by Django 5.1.5 on 2025-02-05 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0003_latest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('box', models.CharField(blank=True, max_length=50)),
                ('descrepti', models.TextField(null=True)),
            ],
        ),
    ]
