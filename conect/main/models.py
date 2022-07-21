from django.db import models

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Cohort(models.Model):
    cohort_id = models.IntegerField(primary_key=True)
    cohort_name = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cohort'


class CohortHasPatient(models.Model):
    cohort_cohort = models.OneToOneField(Cohort, models.DO_NOTHING, primary_key=True)
    patient_patient = models.ForeignKey('Patient', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cohort_has_patient'
        unique_together = (('cohort_cohort', 'patient_patient'),)


class DataFile(models.Model):
    md5 = models.CharField(primary_key=True, max_length=100)
    file_path = models.CharField(max_length=200, blank=True, null=True)
    data_type = models.CharField(max_length=20, blank=True, null=True)
    analysis_stage = models.CharField(max_length=45, blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    creation_date = models.DateField()
    idworkflow = models.ForeignKey('Workflow', models.DO_NOTHING, db_column='idworkflow')

    class Meta:
        managed = False
        db_table = 'data_file'


class Patient(models.Model):
    patient_id = models.CharField(primary_key=True, max_length=40)
    gender = models.CharField(max_length=6, blank=True, null=True)
    greff_type = models.CharField(max_length=20, blank=True, null=True)
    diagnosis_date = models.DateField(blank=True, null=True)
    age_at_diagnosis = models.IntegerField(db_column='Age_at_diagnosis', blank=True, null=True)  # Field name made lowercase.
    project = models.ForeignKey('Project', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient'


class Project(models.Model):
    project_id = models.IntegerField(primary_key=True)
    project_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class ProjectHasCohort(models.Model):
    project_project = models.OneToOneField(Project, models.DO_NOTHING, primary_key=True)
    cohort_cohort = models.ForeignKey(Cohort, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_has_cohort'
        unique_together = (('project_project', 'cohort_cohort'),)


class Sample(models.Model):
    sample_id = models.CharField(primary_key=True, max_length=30)
    tmb = models.FloatField(db_column='TMB')  # Field name made lowercase.
    origin = models.CharField(max_length=45, blank=True, null=True)
    disease_stage = models.CharField(max_length=45, blank=True, null=True)
    blast_purcentage = models.FloatField(blank=True, null=True)
    cellularity = models.FloatField(blank=True, null=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample'


class SampleHasDataFile(models.Model):
    sample_sample = models.OneToOneField(Sample, models.DO_NOTHING, primary_key=True)
    data_file_md5 = models.ForeignKey(DataFile, models.DO_NOTHING, db_column='data_file_md5')

    class Meta:
        managed = False
        db_table = 'sample_has_data_file'
        unique_together = (('sample_sample', 'data_file_md5'),)


class SampleHasWorkflow(models.Model):
    sample_sample = models.OneToOneField(Sample, models.DO_NOTHING, primary_key=True)
    workflow_idworkflow = models.ForeignKey('Workflow', models.DO_NOTHING, db_column='workflow_idworkflow')

    class Meta:
        managed = False
        db_table = 'sample_has_workflow'
        unique_together = (('sample_sample', 'workflow_idworkflow'),)


class Sequencing(models.Model):
    sequencing_id = models.IntegerField(primary_key=True)
    sequencing_name = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    data_file_md5 = models.ForeignKey(DataFile, models.DO_NOTHING, db_column='data_file_md5')

    class Meta:
        managed = False
        db_table = 'sequencing'


class Workflow(models.Model):
    idworkflow = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workflow'
