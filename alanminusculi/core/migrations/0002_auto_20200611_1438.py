# Generated by Django 3.0.6 on 2020-06-11 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='identity',
            options={'ordering': ['name'], 'verbose_name': 'Identidade', 'verbose_name_plural': 'Identidades'},
        ),
        migrations.AlterField(
            model_name='identity',
            name='facebook',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='github',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='GitHub'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='instagram',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='linkedin',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='LinkedINn'),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('icon', models.CharField(max_length=100, verbose_name='Nome')),
                ('identity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Identity')),
            ],
            options={
                'verbose_name': 'Habilidade',
                'verbose_name_plural': 'Habilidades',
                'ordering': ['name'],
            },
        ),
    ]