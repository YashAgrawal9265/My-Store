# Generated by Django 3.1.1 on 2020-09-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('head0', models.CharField(max_length=50)),
                ('chead0', models.CharField(max_length=5000)),
                ('head1', models.CharField(max_length=50)),
                ('chead1', models.CharField(max_length=5000)),
                ('head2', models.CharField(max_length=50)),
                ('chead2', models.CharField(max_length=5000)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('thumbnail', models.ImageField(default='', upload_to='blog/images')),
            ],
        ),
    ]
