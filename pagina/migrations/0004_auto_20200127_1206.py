# Generated by Django 3.0.2 on 2020-01-27 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0003_auto_20200127_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='motivo',
            field=models.TextField(),
        ),
    ]
