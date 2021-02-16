# Generated by Django 2.2.6 on 2020-09-23 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0011_remove_publisher_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pubkisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_author', to='p_library.Publisher'),
        ),
    ]
