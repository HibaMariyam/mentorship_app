# Generated by Django 5.0.2 on 2024-02-13 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0003_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, default=45.09, max_digits=6),
            preserve_default=False,
        ),
    ]
