# Generated by Django 4.0.6 on 2022-07-21 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('cohort_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cohort_name', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'cohort',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('md5', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('file_path', models.CharField(blank=True, max_length=200, null=True)),
                ('data_type', models.CharField(blank=True, max_length=20, null=True)),
                ('analysis_stage', models.CharField(blank=True, max_length=45, null=True)),
                ('size', models.FloatField(blank=True, null=True)),
                ('creation_date', models.DateField()),
            ],
            options={
                'db_table': 'data_file',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('greff_type', models.CharField(blank=True, max_length=20, null=True)),
                ('diagnosis_date', models.DateField(blank=True, null=True)),
                ('age_at_diagnosis', models.IntegerField(blank=True, db_column='Age_at_diagnosis', null=True)),
            ],
            options={
                'db_table': 'patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.IntegerField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('sample_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('tmb', models.FloatField(db_column='TMB')),
                ('origin', models.CharField(blank=True, max_length=45, null=True)),
                ('disease_stage', models.CharField(blank=True, max_length=45, null=True)),
                ('blast_purcentage', models.FloatField(blank=True, null=True)),
                ('cellularity', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sample',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sequencing',
            fields=[
                ('sequencing_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sequencing_name', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'sequencing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('idworkflow', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'workflow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CohortHasPatient',
            fields=[
                ('cohort_cohort', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.cohort')),
            ],
            options={
                'db_table': 'cohort_has_patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectHasCohort',
            fields=[
                ('project_project', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.project')),
            ],
            options={
                'db_table': 'project_has_cohort',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SampleHasDataFile',
            fields=[
                ('sample_sample', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.sample')),
            ],
            options={
                'db_table': 'sample_has_data_file',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SampleHasWorkflow',
            fields=[
                ('sample_sample', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.sample')),
            ],
            options={
                'db_table': 'sample_has_workflow',
                'managed': False,
            },
        ),
    ]
