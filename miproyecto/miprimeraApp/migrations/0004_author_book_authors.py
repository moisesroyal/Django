# Generated by Django 5.2 on 2025-04-05 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miprimeraApp', '0003_publisher_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='authors', to='miprimeraApp.author'),
        ),
    ]
