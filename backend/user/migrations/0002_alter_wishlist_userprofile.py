# Generated by Django 4.0.2 on 2022-03-08 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='userProfile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.userprofile'),
        ),
    ]
