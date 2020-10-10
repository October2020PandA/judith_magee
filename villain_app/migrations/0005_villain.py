# Generated by Django 2.2 on 2020-10-10 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('villain_app', '0004_delete_villain'),
    ]

    operations = [
        migrations.CreateModel(
            name='Villain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
                ('interests', models.CharField(max_length=45)),
                ('villain_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_likes', models.ManyToManyField(related_name='user_likes_villain', to='villain_app.User')),
                ('user_villain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_adds_villain', to='villain_app.User')),
            ],
        ),
    ]