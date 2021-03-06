# Generated by Django 3.2.5 on 2021-07-04 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dj_relations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frameworks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('languages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj_relations.languages')),
            ],
        ),
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('framework', models.ManyToManyField(db_table='dd', to='dj_relations.Frameworks')),
            ],
        ),
    ]
