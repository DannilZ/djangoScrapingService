# Generated by Django 3.1.2 on 2020-10-19 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_auto_20201019_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('title', models.CharField(max_length=250, verbose_name='Наименование вакансии')),
                ('company', models.CharField(max_length=250, verbose_name='Название компании')),
                ('description', models.TextField(verbose_name='Описание вакансии')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.city', verbose_name='город')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.language', verbose_name='язык программирования')),
            ],
            options={
                'verbose_name': 'вакансия',
                'verbose_name_plural': 'вакансии',
            },
        ),
    ]