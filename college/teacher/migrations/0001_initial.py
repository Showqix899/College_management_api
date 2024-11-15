# Generated by Django 5.1.2 on 2024-11-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('catagory', models.CharField(choices=[('S', 'Science'), ('C', 'Commerce'), ('A', 'Arts')], max_length=1)),
                ('subject_id', models.CharField(blank=True, max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField(max_length=400)),
                ('subject', models.ManyToManyField(related_name='teachers', to='teacher.subject')),
            ],
        ),
    ]
