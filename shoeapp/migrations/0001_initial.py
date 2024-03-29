# Generated by Django 5.0.1 on 2024-03-18 17:05

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('shoe_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('size', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoeapp.cart')),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoeapp.shoe')),
            ],
        ),
        migrations.AddField(
            model_name='shoe',
            name='tags',
            field=models.ManyToManyField(to='shoeapp.tag'),
        ),
    ]
