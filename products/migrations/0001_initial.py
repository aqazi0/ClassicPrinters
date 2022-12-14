# Generated by Django 3.1.4 on 2022-09-05 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='visiting_card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(default='', max_length=30)),
                ('card_cat', models.CharField(default='', max_length=30)),
                ('card_qual', models.CharField(choices=[('matt', 'matt'), ('UV', 'UV'), ('glossy', 'glossy'), ('texture', 'texture'), ('varnish', 'varnish')], default='matt', max_length=20)),
                ('card_orien', models.CharField(choices=[('horizontal', 'horizontal'), ('vertical', 'vertical')], default='horizontal', max_length=15)),
                ('card_price', models.IntegerField(default=0)),
                ('card_image', models.ImageField(default='', upload_to='cards/')),
            ],
        ),
    ]
