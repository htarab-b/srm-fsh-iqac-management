# Generated by Django 4.2.14 on 2024-07-29 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_formdetailsmodel_subject_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdetailsmodel',
            name='Department',
            field=models.CharField(default='Computer Science', max_length=55),
            preserve_default=False,
        ),
    ]
