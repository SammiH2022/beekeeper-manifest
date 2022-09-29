# Generated by Django 4.1.1 on 2022-09-29 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ManifestApp', '0003_sensor_labels'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capability', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='compute',
            name='zone',
            field=models.CharField(choices=[('core', 'core'), ('detector', 'detector')], max_length=30),
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30)),
                ('hw_model', models.CharField(max_length=30)),
                ('hw_version', models.CharField(max_length=30)),
                ('sw_version', models.CharField(max_length=30)),
                ('datasheet', models.CharField(max_length=30)),
                ('cpu', models.CharField(max_length=30)),
                ('cpu_ram', models.CharField(max_length=30)),
                ('gpu_ram', models.CharField(max_length=30)),
                ('shared_ram', models.CharField(max_length=30)),
                ('capabilities', models.ManyToManyField(to='ManifestApp.capability')),
            ],
        ),
        migrations.AlterField(
            model_name='compute',
            name='cname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ManifestApp.hardware'),
        ),
    ]
