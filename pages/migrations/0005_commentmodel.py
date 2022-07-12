# Generated by Django 4.0.6 on 2022-07-12 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0004_alter_articlemodel_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izoh', models.CharField(max_length=400)),
                ('maqola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='izohlar', to='pages.articlemodel')),
                ('muallif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
