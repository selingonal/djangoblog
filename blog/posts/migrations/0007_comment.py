# Generated by Django 2.0.6 on 2018-06-14 13:56

from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20180613_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=posts.models.upload_location, width_field='width_field')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='posts.Post')),
            ],
        ),
    ]