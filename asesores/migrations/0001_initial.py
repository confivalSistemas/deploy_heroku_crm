# Generated by Django 2.2.6 on 2020-01-23 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfil_asesor', '0001_initial'),
        ('municipio', '0001_initial'),
        ('comision', '0001_initial'),
        ('genero', '0002_auto_20200123_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsesoresDb',
            fields=[
                ('cod_asesor', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo')),
                ('nombre', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nombres Asesor')),
                ('apellido', models.CharField(blank=True, max_length=20, null=True, verbose_name='Apellidos Asesor')),
                ('direccion', models.CharField(blank=True, max_length=154, null=True, verbose_name='Dirección')),
                ('direccion2', models.CharField(blank=True, max_length=154, null=True, verbose_name='Dirrección')),
                ('celular', models.CharField(blank=True, max_length=15, null=True, verbose_name='Número de Celular')),
                ('mail', models.CharField(blank=True, max_length=50, null=True, verbose_name='E-Mail')),
                ('t_asesor', models.CharField(blank=True, max_length=15, null=True, verbose_name='Número de Teléfono')),
                ('cedula', models.CharField(blank=True, max_length=15, null=True, verbose_name='Número de Cedula')),
                ('c_cedula', models.CharField(blank=True, max_length=150, null=True, verbose_name='Copia de Cedula')),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de Registro')),
                ('fecha_s', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de Actualización')),
                ('fechanacimiento', models.DateField(blank=True, db_column='fechaNacimiento', null=True, verbose_name='fecha de Nacimiento')),
                ('fechaexpedicion', models.DateField(blank=True, db_column='fechaExpedicion', null=True, verbose_name='Fecha de Expedición')),
                ('cod_ciudad', models.CharField(blank=True, max_length=15, null=True)),
                ('departamento', models.CharField(blank=True, max_length=18, null=True)),
                ('ciudad', models.ForeignKey(blank=True, db_column='ciudad', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='AsesoresDb.ciudad+', to='municipio.Municipio', verbose_name='Ciudad')),
                ('ciudad2', models.ForeignKey(blank=True, db_column='ciudad2', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='AsesoresDb.ciudad2+', to='municipio.Municipio', verbose_name='Ciudad 2')),
                ('ciudadexpedicion', models.ForeignKey(blank=True, db_column='ciudadExpedicion', null=True, on_delete=django.db.models.deletion.PROTECT, to='municipio.Municipio', verbose_name='Ciudad de Expedición')),
                ('comision', models.ForeignKey(blank=True, db_column='comision', null=True, on_delete=django.db.models.deletion.PROTECT, to='comision.Comisiones', verbose_name='Comision')),
                ('genero', models.ForeignKey(db_column='genero', on_delete=django.db.models.deletion.PROTECT, to='genero.Genero')),
                ('perfil', models.ForeignKey(blank=True, db_column='perfil', null=True, on_delete=django.db.models.deletion.PROTECT, to='perfil_asesor.Perfilasesor', verbose_name='Perfil del Asesor')),
            ],
            options={
                'verbose_name': 'Asesor/Referenciador',
                'verbose_name_plural': 'Asesores/Referenciadores',
                'db_table': 'asesores_db',
                'ordering': ['cod_asesor'],
                'managed': True,
            },
        ),
    ]
