# Generated by Django 2.2.1 on 2019-06-03 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArquivoExcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='')),
                ('data_upload', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CampanhaDoacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(verbose_name='Data Início')),
                ('data_fim', models.DateField(verbose_name='Data Fim')),
            ],
            options={
                'verbose_name': 'Campanha de Doação',
                'verbose_name_plural': 'Campanhas de Doação',
                'ordering': ['-data_inicio'],
            },
        ),
        migrations.CreateModel(
            name='Exemplar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(verbose_name='Quantidade')),
                ('campanha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.CampanhaDoacao', verbose_name='Campanha')),
            ],
            options={
                'verbose_name': 'Exemplar',
                'verbose_name_plural': 'Exemplares',
                'ordering': ['quantidade'],
            },
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='Título')),
            ],
            options={
                'verbose_name': 'Obra',
                'verbose_name_plural': 'Obras',
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar_url', models.URLField(blank=True, null=True)),
                ('access_key', models.CharField(max_length=100)),
                ('is_admin', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateField(verbose_name='Data Início')),
                ('status_pedido', models.CharField(choices=[('DT', 'Deferido totalmente'), ('I', 'Indeferido'), ('DP', 'Deferido parcialmente')], max_length=2, verbose_name='Esfera Federação')),
                ('campanha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.CampanhaDoacao', verbose_name='Campanha de Doação')),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_requisicao', models.DateField(verbose_name='Data Requisição')),
                ('quantidade', models.PositiveIntegerField(verbose_name='Quantidade')),
                ('exemplar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Exemplar', verbose_name='Exemplar')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Pedido', verbose_name='Item do pedido')),
            ],
        ),
        migrations.AddField(
            model_name='exemplar',
            name='obra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Obra', verbose_name='Obra'),
        ),
    ]
